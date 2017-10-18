# -*- coding: utf-8 -*-

import urllib
import requests
import sys
import BeautifulSoup
import time
import smtplib
import re
from email.mime.text import MIMEText
from datetime import datetime
import random

reload(sys)
sys.setdefaultencoding('utf8')

# add as much urls as you want 
urls = ['https://www.guess.eu/en/catalog/view/asap-rocky/men/aap-rocky-london-t-shirt/m7fp91k5dd1','https://www.guess.eu/en/catalog/view/asap-rocky/men/aap-rocky-london-t-shirt/m7fp92r5dd1','https://www.guess.eu/en/catalog/view/asap-rocky/men/aap-rocky-london-sweatshirt/m7fp93r4bd0']

# this is where you put your @ mail, same thing you can add as much as you want 
tab = [''] 

# content mail, what will be send to your mail, as I did this program in a hurry I didn't use the advanced mail feature
# for Python so please test it before running the bot in real conditions...
content = ['ASAP TEE GUESS ALERT bit.ly/2yryHb2','ASAP TEE GUESS ALERT bit.ly/2gNj2ca','ASAP SWEAT GUESS ALERT bit.ly/2x5H1cV']

i = 0

# Needs to be changed with a better log function
def currentTime():
    current = str(datetime.now())
    return current

print(currentTime(), ': Autochecker ASAP GUESS 0.1 bot launched')
    

def autochecker(url):
    with requests.session() as s:
    	print(currentTime(), "Making request...")
    	req = s.get(url).text
    	soup = BeautifulSoup.BeautifulSoup(req)
    	for div in soup.findAll("div",{"class":"buttons"}):
    		for k in div.findAll("a"):
    			if "stay tuned" in k.text.lower():
    				print(currentTime(), "No difference")
    				return 1
    		return 0


def sendingMail(tab, content):
    f = 0
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()

    mail.starttls()
 
    mail.login('yourmail@gmail.com', 'yourpasswordgmail') # this is where you input your GMAIL credentials
    while f < len(tab):
        mail.sendmail('yourmail@gmail.com', tab[f], content) # here too 
        f = f + 1
        print(f , len(tab))

while True:
	for u in urls:
		if autochecker(u) == 0:
			print(currentTime(), "Trigerred")
			info = content[urls.index(u)]
			sendingMail(tab,info)
			print(currentTime(), "Something instock, sending mail...")
		time.sleep(random.uniform(3,5.4))



