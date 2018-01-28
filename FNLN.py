import argparse
import urllib.request
import re
from html.parser import HTMLParser
import requests

import datetime
from time import sleep

# define
WAIT= ["1", "4", "7"]
TRY= ["5", "6", "8", "9"]
GO= ["2", "3"]

# parse arguments
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--location", action="store", dest="location", help="Set forecast location")
location= parser.parse_args().location
url = 'http://norway-lights.com/'+location+'/'



#notify
def notification(message):
    report = {"value1": location, "value2": message, "value3": url}
    print(requests.post("https://maker.ifttt.com/trigger/forecast_result/with/key/clihE0CsNV7v92HFy0awnMSfmZYYmTaBAaJmNeWNeIn", data=report))


def get_forecast():
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

class MyHTMLParser(HTMLParser):
    attrs_figure= ""
    def handle_starttag(self, tag, attrs):
        if tag == "figure":
            self.attrs_figure= attrs
            #print (attrs)
    def get_attrs(self):
        return self.attrs_figure

def send_notify():
    print(datetime.datetime.now().time())
    parser = MyHTMLParser()
    parser.feed(get_forecast())
    forecast_text= parser.get_attrs()[0][1]

    print(forecast_text[18])
    if forecast_text[18] in GO:
        print("GO")
        notification("GO")
    elif forecast_text[18] in TRY:
        print("TRY")
        notification("TRY")
    else:
        print("WAIT")
        #notification("WAIT")
while datetime.datetime.now().time().minute!=0:
    sleep(60)
while 1:
    if datetime.datetime.now().time().hour <= 7:
        send_notify()
    sleep(3600)
