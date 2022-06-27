from calendar import get_calendar_data
from functions import average
from listings import get_listings_data

calendar_data = get_calendar_data()

data = get_listings_data(calendar_data)

for neighborhood in data:
    for room_type in data[neighborhood]:
        average_price = average(data[neighborhood][room_type]['price_sum'] , data[neighborhood][room_type]['counter'])
        average_rating = average(data[neighborhood][room_type]['rating_sum'] , data[neighborhood][room_type]['counter'])
        average_occupancy = average(data[neighborhood][room_type]['occupancy_percentage_sum'] * 100, data[neighborhood][room_type]['counter'])
        data[neighborhood][room_type] = [ average_price , average_rating, average_occupancy ]

print(data)
