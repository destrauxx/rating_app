from random import randint
from bs4 import BeautifulSoup
import requests

from colorama import init, Fore
init()

name_generator = 'https://www.name-generator.org.uk/quick/'
name_page = requests.get(name_generator).text
name_parser = BeautifulSoup(name_page, 'html.parser')
# print(name_page)
for i in range(5):
    # Creation of a name by parsing from the site of the name generator,
    # formatting it to match the format of the record name.
    name = name_parser.find_all(class_ = 'name_heading')[i].get_text().split()
    print(name)
    name = name[0] + "_" + name[1] + str(randint(1, 10))
    print(Fore.LIGHTGREEN_EX + f'Element {name} have created successfully with rating!' + Fore.WHITE) 
# Displaying information about the completion of work on the creation of a rating record
print(Fore.BLUE + "\nCompleted element creation!" + Fore.WHITE)