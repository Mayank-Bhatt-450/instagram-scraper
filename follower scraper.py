import itertools
import os

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
q=open('output.txt','r')
last=q.read().split('\n')
q.close()
def freshtab():
    global driver
    main_window = driver.current_window_handle

    driver.execute_script("window.open();")

    driver.switch_to_window(main_window)
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
def findandclick(xpath='//*'):
    global driver
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ',xpath)
        return        
    elem.click()
def createdriver():
    global driver
    driver = webdriver.Chrome()
def login(PROXY=''):
    global driver
    username = "@gmail.com"  # <username here>
    password = ""  # <password here>
    driver.get("https://www.instagram.com/accounts/login/")

    username = '@gmail.com' #your username
    password = '' #your password
    driver.get("https://www.instagram.com/accounts/login/")
    try:
        elem = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH,'//input'))
            )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ','//input')
    elem = driver.find_elements_by_xpath('//input')
    elem[0].send_keys(username)
    elem[1].send_keys(password)
    elem[1].send_keys(Keys.RETURN)
    findandclick('//button[@class="aOOlW   HoLwm "]')
    #input('----=---')
    '''

    waiter.find_write(driver, "//div/input[@name='username']", username, by=XPATH)
    waiter.find_write(driver, "//div/input[@name='password']", password, by=XPATH)
    waiter.find_element(driver, "//div/button[@type='submit']", by=XPATH).click()
    '''

    # Wait for the user dashboard page to load
    #waiter.find_element(driver, "//a/span[@aria-label='Find People']", by=XPATH)
def append(l):
    a=open('output.txt','a+')
    for i in l:
        a.write(i+'\n')
    a.close()
def doneappend(l):
    a=open('Doneuser.txt','a+')
    for i in l:
        a.write(i+'\n')
    a.close()
def delete(element):
    driver.execute_script(
    '''
    var element = arguments[0];
    element.parentNode.removeChild(element);
    '''
    , element)
def scrape_followers(driver, account):
    global last
    print('in')
    # Load account page
    try:
        driver.get("https://www.instagram.com/{0}/".format(account))
        "//div/div[2]/div[1]/div[2]"

        # Click the 'Follower(s)' link
        # driver.find_element_by_partial_link_text("follower").click()
        waiter.find_element(driver, "//a[@href='/"+account+"/followers/']", by=XPATH).click()
        time.sleep(1)
        # Wait for the followers modal to load
        waiter.find_element(driver, "//div[@role='dialog']", by=XPATH)
        #scroll for perfect location
        time.sleep(3)
        try:
            drive.find_element_by_xpath('//div/[@class="_7UhW9   xLCgt      MMzan  KV-D4        uL8Hv         "]')
            input('followers not showing')
        except:
            print('followers are showing and scrapping is started....')
            pass
        name=waiter.find_element(driver, 'ul div li:nth-child(12)')
        driver.execute_script("arguments[0].scrollIntoView();", name)
        time.sleep(2)
        name=waiter.find_element(driver, 'ul div li:nth-child(22)')
        driver.execute_script("arguments[0].scrollIntoView();", name)
    except:
        return('follower not found')
    
    #driver.execute_script("window.scrollTo(0, 100000);",'')#driver.execute_script('window.scrollBy(0,500)','')
    #input('-++++++')

    # At this point a Followers modal pops open. If you immediately scroll to the bottom,
    # you hit a stopping point and a "See All Suggestions" link. If you fiddle with the
    # model by scrolling up and down, you can force it to load additional followers for
    # that person.

    # Now the modal will begin loading followers every time you scroll to the bottom.
    # Keep scrolling in a loop until you've hit the desired number of followers.
    # In this instance, I'm using a generator to return followers one-by-one


    follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    count=1
    timetaken=time.time()
    lists=[]
    try:
        for i in range(1,16):
            name=waiter.find_element(driver, follower_css.format(i))
            user=name.text
            if user not in last:
                #print(name.text)
                lists.append(name.text)
                last.append(name.text)
                count+=1
    except:
        print('error occour before 16th element')
        pass
        
    while True:
        for ok in range(2):
                try:
                    fullelement=waiter.find_element(driver,'ul div li:nth-child(16)')
                    name=waiter.find_element(fullelement, follower_css.format(16))
                    break
                except:
                    print('error' ,ok)
                    time.sleep(1)
        try:
            user=name.text
            if user not in last:
                lists.append(name.text)
                last.append(name.text)
                count+=1
                #print(name.text)
            delete(fullelement)
        except:
            print('error user ended..')
            a=time.time()
            print('\ntime taken for ',count,'users=',a-timetaken,'\n\n')
            print('___________________________________________________')
            append(lists)
            lists=[]
            return
            break
        if count%12==0:
            time.sleep(0.6)
        
        if count%1000==0:
            a=time.time()
            print('\ntime taken for ',count,'users=',a-timetaken)
            
            timetaken=a
            append(lists)
            lists=[]
        #count+=1

        # Instagram loads followers 12 at a time. Find the last follower element
        # and scroll it into view, forcing instagram to load another 12
        # Even though we just found this elem in the previous for loop, there can
        # potentially be large amount of time between that call and this one,
        # and the element might have gone stale. Lets just re-acquire it to avoid
        # that
def destroy(driver):
    driver.close()
account = 'trolls_official'
driver = ''
#/////////////
k=open('new following above 1m.txt','r')
ulist=k.read().split('\n')
k.close()

prxi=['']
cnt=0
phase=0
createdriver()
login()
while phase<len(ulist):
    ik=ulist[phase]
    f=prxi[0]
    print(ik,'proxy=',f)
    freshtab()
    fo=scrape_followers(driver, ik)
    time.sleep(60)
    phase+=1
    '''
    if cnt%5==0:
        driver.quit()
        createdriver()
        login()
    '''
    cnt+=1    
    doneappend([ik])
    
    #driver.quit()
    #driver.close()
    #destroy(driver)



        





input('ended')
