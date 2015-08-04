import urllib2,re
from bs4 import BeautifulSoup

falabella_tv_dict={}

falabella_url="http://www.falabella.com"
ripley_url="http://www.ripley.cl"

ripley_led_uri="http://www.ripley.cl/ripley-chile/tecnologia/tv/led"
falabella_led_uri="http://www.falabella.com/falabella-cl/category/cat2850014/LED?Nrpp=67"


# ripley_page = urllib2.urlopen(ripley_uri).read()

def getTVLinks():
    falabella_page=urllib2.urlopen(falabella_led_uri).read()
    soup=BeautifulSoup(falabella_page)
    falabella_tv_url=[]
    elements=soup.find_all("div",class_="quickView")
    count=0
    for element in elements:
        falabella_tv_url.append(element.a['href'])
        count+=1
    return falabella_tv_url

def clearString(word):
    return word.replace("$","").replace("Internet:","").replace(" ","").replace(".","")



if __name__ == '__main__':
    falabella_tv_url=getTVLinks()
    for url in falabella_tv_url:
        tv_page=urllib2.urlopen(falabella_url+url).read()
        soupHandler=soup=BeautifulSoup(tv_page)

        price=clearString(soupHandler.find("div",class_="precio1").text)
        model=soupHandler.find('th',text="Modelo").parent.td.text
        print "Model: %s, Price:%i" %(model,int(price))
        falabella_tv_dict[model]=int(price)

    print falabella_tv_dict
