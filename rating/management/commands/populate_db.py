from django.core.management.base import BaseCommand

from rating.models import Rating

class Command(BaseCommand):
    help = 'adding some entries to Rating models'
    missing_args_message = 'You do not entry the number of required to create rating nodes'
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)
    
    def handle(self, *args, **options):
        from random import randint
        from bs4 import BeautifulSoup
        import requests

        from colorama import init, Fore
        init()

        name_generator = 'https://www.name-generator.org.uk/quick/'
        count = options.get('count', 1)

        for i in range(count):
            # Creation of a name by parsing from the site of the name generator,
            # formatting it to match the format of the record name.
            name_page = requests.get(name_generator).text
            name_parser = BeautifulSoup(name_page, 'html.parser')
            name = name_parser.find(class_ = 'name_heading').get_text().split()
            name = name[0] + "_" + name[1] + str(randint(1, 10))

            # Making a copy of the number of records in the database before creating the record
            count_ratings = Rating.objects.count()

            # Creating a record in the database and saving it
            r = Rating(name=name, text='Created from command line', rate=randint(1, 5))
            r.save()

            # Displaying the status of record creation in accordance with the database data
            if count_ratings < Rating.objects.count():
                print(Fore.LIGHTGREEN_EX + f'Element {name} have created successfully with rating {r.rate}!' + Fore.WHITE)   
            else:
                print(Fore.RED + f'Element {name} have not created!' + Fore.WHITE)

        # Displaying information about the completion of work on the creation of a rating record
        print(Fore.BLUE + "\nCompleted element creation!" + Fore.WHITE)