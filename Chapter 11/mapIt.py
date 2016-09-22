#! python3
# mapIt.py - Launches a map in the browser using an address from the command line

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # get address from command line

else:
    address = pyperclip.paste()


webbrowser.open('http://www.google.com/maps/place/' + address)

