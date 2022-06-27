from calendar import get_calendar_data
from functions import average
from listings import get_listings_data

calendar_data = get_calendar_data()
listings_data = get_listings_data(calendar_data)

data = {}

for neighborhood in listings_data:
    data[neighborhood] = {}

    for room_type in listings_data[neighborhood]:
        data[neighborhood][room_type] = {}

        price_sum = listings_data[neighborhood][room_type]['price_sum']
        rating_sum = listings_data[neighborhood][room_type]['rating_sum']
        occupancy_percentage_sum = listings_data[neighborhood][room_type]['occupancy_percentage_sum'] * 100
        counter = listings_data[neighborhood][room_type]['counter']

        average_price = average(price_sum, counter)
        average_rating = average(rating_sum, counter)
        average_occupancy = average(occupancy_percentage_sum, counter)

        data[neighborhood][room_type] = [
            average_price,
            average_rating,
            average_occupancy
        ]

print(data)
