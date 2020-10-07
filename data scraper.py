#`````````````````````````````````````````````````````````````

import time,random,os
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
#`````````````````````````````````````````````````````````````
from datetime import datetime


#data=''' <a href="/p/B3yrWs7JrZ6/" class="focus-visible" data-focus-visible-added=""><div class="eLAPa"><div class="KL4Bh"><img class="FFVAD" decoding="auto" sizes="293px" srcset="https://instagram.fdel5-1.fna.fbcdn.net/vp/3b5ca96fe767331443d91755b713e91b/5DAD607D/t51.2885-15/e35/s150x150/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102 150w,https://instagram.fdel5-1.fna.fbcdn.net/vp/24f1456531c56b1b18bf58e71ec6b502/5DAD5490/t51.2885-15/e35/s240x240/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102 240w,https://instagram.fdel5-1.fna.fbcdn.net/vp/766265de39f8f63b74264e2d42fd1f18/5DAD2183/t51.2885-15/e35/s320x320/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102 320w,https://instagram.fdel5-1.fna.fbcdn.net/vp/06a18fd3abf38e632245a51105ee1aa1/5DAD3238/t51.2885-15/e35/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102 480w,https://instagram.fdel5-1.fna.fbcdn.net/vp/06a18fd3abf38e632245a51105ee1aa1/5DAD3238/t51.2885-15/e35/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102 640w" src="https://instagram.fdel5-1.fna.fbcdn.net/vp/06a18fd3abf38e632245a51105ee1aa1/5DAD3238/t51.2885-15/e35/72701790_928582860837578_13275829055018776_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&amp;_nc_cat=102" style="object-fit: cover;"></div><div class="_9AhH0"></div></div><div class="u7YqG"><span aria-label="Video" class="mediatypesSpriteVideo__filled__32 u-__7"></span></div><div class="qn-0x" style="background-color: rgba(0, 0, 0, 0.3);"><ul class="Ln-UN"><li class="-V_eO"><span>1,669</span><span class="_1P1TY coreSpritePlayIconSmall"></span></li><li class="-V_eO"><span>6</span><span class="_1P1TY coreSpriteSpeechBubbleSmall"></span></li></ul></div></a>'''
#soup = BeautifulSoup(data, 'lxml')#.find_element_by_xpath('//div[1]/div[1]/img')
#srcc=soup.find('img')['src']#img.get_attribute("src")
#input('start'+srcc)
#"""
packed_extension_path = 'extension_5_0_8_0.crx'

options = Options()
options.add_extension(packed_extension_path)
driver = webdriver.Chrome(options=options)
#ZIP
'''
unpacked_extension_path = 'chorpath.zip'

options = Options()
options.add_argument('--load-extension={}'.format(unpacked_extension_path))
driver = webdriver.Chrome(options=options)
'''

#driver = webdriver.Chrome('chromedriver.exe',chrome_options = chrome_options)
#driver=webdriver.Chrome()
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
###################
def findit(xpath='//*'):
    global driver
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ',xpath)
        return
    return elem
def imagedownload(link):
    count=0
    times=str(str(datetime.utcnow()).split(' ')[0])
    f=os.listdir('.\\data')
    k=0
    pth=os.getcwd()
    while True:
        g=times+"#"+str(k)+'.jpg'
        if  g in f:
           k+=1
        else:
            f = open(pth+'\\data\\'+g,'wb')
            f.write(requests.get(link).content)
            f.close()
            #print(pth+'\\data\\'+g,"PNG")
            break
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
            
