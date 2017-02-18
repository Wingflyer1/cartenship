import urllib.request
import urllib.parse
import re
from datetime import datetime, date

url = 'https://themoneyconverter.com/NOK/Exchange_Rates_For_Norwegian_Krone.aspx'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
respData = respData.splitlines()

pat = [(re.compile(r'NOK to EUR</td><th>(.*?)</th>')),
       (re.compile(r'NOK to USD</td><th>(.*?)</th>')),
       (re.compile(r'NOK to DKK</td><th>(.*?)</th>')),
       (re.compile(r'NOK to SEK</td><th>(.*?)</th>')),
       ]
results = []

currencies = ['EUR',
              'USD',
              'DKK',
              'SEK',
              ]

results.append(datetime.datetime.now())

for i in range(0, len(pat)):
	result = re.findall(pat[i], str(respData))
	res = result[0]
	curr = str(currencies[i])
	results.append([res])

def write_currencies():
	f = open('currencies.txt','w')
	for i in results:
		f.write(str(i)+'\n')
	f.close()

write_currencies()

f = open('currencies.txt', 'r')
b = f.read()
