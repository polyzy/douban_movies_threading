# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import threading
import Queue
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

queue = Queue.Queue()
THREAD_NUM = 4
class MyThread(threading.Thread):
	def __init__(self,thread_id,num):
		super(MyThread,self).__init__()
		self.thread_id = thread_id
		self.num = num
	def run(self):
		global queue
		while not queue.empty():
			url = queue.get()
			crawler(url,self.num,self.thread_id)
			queue.task_done()

def crawler(url,top_num,thread_id):
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	for movie in soup.find_all('a',{"class":"title"}):
		with open("/home/smart/data.txt","a+") as f:
			film_list = str(top_num)+" : "+movie.text+"#####"+str(thread_id)+'\n'
			f.write(film_list)
		top_num += 1
	try:
		next_page = soup.find_all("span",{"class":"next"})[0].find("a")['href']
		next_page_url = "http://www.douban.com/tag/2011/movie" + next_page
		time.sleep(3)
		if top_num < 100:
			return crawler(next_page_url,top_num,thread_id)
	except TypeError:
		print "This is the last page"

def main():
	top_num = 1
	global queue
	threads = []
	url = "http://www.douban.com/tag/%d/movie"
	years = [2011,2012,2013,2014]
	for i in years:
		queue.put(url%i)
	for i in range(THREAD_NUM):
		thread = MyThread(i,top_num)
		thread.start()
		threads.append(thread)
	for thread in threads:
		thread.join()
	queue.join()


if __name__ == "__main__":
	a=time.time()
	main()
	b=time.time()
	print b-a	#23.539265871