def test(account,link):
    global driver
    driver.get("https://www.instagram.com/"+account+"/")
    try:
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//a[@href="/'+account+'/followers/"]/span'))
        )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ','//a[@href="/'+account+'/followers/"]/span')
    follower=convert(driver.find_element_by_xpath('//a[@href="/'+account+'/followers/"]/span').text)
    postlist=[]
    meta_postlist=[]
    
    #driver.find_element_by_tag_name('body').send_keys(Keys.END)
    for i in range(14):
        driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
    while True:
        driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
        elem=driver.switch_to.active_element#.get_attribute('outerHTML'))
        soup = BeautifulSoup(elem.get_attribute('outerHTML'), 'lxml')#.find_element_by_xpath('//div[1]/div[1]/img')
        #src=soup.find('img')['src']
        #'''
        try:
            src=soup.find('img')['src']#img.get_attribute("src")
        except:
            print(soup)
        #'''
        #print(src,'\n',)#elem.get_attribute('outerHTML'),'\n')
        
        if src ==link:
            return([postlist,meta_postlist])
        else:
            pass
        
        while True:
            try:
                action = webdriver.ActionChains(driver)
                action.move_to_element(elem).perform()
                break
            except:
                print('error')
        
        for k in range(10):
            try:
                li=int(convert(driver.find_element_by_xpath(
                "//div[contains(@class,'qn-0x')]/ul/li[1]/span[1]").text))
                #print(li)
                likes=float(li/int(follower))*100
                co=int(convert(driver.find_element_by_xpath(
                "//div[contains(@class,'qn-0x')]/ul/li[2]/span[1]").text))
                comments=float(co/int(follower))*100
                postlist.append(src)
                meta_postlist.append(str(likes+comments))
                #input('-==-=-=-=--=-=-')
                print( likes,comments)    
                break

            except:
                pass
                #continue
                print('except',driver.switch_to.active_element.get_attribute('outerHTML'))
        if "PlayIcon" in driver.find_element_by_xpath(
                "//div[contains(@class,'qn-0x')]").get_attribute('outerHTML'):
            print('vid',src)
            continue
        






        

##############################################################

####################LOGIN SECTION#############################
username = '@gmail.com' #your username
password = '' #your password
#post_api=client(username, password)#---------
#///////////////////////

#post(image='video.mp4')
#post()
#story()
#input('posted')
#///////////////////////
driver.get("https://www.instagram.com/accounts/login/")
#printing code
#elem = driver.find_element_by_xpath("//*")
#source_code = elem.get_attribute("outerHTML")
#print(source_code)
#elem[0].click()
#elem[0].clear()

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


#findandclick('//button[@class="GAMXX"]')
#findandclick('//div[@class="mt3GC"]/button[@class="aOOlW   HoLwm "]')
#findandclick('//div[@class="                  Igw0E     IwRSH        YBx95      vwCYk                                                                                                               "]/a[@href="/"]')
findandclick('//div[@class="mt3GC"]/button[@class="aOOlW   HoLwm "]')
account='fitness_importances'
yesterdaylink='https://instagram.fdel5-1.fna.fbcdn.net/vp/20ffea9a5482b4422f1ca1178a9283b2/5E622EF5/t51.2885-15/sh0.08/e35/c0.104.1080.1080a/s640x640/72228003_675366532956455_8180832426578930069_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&_nc_cat=111'
#'https://instagram.fdel5-1.fna.fbcdn.net/vp/b1d50b692b6b3a664045b7eb29eafa30/5DABB43F/t51.2885-15/e35/71104795_337058133757339_7659983051926051984_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&_nc_cat=107'
#'https://instagram.fdel5-1.fna.fbcdn.net/vp/a6fdcc84d7fd94f7d53bb85ee333decf/5E4381A1/t51.2885-15/sh0.08/e35/c0.126.1080.1080a/s640x640/72103563_194987291531880_3576645070766579456_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&_nc_cat=100'
#'https://instagram.fdel5-1.fna.fbcdn.net/vp/20ffea9a5482b4422f1ca1178a9283b2/5E622EF5/t51.2885-15/sh0.08/e35/c0.104.1080.1080a/s640x640/72228003_675366532956455_8180832426578930069_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&_nc_cat=111'


#print(targetpostscraper(account,yesterdaylink))
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#//////
def top15(account,link):
    print(test(account,link))
link='https://instagram.fdel5-1.fna.fbcdn.net/vp/f18f6cce58a9c61b144d4a8facb5bf0f/5E275BB1/t51.2885-15/sh0.08/e35/s640x640/67690317_1107649732957967_2669064926208894720_n.jpg?_nc_ht=instagram.fdel5-1.fna.fbcdn.net&_nc_cat=111'
top15(account,link)
#//////
#driver.quit()
#"""
