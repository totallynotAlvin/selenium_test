from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep


def send_date(driver, day_txt, month_txt, year_txt, clear=True):
    
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

    sleep(2)

    submit = driver.find_element(By.ID, "submit")
    submit.click()
    sleep(1)
    Alert(driver).accept()


def test_suite(driver, url):
    driver.get(url)

    send_date("a", "b", "c")
    sleep(2)
    assert "Something went wrong... Check your input" not in driver.page_source
    input("please press enter to continue")

    send_date("1", "2", "1992")
    assert "02 February 1992" in driver.page_source
    sleep(2)

    send_date("2", "2", "1992")
    assert "03 February 1992" in driver.page_source
    input("please press enter to continue")

    day = driver.find_element(By.ID, "day")
    day.send_keys(Keys.DOWN)
    day.send_keys(Keys.DOWN)
    day.send_keys(Keys.DOWN)
    sleep(3)

    submit = driver.find_element(By.ID, "submit")
    submit.click()
    input("please press enter to continue")

    assert "Something went wrong... Check your input" in driver.page_source
    sleep(2)

    send_date("28", "2", "2022")
    assert "01 March 2022" in driver.page_source


driver = webdriver.Chrome()
url_v1 = "https://next-day.herokuapp.com"
input("please press enter to start v1 tests")
test_suite(driver, url_v1)

input("please press enter to continue to v2 tests")

url_v2 = "https://next-day.herokuapp.com/v2"
test_suite(driver, url_v2)

input("please press enter to close")
driver.close()
