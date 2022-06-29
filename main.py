from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from airbnb_calendar import get_calendar_data
from airbnb_listings import get_listings_data
from functions import average, normalize_str

def main():
    (airbnb_data, neighbourhoods, room_types) = _read_airbnb_data()

    for neighbourhood in neighbourhoods:
        for room_type in room_types:
            (average_occupancy, average_price, average_rating) = \
                _filter_average_data_by_neighbourhood_by_room_type(airbnb_data,
                    neighbourhood,
                    room_type)

            _generate_plot_data(room_type, average_occupancy, average_price, average_rating)

    _plot(neighbourhoods, room_types)

def _read_airbnb_data() -> Tuple[dict, list, list]:
    calendar_data = get_calendar_data()
    return get_listings_data(calendar_data)

def _get_relative_distances(width: float, bars: list):
    start = -0.5 * len(bars)

    positions = {}

    for (idx, current_bar) in enumerate(bars):
        positions[current_bar] = (start + idx) * width
    
    return positions

def _filter_average_data_by_neighbourhood_by_room_type(data: dict, neighbourhood: str, room_type: str) -> Tuple[float, float, float]:
    if room_type in data[neighbourhood].keys():
        occupancy_percentage_sum = data[neighbourhood][room_type]['occupancy_percentage_sum'] * 100
        price_sum = data[neighbourhood][room_type]['price_sum']
        rating_sum = data[neighbourhood][room_type]['rating_sum']
        counter = data[neighbourhood][room_type]['counter']
    else:
        occupancy_percentage_sum = 0
        price_sum = 0
        rating_sum = 0
        counter = 0
    
    if counter != 0:
        average_occupancy = average(occupancy_percentage_sum, counter)
        average_price = average(price_sum, counter)
        average_rating = average(rating_sum, counter)
    else:
        average_occupancy = 0
        average_price = 0
        average_rating = 0

    return (average_occupancy, average_price, average_rating)

def _normalize_room_types(room_types: list) -> dict:
    normalized_room_types = {}

    for room_type in room_types:
        normalized_room_type = normalize_str(room_type)
        if normalized_room_type not in normalized_room_types.keys():
            normalized_room_types[normalized_room_type] = room_type
    
    return normalized_room_types

def _generate_plot_data(room_type: str, average_occupancy: float, average_price: float, average_rating: float):
    normalized_room_type = normalize_str(room_type)
    if f'_{normalized_room_type}_occupancy' not in globals():
        globals()[f'_{normalized_room_type}_occupancy'] = []
    if f'_{normalized_room_type}_price' not in globals():
        globals()[f'_{normalized_room_type}_price'] = []
    if f'_{normalized_room_type}_rating' not in globals():
        globals()[f'_{normalized_room_type}_rating'] = []
    
    globals()[f'_{normalized_room_type}_occupancy'].append(average_occupancy)
    globals()[f'_{normalized_room_type}_price'].append(average_price)
    globals()[f'_{normalized_room_type}_rating'].append(average_rating)

def _plot(neighbourhoods: list, room_types: list):
    sns.set()

    normalized_room_types = _normalize_room_types(room_types)
    x = np.arange(len(neighbourhoods))
    width = 0.20
    relative_distances = _get_relative_distances(width, normalized_room_types)
    fig, ax = plt.subplots()
    for normalized_room_type in normalized_room_types.keys():
        ax.bar(x + relative_distances[normalized_room_type], globals()[f'_{normalized_room_type}_rating'], width, label=normalized_room_types[normalized_room_type])

    ax.set_xticks(x, neighbourhoods)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_title('Average Price per Neighborhood per Room Type', fontsize = 14)
    plt.xticks(rotation = 90, fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.xlabel('Neighbourhoods', fontsize = 12)
    plt.ylabel('Average Price', fontsize = 12)
    fig.tight_layout()
    plt.show()

main()