import googlemaps

API_Key = 'AIzaSyCpvaP1KDRxjb3YZUTFCwuoGEiqVf1XGgs'
gmaps = googlemaps.Client(key=API_Key)

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


def choix_caserne(lat, long):

    duration_opt = 10000000
    Choix = casernes[0]

    for caserne in casernes:
        travel = gmaps.distance_matrix((lat, long), caserne.coord)
        duration_caserne = travel["rows"][0]['elements'][0]['duration']['value']
        if duration_caserne < duration_opt:
            Choix = caserne
            duration_opt = duration_caserne
        else:
            Choix = Choix

    return Choix

a = gmaps.geocode("4635 rue saint Urbain")
lat = a[0]['geometry']['viewport']['southwest']['lat']
lng = a[0]['geometry']['viewport']['southwest']['lng']

cas_choisie = choix_caserne(lat, lng)
print(cas_choisie.name)




