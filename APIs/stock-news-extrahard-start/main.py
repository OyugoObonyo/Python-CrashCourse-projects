import datetime
import requests
import smtplib
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API = os.environ.get('STOCKS_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
EMAIL = os.environ.get('EMAIL_ADDRESS')
PASSWORD = os.environ.get('EMAIL_PASSWORD')
RECIPIENT = os.environ.get('RECIPIENT_EMAIL')

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API,
}

# Get stock data from alphavantage API
response = requests.get("https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Get yesterday date and day before yesterday date
yesterday = str((datetime.datetime.now() - datetime.timedelta(1)).date())
before_yesterday = str((datetime.datetime.now() - datetime.timedelta(2)).date())
price_yesterday = float(data[yesterday]['4. close'])
price_before_yesterday = float(data[before_yesterday]['4. close'])

# Check for price change in the stock
price_change = abs((price_yesterday-price_before_yesterday)/price_before_yesterday * 100)
price_change = round(price_change, 2)

if price_change >= 0:
    params = {
        "q": "tesla",
        "apiKey": NEWS_API_KEY
    }
    r = requests.get("https://newsapi.org/v2/top-headlines", params=params)
    r.raise_for_status()
    news = r.json()['articles']
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=RECIPIENT,
        msg=f"Subject:TESLA PRICE CHANGE\n\nSTOCK PRICE CHANGE(in %): {price_change}\nHEADLINE:{news[0]['title']}\n{news[0]['url']}")
    connection.close()
