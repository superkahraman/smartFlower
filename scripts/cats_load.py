import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript cats_load

from smartpet.models import Pet, petBreed, petType, User


def run():
    fhand = open('smartpet/meow.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    # Pet.objects.all().delete()
    # petBreed.objects.all().delete()

    # Name,Breed,Weight
    # Abby,Sphinx,6.4
    # Annie,Burmese,7.6
    # Ash,Manx,7.8
    # Athena,Manx,8.9
    # Baby,Tabby,6.9

    for row in reader:
        # print(row[0] + " [" + row[1] + "]")
        print(row)
        b, created = petBreed.objects.get_or_create(
            name=row[1], defaults={'pettype': petType(id=1)})
        print(created)

        c = Pet(name=row[0], petbreed=b,
                pettype=petType(id=1), owner=User(id=1))
        c.save()
