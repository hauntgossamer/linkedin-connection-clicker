from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from secrets import email, password
from time import sleep
browser = webdriver.Firefox()
class LinkedInBot():

        
    def login(self):
        browser.get('https://linkedin.com')
        
        sign_in = browser.find_element_by_xpath('/html/body/nav/a[3]')
        sign_in.click() 
        
        browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input').send_keys("", email)
        
        browser.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input').send_keys("", password, Keys.ENTER)
        
    def commenceClicking(self):
            
            browser.maximize_window()
            browser.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]').click()
            
            sleep(5)
                        
            
            while True:
                try:
                    connectbuttons = browser.find_elements_by_tag_name('span')
                    for x in range(0, len(connectbuttons)):
                        if connectbuttons[x].is_displayed():
                            if connectbuttons[x].get_property('innerText') == "Connect":
                                connectbuttons[x].click()
                                sleep(0.5)
                except StaleElementReferenceException:
                    sleep(10)
            else:
               for x in range(0, len(connectbuttons)):
                    if connectbuttons[x].is_displayed():
                        if connectbuttons[x].get_property('innerText') == "Connect":
                            connectbuttons[x].click()
                            sleep(0.5) 
            