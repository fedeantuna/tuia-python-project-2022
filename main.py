import csv, gzip
from functions import average

calendar_file = './calendar.csv.gz'
listings_file = './listings.csv.gz'

calendar_data = {}

with gzip.open(calendar_file, 'rt') as calendar:
    calendar_reader = csv.reader(calendar, delimiter=',')

    calendar_header = next(calendar_reader)
    calendar_listing_id_index = calendar_header.index('listing_id')
    calendar_available_index = calendar_header.index('available')

    for row in calendar_reader:        
        calendar_listing_id = row[calendar_listing_id_index]
        calendar_available = row[calendar_available_index]

        if calendar_listing_id not in calendar_data.keys():
            calendar_data[calendar_listing_id] = 0
        
        if calendar_available == 'f':
            calendar_data[calendar_listing_id] += 1

data = {}

with gzip.open(listings_file, 'rt') as listings:
    listings_reader = csv.reader(listings, delimiter=',')

    listings_header = next(listings_reader)
    listing_id_index = listings_header.index('id')
    listing_price_index = listings_header.index('price')
    listing_rating_index = listings_header.index('review_scores_rating')
    listing_neighbourhood_index = listings_header.index('neighbourhood')
    listing_room_type_index = listings_header.index('room_type')

    for row in listings_reader:
        listing_id = row[listing_id_index]
        if listing_id not in calendar_data.keys():
            continue

        rating = row[listing_rating_index]
        if rating == '':
            continue

        price = float(row[listing_price_index][1:].replace(',',''))
        rating = float(rating)
        neighbourhood = row[listing_neighbourhood_index]
        room_type = row[listing_room_type_index]
        occupancy_percentage = calendar_data[listing_id] / 365

        if neighbourhood not in data.keys():
            data[neighbourhood] = {
                room_type: {
                    'occupancy_percentage_sum': 0,
                    'price_sum': 0,
                    'rating_sum': 0,
                    'counter': 0
                }
            }
        
        if room_type not in data[neighbourhood].keys():
            data[neighbourhood][room_type] = {
                'occupancy_percentage_sum': 0,
                'price_sum': 0,
                'rating_sum': 0,
                'counter': 0
            }

        data[neighbourhood][room_type]['occupancy_percentage_sum'] += occupancy_percentage
        data[neighbourhood][room_type]['price_sum'] += price
        data[neighbourhood][room_type]['rating_sum'] += rating
        data[neighbourhood][room_type]['counter'] += 1


for neighborhood in data:
    for room_type in data[neighborhood]:
        average_price = average(data[neighborhood][room_type]['price_sum'] , data[neighborhood][room_type]['counter'])
        average_rating = average(data[neighborhood][room_type]['rating_sum'] , data[neighborhood][room_type]['counter'])
        average_occupancy = average(data[neighborhood][room_type]['occupancy_percentage_sum'] * 100, data[neighborhood][room_type]['counter'])
        data[neighborhood][room_type] = [ average_price , average_rating, average_occupancy ]


print(data)
