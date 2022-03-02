# This script creates "comma seperated" list for creating Pets

import random
from random import randrange

# petTypes

pettype_str = "Cat,Dog,Fish,Snake"
# "Cat,Dog,Fish,Snake,Rabbit,Bird,Iguana,Spider,Duck,Monkey"


# Cat Breeds List
catbreed_str = "Ragdoll,Exotic Shorthair,Maine Coon,Persian,British Shorthair,Devon Rex,Abyssinian,American Shorthair,Scottish Fold,Sphynx,Oriental,Siamese,Cornish Rex,Norwegian Forest Cat,Siberian,Birman,Russian Blue,Bengal,Tonkinese,Burmese,Ocicat"
# Dog Breeds List
dogbreed_str = "Retriever (Labrador),French Bulldog,German Shepherd Dog,Golden Retriever,Bulldog,Poodle,Beagle,Rottweiler,Pointer (German Shorthaired),Dachshund,Pembroke Welsh Corgi,Australian Shepherd,Yorkshire Terrier,Boxer,Great Dane,Siberian Huskie,Cavalier King Charles Spaniel,Doberman Pinscher,Miniature Schnauzer"


breedstr = '''Persian
Siamese
Sphinx
Burmese
Scottish-Fold
Tabby
Manx'''

namestr = '''Bella
Kitty
Lily
Lilly
Charlie
Lucy
Leo
Milo
Jack
Nala
Sam
Simba
Chloe
Baby
Sadie
Ziggy
Princess
Salem
Sophie
Shadow
Izzy
Cleo
Boots
Loki
Daisy
Cooper
Missy
Oreo
Tiger
Lulu
Tucker
Jasmine
Jackson
Murphy
Pepper
Fiona
Jax
Frank
Romeo
Millie
Abby
Minnie
Olivia
Lola
Athena
Teddy
Ruby
Oscar
Bear
Moose
Pumpkin
Willow
Mittens
Coco
Penny
Sammy
Sammie
Theo
Kali
Bob
Clyde
Tigger
Buddy
Joey
Emma
Ollie
Toby
George
Marley
Bagheera
Belle
Binx
Boo
Ash
Scout
Gizmo
Louie
Ginger
Midnight
Mochi
Blue
Frankie
Rosie
Ella
Calvin
Lucky
Hazel
Thor
Gus
Maggie
Piper
Harley
Rocky
Peanut
Mimi
Kitten
Remy
Remi
Annie
Sunny
Layla
Leila
Riley
Walter
'''

names = namestr.split()
breeds = breedstr.split()
pettypes = pettype_str.split(",")
catbreeds = catbreed_str.split(",")


pets = list()  # We're creating empty list
# We process every row with uniqe names
# It means this script creates Pets records for each name
# Otherthings (pettype,petbreed,owner) are created by random
for name in names:
    pettype = random.choice(pettypes)
    if pettype == 'Cat':
        petbreeds = catbreed_str.split(",")
        print(name + "," + pettype + "," + random.choice(petbreeds) + ",")
    elif pettype == 'Dog':
        petbreeds = dogbreed_str.split(",")
        print(name, pettype, random.choice(petbreeds))
#    cat = name+','+random.choice(catbreeds)+','+str(6.0+randrange(40)/10.0)
#    pets.append(cat)

# for cat in sorted(pets):
#    print(cat)
