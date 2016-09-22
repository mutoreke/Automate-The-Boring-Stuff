#parsing HTML with BeautifulSoup module

import bs4
exampleFile =  open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select( '#author')
print(len(elems))
#pull <p> elem

pElems = exampleSoup.select('p')
print(str(pElems[0]))

