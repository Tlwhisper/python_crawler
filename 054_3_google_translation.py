import urllib.request
import urllib.parse

url = 'https://play.google.com/log?format=json&hasfast=true'
data = {}



response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
