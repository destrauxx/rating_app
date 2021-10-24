from bs4 import BeautifulSoup
import requests 
from colorama import init, Fore, Back
name_creator = 'https://www.name-generator.org.uk/quick/'

name_page = requests.get(name_creator).text
name_parser = BeautifulSoup(name_page, 'html.parser')
name_data = []

name = name_parser.find(class_ = 'name_heading').get_text().split()

print(name[0] + '_' + name[1])