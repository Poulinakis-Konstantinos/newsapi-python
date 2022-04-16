from newsapi import NewsApiClient
from datetime import date, timedelta
import sys 
import pandas as pd 
import os 
import re 

API_KEY = '3ebe15f1d7784766939ca966eb867d80'
# Business category sources 
source = ['australian-financial-review', 'bloomberg', 'business-insider', 
            'financial-post', 'fortune', 'the-wall-street-journal', 'market-watch', 'seeking-alpha', 'motley-fool',
            'reuters', 'new-york-times', 'the-guardian']
sources = ''
for sor in source :
    sources = sources + ' ' + sor
sources=None
# default key-word
q = ''


def fetch(q=q, yest=False) : 
    '''Fetch news for key-word q.
      q (str) : The key word to search news for.
      yest(bool) : Whether to fetch news from yesterday or not. If False fetches only today's news.
                        Neccessary for when requesting during 24:00 - 01:00 am (1 hour delay). '''

    # instantiate api object
    api = NewsApiClient(api_key=API_KEY)
    # today's date in Year-month-day format
    today = date.today().strftime("%Y-%m-%d")

    if yest==False : 
        # fetch today's news for key-word q 
        request = api.get_everything(q=q, from_param=today, to=today,
                                    sort_by='relevancy', language='en' , sources=sources)
    else : 
        yesterday = date.today() - timedelta(1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        # fetch yesterday's and today's news for key-word q 
        request = api.get_everything(q=q, from_param=yesterday, to=today,
                                     sort_by='relevancy', language='en' , sources=sources)

    #print(f"Fetced {request['totalResults']} news articles for {q} during {today}")
    articles = request['articles']
    print(f"Total articles fetched {len(articles)} for {q} during {today} out of {request['totalResults']} available")
    # write article information into a datafraeme and save it in a .csv
    df = pd.DataFrame(articles)
    # clean the text fetched
    for col in df.columns : 
        df[col] =  [re.sub(r"[^a-zA-Z0-9-_\s.]", '', str(x)) for x in df[col]]
    


    if yest :
        df['date'] = yesterday
        # create a folder for the requested date to save news into 
        if not os.path.exists(f'news_data/{yesterday}') : os.makedirs(f'news_data/{yesterday}')
        print(f"Saving articles to  news_data/{yesterday}/{q}_{yesterday}.csv")
        name = f"news_data/{yesterday}/{q}_{yesterday}.csv"
    else :
        df['date'] = today
        # create a folder for the requested date to save news into 
        if not os.path.exists(f'news_data/{today}') : os.makedirs(f'news_data/{today}')
        print(f"Saving articles to  news_data/{today}/{q}_{today}.csv")
        name = f"news_data/{today}/{q}_{today}.csv"
    df.to_csv(name)


if __name__=='__main__' :
    # key-word to fetch news for
    q  = sys.argv[1]
    if len(sys.argv) > 1:
        yest = sys.argv[2]
    else : yest=None

    # instantiate api object
    api = NewsApiClient(api_key=API_KEY)
    # today's date in Year-month-day format
    today = date.today().strftime("%Y-%m-%d")

    if yest==None : 
        # fetch today's news for key-word q 
        request = api.get_everything(q=q, from_param=today, to=today,
                                    sort_by='relevancy', language='en' , sources=sources)
    else : 
        yesterday = date.today() - timedelta(1)
        yesterday = yesterday.strftime("%Y-%m-%d")
        # fetch yesterday's and today's news for key-word q 
        request = api.get_everything(q=q, from_param=yesterday, to=today,
                                     sort_by='relevancy', language='en' , sources=sources)

   # print(f"Fetced {request['totalResults']} news articles for {q} during {today}")
    articles = request['articles']
    print(f"Total articles fetched {len(articles)} for {q} during {today} out of {request['totalResults']} available")
    # write article information into a datafraeme and save it in a .csv
    df = pd.DataFrame(articles)
    # clean the text fetched
    for col in df.columns : 
        df[col] =  [re.sub(r"[^a-zA-Z0-9-_\s.]", '', str(x)) for x in df[col]]
    
    if yest != None :
        df['date'] = yesterday
        print(f"Saving articles to  news_data/{q}_{yesterday}.csv")
        name = f"news_data/{q}_{yesterday}.csv"
    else :
        df['date'] = today
        print(f"Saving articles to  news_data/{q}_{today}.csv")
        name = f"news_data/{q}_{today}.csv"
    df.to_csv(name )



