
# coding: utf-8

# # Downloading Stock Data 
#     - Class to get symbols and download stock data
#         - further checks on date range needs to be added
#         - need to eliminate Unnamed columns in dataframe

# In[ ]:


from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from datetime import datetime

class StockData():
    def __init__(self, file_name):
        
        self.file_name = file_name
        self.symbol_dict = {}
        
        
    def stock_downloads(self):
        for x, y in self.file_name['Symbol'].iteritems():
            try:
                self.symbol_df(y)
            except Exception as e:
                print(e)
                print("Failed to pass to symbol_df", y)
                continue

    
    def symbol_df(self, ticker):
        
        stock = pd.read_csv('data/NASDAQ Data/' + ticker + '.csv')
        start_date = '2010-01-31'
        end_date = '2019-02-21'

        df_symbol = ("df" + "_" + ticker)
        df_symbol = data.DataReader(ticker, 'yahoo', start_date, end_date)
        df_symbol = stock.append(df_symbol)
        self.symbol_dict[ticker] = df_symbol
        self.create_csv(self.symbol_dict)
    
    def create_csv(self, symbol_dict):
        for x in self.symbol_dict.keys():
            self.symbol_dict[x].to_csv('data/NASDAQ Data/' + x + '.csv')
            display(self.symbol_dict[x].tail())
        


# In[ ]:


import pandas as pd
nyse = pd.read_csv('data/NASDAQCompanyList.csv')

nyse = nyse.tail() # temp for testing new functionality

stock = StockData(nyse)
stock.stock_downloads()


# In[ ]:


# future addition

# stock = pd.read_csv('data/NASDAQ Data/NVDA.csv')
# stock['Day Diff'] = stock['Adj Close'] - stock['Adj Close'].shift()
# stock['Day Percentage Change'] = ((stock['Adj Close'] - stock['Adj Close'].shift())/stock['Adj Close'])*100
# date = stock['Date'].iloc[0] 
# date = datetime.strptime(date, "%Y-%d-%m")
# date = date + dt.timedelta(1)
# print(date)

