from bs4 import BeautifulSoup
import urllib

dict_tv = {}

base_url = "http://www.tvsubtitles.net/tvshows.html"

url_obj = urllib.urlopen(base_url).read()
soup = BeautifulSoup(url_obj, "lxml")
links = soup("a")

for i in links:
	temp=i.get('href')
    	if("tvshow-" in str(temp)):
		name = i.text
		name = name.lower()
		temp = temp[7:]
		code = temp.partition("-")[0]
		#print name + " " + code
		dict_tv[name] = code

#print dict_tv
