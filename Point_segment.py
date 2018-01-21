def test_segment(coord1, coord2, coord3):
    inc = 0.1
    droite = 0
    m1 = abs((coord2[1] - coord1[1]) / (coord2[0] - coord1[0]))
    m2 = abs((coord3[1] - coord1[1]) / (coord3[0] - coord1[0]))
    if abs(m1 - m2) <= inc:
        if (coord3[0] >= coord1[0] and coord3[0] <= coord2[0]) or (coord3[0] >= coord2[0] and coord3[0] <= coord1[0]):
            if (coord3[1] >= coord1[1] and coord3[1] <= coord2[1]) or (coord3[1] >= coord2[1] and coord3[1] <= coord1[1]):
                droite += 1
            else:
                droite = droite
        else:
            droite = droite
    else:
        droite = droite
    return droite

coord1 = 45.5082173272, -73.5747242614
coord2 = 45.509215371, -73.57685081
coord3 = 45.506977227, -73.5721068227

a = test_segment(coord1, coord2, coord3)
print(a)
