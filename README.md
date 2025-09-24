# 💧 FBW & Economic Equality Tracker
Tracks **Free Basic Water (FBW)** provision trends and assesses **economic equality** outcomes.

## Pages
- **🏁 Overview + Parameters** — set FBW minimum (default 6 kL/month), title
- **📥 Data Intake** — upload unified dataset
- **📈 FBW Trends & Compliance** — coverage vs indigent register; litres vs 6 kL minimum
- **⚖️ Inequality Lens** — coverage vs unemployment & revenue per household; inequality index
- **📝 Report Generator** — creates a PDF report summarising KPIs, narrative, and tables

## Expected columns
`year, wsa, households_total, households_indigent, fbw_households_served, litres_provided_total, revenue_Rm, unemployment_rate`

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
