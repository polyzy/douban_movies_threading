import requests
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def crawler(url,top_num):
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	for movie in soup.find_all('a',{"class":"title"}):
		print top_num, movie.text
		with open("/home/smart/data1.txt","a+") as f:
			film_list = str(top_num)+" : "+movie.text+'\n'
			f.write(film_list)
		top_num += 1
	try:
		next_page = soup.find_all("span",{"class":"next"})[0].find("a")['href']
		next_page_url = "http://www.douban.com/tag/2011/movie" + next_page
		time.sleep(3)
		if top_num < 100:
			return crawler(next_page_url,top_num)
	except TypeError:
		print "This is the last page"

def main():
	years = [2011,2012,2013,2014]
	top_num = 1
	for year in years:
		start_url = "http://www.douban.com/tag/%d/movie"%year
		crawler(start_url, top_num)


if __name__ == "__main__":
	a = time.time()
	main()
	b =time.time()
	print "###########################3"
	print b-a	#92.4774909019