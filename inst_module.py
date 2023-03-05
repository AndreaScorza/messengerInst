from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

def getMessages():
    
    ret_val = []
    
    # Start the webdriver and navigate to the Instagram login page
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    # Wait for the login page to load
    time.sleep(2)

    # Click the "Accept Cookies" button
    accept_button = driver.find_element(By.XPATH, "//button[text()='Allow essential and optional cookies']")
    accept_button.click()

    # Wait for the cookies banner to disappear
    time.sleep(1)

    # Wait for an additional second
    time.sleep(1)

    # Enter the username and password into the form fields
    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys(os.getenv('USERNAME'))

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(os.getenv('PASSWORD'))

    # Submit the form to log in
    password_field.send_keys(Keys.RETURN)

    # Wait for the dashboard page to load
    time.sleep(7)

    # Find the <span> element by XPath
    span_element = driver.find_element(By.XPATH, "//span[@class='xwmz7sl xo1l8bm x1ncwhqj xyqdw3p x1mpkggp xg8j3zb x1t2a60a']")

    # Get the text content of the <span> element and convert it to an integer
    notification_number = int(span_element.text)
    print("The number of notificaiton is ", notification_number)

    if notification_number > 0:
        span_element.click()
        
        time.sleep(1);
        
        # We need to close the popup turn on notifications
        turn_on_notifications = driver.find_element(By.XPATH, "//button[text()='Not Now']")
        turn_on_notifications.click()
        
        time.sleep(1)
        
        
        # run trhough the list of chat with the notificaiton number and get the sender and the text 
        for x in range(notification_number):
            title_xpath = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[' + str(x + 1) + ']/div/a/div/div[2]/div[1]/div/div/div/div'
            message_xpath = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[' + str(x + 1) + ']/div/a/div/div[2]/div[2]/div/div/span[1]/span'
            title_element = driver.find_element(By.XPATH, title_xpath)
            message_element = driver.find_element(By.XPATH, message_xpath)
            ret_val.append([title_element.text , message_element.text])
            #print(title_element.text + " : ", message_element.text)
            time.sleep(1)
        
                

    # Print the title of the dashboard page to confirm login
    print(driver.title)

    # Close the webdriver
    driver.quit()
    
    return ret_val