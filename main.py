import matplotlib.pyplot as plt
import seaborn as sns

from airbnb_calendar import get_calendar_data
from airbnb_listings import get_listings_data
from functions import average

def main():
    (airbnb_data, neighbourhoods, room_types) = _read_airbnb_data()
    normalized_room_types = []

    for neighbourhood in neighbourhoods:
        for room_type in room_types:
            normalized_room_type = room_type.lower().replace(' ', '_').replace('/', '_')
            if normalized_room_type not in normalized_room_types:
                normalized_room_types.append(normalized_room_type)

            if room_type in airbnb_data[neighbourhood].keys():
                price_sum = airbnb_data[neighbourhood][room_type]['price_sum']
                rating_sum = airbnb_data[neighbourhood][room_type]['rating_sum']
                occupancy_percentage_sum = airbnb_data[neighbourhood][room_type]['occupancy_percentage_sum'] * 100
                counter = airbnb_data[neighbourhood][room_type]['counter']
            else:
                price_sum = 0
                rating_sum = 0
                occupancy_percentage_sum = 0
                counter = 0
            
            if counter != 0:
                average_occupancy = average(occupancy_percentage_sum, counter)
                average_price = average(price_sum, counter)
                average_rating = average(rating_sum, counter)
            else:
                average_occupancy = 0
                average_price = 0
                average_rating = 0

            if f'{normalized_room_type}_occupancy' not in locals():
                locals()['%s_occupancy' % normalized_room_type] = []
            if f'{normalized_room_type}_price' not in locals():
                locals()['%s_price' % normalized_room_type] = []
            if f'{normalized_room_type}_rating' not in locals():
                locals()['%s_rating' % normalized_room_type] = []
            
            locals()['%s_occupancy' % normalized_room_type].append(average_occupancy)
            locals()['%s_price' % normalized_room_type].append(average_price)
            locals()['%s_rating' % normalized_room_type].append(average_rating)

    print(list(airbnb_data.keys()))
    for normalized_room_type in normalized_room_types:
        print(locals()['%s_occupancy' % normalized_room_type])
        print(locals()['%s_price' % normalized_room_type])
        print(locals()['%s_rating' % normalized_room_type])

def _read_airbnb_data():
    calendar_data = get_calendar_data()
    return get_listings_data(calendar_data)

main()