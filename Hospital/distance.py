from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)



def dist_location(lat1,lon1,lat2,lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    # print("Result:", distance)
    # print("Should be:", 278.546, "km")

    return distance


def get_small_distance(sugiest_hospital, get_random_patient):
    min_dis = 99999999999
    list_small_dis = []
    for hospital_dis in sugiest_hospital:
        if dist_location(hospital_dis[4], hospital_dis[5], get_random_patient[1], get_random_patient[2]) < min_dis:
            list_small_dis = []
            min_dis = dist_location(
                hospital_dis[4], hospital_dis[5], get_random_patient[1], get_random_patient[2])
            list_small_dis.append(hospital_dis)
    return list_small_dis, min_dis
