from selenium import webdriver
import sys
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
print("登录")
url = 'http://codeforces.com/enter?back=%2F'
browser.get(url)
usernameBox = browser.find_element_by_id('handleOrEmail')
passwordBox = browser.find_element_by_id('password')
usernameBox.click()
usernameBox.clear()
usernameBox.send_keys('username')
passwordBox.click()
passwordBox.clear()
time.sleep(2)
passwordBox.send_keys('password')
login = browser.find_element_by_class_name('submit')
login.click()
print("登录完成")
time.sleep(2)
friends = ['tourist'] # 把你要添加的好友昵称列表写在这里
print('开始添加好友')
for i in friends:
    href = 'http://codeforces.com/profile/' + i
    browser.get(href)
    time.sleep(2)
    try:
        addFriend = browser.find_element_by_xpath('//img[contains(@title,"Click to add to friends")]')
        addFriend.click()
        print("已添加: " + i)
    except Exception:
        print(i + " 已经是您的好友，无需再次添加")
    time.sleep(1)
