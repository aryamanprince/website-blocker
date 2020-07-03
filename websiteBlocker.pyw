# -*- coding: utf-8 -*-
import time
from datetime import datetime as d
#host path
host_path="C:\Windows\System32\drivers\etc\host"
#local ip
redirect = "127.0.0.1"
website_list=["facebook.com","twitter.com","cnn.com"] # websites to be blocked

while True:
    #time of work
    if d(d.now().year,d.now().month,d.now().day,8) < d.now() < d(d.now().year,d.now().month,d.now().day,17):
        print("Working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content: #checks if website is website to be blocked
                    pass #do nothing
                else:
                    #map hostnames to your local ip address
                    file.write(redirect+" "+website+"\n")
                    
    else:
        print("Non working hours....")
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0) #seeks the current position in file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #resizes the file to current position in file
    time.sleep(5)