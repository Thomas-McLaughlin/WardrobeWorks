"""
This program goes to the grailed site and pulls down the categories that are available to sell
"""
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def get_selects(driver):
    i = 1
    categories = []
    while (1):
        try:
            category = driver.find_element_by_xpath(
                "//*[@id=\"CategoryPage\"]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/a[{}]/p".format(i))
            categories.append(category.text)
            i += 1
        except NoSuchElementException:
            break
    return categories


def main():
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    # option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()

    driver.get("https://grailed.com/categories/all")
    time.sleep(3)

    categories = get_selects(driver)

    sub_categories = []
    for cat in categories:
        url = "https://grailed.com/categories/" + str(cat).lower()
        print(url)
        driver.get(url)
        time.sleep(10)
        subs = get_selects(driver)
        sub_categories.append(subs)

    driver.close()
    [print(cat) for cat in categories]
    [print(sub) for sub in sub_categories]


main()
