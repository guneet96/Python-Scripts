from bs4 import BeautifulSoup as bs
import urllib

base = "http://www.ssbcrack.com/2013/11/word-association-test-negative-words.html"
flag = 0
negl = []	
urlobj = urllib.urlopen(base).read()
soup = bs(urlobj, "lxml")

ltag = soup("li")

for i in ltag:
	if i.text == "Anger":
		flag = 1
	
	if flag:
		negl.append(str(i.text))
		
	if i.text == "Worthless/Zero":
		flag = 0

#print negl



