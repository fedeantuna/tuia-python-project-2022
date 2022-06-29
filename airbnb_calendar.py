import csv, gzip

_file_path = './calendar.csv.gz'

def get_calendar_data() -> dict:
    data = {}

    with gzip.open(_file_path, 'rt', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')

        header = next(reader)
        listing_id_index = header.index('listing_id')
        available_index = header.index('available')

        for row in reader:        
            listing_id = row[listing_id_index]
            available = row[available_index]

            if listing_id not in data.keys():
                data[listing_id] = 0
            
            if available == 'f':
                data[listing_id] += 1
    
    return data