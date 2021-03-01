"""
Tom McLaughlin
This file holds the logic for taking action on grailed.com:
- Posting Items
- Dropping Prices
"""
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import traceback
from selenium.webdriver import ActionChains
import os
import tkinter.messagebox as mb


driver = webdriver.Chrome()
driver.maximize_window()


def drop_all_prices():
    """Drop all of a user's items prices"""
    try:
        try:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
        except:
            traceback.print_exc()
            print("Initialization failed...")

        for i in range(1, 10):
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
            item = driver.find_element_by_xpath(
                "//*[@id=\"wardrobe\"]/div/div[3]/div/div/div/div[{}]/a/div[1]/img".format(i))
            item.click()
            time.sleep(3)

            # Stub for dropping all prices, may be a better way to do this

    except NoSuchElementException:
        print("There was an error in Drop All Prices\n")
        traceback.print_exc()


def bump_all_items():
    """Bump all of a user's items that can be bumped

    Limitations:
        - Currently only works with 6 items, needs to scroll down
          on the DOM to access the buttons that are lower
        - Doesn't close the bump notices after they come up
    """
    try:
        # Initialize
        try:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
        except:
            traceback.print_exc()
            print("Initialization failed...")

        # Fetch the number of items on the page and loop through all of them.
        # Fixme: If the header bars are not closed, scroll to
        # the bottom of the page

        for i in range(1, 10):
            time.sleep(2)
            item = driver.find_element_by_xpath(
                "//*[@id=\"wardrobe\"]/div/div[3]/div/div[2]/div[2]/div/div[{}]/div[2]/button[2]".format(i))
            item.click()
            print("Item {} bumped".format(i))

    except NoSuchElementException:
        traceback.print_exc()
        print("There was an error in Bump All Items\n")


def clear_wardrobe():
    """Clears the user's wardrobe so that they have no items listed"""
    try:
        # Initialize
        try:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
        except:
            traceback.print_exc()
            print("Initialization failed...")

        # Fetch the number of items on the page and loop through all of them.
        while True:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
            item = driver.find_element_by_xpath("//*[@id=\"wardrobe\"]/div/div[3]/div/div/div/div[1]/a/div[1]/img")
            # //*[@id="wardrobe"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/a/div[2]/img
            item.click()
            time.sleep(3)

            actions = ActionChains(driver)
            element = driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div[2]/div[4]/h3")
            actions.move_to_element(element).perform()
            time.sleep(0.2)

            button = driver.find_element_by_link_text("DELETE THIS POSTING")

            if button.text == "DELETE THIS POSTING":
                button.click()
                driver.switch_to_alert().accept()
                time.sleep(1)

    except NoSuchElementException:
        print("Something went wrong in clearWardrobe()")
        traceback.print_exc()


def post_item():
    """Post new items to grailed.com"""

    # Fixme: This function is currently not working.
    # Close driver to prevent memory leak for test
    driver.close()  

    FOLDER_PATH = r'../Products/'
    item_folders = os.listdir(FOLDER_PATH)

    item_directories = []
    for folder in item_folders:
        if '.DS' in folder:
            continue
        else:
            item_directories.append(os.listdir(FOLDER_PATH + folder + '/'))

    # For each item folder:-

    # Read in the information from config files
    item_title = ''
    item_desc = ''
    item_price = ''
    item_pics = []

    # Post the Item
    exit()  # Close the program at the end of my test

    # RUN THIS - DEBUG IT - AND WRAP IT IN TRY EXCEPT STATEMENTS
    # Set dummy title
    driver.get('https://www.grailed.com/sell')
    time.sleep(3)
    search_item = driver.find_element_by_id('search-by-item-name')
    search_item.send_keys(item_title)

    # This allows for you to create your own listing from scratch, 
    # using the search item name you created above
    time.sleep(3)
    start_from_scratch = driver.find_element_by_xpath(
        "//*[contains(text(), 'Start from scratch')]")
    start_from_scratch.click()

    # This clicks the categoy box, which would trigger the dropdowns.
    time.sleep(6)
    category = driver.find_element_by_xpath(
        '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/input')
    category.click()

    # Finding the footwear button
    time.sleep(2)
    footwear = driver.find_element_by_xpath(
        '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[1]/h2[4]')
    footwear.click()

    # Finding the lowtop shoes button
    time.sleep(2)
    lowtop_shoes = driver.find_element_by_xpath(
        '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[2]/h2[5]')
    lowtop_shoes.click()

    # Configured the designer to say not sure because of all the options it offers. Can be easily changed
    time.sleep(2)
    designer = driver.find_element_by_id('designer-autocomplete')
    designer.send_keys('Not sure')

    #   Clicks the auto complete for the text typed above. This is iffy, as sometimes a random unrelated name comes up even
    #   when you click not sure.
    time.sleep(6)
    not_sure = driver.find_element_by_class_name('autocomplete')
    not_sure.click()

    #   Finds the size button
    size = driver.find_element_by_name('size')
    size.click()

    #   Adds the size. To change, just replace the 9 with whatever number you'd like.
    time.sleep(2)
    the_size = driver.find_element_by_xpath("//option[@value='9']")
    the_size.click()

    #   Chooses the color. Elected N/A.
    time.sleep(2)
    color = driver.find_element_by_id('color-autocomplete')
    color.send_keys('N/A')
    time.sleep(2)

    #   This is to click off the color, so your program can continue
    clickoff = driver.find_element_by_id('sellform')
    clickoff.click()

    #   Clicking condition new
    time.sleep(4)
    the_condition = driver.find_element_by_xpath("//option[@value='is_new']")
    the_condition.click()

    #   Sending description from text file in description folder
    time.sleep(2)
    description = driver.find_element_by_xpath('//*[@id="sellform"]/div/div[2]/form/div[5]/textarea')
    description.send_keys(item_desc)

    #   Sending price from text file in price folder
    time.sleep(2)
    input_price = driver.find_element_by_name('price')
    input_price.send_keys(item_price)
    time.sleep(2)

    #   Turning the smart pricing off
    driver.find_elements_by_class_name('--slider')[1].click()

    # Photo upload block
    upload_photos = driver.find_element_by_id('photo_input_0')
    images = ''
    for pic in item_pics:
        images += pic + '\n'
    images.rstrip()
    upload_photos.send_keys(images)


def log_in():
    """Instantiate the web driver, log the user and switch to the page"""
    try:
        driver.get(url="https://www.grailed.com/sell")
        cont = mb.askyesno(
            "Login Popup", 'Please log in and then press "yes" to continue')
        if not cont:
            return driver

    except:
        print("Launching driver.get('https://www.grailed.com/')")

    return driver


def log_off():
    """Close down the driver"""
    print("Exiting...")
    driver.close()
    exit(0)
