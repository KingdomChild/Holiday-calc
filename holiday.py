
def days(hotel):
    return hotel
def rent(car):
    return car
def city(plane):
    return plane


hotel_i = raw_input("How many nights are you staying? ")
hotel = float(hotel_i) * 180.00


print


car = float(hotel_i) * 120.00


print


plane_i = raw_input("Please choose a or b for the town you are flying to:\na. Durban - R1100\nb. Cape Town - R1200\n").upper()


print


if plane_i == "A":
    plane = 1100.00
    print "Your total holiday cost is R" + str(days(hotel) + rent(car) + city(plane))
    
if plane_i == "B":
    plane = 1200.00
    print "Your total holiday cost is R" + str(days(hotel) + rent(car) + city(plane))


