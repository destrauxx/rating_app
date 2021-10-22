from bs4 import BeautifulSoup
import requests 
name_creator = 'https://www.name-generator.org.uk/quick/'

name_page = requests.get(name_creator).text
name_parser = BeautifulSoup(name_page, 'html.parser')
name_data = []

count = 2
name = [i.get_text() for i in name_parser.find_all(class_ = 'name_heading')[:count]]
print(name)