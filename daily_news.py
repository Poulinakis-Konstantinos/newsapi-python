from fetch_news import fetch

if __name__=='__main__' : 

    # stocks = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA', 'NVDA', 'BRK', 'FB', 'JPM',
    #         'UNH', 'JNJ', 'PG', 'V', 'HD', 'BAC', 'XOM', 'MA', 'DIS', 'PFE', 'CVX',
    #         'ABBV', 'KO', 'CSCO', 'AVGO', 'VZ', 'PEP', 'WMT',
    #         'ADBE', 'INTC', 'AMD', 'QCOM', 'MCD',
    #         'NFLX', 'NKE', 'UPS', 'AMAT', 'AXP', 'GS']
  #  stocks = ['nvidia', 'facebook', 'Intel', 'Tesla', 'Apple', 'Microsoft', 'Google', 'Amazon', 'Pfizer', 'P&G', 'JP Morgan',
   #           'NFLX', 'QCOM', 'WMT', 'GOOG', 'BRK', 'ADBE', 'Viza', 'Mastercard']
    stocks = ['AMZN',]
    for stock in stocks :
        fetch(q=stock, yest=True)