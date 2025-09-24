import streamlit as st, pandas as pd, numpy as np, matplotlib.pyplot as plt
from pathlib import Path
st.title("📊 Equity + Compliance")
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/data/equality.csv")
if not p.exists(): st.warning("No dataset. Use Data Intake."); st.stop()
df = pd.read_csv(p)
aff = (df["tariff_typical"]*12) / df["median_income"].replace(0,1)  # annual bill share of income
df["affordability_pct"] = aff
fbw_ok = st.number_input("FBW minimum (kL/month) for indigent HHs", value=6.0, step=1.0)
df["fbw_compliant"] = (df["fbw_kl"] >= fbw_ok).astype(int)
st.dataframe(df)
st.metric("Share FBW-compliant", f"{df['fbw_compliant'].mean():.0%}")
fig = plt.figure(figsize=(6,3)); df.sort_values("affordability_pct").plot(x="wsa_name", y="affordability_pct", kind="barh", legend=False)
plt.xlabel("Affordability (bill share of income)"); st.pyplot(fig)
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download equity table", csv, "wsa_equity.csv", "text/csv")
