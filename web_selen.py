from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

class Login(webdriver.Chrome):
    def __init__(self,driver_path=r"C:\Program Files (x86)\chromedriver.exe"):
        self.driver_path=driver_path
        os.environ['PATH'] += self.driver_path                         #for paths
        super(Login, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def first_page(self):
        self.get('https://mdbootstrap.com/docs/standard/extended/login/#!')        #scroll down a little
        self.execute_script("window.scrollTo(0,1200)")
     
    def register_button_handler(self):                            #register button
        self.find_element("id","tab-register").click()   
        
    def fill_page(self,value,value1,value2,value3):
        name=self.find_element("id","registerName")                    #fill the page with the datas in excel file
        name.click()
        name.send_keys(value)
        username=self.find_element("id","registerUsername")         
        username.send_keys(value1)
        email=self.find_element("id","registerEmail")
        email.send_keys(value2)
        password=self.find_element("id","registerPassword")
        password.send_keys(value3)
        password1=self.find_element("id","registerRepeatPassword")
        password1.send_keys(value3)
    
    def register_page(self):
        regis= self.find_element(By.CSS_SELECTOR,"div[id='pills-register'] button[type='submit']").click()   #just click register button
        
    def quit(self) -> None:
        return super().quit()


