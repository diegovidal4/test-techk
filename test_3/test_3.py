import urllib2,re
from bs4 import BeautifulSoup

falabella_tv_dict={}

falabella_url="http://www.falabella.com"
ripley_url="http://www.ripley.cl"

ripley_led_uri="http://www.ripley.cl/ripley-chile/tecnologia/tv/led?pageSize=100"
falabella_led_uri="http://www.falabella.com/falabella-cl/category/cat2850014/LED?Nrpp=100"


# ripley_page = urllib2.urlopen(ripley_uri).read()

def getTVLinks():
    """
    Buscar los links de todas las TV del catalogo de falabella y las entrega en una lista:
    Return:
    - Lista con todos los links de las TV
    """
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
    """
    Limpia el string de caracteres indeseados
    Args:
    - Word: String a limpiar.
    Return:
    - String sin caracteres indeseados
    """
    return word.replace("$","").replace("Internet:","").replace(" ","").replace(".","")

def getTVData():
    """
    Genera un diccionario con el modelo y el precio
    """
    falabella_tv_url=getTVLinks()
    for url in falabella_tv_url:
        tv_page=urllib2.urlopen(falabella_url+url).read()
        soupHandler=soup=BeautifulSoup(tv_page)

        price=clearString(soupHandler.find("div",class_="precio1").text)
        model=soupHandler.find('th',text="Modelo").parent.td.text
        print "Model: %s, Price:%i" %(model,int(price))
        falabella_tv_dict[model]=int(price)

    return falabella_tv_dict



if __name__ == '__main__':
