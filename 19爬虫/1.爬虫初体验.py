
import urllib2

# request = urllib2.urlopen('http://www.baidu.com')
# print(request.read())

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

request = urllib2.Request('http://www.baidu.com',headers = headers)

response = urllib2.urlopen(request)

html = response.read()
