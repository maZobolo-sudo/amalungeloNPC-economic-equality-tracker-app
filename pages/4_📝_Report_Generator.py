import streamlit as st, pandas as pd
from pathlib import Path
from src.config import load_config
from src.report import make_report
st.title("📝 Generate 'State of Economic Equality' Report")
WORKSPACE = st.secrets.get("workspace_key","default")
cfg = load_config(WORKSPACE)
p = Path(f"tenants/{WORKSPACE}/data/fbw.csv")
if not p.exists(): st.warning("No dataset. Use Data Intake."); st.stop()
df = pd.read_csv(p)
latest = df.sort_values("year").groupby("wsa").tail(1).copy()
latest["coverage_pct"] = (latest["fbw_households_served"]/latest["households_indigent"].replace(0,1)).clip(0,2)*100
latest["litres_per_hh_month"] = (latest["litres_provided_total"]/latest["fbw_households_served"].replace(0,1)).fillna(0)
overall_cov = latest["coverage_pct"].mean()
below_min_share = (latest["litres_per_hh_month"] < cfg["fbw_min_kl_per_month"]*1000).mean()*100
kpis = {
    "Avg coverage of indigent households": f"{overall_cov:.1f}%",
    "Municipalities below 6 kL minimum": f"{below_min_share:.0f}%"
}
notes = st.text_area("Narrative summary (optional)", value="FBW coverage and litres per household are compared to statutory benchmarks. Results indicate areas of under-delivery and inequality by municipal revenue base and unemployment rates.")
score = latest[["wsa","coverage_pct","litres_per_hh_month","unemployment_rate","revenue_Rm"]].sort_values("coverage_pct")
tables = {"Coverage & litres (latest year)": score.rename(columns={"coverage_pct":"coverage_%","revenue_Rm":"revenue_R_millions"})}
out = Path(f"tenants/{WORKSPACE}/reports/fbw_state_of_equality.pdf"); out.parent.mkdir(parents=True, exist_ok=True)
if st.button("Generate PDF"):
    make_report(out, cfg.get("report_title","State of Economic Equality Report — Free Basic Water"), kpis, notes, tables)
    st.success(f"Report saved to {out}")
    with open(out, "rb") as f:
        st.download_button("⬇️ Download PDF", f, file_name="fbw_state_of_equality.pdf", mime="application/pdf")
