import urllib.request


page = urllib.request.urlopen('http://example.com')
text = page.read().decode('utf8')
start_at = text.find('<h1>') + 4
stop_at = text.find('</h1>')
print(start_at)
print(stop_at)
result = text[start_at:stop_at]
print(result)
