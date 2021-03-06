"""
This program goes to the grailed site and pulls down the categories/subcategories that are available to sell
"""
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import json
import os

def get_selects(driver):
    """
    Get the categories from the grailed site
    :param driver:
    :return a list of the categories available on the grailed site:
    """
    i = 1
    categories = []
    while 1:
        try:
            category = driver.find_element_by_xpath(
                "//*[@id=\"CategoryPage\"]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/a[{}]/p".format(i))
            categories.append(str(category.text))
            i += 1
        except NoSuchElementException:
            break
    return categories


def get_subs(driver, cat):
    """
    Gets a list of the subcategories for a given category from the grailed site
    :param driver:
    :param cat - The name of the category we want the subcategories of:
    :return a list of the subcategories for the given cat:
    """
    cat_to_int = {'tops':'2', 'bottoms':'3', 'outerwear':'4', 'footwear':'5', 'tailoring':'6', 'accessories':'7'}
    subs = []
    item = 1
    while 1:
        try:
            category = cat_to_int[cat.lower()]
            sub = driver.find_element_by_xpath(
                "//*[@id=\"CategoryPage\"]/div[1]/div/div[3]/div[1]/div[{}]/div/a[{}]".format(category, item)).get_attribute("innerText")
            subs.append(sub)
            item += 1
        except NoSuchElementException:
            break
    return subs


def get_designers(driver):
    """
    Gets the designers allowed to be sold on grailed
    :param driver:
    :return a list of the designers that are allowed to be sold on grailed:
    """
    driver.get("https://grailed.com/designers")
    time.sleep(3)
    anchors = ['pound', 'a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z']
    designers = []
    for tag in anchors:
        i = 1
        while 1:
            try:
                for a in range(1,3):
                    designer = driver.find_element_by_xpath(
                        "//*[@id=\"anchor-{}\"]/div[2]/div[{}]/a[{}]".format(tag, str(a), str(i)))
                    designers.append(designer.get_attribute('innerText'))
                i += 1
            except NoSuchElementException:
                break
    return designers


def main():
    """
    Driver for the pull selects script. Generates a dictionary holding the categories and their subcategories
    :return:
    """
    driver_directory = os.path.abspath(os.getcwd())
    driver = webdriver.Chrome(driver_directory + '/chromedriver')
    driver.maximize_window()
    driver.get("https://grailed.com/categories/all")
    time.sleep(3)

    categories = get_selects(driver)

    sub_categories = []
    for cat in categories:
        url = "https://grailed.com/categories/" + str(cat).lower()
        driver.get(url)
        time.sleep(6)
        subs = get_subs(driver, cat)
        sub_categories.append(subs)

    selects = {}
    for i in range(len(categories)):
        selects[categories[i]] = sub_categories[i]

    with open("configs/selects.json", "w") as outfile:
        json.dump(selects, outfile)

    designers = get_designers(driver)
    with open("configs/designers.txt", mode = 'w') as fh:
        [fh.write(designer + '\n') for designer in designers]

    driver.quit()


main()
