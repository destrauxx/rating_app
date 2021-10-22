from django.core.management.base import BaseCommand

from rating.models import Rating

class Command(BaseCommand):
    help = 'adding some entries to Rating models'
    missing_args_message = 'kek'
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)
    
    def handle(self, *args, **options):
        from random import randint
        from bs4 import BeautifulSoup
        import requests 
        name_creator = 'https://www.name-generator.org.uk/quick/'

        name_page = requests.get(URL).text
        name_parser = BeautifulSoup(name_page, 'html.parser')
        name_data = {}

        for row in name_parser.find_all(class_ = 'name_heading'):
            ids, name = row.find_all('td')[0].get_text(), row.find_all('td')[1].get_text()
            name_data[name] = ids
            print(ids, name, name_data)
        count = options.get('count', 1)
        for i in range(count):
            r = Rating(name=i, text='created from command line', rate=randint(1, 5))
            r.save()
            print('Element have created successfuly!')
        print('Done!')