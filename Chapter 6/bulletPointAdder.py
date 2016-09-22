#! python3
# bulletPoint.Adder. py - Adds Wikipedia bullet ppoints to the start of each line

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
