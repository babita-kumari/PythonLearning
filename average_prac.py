ev_data = [['vehicle', 'range', 'price'],
           ['Tesla Model 3 LR', '310', '49900'],
           ['Hyundai Ioniq EV', '124', '30315'],
           ['Chevy Bolt', '238', '36620']]

print(ev_data)

for row in ev_data[1:]:
    print(row)
    ev_range=row[1]
    ev_range=int(ev_range)
    row[1]=ev_range
print(ev_data)

total_range=0
for row in ev_data[1:]:
    ev_range=row[1]
    total_range+=ev_range

number_of_cars=len(ev_data[1:])
print(number_of_cars)

average_range=total_range/number_of_cars
print(average_range)

total_price=0

for row in ev_data[1:]:
    ev_price=row[2]
    ev_price=int(ev_price)
    row[2]=ev_price
    total_price+=ev_price
average_price=total_price/number_of_cars
print(average_price)

for row in ev_data[1:]:
    ev_price=row[2]
    ev_vehicle=row[0]
    if ev_price>40000:
        print(ev_vehicle)




