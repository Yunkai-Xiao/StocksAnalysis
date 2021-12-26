import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import requests
from datetime import datetime
import os


class Scraper:
  def __init__(self):
    self.datas = {}
    self.tickerslist = os.environ['TICKERLIST']
    self.scrap_data()

  def scrap_data(self):
    with open(self.tickerslist, 'r') as f:
      tickers = f.readlines()
      for tick in tickers:
        self.datas[tick.strip()] = None
    for key in self.datas:
      try:
        if os.path.isfile(os.environ['DATASTORAGE']+key+".csv"):
          ts = os.path.getmtime(os.environ['DATASTORAGE']+key+".csv")
          now = datetime.timestamp(datetime.now())
          if now - ts < 24*60*60:
            self.datas[key] = pd.read_csv(os.environ['DATASTORAGE']+key+".csv")
            continue
          else:
            cur_data = yf.download(key, start = '2019-01-01', end='2021-09-30', progress=False)
            cur_data.to_csv(os.environ['DATASTORAGE']+key+".csv")
            self.datas[key] = cur_data
        print("Ticker: %s is loaded" % key)
      except requests.exceptions.ConnectionError as e:
        print("Ticker: %s downloaded failed." % key)
        exit(-1)
    print("All data is loaded successfully.")

  def get_data(self):
    return self.datas

sc = Scraper()
  
