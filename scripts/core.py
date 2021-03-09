"""
This file holds the logic for taking action on grailed.com:
"""
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import traceback
from selenium.webdriver import ActionChains
import sqlite3
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
    # Fixme: This function is currently not working. It also is the most work.

    # Open a connection to the database
    conn = sqlite3.connect('../data/item_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    returns = c.fetchall()
    conn.close()

    # Get the items that need posting
    to_post = []
    for retval in returns:
        if retval[1] == '':
            to_post.append(retval)
            print(retval)

    # Fixme: Post_date and url need to be updated in the db at the end when this loop runs
    for item in to_post:
        item_title = item[0]
        post_price = item[3]
        description = item[6]
        designer = item[7]
        category = item[8]
        size = item[9]
        condition = item[10]

        # Sanity Check
        print("title: {}\n price: {}\n descr: {}\n designer: {}\n condition: {}\n category: {}\n size: {}\n".format(
            item_title, post_price, description, designer, condition, category, size))

        # Post the Item
        driver.get('https://www.grailed.com/sell')
        time.sleep(3)
        title = driver.find_element_by_xpath("//*[@id=\"sellform\"]/div/div[2]/form/div[1]/div/div[2]/div[1]/input")
        title.send_keys(item_title)

        # This clicks the category box, which would trigger the dropdowns. - needs to be generalized
        time.sleep(6)
        category = driver.find_element_by_xpath(
            '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/input')
        category.click()

        # Set Category (accessories) - needs to be generalized
        time.sleep(2)
        footwear = driver.find_element_by_xpath(
            '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[1]/h2[4]')
        footwear.click()

        # Set sub category (jewelry) - needs to be generalized
        time.sleep(2)
        lowtop_shoes = driver.find_element_by_xpath(
            '//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[2]/h2[5]')
        lowtop_shoes.click()

        # Set the designer
        time.sleep(2)
        designer = driver.find_element_by_id('designer-autocomplete')
        designer.send_keys('Not sure')
        time.sleep(6)
        not_sure = driver.find_element_by_class_name('autocomplete')
        not_sure.click()

        # Fixme: Works up until here
        #  Set the size
        size = driver.find_element_by_name('size')
        size.click()
        time.sleep(2)
        the_size = driver.find_element_by_xpath("//option[@value={}]".format(size))
        the_size.click()

        #   Chooses the color. Elected N/A.
        time.sleep(2)
        color = driver.find_element_by_id('color-autocomplete')
        color.send_keys('N/A') # N/A isn't a dropdown option, can you enter anything if you click off?
        time.sleep(2)
        #   This is to click off the color dropdown, so your program can continue
        clickoff = driver.find_element_by_id('sellform')
        clickoff.click()

        #   Set Condition
        time.sleep(4)
        the_condition = driver.find_element_by_xpath("//option[@value='is_new']")
        the_condition.click()

        #   Sending description from text file in description folder
        time.sleep(2)
        description = driver.find_element_by_xpath('//*[@id="sellform"]/div/div[2]/form/div[5]/textarea')
        description.send_keys(description)

        #   Sending price from text file in price folder
        time.sleep(2)
        input_price = driver.find_element_by_name('price')
        input_price.send_keys(post_price)
        time.sleep(2)

        #   Turning the smart pricing off
        driver.find_elements_by_class_name('--slider')[1].click()

        # Fixme: The database needs to take up to 6 images for upload when the template is made, they must be able
        #  to upload here
        # # Photo upload block
        # upload_photos = driver.find_element_by_id('photo_input_0')
        # images = ''
        # for pic in item_pics:
        #     images += pic + '\n'
        # images.rstrip()
        # upload_photos.send_keys(images)


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

# post_item()