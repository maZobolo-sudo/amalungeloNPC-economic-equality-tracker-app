import streamlit as st, pandas as pd
from pathlib import Path
st.title("📥 Data Intake")
st.caption("Upload a unified CSV with these columns: year, wsa, households_total, households_indigent, fbw_households_served, litres_provided_total, revenue_Rm, unemployment_rate")
up = st.file_uploader("Upload FBW dataset CSV", type=["csv"])
if not up: st.stop()
df = pd.read_csv(up)
WORKSPACE = st.secrets.get("workspace_key","default")
p = Path(f"tenants/{WORKSPACE}/data/fbw.csv"); p.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(p, index=False); st.success(f"Saved to {p}"); st.dataframe(df.head())
