'libreria per accedere alle pagine web'
'per scaricare la libreria da terminale pip install requests bs4'
import requests
from bs4 import BeautifulSoup
import smtplib
import time

Url ='https://www.amazon.it/Apple-MWP22TY-A-AirPods-Pro/dp/B07ZPNLGDP/ref=sr_1_1_sspa?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=airpods+pro&qid=1619987547&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE0WDFSTVhGTzFJMFgmZW5jcnlwdGVkSWQ9QTAwMTk0NzYxRkVWS1dKTTRaVEwzJmVuY3J5cHRlZEFkSWQ9QTA0NTU0MzIxRTNEV005N1MyUFZJJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0'}

def check_price():
 page = requests.get(Url, headers=headers)
 soup = BeautifulSoup(page.content, 'html.parser')
 prezzo = soup.find(id="priceblock_ourprice").get_text().strip()
 conversione_prezzo = float(prezzo[0:3])
 titolo = soup.find(id="productTitle").get_text().strip()
 print("Il seguente prodotto "+titolo+ " in questo momento costa: "+prezzo)
 if(conversione_prezzo < 150):
     send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    'codifica la conessione'
    server.starttls()
    server.ehlo()
    server.login('abramo.limi@gmail.com', 'jlmsgmcdwbwrwxwx')
    subject = 'il prezzo e sceso'
    body='controlla il link di amazon: https://www.amazon.it/Apple-MWP22TY-A-AirPods-Pro/dp/B07ZPNLGDP/ref=sr_1_1_sspa?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=airpods+pro&qid=1619987547&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE0WDFSTVhGTzFJMFgmZW5jcnlwdGVkSWQ9QTAwMTk0NzYxRkVWS1dKTTRaVEwzJmVuY3J5cHRlZEFkSWQ9QTA0NTU0MzIxRTNEV005N1MyUFZJJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'abramo.limi@gmail.com',
        'limi.ibrahim@outlook.it',
        msg
    )
    print('email inviata ')
    server.quit()



while(True):
    check_price()
    time.sleep(3600)
















