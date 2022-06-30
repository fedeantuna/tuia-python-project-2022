import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from typing import List, Tuple

from airbnb_calendar import get_calendar_data
from airbnb_listings import get_listings_data
from functions import average, normalize_str, normalize_str_list

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
    """
    Reads the Airbnb files and merges them into a dictionary
    containing the average occupancy, average price and average rating
    organized by neighbourhood and room type

    Returns:
        A dictionary containing the average occupancy, average price and average
    rating organized by neighbourhood and room type
    """

    calendar_data = get_calendar_data()
    return get_listings_data(calendar_data)

def _filter_average_data_by_neighbourhood_by_room_type(data: dict, neighbourhood: str, room_type: str) -> Tuple[float, float, float]:
    """
    Filters the given data by neighbourhood and room type to find
    the average occupancy, average price and average rating

    Arguments:
        data: a dictionary representing the Airbnb data
        neighbourhood: a string representing the filtering neighbourhood
        room_type: a string representing the filtering room_type

    Returns:
        The average average occupancy, average price and average rating
    for the given data filtered by neighbourhood and room type
    """

    if room_type in data[neighbourhood].keys():
        occupancy_percentage_sum = data[neighbourhood][room_type]['occupancy_percentage_sum'] * 100
        price_sum = data[neighbourhood][room_type]['price_sum']
        rating_sum = data[neighbourhood][room_type]['rating_sum']
        counter = data[neighbourhood][room_type]['counter']
    else:
        occupancy_percentage_sum = np.nan
        price_sum = np.nan
        rating_sum = np.nan
        counter = 0

    if counter != 0:
        average_occupancy = average(occupancy_percentage_sum, counter)
        average_price = average(price_sum, counter)
        average_rating = average(rating_sum, counter)
    else:
        average_occupancy = np.nan
        average_price = np.nan
        average_rating = np.nan

    return (average_occupancy, average_price, average_rating)

def _generate_plot_data(room_type: str, average_occupancy: float, average_price: float, average_rating: float):
    """
    Generates the data needed for plotting. Given a room type and it's
    average occupancy, average price and average rating, it will generate
    the corresponding lists for each average value with the room type. If
    the list already exists, it will keep adding to its values. Correct use
    of this function requires that a matching neighbourhood list exists.

    Arguments:
        room_type: a string representing the room type
        average_occupancy: a float representing the average occupancy
        average_price: a float representing the average price
        average_rating: a float representing the average rating
    """

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

def _plot(neighbourhoods: List[str], room_types: List[str]):
    """
    Generates different graphs for the user to see based on the
    neighbourhoods and room types that it receives.

    Arguments:
        neighbourhoods: a list of the neighbourhoods
        room_types: a list of the room types
    """

    sns.set()

    x = np.arange(len(neighbourhoods))
    width = 0.20
    normalized_room_types = normalize_str_list(room_types)
    relative_distances = _get_relative_distances(width, normalized_room_types.keys())

    fig, axs = plt.subplots(1, 2)
    ax0 = axs[0].twinx()
    ax1 = axs[1].twinx()

    arr = ['#449c0b', '#84206b', '#e55c30', '#f6d746']
    i = 0
    for normalized_room_type in normalized_room_types.keys():
        occupancies = globals()[f'_{normalized_room_type}_occupancy']
        prices = globals()[f'_{normalized_room_type}_price']
        ratings = globals()[f'_{normalized_room_type}_rating']

        axs[0].bar(x + relative_distances[normalized_room_type], occupancies, width, label=normalized_room_types[normalized_room_type], color = arr[i])
        ax0.scatter(x + relative_distances[normalized_room_type], prices, color = '#140b34', marker = 'd', linewidths = 1.5)

        axs[1].bar(x + relative_distances[normalized_room_type], occupancies, width, label=normalized_room_types[normalized_room_type], color = arr[i])
        ax1.scatter(x + relative_distances[normalized_room_type], ratings, color = '#140b34', marker = 'd', linewidths = 1.5)

        i += 1

    axs[0].set_title('Occupancy', fontsize = 14)
    axs[0].set_xticks(x, neighbourhoods, rotation = 90, fontsize = 10)
    axs[0].legend(loc='upper left', fontsize = 10)

    axs[1].set_title('Rating', fontsize = 14)
    axs[1].set_xticks(x, neighbourhoods, rotation = 90, fontsize = 10)
    axs[1].legend(loc='upper right', fontsize = 10)

    fig.tight_layout()

    plt.show()

def _get_relative_distances(width: float, bars: List[str]):
    """
    Calculates the distance at which each bar on a bar plot has to be relative
    to the x axis tick given the bars width.

    Arguments:
        width: a float representing the width of each bar
        bars: a list representing the bars for a given x tick
    
    Returns:
        A dictionary containing the distance to the x axis tick for each
    bar
    """

    start = -0.5 * len(bars)

    positions = {}

    for idx, current_bar in enumerate(bars):
        positions[current_bar] = (start + idx) * width

    return positions

main()