from urllib.request import urlopen
from xml.etree.ElementTree import parse

url = "http://www.cbr.ru/scripts/XML_daily.asp"

xml = urlopen(url)
tree = parse(xml)

root = tree.getroot()

ID = "R01200" #ID гонконского доллара

for valute in root.findall('Valute'):   #линейный поиск нужной валюты по ID
    if (ID == valute.get("ID")):        #

        value = valute.find("Value").text      #получаем значение 
        nominal = valute.find("Nominal").text  #получаем номинал 
        char = valute.find("CharCode").text    #получаем название

        value = float(value.replace(',','.'))   # конвертация для в значения
        nominal = int(nominal)                  #

        print("1 " + char + " = " + str(value / nominal) + " RUB") 
        break #прекращение поиска
