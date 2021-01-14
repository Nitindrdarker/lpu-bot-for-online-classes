from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import pandas
import datetime
import time
import schedule


c = []
class Myclass:
    def __init__(self):
        time.sleep(10)
        self.driver = webdriver.Edge(executable_path = "C:\Program Files (x86)\msedgedriver.exe")
        self.driver.get('https://myclass.lpu.in/')
    def attend(self, i):
        global c
        c = self.driver.find_elements_by_class_name('fc-content')
        c[i].click()
        time.sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/a')#enter the xpath of the join button here
        time.sleep(15)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i')#listining



    def leave(self):
        self.driver.back()
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[4]/div[2]/button[1]')#enter the xpath of the leave meeting option appered after prssing back button on your browser
        global c
        time.sleep(10)
        c = self.driver.find_elements_by_class_name('fc-content')
        
        
    def login(self,username,password):
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]').send_keys(password)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button').click()
    def navigate(self):
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a').click()
    def find_classes(self):
        
        global c
        
        time.sleep(5)
        weekday = datetime.datetime.now().weekday()
        time_of_class = pandas.read_csv('timetable.csv')
        if(weekday == 0):
            
            classtime = time_of_class['Monday']
            leave_time = time_of_class['leavemon']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)
        elif(weekday == 1):
            
            classtime = time_of_class['Tuesday']
            leave_time = time_of_class['leavetue']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)
        elif(weekday == 2):
            
            classtime = time_of_class['Wednesday']
            leave_time = time_of_class['leavewed']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)
        elif(weekday == 3):
            
            classtime = time_of_class['Thursday']
            leave_time = time_of_class['leavethur']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)
        elif(weekday == 4):
            
            classtime = time_of_class['Friday']
            leave_time = time_of_class['leavefri']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)
        elif(weekday == 5):
            
            classtime = time_of_class['Saturday']
            leave_time = time_of_class['leavesat']
            c = self.driver.find_elements_by_class_name('fc-content')
            for i in range(len(c)):
                schedule.every().monday.at(str(classtime[i])).do(self.attend, i)
                schedule.every().monday.at(str(leave_time[i])).do(self.leave)

        while(True):
            schedule.run_pending()
            time.sleep(1)


    



                
                   
                
                
    
            
            
        
                
                    
 
username = '' #registration number
password = '' #password 
myclass = Myclass()
myclass.login(username,password)
myclass.navigate()
myclass.find_classes()




    
    
    








