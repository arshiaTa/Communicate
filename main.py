import codecs
import urllib.request

html_res = urllib.request.urlopen('https://www.wikipedia.org/')
html_content = html_res.read()
file = codecs.open("ServerFile/www.wikipedia.org.html", "w", "utf-8")
file.write(html_content.decode())
file.close()
