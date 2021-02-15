"""
Tom McLaughlin
"""
from selenium.common.exceptions import NoSuchElementException
import time
import traceback
import tkinter as tk
from selenium import webdriver
from selenium.webdriver import ActionChains
import os

"""
@TODO:
1) Finish the post Item code so that Items can be posted - each part of the item settings needs to work

2) Build out non-extension functionality
    - Build out functions with passed in strings and lists so that the master yaml can be used to post items at scale

3) Write logging to keep track of progress and item post history/urls - this also can be made into a useful format to 
show the user their sales history and metrics
    
4) Future functionality
    Users
    - Manual add page url to url list, so that if the user manually posts an item it can be tracked by the system still
    - Interface for creating an item listing natively in the program
    - Build in read of Item URLs to show the post history and some basic Wardrobe statistics
    
    Maintainability:
    - Build in config to read in the xpaths of necessary DOM lookups so non technical people can service the program

5) Improve Readme, usage, and documentation
    - Create user documentation with screenshots so that people can easily learn how to use the system
"""

# Declare global driver for use in functions, this should allow us to login only once
driver = webdriver.Chrome()
driver.maximize_window()


def drop_all_prices():
    """THIS METHOD WILL DROP ALL OF A USER'S ITEM'S PRICES
    """
    try:
        # Initialize
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
    """THIS METHOD WILL BUMP ALL OF A USER'S ITEMS THAT CAN BE BUMPED
        - Currently only works with 6 items, needs to scroll down on the DOM to access the buttons that are lower
        - should probably close the bump notices after they come up
    """
    try:
        # Initialize
        try:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
        except:
            traceback.print_exc()
            print("Initialization failed...")

        # GET THE MAX NUMBER OF ITEMS ON A PAGE, THEN GO THROUGH PAGES UNTIL NO MORE ELEMENTS ARE FOUND
        # Needs to be fixed so the header bars are closed, otherwise scroll to the bottom of the page

        for i in range(1,10):
            time.sleep(2)
            item = driver.find_element_by_xpath(
                "//*[@id=\"wardrobe\"]/div/div[3]/div/div[2]/div[2]/div/div[{}]/div[2]/button[2]".format(i))
            item.click()
            print("Item {} bumped".format(i))

    except NoSuchElementException:
        traceback.print_exc()
        print("There was an error in Bump All Items\n")


def clear_wardrobe():
    """
    This method will clear the user's wardrobe so that they have no items listed
    """
    try:
        # Initialize
        try:
            driver.get("https://www.grailed.com/users/myitems")
            time.sleep(2)
        except:
            traceback.print_exc()
            print("Initialization failed...")

        # GET THE MAX NUMBER OF ITEMS ON A PAGE, THEN GO THROUGH PAGES UNTIL NO MORE ELEMENTS ARE FOUND
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
    """
    This method posts the new items to grailed.com
    """

    ##CURRENTLY WORKING HERE, IT WILL BREAK AND NOT WORK IF YOU ATTEMPT TO POST RIGHT NOW
    driver.close() # Close Driver to prevent memory leak for test

    FOLDER_PATH = r'../Products/'
    item_folders = os.listdir(FOLDER_PATH)

    item_directories = []
    for folder in item_folders:
        if '.DS' in folder:
            continue
        else:
            item_directories.append(os.listdir(FOLDER_PATH + folder + '/'))

    # For each item folder:-

    # Open the Yaml and get the information
    # Read in the information from config files
    item_title = ''
    item_desc = ''
    item_price = ''
    item_pics = []

    # Post the Item
    exit() # Close the program at the end of my test


# RUN THIS - DEBUG IT - AND WRAP IT IN TRY EXCEPT STATEMENTS
#   Set dummy title
    driver.get('https://www.grailed.com/sell')
    time.sleep(3)
    search_item = driver.find_element_by_id('search-by-item-name')
    search_item.send_keys(item_title)

#   This allows for you to create your own listing from scratch, using the search item name you created above
    time.sleep(3)
    start_from_scratch = driver.find_element_by_xpath("//*[contains(text(), 'Start from scratch')]")
    start_from_scratch.click()

#   This clicks the categoy box, which would trigger the dropdowns.
    time.sleep(6)
    category = driver.find_element_by_xpath('//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/input')
    category.click()

#   Finding the footwear button
    time.sleep(2)
    footwear = driver.find_element_by_xpath('//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[1]/h2[4]')
    footwear.click()

#   Finding the lowtop shoes button
    time.sleep(2)
    lowtop_shoes = driver.find_element_by_xpath('//*[@id="sellform"]/div/div[2]/form/div[1]/div/div[1]/div[1]/div/div/div/div[2]/h2[5]')
    lowtop_shoes.click()

#   Configured the designer to say not sure because of all the options it offers. Can be easily changed
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
    """
    This is responsible for instantiating the web driver, as well as getting
    the user logged in and on the proper page
    
    Change this so that instead of a command line interface it uses a tkinter continue box, itll be more intuitive that way and be distributable
    """
    # Begin login block
    try:
        driver.get(url="https://www.grailed.com/sell")  # Get the web page
        # Wait for user input to continue allowing fort logging in...
        cont = input("Please Log in then enter 'y' to continue: ")
        while cont != 'y':
            time.sleep(0.5)
            cont = input(": ")

    except:
        print("Launching driver.get('https://www.grailed.com/')")
    return driver


def log_off():
    print("Exiting...")
    driver.close()
    exit(0)


def main():
    """
    This is the driver of wardrobewizard, from here all the commands are invoked as functions that run alongside
    the created Tkinter window. When the User logs in, the webdriver opens the grailed site, where the user manually
    logs in, bypasses captcha, and enters 'y' into the terminal. At that point the commands below can be executed
    by clicking their button in the Tkinter window.
    """

    # Use globally declared driver variable to carry out actions on the users behalf
    # Create the GUI that will serve for the interaction between the user and the program
    root = tk.Tk()
    root.winfo_toplevel().title("WardrobeWizard V0.1")

    # Create and stack buttons for login functionality of the application
    button = tk.Button(root, text="Log In", command=log_in)
    button.place(relx = 0.5,
                 rely = 0.10,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Bump All Items", command=bump_all_items)
    button.place(relx = 0.5,
                 rely = 0.25,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Drop All Prices", command=drop_all_prices)
    button.place(relx = 0.5,
                 rely = 0.40,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Clear Wardrobe", command=clear_wardrobe)
    button.place(relx = 0.5,
                 rely = 0.55,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Post Items", command=post_item)
    button.place(relx = 0.5,
                 rely = 0.70,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Log Off", command=log_off)
    button.place(relx = 0.5,
                 rely = 0.85,
                 anchor = 'center')

    root.mainloop()


# Starts the program and cleans up when it is done.
main()

# Make sure everything closed successfully
try:
    driver.close()
except:
    print("Driver was previously closed\n")
