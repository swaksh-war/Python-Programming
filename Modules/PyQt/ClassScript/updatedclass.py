# Your id below
id_ = "12016043"
# your password below
pass_ = "SandyRuby@12"

method = "Microphone"

poll = "B"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#setting permissions to the browser
opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic":1,
})

#locating the webdriver
driver = webdriver.Chrome(options=opt,executable_path="C:\ProgramData\chromedriver.exe")

#the class joining function
def onlineclassscript():
    
    #connecting to login page
    driver.get("https://myclass.lpu.in")
    print(driver.title)

    #logging in
    username = driver.find_element_by_name("i")
    username.send_keys(id_)
    password = driver.find_element_by_name("p")
    password.send_keys(pass_)
    password.send_keys(Keys.ENTER)

    #finding and clicking on Classes/Meetings
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "View Classes/Meetings")
        )
    )

    search = driver.find_element_by_link_text("View Classes/Meetings")
    search.click()
    
    #finding any running classes
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "fc-content")
        )
    )
    #joining the running classes
    import time
    while True:
        try:
            driver.refresh()
            search = driver.find_element_by_css_selector('a[style*="color: white; background: green;"]')
            search.click()
            break
        except Exception as e:
            print(" No Class in progress yet... ")
            time.sleep(120)
    
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[role="button"]')
        )
    )
    search = driver.find_element_by_css_selector('a[role="button"]')
    search.click()
    
    #switching to the audio choice frame
    match_search = WebDriverWait(driver,400).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'frame')
        )
    )
    iframe = driver.find_element_by_id('frame')
    driver.switch_to.frame(iframe)
    
    #choosing microphone method
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
        )
    )
    search = driver.find_element_by_css_selector('button[aria-label="' + method +'"]')
    search.click()
    
    #doing echo test
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
        )
    )
    search = driver.find_element_by_css_selector('button[aria-label="Echo is audible"]')
    search.click()
    
    #waiting for class end
    while True:
        try:
            match_search = WebDriverWait(driver,3).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                )
            )
            #joining any next class if any 
            onlineclassscript()
        except:
            try:
                match_search = WebDriverWait(driver,117).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                    )
                )
                time.sleep(4000)
                try:
                    search = driver.find_element_by_css_selector('button[aria-label="'+poll+'"]')
                    search.click()
                    print("Poll Attended")
                except Exception as e:
                    search = driver.find_element_by_css_selector('button[aria-label="Yes"]')
                    search.click()
                    print("Poll Attended")
            except Exception as e:
                print("class in progress")
            

onlineclassscript()
