import tkinter as tk
import scripts.core as core


def wardrobeWizard():
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
    button = tk.Button(root, text="Log In", command=core.log_in)
    button.place(relx = 0.5,
                 rely = 0.10,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Bump All Items", command=core.bump_all_items)
    button.place(relx = 0.5,
                 rely = 0.25,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Drop All Prices", command=core.drop_all_prices)
    button.place(relx = 0.5,
                 rely = 0.40,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Clear Wardrobe", command=core.clear_wardrobe)
    button.place(relx = 0.5,
                 rely = 0.55,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Post Items", command=core.post_item)
    button.place(relx = 0.5,
                 rely = 0.70,
                 anchor = 'center')

    # Create and stack buttons for functionality of the application
    button = tk.Button(root, text="Log Off", command=core.log_off)
    button.place(relx = 0.5,
                 rely = 0.85,
                 anchor = 'center')

    root.mainloop()


# Starts the program for testing
if __name__ == '__main__':
    wardrobeWizard()