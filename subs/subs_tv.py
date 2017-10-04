import requests
from bs4 import BeautifulSoup
from list_tv import dict_tv
import os
import urllib
import urllib2
import zipfile

def begin_extraction(pack_url, dl_url):
	print dl_url
	print pack_url
	request = urllib2.urlopen( dl_url )

	#save
	file_name = name + "_season_" + season + ".zip"
	output = open(file_name, "w")
	output.write(request.read())
	output.close()
	ubu_desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
	#win_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  
	current_path = os.path.dirname(os.path.abspath(__file__)) + "/" + file_name
	file_path = ubu_desktop + "/" + str(name) + "_subtitles_season_" + season
	if not os.path.exists(file_path):
		os.makedirs(file_path)
	zip_ref = zipfile.ZipFile(current_path, 'r')
	zip_ref.extractall(file_path)
	zip_ref.close()
	print "Subtitles downloaded on your desktop  ^_^  "

base_url = "http://www.tvsubtitles.net/"
sub_url = "www.tvsubtitles.net/"
name = raw_input("Enter the name of the TV show - ")
if name not in dict_tv:
	print "TV show does not exists. Please try again.";

if name in dict_tv:
	season = raw_input("Enter the season number of the tv show(must be a valid integer) - ")
	url = base_url + "tvshow-" + dict_tv[name] + "-" + season + ".html"
	pack_url = base_url + "subtitle-" + dict_tv[name] + "-" + season + "-en.html"
	dl_url = base_url + "download-" + dict_tv[name] + "-" + season + "-en.html"
	pack_html = urllib.urlopen(pack_url).read()
	pack_soup = BeautifulSoup(pack_html, "lxml")
	text = pack_soup("td")
	
	all_available = 0
	checker = season + "x01"
	for i in text:
		if(i.get('width' == "70%")):
			print "oka"
			if(str(checker) in str(i.contents[0])):
				all_available = 1
	
	if all_available == 1:
		print "OK report!!"
		begin_extraction(pack_url, dl_url)
	else:
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, "lxml")
		link = soup("a")
		
		list_sub = []	
	
		for i in link:
			temp = i.get('href')	
			if("subtitle-" in str(temp) and "/en.gif" in str(i.contents[0])):
				list_sub.append(temp)
		
		for j in list_sub:
			pack_temp_url = base_url + str(j) 
			temp = j[8:]
			temp_url = base_url + "download" + str(temp)
			begin_extraction(pack_temp_url, temp_url)
		
		#print url
		#print dict_tv[name]	
