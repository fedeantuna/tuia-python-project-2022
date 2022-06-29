from airbnb_calendar import get_calendar_data
from airbnb_listings import get_listings_data
from functions import average

def main():
    airbnb_data = _read_airbnb_data()
    
    data = {}

    for neighbourhood in airbnb_data:
        data[neighbourhood] = {}

        for room_type in airbnb_data[neighbourhood]:
            data[neighbourhood][room_type] = {}

            price_sum = airbnb_data[neighbourhood][room_type]['price_sum']
            rating_sum = airbnb_data[neighbourhood][room_type]['rating_sum']
            occupancy_percentage_sum = airbnb_data[neighbourhood][room_type]['occupancy_percentage_sum'] * 100
            counter = airbnb_data[neighbourhood][room_type]['counter']

            average_occupancy = average(occupancy_percentage_sum, counter)
            average_price = average(price_sum, counter)
            average_rating = average(rating_sum, counter)

            data[neighbourhood][room_type] = {
                'average_occupancy': average_occupancy,
                'average_price': average_price,
                'average_rating': average_rating
            }

    print(data)

def _read_airbnb_data():
    calendar_data = get_calendar_data()
    listings_data = get_listings_data(calendar_data)

    return listings_data

main()