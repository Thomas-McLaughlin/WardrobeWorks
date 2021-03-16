The purpose of this program is to improve use of the "Grailed.com" marketplace for sellers who want an easier workflow, to cut down on repetitive actions, and gain greater insight into their sales data.

In Grailed's defense, they regularly introduce new features to help such as a 'smart pricing' option that allows you to bump automatically when possible until the item reaches a price floor. 

This program aims to solve the following issues.</br>
    -Posting a set of items defined by templates</br>
    -Managing 'bumps' of items</br>
    -Deleting postings/wiping inventories for a fresh start</br>
    -Basic post date, likes, sales price, sales over time, revenue over time metrics that are helpful to sellers</br>

Use Case Diagram:
![alt text](Use%20Case.png)

Requirements:</br>
    Install the wardrobewizard package on your computer</br>
    You need python 2.7 installed to run the program</br>
    You need Google Chrome installed to run the program</br>
    
TO USE:</br>
    Run wardrobewizard.py with the command 'python2 wardrobewizard.py'</br>
    Go to the opened Tkinter window</br>
    Click Log in</br>
    Log in to your Grailed Account and Pass Captcha</br>
    Click the 'yes' key from the popup window</br>
    Click the Wardrobe operations that you want to carry out that session</br>
    The wizard carries out the rest!</br>

Currently:</br>
    Work is being done on the program so that all of the UI is handled through a browser. If you have correctly 
    downloaded the github repo and dependencies you should be able to look at the current state of the web UI by running
    the commands:</br>
    export FLASK_APP=flask_site.py</br>
    export FLASK_ENV=development</br>
    flask run</br>
    Then open a browser window to http://127.0.0.1:5000/ to see the UI and interact </br>
    
This program requires the user to supply all product images, descriptions, pricing, and configurations for maintenance tasks.</br>

<h1>For New Contributors</h1></br>
The focus of the development is around two components: core.py and the flask app that serves as the interface.</br>
The remaining tasks are to get the following working:</br>
1) post_items: This should read from the item_data.db and take the items that don't have a post date, and posts them to grailed - this is a little complicated and requres familiarity with the site.</br></br>
2) sales.html: This is where all the sales data from sales_data.db can be viewed and analyzed. It will consist of a table view, and a graph view.</br>
-The table view should just list the sales_data.db information as a table in an orderly fashion.</br>
-The graph view should show sales over time.</br></br>
3) manage.html: This is where the user can view the information in their item_data.db - it should have a table laying out their templates and values of each field in the template, with a radio button to the far right to post the item</br></br>

As you go through the code and run into issues, it may be helpful to other contributors if you update the troubleshooting wiki file with what helped you get past those issues. This will go a long way to creating a documentation page to help everyone understand the code base.
