from time import sleep
import pandas as pd
from finvizfinance.screener.overview import Overview

foverview = Overview()
filters_dict = {'Index':'S&P 500','Sector':'Any' ,'Market Cap.': '+Mid (over $2bln)' , 'Average Volume': 'Over 500K' , 'Average True Range': 'Over 0.75'}
foverview.set_filter(filters_dict=filters_dict)
data = foverview.screener_view()


for d in data.values:
    StockTicker = d[0]
    StockCompany = d[1]
    StockSector = d[2]
    StockCountry = d[4]
    message = f'The Stock {StockCompany} with the Symbol {StockTicker} from The {StockSector} Sector can be Good For The Swing algorightm '
    print(message)




    foverview.set_filter(filters_dict=filters_dict)