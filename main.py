from selenium import webdriver
from selenium.webdriver.common.by import By

baby_driver = webdriver.Chrome() # Yes, a reference to the movie.
baby_driver.get("https://www.python.org/")

time_elements = baby_driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_elements = baby_driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

if len(time_elements) is not len(event_elements): # Early return pattern
    raise Exception("The number or time elements do not correspond with that of event elements.")

event_dictionary = {}

for i in range(len(time_elements)):
    event_dictionary[i] = {
        "time": time_elements[i].get_attribute("datetime"),
        "event": event_elements[i].text
    }

print(event_dictionary)

baby_driver.quit()