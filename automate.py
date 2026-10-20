from selenium import webdriver # webdriver is main interface 
from selenium.webdriver.common.by import By # this import element location like search boxes,button, or text fields
from selenium.webdriver.common.keys import Keys #this help simulate keyboard actions (like pressing Enter, Tab, or typing special keys).
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#path to your chromeDriver
service = Service(r"C:\Users\SAMIKSHA KUMARI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#open whatsapp web
driver.get("https://web.whatsapp.com/")
print("scan the qr code ")

time.sleep(15) # wait for QR scan

friend_name = "Nobi 🐱"
wait = WebDriverWait(driver, 60)
# Find the search box using a flexible selector
search_box = wait.until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//div[@contenteditable="true" and @role="textbox"]'
    ))
)



search_box.click()
search_box.send_keys(friend_name)
time.sleep(2)
search_box.send_keys(Keys.ENTER)


# Send 100 messages
for i in range(100):
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys(f" NATURE  {i+1} from Selenium (python)!")
    message_box.send_keys(Keys.ENTER)
    time.sleep(0.5)  # small delay to avoid spam detection