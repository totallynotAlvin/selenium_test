from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://next-day.herokuapp.com"
driver.get(url)

def send_date(day_txt, month_txt, year_txt, clear=True):
    

    day = driver.find_element(By.ID, "day")
    month = driver.find_element(By.ID, "month")
    year = driver.find_element(By.ID, "year")

    if clear:
        day.clear()
        month.clear()
        year.clear()

    day.send_keys(day_txt)
    month.send_keys(month_txt)
    year.send_keys(year_txt)

    submit = driver.find_element(By.ID, "submit")
    submit.click()


send_date("a", "b", "c")
assert "Something went wrong... Check your input" not in driver.page_source
sleep(1)

send_date("1", "2", "1992")
assert "02 February 1992" in driver.page_source
sleep(1)

send_date("2", "2", "1992")
assert "03 February 1992" in driver.page_source
sleep(1)
# driver.close()
