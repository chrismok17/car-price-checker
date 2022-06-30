from selenium import webdriver
from selenium.webdriver.common.by import By


def hyundai_surrey():
    url = "https://www.jphyundaisurrey.com/showroom/index.htm"
    path = r'C:\\Users\\chrismok\Documents\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.get(url)

    # title = driver.title
    
    car = driver.find_elements(By.CLASS_NAME, "fn  ")
    price = driver.find_elements(By.CLASS_NAME, "price.h3")

    driver.implicitly_wait(5)

    with open("vehicles.json", "w") as jsonfile:
        pass

    for i in car:
        vehicles = {
            "vehicle": i.text.replace("\n", " "),
        }
        
        
        print(f'Printing: {vehicles}')

    driver.quit()
    
    
    # print(car)
    # return span

def main():
    hyundai_surrey()

if __name__ == "__main__":
    main()