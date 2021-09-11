from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
chrome_drive_path =  "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)


ID = "hieplecoding@gmail.com"
PASSWORD = "giahan2310"
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=107144641&keywords=python%20developer&location=Vienna%2C%20Austria"
PHONE = "+4367762943449"

driver.get(URL)


# step 1 get signin

signin = driver.find_element_by_class_name("nav__button-secondary")
signin.click()
# accept cookies then write name, password and click sigin
cookies = driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
cookies.click()

time.sleep(3)
id = driver.find_element_by_id("username")
id.send_keys(ID)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
# step 2 try to apply one easy job with phone number
time.sleep(5)
apply_lists = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in apply_lists:
    listing.click()
    time.sleep(5)
#   try to locate the submit button, if cannot locate them skip the job
    try:
        appy_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        appy_button.click()
        time.sleep(5)
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(5)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("too complicated")
            continue
        else:
            submit_button.click()

        time.sleep(3)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("no , skip")
        continue

time.sleep(5)
driver.quit()
time.sleep(5)
