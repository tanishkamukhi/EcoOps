import pandas as pd
from .models import insert_energy

def load_energy_csv(path, org_id=1):
    df = pd.read_csv(path)
    for _, row in df.iterrows():
        insert_energy(
            org_id,
            row.get("asset_name","Unknown"),
            row["period_start"],
            row["period_end"],
            row["kwh"],
            row.get("cost_inr", 0)
        )
    print("✅ Imported", len(df), "rows from", path)

if __name__ == "__main__":
    load_energy_csv("sample_energy.csv")
