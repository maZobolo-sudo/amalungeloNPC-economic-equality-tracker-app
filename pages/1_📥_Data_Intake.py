import streamlit as st, pandas as pd
from pathlib import Path
st.title("📥 Data Intake")
up = st.file_uploader("Upload WSA equity CSV (wsa_name, households, indigent_share, fbw_kl, tariff_typical, median_income)", type=["csv"])
if not up: st.stop()
df = pd.read_csv(up)
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/data/equality.csv"); p.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(p, index=False); st.success(f"Saved to {p}"); st.dataframe(df.head())
