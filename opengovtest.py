# * Task 1: As an admin, create an account for a new customer
# * Task 2: As an admin, create a new tour
# * Task 3: As a new customer, book a tour

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_first = "Carl"
user_last = "Yastremski"
user_email = "carl@redsox.com"
user_password = "Brs1960!"
user_address1 = "#4 Yawkey Way"
user_city = "Boston"
user_state = "MA"
user_postcode = "02215"
user_phone = "6175551212"
user_mobile = "6172222222"

driver = webdriver.Chrome()
driver.get("https://phptravels.org/register.php")
assert "Register" in driver.title

elem = driver.find_element_by_name("firstname")
elem.send_keys(user_first)

elem = driver.find_element_by_name("lastname")
elem.send_keys(user_last)

elem = driver.find_element_by_name("email")
elem.send_keys(user_email)

elem = driver.find_element_by_id("inputNewPassword1")
elem.send_keys(user_password)

elem = driver.find_element_by_name("password2")
elem.send_keys(user_password)

elem = driver.find_element_by_name("address1")
elem.send_keys(user_address1)

elem = driver.find_element_by_name("city")
elem.send_keys(user_city)

elem = driver.find_element_by_name("state")
elem.send_keys(user_state)

elem = driver.find_element_by_name("postcode")
elem.send_keys(user_postcode)

elem = driver.find_element_by_id("country")
for option in elem.find_elements_by_tag_name('option'):
    if option.text.strip() == 'United States':
        option.click()
        
elem = driver.find_element_by_name("phonenumber")
elem.send_keys(user_phone)

elem = driver.find_element_by_id("customfield1")
for option in elem.find_elements_by_tag_name('option'):
    if option.text.strip() == 'Friend':
        option.click()
        
elem = driver.find_element_by_name("customfield[2]")
elem.send_keys(user_mobile)

driver.find_element_by_css_selector('.btn.btn-large.btn-primary').click()

