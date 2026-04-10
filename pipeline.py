from datetime import date
from config import *
from compute import *
from db import *
import pandas as pd
import os

def save_to_csv(date, mnav, ev, btc_nav):
    file = "data/mnav.csv"

    new_row = {
        "date": date,
        "mnav": mnav,
        "ev": ev,
        "btc_nav": btc_nav
    }

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame([new_row])])
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(file, index=False)

def run_pipeline():
    market_cap, net_debt = get_stock_data(TICKER)
    btc_price = get_btc_price()

    ev = compute_ev(market_cap, net_debt, PREFERRED_STOCK)
    mnav, btc_nav = compute_mnav(ev, btc_price, BTC_HOLDINGS)

    today = str(date.today())

    insert_data(today, mnav, ev, btc_nav)
    save_to_csv(today, mnav, ev, btc_nav)

    print(f"{today} | mNAV={mnav:.3f}")

if __name__ == "__main__":
    init_db()
    run_pipeline()
