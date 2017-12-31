import urllib.request
import urllib.parse

##x = urllib.request.urlopen('https://www.google.com')
##print(x.read())

url = 'https://pythonprogramming.net'
values = {'s':'basic'
          }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)

try:
    print('''
.
.
.
.
.
.
.

.
..

..

.
'''
)
    x = urllib.request.urlopen('https://www.google.co.in/search?=q=test')
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?=test'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0'

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeader.txt','w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))

    
    
