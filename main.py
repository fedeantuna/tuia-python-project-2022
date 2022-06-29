import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from airbnb_calendar import get_calendar_data
from airbnb_listings import get_listings_data
from functions import average

def main():
    (airbnb_data, neighbourhoods, room_types) = _read_airbnb_data()
    normalized_room_types = []

    for neighbourhood in neighbourhoods:
        for room_type in room_types:
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
            
            normalized_room_type = room_type.lower().replace(' ', '_').replace('/', '_')
            if normalized_room_type not in normalized_room_types:
                normalized_room_types.append(normalized_room_type)

            if f'{normalized_room_type}_occupancy' not in locals():
                locals()[f'{normalized_room_type}_occupancy'] = []
            if f'{normalized_room_type}_price' not in locals():
                locals()[f'{normalized_room_type}_price'] = []
            if f'{normalized_room_type}_rating' not in locals():
                locals()[f'{normalized_room_type}_rating'] = []
            
            locals()[f'{normalized_room_type}_occupancy'].append(average_occupancy)
            locals()[f'{normalized_room_type}_price'].append(average_price)
            locals()[f'{normalized_room_type}_rating'].append(average_rating)

    sns.set()

    x = np.arange(len(neighbourhoods))
    width = 0.20
    relative_distances = _get_relative_distances(width, normalized_room_types)
    fig, ax = plt.subplots()
    for normalized_room_type in normalized_room_types:
        # ax.bar(locals()[f'{normalized_room_type}_occupancy'])
        ax.bar(x + relative_distances[normalized_room_type], locals()[f'{normalized_room_type}_price'], width, label=f'{normalized_room_type}')
        # print(locals()[f'{normalized_room_type}_rating'])

    fig.tight_layout()
    ax.set_xticks(x, neighbourhoods)
    ax.legend()
    plt.show()

def _read_airbnb_data():
    calendar_data = get_calendar_data()
    return get_listings_data(calendar_data)

def _get_relative_distances(width, bars):
    start = -0.5 * len(bars)

    positions = {}

    bar_counter = 0
    for current_bar in bars:
        positions[current_bar] = (start + bar_counter) * width
        bar_counter += 1
    
    return positions

main()