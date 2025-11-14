"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tbody = soup.find('tbody')
        tags = tbody.find_all('tr')
        for tag in tags:
            s = tag.find_all('td')
            if len(s) >= 5:
                male_number = int(s[2].text.replace(',', ''))
                female_number = int(s[4].text.replace(',', ''))
        print(f"Male Number: {male_number}")
        print(f"Female Number:{female_number}")

        driver.quit()


if __name__ == '__main__':
    main()
