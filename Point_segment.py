def test_droite(coord1, coord2, coord3):
    inc = 0.0001
    droite = 0
    m1 = (coord2.y - coord1.y) / (coord2.x - coord1.x)
    m2 = (coord3.y - coord1.y) / (coord3.x - coord1.x)
    if (m1 - m2) <= inc:
        if (coord3.x >= coord1.x and coord3.x <= coord2.x) or (coord3.x >= coord2.x and coord3.x <= coord1.x):
            if (coord3.y >= coord1.y and coord3.y <= coord2.y) or (coord3.y >= coord2.y and coord3.y <= coord1.y):
                droite += 1
            else:
                droite = droite
        else:
            droite = droite
    else:
        droite = droite

    return droite

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

coord1 = point(45.5082173272, -73.5747242614)
coord2 = point(45.509215371, -73.57685081)
coord3 = point(45.506977227, -73.5721068227)

a = test_droite(coord1, coord2, coord3)
print(a)