import argparse
import urllib.request
import re

from html.parser import HTMLParser

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--location", action="store", dest="location", help="Set forecast location")
parser.add_argument("-e", "--email", action="store", dest="email", help="address")
#parser.parse_args()

print(parser.parse_args().email)
WAIT= ["1", "4", "7"]
TRY= ["5", "6", "8", "9"]
GO= ["2", "3"]


url = 'http://norway-lights.com/'+parser.parse_args().location+'/'
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
#print(mystr)


class MyHTMLParser(HTMLParser):
    attrs_figure= ""
    def handle_starttag(self, tag, attrs):
        if tag == "figure":
            self.attrs_figure= attrs
            #print (attrs)
    def get_attrs(self):
        return self.attrs_figure

parser = MyHTMLParser()
parser.feed(mystr)
forecast_text= parser.get_attrs()[0][1]

print(forecast_text[18])
if forecast_text[18] in GO:
    print("Go")
elif forecast_text[18] in TRY:
    print("Try")
else:
    print("Wait")

"""
with urllib.request.urlopen() as response:
    html = response.read()
    #print(html)
    print(type(html))
    m= re.match(r"<figure class=\"forecast forecast-([1-9])\">", html+"")
    #m= re.search(r"forecast-([1-9])", 'sfsdfssdf forecast-7 sddsfdsf')
    
    print(m.group(1))
"""