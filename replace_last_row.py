# repair_last_row.py

import pandas as pd
from datetime import date

from config import *
from compute import *

def repair_last_row():
    file = "data/mnav.csv"

    # 1. Load CSV
    df = pd.read_csv(file)

    if df.empty:
        print("CSV is empty, nothing to repair.")
        return

    # 2. Get last date
    last_date = df.iloc[-1]["date"]
    today = str(date.today())

    print(f"Last row date: {last_date}")
    print(f"Today: {today}")

    # Optional safety check
    if last_date != today:
        print("Warning: Last row is not today. Still replacing it.")

    # 3. Recompute values
    market_cap, net_debt = get_stock_data(TICKER)
    btc_price = get_btc_price()

    ev = compute_ev(market_cap, net_debt, PREFERRED_STOCK)
    mnav, btc_nav = compute_mnav(ev, btc_price, BTC_HOLDINGS)

    # 4. Replace last row
    df.iloc[-1] = {
        "date": last_date,
        "mnav": mnav,
        "ev": ev,
        "btc_nav": btc_nav,
    }

    # 5. Save back
    df.to_csv(file, index=False)

    print("Last row successfully repaired!")
    print(df.tail())


if __name__ == "__main__":
    repair_last_row()