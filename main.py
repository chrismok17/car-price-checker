import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def hyundai_surrey():
    url = "https://www.jphyundaisurrey.com/new-inventory/index.htm?search=&model=Elantra&gvBodyStyle=Sedan"
    # page = requests.get(url)

    # soup = BeautifulSoup(page.content, "html.parser")
    # result = soup.find_all("div", class_="vehicle-card-body ddc-font-size-small d-sm-flex flex-sm-row")
    path = r'C:\\Users\\chrismok\Documents\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)
    title = driver.title
    driver.implicitly_wait(0.5)
    # driver.find_element("vehicle-card-body ddc-font-size-small d-sm-flex flex-sm-row").send_keys(".")

    # js = "document.getElementByClass('vehicle-card-body ddc-font-size-small d-sm-flex flex-sm-row').options[1].text = '100';"
    # driver.execute_script(js)
    driver.quit()
    return title

def main():
    print(hyundai_surrey())

    # path = r'C:\\Users\\chrismok\Documents\\geckodriver.exe'
    # driver = webdriver.Firefox(executable_path=path)
    # driver.get("https://google.com")

    # title = driver.title

    # driver.implicitly_wait(0.5)

    # search_box = driver.find_element(by=By.Name, value="q")
    # search_button = driver.find_element(by=By.NAME, value="btnK")

    # search_box.send_keys("Selenium")
    # search_button.click()

    # value = search_box.get_attribute("value")

    # driver.quit()

if __name__ == "__main__":
    main()