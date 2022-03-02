# python3 manage.py runscript create_users
import random
from random import randrange
from django.contrib.auth.models import User
from django.db.models import Max
from smartpet.models import Pet, petBreed, petType


def printtitle(mesaj):
    print("")
    print("="*24)
    print("     " + str(mesaj))
    print("="*24)


# User strings
usernames_str = "coni,sezium,banker,littlegirl,officeboy,carrot,mahmut,ricardo,emanuel,kullanici,patates,ajda,canan,"
usernames_str += "michel,betty,michael,rebecca,sandra,lisa,martha,ulrich,stephan,bill,robert,aras,ceyhun,naz,elif,meltem"
firstnames_str = "Elma,Armut,Portakal,Mandalina,Muz,Karpuz,Nar,Ananas,Çilek,Kiraz,Vişne,Kayisi,Şeftali,Kavun,Üzüm"
lastnames_str = "Kirmizi,Mavi,Yesil,Mor,Kahverengi,Sarı,Turuncu,Turkuaz,Pembe,Fusya,Lacivert,Haki,Gri,Krem,Bej,Bakır,Bordo,Güldane"
mailextensions_str = "gmail.com,hotmail.com,outlook.com,yahoo.com,mail.com"

usernames = usernames_str.split(",")
firstnames = firstnames_str.split(",")
lastnames = lastnames_str.split(",")
mailextensions = mailextensions_str.split(",")


# petTypes
pettype_str = "Cat,Dog,Fish,Snake"
# "Cat,Dog,Fish,Snake,Rabbit,Bird,Iguana,Spider,Duck,Monkey"
# Cat Breeds List
catbreed_str = "Ragdoll,Exotic Shorthair,Maine Coon,Persian,British Shorthair,Devon Rex,Abyssinian,American Shorthair,Scottish Fold,Sphynx,Oriental,Siamese,Cornish Rex,Norwegian Forest Cat,Siberian,Birman,Russian Blue,Bengal,Tonkinese,Burmese,Ocicat"
# Dog Breeds List
dogbreed_str = "Retriever (Labrador),French Bulldog,German Shepherd Dog,Golden Retriever,Bulldog,Poodle,Beagle,Rottweiler,Pointer (German Shorthaired),Dachshund,Pembroke Welsh Corgi,Australian Shepherd,Yorkshire Terrier,Boxer,Great Dane,Siberian Huskie,Cavalier King Charles Spaniel,Doberman Pinscher,Miniature Schnauzer"
# Fish Breeds List
fishbreed_str = "Hamsi,Lüfer,Zargana,Çinekop,Japon,Ciklet"
# Snake Breeds List
snakebreed_str = "Python,Cobra,Anaconda,Engerek,Chikichiki Çıngıraklı,Waterloo"
# Pet Names List
petnames_str = "Bella,Kitty,Lily,Lilly,Charlie,Lucy,Leo,Milo,Jack,Nala,Sam,Simba,Chloe,Baby,Sadie,Ziggy,Princess,Salem,Sophie,Shadow,Izzy,Cleo,Boots,Loki,Daisy,Cooper,Missy,Oreo,Tiger,Lulu,Tucker,Jasmine,Jackson,Murphy,Pepper,Fiona,Jax,Frank,Romeo,Millie,Abby,Minnie,Olivia,Lola,Athena,Teddy,Ruby,Oscar,Bear,Moose,Pumpkin,Willow,Mittens,Coco,Penny,Sammy,Sammie,Theo,Kali,Bob,Clyde,Tigger,Buddy,Joey,Emma,Ollie,Toby,George,Marley,Bagheera,Belle,Binx,Boo,Ash,Scout,Gizmo,Louie,Ginger,Midnight,Mochi,Blue,Frankie,Rosie,Ella,Calvin,Lucky,Hazel,Thor,Gus,Maggie,Piper,Harley,Rocky,Peanut,Mimi,Kitten,Remy,Remi,Annie,Sunny,Layla,Leila,Riley,Walter"


pettypes = pettype_str.split(",")
catbreeds = catbreed_str.split(",")
dogbreeds = dogbreed_str.split(",")
fishbreeds = fishbreed_str.split(",")
snakebreeds = snakebreed_str.split(",")
petnames = petnames_str.split(",")


# create Users
#
# username = each usernames
# first_name = Random
# last_name = Random
# email = username[RandomNumber]@[RandomMailExtension]

# =======================================================================================================
printtitle("Creating Users...")

created_users = 0
skipped_users = 0
for user_name in usernames:

    kontroluser = User.objects.get_or_create(
        username=user_name, defaults={'first_name': random.choice(firstnames),
                                      'last_name': random.choice(lastnames),
                                      'email': user_name + str(randrange(18, 32)) + "@" + random.choice(mailextensions)}
    )
    # kontroluser list
    print(kontroluser)
    # kontroluser = (<User: user_name>, True/False)
    if kontroluser[1] == True:  # If operation succesful
        created_users += 1
    else:
        skipped_users += 1
print(str(created_users) + " created.")
print(str(skipped_users) + " skipped.")
print("Total: " + str(len(usernames)))

# =======================================================================================================
printtitle("Selecting Random User")

# Select Random User.id


def user_random():
    max_id = User.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        randomuser = User.objects.filter(pk=pk).first()
        if randomuser:
            return randomuser.id


print("Random User.id : " + str(user_random()))

# =======================================================================================================
# Creating petTypes
printtitle("Creating petTypes (Cat,Dog,Fish,Snake etc.)")
for pettype in pettypes:
    created = petType.objects.get_or_create(name=pettype)
    print(created)

# =======================================================================================================
printtitle("Creating petnames...")
for petname in petnames:
    pettype = random.choice(pettypes)
    if pettype == 'Cat':
        petbreeds = catbreeds
    elif pettype == 'Dog':
        petbreeds = dogbreeds
    elif pettype == 'Fish':
        petbreeds = fishbreeds
    elif pettype == 'Snake':
        petbreeds = snakebreeds

    petbreed = random.choice(petbreeds)
    owner = user_random()
    print(petname + "," + pettype + "," + petbreed + "," + str(owner))

    # b, created = petBreed.objects.get_or_create(
    #     name=petbreed, defaults={'pettype': petType(name=pettype)})
    # print(created)

    # c = Pet(name=row[0], petbreed=b,
    #         pettype=petType(id=1), owner=User(id=1))
    # c.save()
