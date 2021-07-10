import urllib.request, urllib.parse, urllib.error

url = 'http://www.dr-chunk.com/page1.html'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
