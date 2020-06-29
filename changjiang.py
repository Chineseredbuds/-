#coding:utf8
import datetime
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import csv
from tkinter import *

def doSth(url,csvname,elements,attr):
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = Firefox(executable_path='geckodriver', options=options)
    time.sleep(2)
    url=url
    driver.get(url)
    time.sleep(2)
    html=driver.page_source
    elements=elements

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll(elements,{attr:"sssq"})[0]
    if table is None:
        print("no table");
        exit(1)
    rows = table.findAll("tr")
    #print(rows)

    csvFile = open(csvname,'at+',newline='',encoding='utf-8')
    writer = csv.writer(csvFile)
    nowtime = datetime.datetime.now()

    if nowtime.day==1:
    	time_now=datetime.datetime.now().strftime("%Y-%m-%d")
    	writer.writerow([time_now])
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)

    finally:
        csvFile.close()
        driver.quit()
    return 0

 

def main():
    '''
    tk = Tk()
    canvas = Canvas(tk,width = 200, height = 200)
    canvas.pack()
    canvas.create_text(100,40,text = "running",fill = "blue",font = ("Times",16))

    #canvas.create_rectangle(10,70,190,130)
    tk.mainloop()
    '''

    m=20
    url2='http://www.cjh.com.cn/sssqcwww.html'
    csvname1="changhjiang.csv"
    url1='http://120.202.31.240/sqindex.html'
    csvname2="changhjiang2.csv"
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        #hour=[8,9,12,16,20]
        #for h in  hour:
            #if now.hour == h and now.minute == m:
        if now.minute == m:
            doSth(url1,csvname1,"table","class")
            doSth(url2,csvname2,"tbody","id")
                
                
        time.sleep(60)
    
 
main()
