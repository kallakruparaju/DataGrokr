import urllib.request, urllib.error, urllib.parse
import re
from bs4 import BeautifulSoup


print("please enter the url")
url = input()

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent)
print(soup.get_text())