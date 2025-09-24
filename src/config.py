import json
from pathlib import Path
def cfg_path(workspace: str):
    p = Path(f"tenants/{workspace}/config"); p.mkdir(parents=True, exist_ok=True)
    return p / "fbw_params.json"
DEFAULTS = {
  "fbw_min_kl_per_month": 6.0,
  "inequality_bins": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
  "report_title": "State of Economic Equality Report — Free Basic Water"
}
def load_config(workspace: str):
    p = cfg_path(workspace)
    if not p.exists(): return DEFAULTS.copy()
    try: return json.loads(p.read_text())
    except Exception: return DEFAULTS.copy()
def save_config(workspace: str, cfg: dict):
    p = cfg_path(workspace); p.write_text(json.dumps(cfg, indent=2)); return p
