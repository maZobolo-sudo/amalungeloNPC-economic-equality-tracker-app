import streamlit as st, pandas as pd
from src.config import load_config, save_config
st.title("🏁 Overview + Parameters")
WORKSPACE = st.secrets.get("workspace_key","default")
cfg = load_config(WORKSPACE)
st.markdown("""
This app tracks **Free Basic Water (FBW)** provision trends and assesses **economic equality** impacts.
- Upload datasets on the Data Intake page.
- Adjust FBW minimum (default **6 kL/month**) and report title here.
""")
cfg["fbw_min_kl_per_month"] = st.number_input("FBW statutory minimum (kL / household / month)", value=float(cfg.get("fbw_min_kl_per_month",6.0)), step=0.5)
cfg["report_title"] = st.text_input("Report title", value=cfg.get("report_title","State of Economic Equality Report — Free Basic Water"))
if st.button("💾 Save Parameters"):
    p = save_config(WORKSPACE, cfg); st.success(f"Saved parameters to {p}")
st.info("Expected data columns are listed in the **Data Intake** page.")
