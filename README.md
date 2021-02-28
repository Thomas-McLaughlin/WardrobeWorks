The purpose of this program is to improve use of the "Grailed.com" marketplace for sellers who want an easier workflow, to cut down on repetitive actions, and gain greater insight into their sales data.

In Grailed's defense, they regularly introduce new features to help such as a 'smart pricing' option that allows you to bump automatically when possible until the item reaches a price floor. 

This program aims to solve the following issues.</br>
    -Posting a set of items defined by templates</br>
    -Managing 'bumps' of items</br>
    -Deleting postings/wiping inventories for a fresh start</br>
    -Basic post date, likes, sales price, sales over time, revenue over time metrics that are helpful to sellers</br>

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
    
This program requires the user to supply all product images, descriptions, pricing, and configurations for maintenance tasks.
