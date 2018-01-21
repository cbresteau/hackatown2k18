import googlemaps
import json

API_Key = 'AIzaSyCpvaP1KDRxjb3YZUTFCwuoGEiqVf1XGgs'
gmaps = googlemaps.Client(key=API_Key)

#input: coordonnées GPS de l'endroit auquel intervenir

a = gmaps.geocode("4635 rue saint Urbain")
x = a[0]['geometry']['viewport']['southwest']['lat']
y = a[0]['geometry']['viewport']['southwest']['lng']

coord_input = x, y

#load du fichier json des feux

with open('geo_redlights.json') as json_data:
    file = json.load(json_data)

class feu:
    def __init__(self, id, coord):
        self.id = id
        self.coord = coord
        self.on = 0

feux = []

liste = file['features']

for unit in liste:
    feux.append(feu(unit['properties']['id'], unit['geometry']['coordinates']))

#Création des casernes

class caserne:
    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat
        self.coord = long, lat

casernes = []
casernes.append(caserne("RachelEst", 45.5258129621963, -73.5749028744983))
casernes.append(caserne("MontRoyalEst", 45.5360280348549, -73.571933009301))
casernes.append(caserne("LaurierOuest", 45.5229649648134, -73.5932429899519))
casernes.append(caserne("Roosevelt", 45.5152676091238, -73.6407797907479))


#Choix de la caserne qui va intervenir

def choix_caserne(lat, long):

    duration_opt = 10000000
    Choix = casernes[0]

    for caserne in casernes:
        travel = gmaps.distance_matrix(caserne.coord, (lat, long))
        duration_caserne = travel["rows"][0]['elements'][0]['duration']['value']
        if duration_caserne < duration_opt:
            Choix = caserne
            duration_opt = duration_caserne
        else:
            Choix = Choix

    return Choix

#Détermination des étapes du chemin

class etape:
    def __init__(self, id, coord_init, coord_end):
        self.id = id
        self.coord_init = coord_init
        self.coord_end = coord_end

etapes = []
i = 0


#Test quels feux appartiennent à chacun des chemins

def test_segment(coord1, coord2, coord3):
    inc = 0.1
    coord1_x = abs(coord1[0])
    coord2_x = abs(coord2[0])
    coord3_x = abs(coord3[0])
    coord1_y = abs(coord1[1])
    coord2_y = abs(coord2[1])
    coord3_y = abs(coord3[1])
    droite = 0
    m1 = abs((coord3_y - coord1_y) / (coord3_x - coord1_x))
    m2 = abs((coord3_y - coord2_y) / (coord3_x - coord2_x))
    if abs(m1 - m2) <= inc:
        if ((coord3_x - coord1_x >= 0) and (coord3_x - coord2_x <= 0)) or ((coord3_x - coord2_x >= 0) and (coord3_x - coord1_x <= 0)):
            if ((coord3_y - coord1_y >= 0) and (coord3_y - coord2_y <= 0)) or ((coord3_y - coord2_y >= 0) and (coord3_y - coord1_y <= 0)):
                droite += 1
            else:
                droite = droite
        else:
            droite = droite
    else:
        droite = droite
    return droite


def test_inter(coord1, coord3):
    ajout = 0
    inc = 0.0005
    diff1 = abs((coord1[0]-coord3[0]))
    diff2 = abs((coord1[1]-coord3[1]))
    if diff1 <= inc and diff2 <= inc:
        ajout += 1
    else:
        ajout = ajout
    return ajout

feu_imp = []

#Main
cas_choisie = choix_caserne(x, y)
print(cas_choisie.name)

chemin = gmaps.directions(cas_choisie.coord, coord_input)

print("différentes étapes")
for step in chemin[0]['legs'][0]['steps']:
    start_coor = step['start_location']['lat'], step['start_location']['lng']
    end_coor = step['end_location']['lat'], step['end_location']['lng']
    etapes.append(etape(i, start_coor, end_coor))
    i +=1
    print(start_coor)
    print(end_coor)

print("ID des feux")
for feu in feux:
    for etape in etapes:
        feu.on += test_segment(etape.coord_init, etape.coord_end, feu.coord)
        feu.on += test_inter(etape.coord_init, feu.coord)
    if feu.on > 0:
        feu_imp.append(feu)
        print(feu.id)

print(len(feu_imp))

