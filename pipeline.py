from datetime import date
from config import *
from compute import *
from db import *

def run_pipeline():
    market_cap, net_debt = get_stock_data(TICKER)
    btc_price = get_btc_price()

    ev = compute_ev(market_cap, net_debt, PREFERRED_STOCK)
    mnav, btc_nav = compute_mnav(ev, btc_price, BTC_HOLDINGS)

    today = str(date.today())

    insert_data(today, mnav, ev, btc_nav)

    print(f"{today} | mNAV={mnav:.3f}")

if __name__ == "__main__":
    init_db()
    run_pipeline()
