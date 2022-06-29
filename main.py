from airbnb_calendar import get_calendar_data
from functions import average
from airbnb_listings import get_listings_data

calendar_data = get_calendar_data()
listings_data = get_listings_data(calendar_data)

data = {}

for neighbourhood in listings_data:
    data[neighbourhood] = {}

    for room_type in listings_data[neighbourhood]:
        data[neighbourhood][room_type] = {}

        price_sum = listings_data[neighbourhood][room_type]['price_sum']
        rating_sum = listings_data[neighbourhood][room_type]['rating_sum']
        occupancy_percentage_sum = listings_data[neighbourhood][room_type]['occupancy_percentage_sum'] * 100
        counter = listings_data[neighbourhood][room_type]['counter']

        average_occupancy = average(occupancy_percentage_sum, counter)
        average_price = average(price_sum, counter)
        average_rating = average(rating_sum, counter)

        data[neighbourhood][room_type] = {
            'average_occupancy': average_occupancy,
            'average_price': average_price,
            'average_rating': average_rating
        }

print(data)