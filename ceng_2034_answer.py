#!/usr/bin/python3
import requests
import os, threading
from multiprocessing import Pool
import multiprocessing


#Part1
print(os.getpid(),"is pid of itself.") 
print(os.getloadavg(),"1 minute,","5 minute,","15 minute")
load1, load5, load15 = os.getloadavg()
print(load5, "is 5 min average.")
print(multiprocessing.cpu_count(),"is core number.")
nproc = multiprocessing.cpu_count()
if(nproc - load5 < 1):
	exit()

def url_check(url):                        
	print("checking url working or down...", url,)
	r = requests.get(url)                             #to request data from the server.
	if (r.status_code/200 < 1.495):		          #if status code smaller than 299 link is ok
		print("This link is valid----> ", url,"PID:",os.getpid())
	else:
		print("This link is not working----->", url,"PID:",os.getpid())





thread1 = threading.Thread(target=url_check, args=("https://api.github.com",))
thread2 = threading.Thread(target=url_check, args=("http://bilgisayar.mu.edu.tr",))
thread3 = threading.Thread(target=url_check, args=("https://python.org",))
thread4 = threading.Thread(target=url_check, args=("http://akrepnalan.com/ceng2034",))
thread5 = threading.Thread(target=url_check, args=("https://github.com/caesarsalad/wow",))


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

