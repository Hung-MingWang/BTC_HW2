import yfinance as yf
import requests
import pandas as pd


def compute_ev(market_cap, net_debt, preferred_stock):
    return market_cap + net_debt + preferred_stock

def compute_mnav(ev, btc_price, btc_holdings):
    btc_nav = btc_price * btc_holdings
    return ev / btc_nav, btc_nav

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)

    price = stock.history(period="1d")["Close"].iloc[-1]
    shares = stock.info["sharesOutstanding"]

    market_cap = price * shares

    bs = stock.balance_sheet
    net_debt = bs.loc["Net Debt"].iloc[0]

    return market_cap, net_debt

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    return requests.get(url).json()["bitcoin"]["usd"]
