'''
restaurant1 = restaurants(name = 'Saltbebe', area = 'westlands', type = ['luxurious', 'Modern', 'Expensive'], 
reviews = ['Amazing place, very fresh and exotic', 'very Expensive', 'Not worth it', "4/10"], 
contacts = ['0700000000', 'saltshit@gmail.com'])

print(
    'Name : {0:^10s}\nArea : {1:^10s}\nType : {2:^}\nReviews : {3:^}\nContacts : {4:^}'.format(restaurant1.name, restaurant1.area,
    str(restaurant1.types),str(restaurant1.reviews) , str(restaurant1.contacts))

)
'''

#--------------------------------------------------------------------------------------------------------------------------------------

DIST_FROM_CITYBORDER = {'westlands':11, 'thika':40, 'parklands': 10.5, 'ruiru': 50, 'kiambu': 12, 'mlolongo': 18, 'riverside': 6, 
'brookside': 17.89, 'muthaiga': 13.45, 'karen': 19.7, 'langata': 12, 'nairobiwest': 14.68, 'athi river': 16}
DIST_FROM_CITYBORDER_SORTED = {key:value for key, value in sorted(DIST_FROM_CITYBORDER.items(), key = lambda x : x[1])}
TYPES = ['luxurious', 'modern', 'expensive', 'family', 'affordable', 'cheap', 'local', 'italian',
'chinese', 'japanese', 'indian', 'koroga', 'american', 'fast food', 'mexican']

#All restuarants in their locations and types
TOTAREA = {'westlands':set(), 'thika':set(), 'parklands': set(), 'ruiru': set(), 'kiambu': set(), 'mlolongo': set(), 'riverside': set(), 
'brookside': set(), 'muthaiga': set(), 'karen': set(), 'langata': set(), 'nairobiwest': set(), 'athi river': set()}
TOTTYPES = {'luxurious':set(), 'modern':set(), 'expensive':set(), 'family':set(), 'affordable':set(), 'cheap':set(), 'local':set(), 'italian':set(),
'chinese':set(), 'japanese':set(), 'indian':set(), 'koroga':set(), 'american':set(), 'fast food':set(), 'mexican':set()}


class restaurants:
    #rest_loc = {'westlands':0, 'thika':0, 'parklands': 0, 'ruiru': 0}
    def __init__(self, name = None, area = None, types = None, reviews = None, contacts = None): #name:str, area:str.lower(),type: list of str , reviews: list of strs, contacts: list of strs.:
        self.name = name.title()
        self.area = area.lower()
        self.types = list(map(lambda x: x.lower(),types))
        self.reviews = reviews
        self.contacts = contacts
        TOTAREA[area].add(self)
        for i in types:
            TOTTYPES[i].add(self)
        #restaurants.rest_loc[area.lower()] += 1
    def __repr__(self):
        return self.name.title() 
#creating restaurants
chowpaty = restaurants(name = 'Chowpaty', area = 'westlands', types = ['family', 'indian', 'affordable'], 
reviews = ['Amazing place, very fresh and exotic', 'Great service', 'tastes like home and very hygienic', "8/10"], 
contacts = ['0700000000', 'chowpate@gmail.com'])

mercado = restaurants(name = 'Mercado', area = 'westlands', types = ['luxurious', 'modern', 'mexican'], 
reviews = ['Really fast service and technology', 'Great mexican taste', 'Lots of spacing and great interior', "9/10"], 
contacts = ['0700000000', 'mexicoman@gmail.com'])

red_ginger =  restaurants(name = 'Red Ginger', area = 'parklands', types = ['expensive', 'luxurious', 'modern', 'koroga', 'indian'], 
reviews = ['Silent and peaceful as well as quick service', 'Went there with a networth of 2 million and left in debt of 69 million', 'Great place for small groups', "8.5/10"], 
contacts = ['0700000000', 'redginger@gmail.com'])

gordongram = restaurants(name = 'Gordongram', area = 'brookside', types = ['family', 'modern', 'american'], 
reviews = ['Fabulous infrastructure and has playground for kids', 'No prefrozen foods, everything is made at real time', 'Gordon ramsey scared my kids :(', "9/10"], 
contacts = ['0700000000', 'gordonboi@gmail.com'])

#create more restaurants, im too lazy too, ill probably create a program to create more random ones



while True:
    desloc = input('\nLocation of desire(Check for correct spelling):  \n').lower()
    while not(desloc in TOTAREA):
        desloc = input('Sorry location not found, pleasse reenter Location of desire(Check for correct spelling):  \n').lower()
    destypes = [i.strip().lower() for i in (input('Which of these types of restaurants are you looking for :  \n' + str(TYPES) + '\n').split(','))]
    while not(set(destypes).issubset(set(TYPES))):
        print('\nEnter types only from list above, make sure each is seperated by a comma and dont use any other characters\n')
        destypes = [i.strip().lower() for i in (input('\nWhich of these types of restaurants are you looking for :  \n' + str(TYPES)).split(','))]

    results = []
    for i in destypes:
        if TOTAREA[desloc].intersection(TOTTYPES[i]) not in results:
            results.append(TOTAREA[desloc].intersection(TOTTYPES[i]))
    if results == [set()]:
        print('\nNONE FOUND!!')
    else:
        print('\n \n Restaurants found:')
        for i in results[0]:
            print('\nName : {0:^10s}\nArea : {1:^10s}\nType : {2:^}\nReviews : {3:^}\nContacts : {4:^}\n'.format(i.name, i.area,
    str(i.types),str(i.reviews) , str(i.contacts)))


    cont = input('Would you like to see more? (y/n)?')
    if cont == 'y':
        loc_or_type = input('Would you like to see more in the same location or of the same type? (location/type)?').strip().lower()
    else:
        continue
    
    if loc_or_type == 'location':
        for i in TOTAREA[desloc]:
            print('\nName : {0:^10s}\nArea : {1:^10s}\nType : {2:^}\nReviews : {3:^}\nContacts : {4:^}\n'.format(i.name, i.area,
    str(i.types),str(i.reviews) , str(i.contacts)))
    else:
        for x in destypes:
            for i in TOTTYPES[x]:
                print('\nName : {0:^10s}\nArea : {1:^10s}\nType : {2:^}\nReviews : {3:^}\nContacts : {4:^}\n'.format(i.name, i.area,
    str(i.types),str(i.reviews) , str(i.contacts)))
