import itertools

from explicit import waiter, XPATH
from selenium import webdriver
import time,random
from selenium import webdriver
#`````````````````````````````````````````````````````````````
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#`````````````````````````````````````````````````````````````
from instapy_cli import client#post api
#`````````````````````````````````````````````````````````````
from bs4 import BeautifulSoup
import requests
#q=open('Foutput.txt','w')
#q.close()
q=open('new following above 2m.txt','r')
last=q.read().split('\n')
q.close()
def convert(r):
    r=r.replace(',','')
    if '.'in r:
        if 'k'in r:
            r=str(int(float(r.replace('k',''))*1000))
        if 'm' in r:
            r=str(int(float(r.replace('m',''))*1000000))
    else:
        if 'k'in r:
            r=r.replace('k','000')
        if 'm'in r:
            r=r.replace('k','000000')
    return r
def findandclick(driver,xpath='//*',t=10):
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ',xpath)
        return        
    elem.click()
def login(driver):
    username = '@gmail.com' #your username
    password = '' #your password
    driver.get("https://www.instagram.com/accounts/login/")
    try:
        elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//input'))
            )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ','//input')
    elem = driver.find_elements_by_xpath('//input')
    elem[0].send_keys(username)
    elem[1].send_keys(password)
    elem[1].send_keys(Keys.RETURN)
    findandclick('//button[@class="aOOlW   HoLwm "]')


def append(file,l):
    a=open(file,'a+')
    for i in l:
        a.write(i+'\n')
    a.close()
def freshtab():
    global driver
    main_window = driver.current_window_handle

    driver.execute_script("window.open();")

    driver.switch_to_window(main_window)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    
def delete(element):
    driver.execute_script(
    '''
    var element = arguments[0];
    element.parentNode.removeChild(element);
    '''
    , element)
getdelcount=0
getdellist=[]
def getdel(driver,file):
    global getdelcount,getdellist
    
    xpath="/html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/div[1]/div["+str(1)+"]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]"
    #      /html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/div[1]/div[1         ]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]
    #      /html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/div[1]/div[2         ]/div[2]/div[1]/div[1]/a[1]/div[1]/div[1]/div[1]
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
        p=elem.text
        if getdelcount%10==0:
            append(file,getdellist)
            getdellist=[]
        else:
            getdellist.append(p)
        
    except:
        print('--ERROR OCCOUR WHILE SEARCHING ',xpath)
        return 0
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    delete(driver.find_element_by_xpath("//html[1]/body[1]/span[1]/section[1]/main[1]/div[1]/div[1]/div["+str(1)+"]"))
    getdelcount+=1

def resetpage(driver,i):
    driver.get(i)
    findandclick(driver,"//div[contains(text(),'Not Now')]")
    drive=driver.find_element_by_xpath("//div[@class='Nm9Fw']/a/span")
    co=int(convert(drive.text))
    findandclick(driver,"//a[@class='zV_Nj']")
    return co
def scrape_followers(driver, postlist):
    
    for i in range(3):
        print('lol')
        driver.switch_to_window(driver.window_handles[i])
        driver.execute_script("window.open();")
    
    driver.switch_to_window(driver.window_handles[3])
    driver.close()
    driver.switch_to_window(driver.window_handles[0])

    count=3
    lenlist=[0,0,0]
    present=2
    a=0;b=1;c=2
    flag=[0,0,0]
    k=0
    while k<count:
        #print('in')
        print(k,k*3)
    
        if  (a!='' and lenlist[0]>=k):
            print('a')
            driver.switch_to_window(driver.window_handles[0])
            
            if flag[0]==0:
                co=resetpage(driver,postlist[a])
                lenlist[0]=co
                if count<co+k:
                    count=co+k
                flag[0]=1
            
            if getdel(driver,'a-output.txt') ==0:
                if present!=len(postlist)-1:
                    present+=1
                    a=present
                    flag[0]=0
                else:
                    a=''
        
        if  (b!='' and lenlist[1]>=k):
            driver.switch_to_window(driver.window_handles[1])
            
            if flag[1]==0:
                co=resetpage(driver,postlist[b])
                lenlist[1]=co
                if count<co+k:
                    count=co+k
                flag[1]=1
            
            if getdel(driver,'b-output.txt') ==0:
                if present!=len(postlist)-1:
                    present+=1
                    b=present
                    flag[1]=0
                else:
                    b=''
        if  (c!='' and lenlist[2]>=k):
            driver.switch_to_window(driver.window_handles[2])
            
            if flag[2]==0:
                co=resetpage(driver,postlist[c])
                lenlist[2]=co
                if count<co+k:
                    count=co+k
                flag[2]=1
            
            if getdel(driver,'c-output.txt') ==0:
                if present!=len(postlist)-1:
                    present+=1
                    c=present
                    flag[2]=0
                else:
                    c=''
        k+=1
        

    
account = '404bhatt'
packed_extension_path = 'extension_5_0_8_0.crx'
mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

chrome_options.add_extension(packed_extension_path)
driver = webdriver.Chrome(chrome_options=chrome_options)
login(driver)
#///
postlist=[
'https://www.instagram.com/p/B32IEegBC089jAKtFmh-OWwtev55NVK3_kN8c80/',
'https://www.instagram.com/p/B310oDVlNcmqk592KWSc3ZYtDscPtuleqtEH_A0/',
'https://www.instagram.com/p/B32e0RtByUYx5Ekbh2wbJrK7lZyaykzC0J4JKs0/',
'https://www.instagram.com/p/B33abo-HR1QOl6NcTx5A464xkx3QbvvVddTMvo0/',
'https://www.instagram.com/p/B33dwAzAPgYALRYjMbifKQiuB7txBFpTmUvnHw0/']

postlist1=["https://www.instagram.com/p/B31HuZ1A5nE/",
"https://www.instagram.com/p/B31HuZ1A5nE/",
"https://www.instagram.com/p/B3w2lbnAMQd/"]
scrape_followers(driver, postlist)



        





input('ended')
