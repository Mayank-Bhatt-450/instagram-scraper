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
#`````````````````````````````````````````````````````````````
#GVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVG
likecommentflaglist=[]
#GVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVGVG
#####################DEFINATIONS##############################
def findandclick(xpath='//*'):
    global driver
    try:
        elem = WebDriverWait(driver, 60).until(
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
        elem = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH,xpath))
        )
    except:
        print('ERROR OCCOUR WHILE SEARCHING ',xpath)
        return
    return elem
###################
###################
def unfollow(person=''):
    global driver
    if person!='':
        driver.get("https://www.instagram.com/"+str(person)+"/")
    findandclick("//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P   ']")
    findandclick('//button[@class="aOOlW -Cab_   "]')
###################
        
def scrape_followers(driver, account):
    global last,unfollowlist
    input('in')
    # Load account page
    #'''
    # Click the 'Follower(s)' link
    driver.get("https://www.instagram.com/"+account+"/")
    #driver.find_element_by_partial_link_text("follower").click()
    waiter.find_element(driver, "//a[@href='/"+account+"/following/']", by=XPATH).click()
    time.sleep(1)
    # Wait for the followers modal to load
    waiter.find_element(driver, "//div[@role='dialog']", by=XPATH)
    #scroll for perfect location
    name=waiter.find_element(driver, 'ul div li:nth-child(12)')
    driver.execute_script("arguments[0].scrollIntoView();", name)
    time.sleep(2)
    name=waiter.find_element(driver, 'ul div li:nth-child(22)')
    driver.execute_script("arguments[0].scrollIntoView();", name)
    
    #'''
    
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
    
    for i in range(1,61):
        fullelement=waiter.find_element(driver,'ul div li:nth-child({})'.format(i))
        name=waiter.find_element(fullelement, follower_css.format(i))
        driver.execute_script("arguments[0].scrollIntoView();", fullelement)
        user=name.text
        if user  in unfollowlist:
            print(name.text)
            findandclick('//li['+str(i)+']//div[1]//div[2]//button[1]')
            #findandclick('//button[@class="aOOlW -Cab_   "]')
            time.sleep(5)
            findandclick("//button[contains(text(),'Unfollow')]")
            #lists.append(name.text)
            #last.append(name.text)
            count+=1
        time.sleep(10)
    
        #count+=1

        # Instagram loads followers 12 at a time. Find the last follower element
        # and scroll it into view, forcing instagram to load another 12
        # Even though we just found this elem in the previous for loop, there can
        # potentially be large amount of time between that call and this one,
        # and the element might have gone stale. Lets just re-acquire it to avoid
        # that
        
    #print(likecommentflaglist)
    
    #post_len=len(elem)
    #driver.get("https://www.instagram.com/"+str(elem[random.randint(0,post_len-1)]))
    #findandclick('//span[@aria-label="Like"]')
    #print('licked')
###################

    
##############################################################

################SETUP CHROME AS MOBILE#########################


def login(PROXY=''):
    global driver
    if PROXY!='':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome()

    
    username = "@gmail.com"  # <username here>
    password = ""  # <password here>
    driver.get("https://www.instagram.com/accounts/login/")

    username = 'gmail.com' #your username
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
##############################################################

####################LOGIN SECTION#############################

#findandclick('//button[@class="GAMXX"]')
#findandclick('//div[@class="mt3GC"]/button[@class="aOOlW   HoLwm "]')
#findandclick('//div[@class="                  Igw0E     IwRSH        YBx95      vwCYk                                                                                                               "]/a[@href="/"]')
#findandclick('//div[@class="mt3GC"]/button[@class="aOOlW   HoLwm "]')
#elem = driver.find_element_by_xpath('//div[@class="q02Nz _0TPg"]/span[@class="glyphsSpriteNew_post__outline__24__grey_9 u-__7"]')
driver=''
g=open('unfollow.txt','r')
unfollowlist=g.read().split('\n')
unfollowlist=unfollowlist[:len(unfollowlist)-1]
prxi=['116.203.127.92:3128','116.202.51.30:3128','202.134.191.156:8080','116.202.105.177:9050','']

login()
print('login succcessed...')

scrape_followers(driver, 'delhi_waali_baatcheet')
print('khatm')
#elem.click()
#elem.send_keys('F:Untitled (2).jpg')

##############################################################
#driver.get("https://www.instagram.com/kartikaaryan/")
#elem = driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]')

#elem.click()
#elem = driver.find_element_by_xpath('//div[@class="q02Nz _0TPg"]/span[@class="glyphsSpriteNew_post__outline__24__grey_9 u-__7"]')
#^find + button
#xpath('//button[contain(text(),'lol')]')

#///////////////////////
'''
follow('ranveersingh')
like()
comment()
unfollow('ranveersingh')
driver.get("https://www.instagram.com/kartikaaryan/")
'''
#///////////////////////
#memedekh
#https://www.instagram.com/trolls_official/followers/

'''
for i in unfollowlist:
    unfollow(i)
    time.sleep(30)

'''

