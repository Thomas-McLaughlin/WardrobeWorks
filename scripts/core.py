"""
This file holds the logic for taking action on grailed.com:
"""
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import traceback
from selenium.webdriver import ActionChains
import os
import tkinter.messagebox as mb
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--disable-notifications")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1 })
driver = webdriver.Chrome(options=option)
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
            actions = ActionChains(driver)
            actions.move_to_element(item).perform()
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

        # Fixme: This needs to be changed to the full range of the bumpable items
        for i in range(1, 10):
            time.sleep(2)
            item = driver.find_element_by_xpath(
                "//*[@id=\"wardrobe\"]/div/div[3]/div/div[2]/div[2]/div/div[{}]/div[2]/button[2]".format(i))
            actions = ActionChains(driver)
            actions.move_to_element(item).perform()
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
            item = driver.find_element_by_xpath("//*[@id=\"wardrobe\"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/a/div[2]/img")
            item.click()
            time.sleep(3)

            driver.switch_to.window(driver.window_handles[1])

            element = driver.find_element_by_id("user_delete")
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()

            time.sleep(0.5)
            element.click()
            time.sleep(1)

            # Fixme: This needs to be able to input a reason for deletion
            reason = driver.find_element_by_xpath("//select[@id=\"reason\"]/option[text()='Other'")
            reason.click()
            time.sleep(.2)

            reasonBox = driver.find_element_by_xpath("//*[@id=\"notes\"]")
            reasonBox.send_keys("Sold elsewhere")
            time.sleep(0.1)

            driver.find_element_by_xpath("/html/body/div[18]/div/div/div/div[2]/div/form/button").click()

    except NoSuchElementException:
        print("Something went wrong in clearWardrobe()")
        traceback.print_exc()


def post_item():
    """Post new items to grailed.com"""

    # Fixme: This function is currently not working. It also is the most work, and interacts directly with the dbs
    # Close driver to prevent memory leak for test
    driver.close()  

    # Read in the information from db
    

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
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"app\"]/div[8]/a[2]").click()
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
