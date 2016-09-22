#Global and local variable assignments
def spam():
    global eggs
    eggs= 'spam' #Global variable

def bacon():
    eggs = 'bacon' #Local variable

def ham():
    print(eggs)#output is spam

eggs= 42 #replaces spam
spam()#runs function at top
print(eggs)#output should be spam