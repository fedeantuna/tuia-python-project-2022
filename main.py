from asyncore import read
import csv
from functions import average

path = './' # File's path
data = {} # Main variable
firstIteration = True #First iteration check variable
c_data = {}
with open(path + 'calendar.csv', encoding='utf8') as Calendar:
    reader = csv.reader(Calendar, delimiter=',')
    for row in reader:
        if firstIteration:
            cListingIdIndex = row.index('listing_id')
            cAvailableIndex = row.index('available')
            firstIteration = False
            continue
        
        c_listing_id = row[cListingIdIndex]
        c_available = row[cAvailableIndex]

        if c_listing_id not in c_data.keys():
            c_data[c_listing_id] = 0
        
        if c_available == 'f':
            c_data[c_listing_id] += 1

firstIteration = True

with open(path + 'listings.csv', encoding='utf8') as File:
    reader = csv.reader(File, delimiter=',') 
    for row in reader:
        if firstIteration:
            listingIdIndex = row.index('id')
            priceIndex = row.index('price') # Get the price index
            ratingIndex = row.index('review_scores_rating') # Get the rating index
            neighIndex = row.index('neighbourhood') # Get the nighbourhood index
            roomTypeIndex = row.index('room_type') # Get the room type index
            firstIteration = False  # Not first iteration anymore
            continue # Skip to the next iteration
        
        price = float(row[priceIndex][1:].replace(',','')) # Save the price value for this listing
        if row[ratingIndex] != '':
            rating = float(row[ratingIndex]) # Save the rating value for this listing
        else:
            continue
        neighbourhood = row[neighIndex] # Save the 'neighbourhood' value for this listing
        roomType = row[roomTypeIndex] # Save the 'room type' value for this listing
        listingId = row[listingIdIndex]
        if listingId not in c_data.keys():
            continue
        occupied = c_data[listingId] / 365

        if neighbourhood in data.keys():
            if roomType in data[neighbourhood].keys():
                data[neighbourhood][roomType][0] += price # Add this listing price to total
                data[neighbourhood][roomType][1] += 1 #Add 1 to price counter
                data[neighbourhood][roomType][2] += rating # Add this listing rating to total
                data[neighbourhood][roomType][3] += occupied
            else:
                data[neighbourhood][roomType] = [ price, 1 , rating, occupied ] # Create a data list for new room type
        else:
            data[neighbourhood] = {roomType : [ price, 1 , rating, occupied ]} # Create a data list for new neighbourhood


for neigh in data:
    for roomT in data[neigh]:
        priceAv = average(data[neigh][roomT][0] , data[neigh][roomT][1]) # Average for prices
        ratingAv = average(data[neigh][roomT][2] , data[neigh][roomT][1]) # Average for ratings
        occupiedAv = average(data[neigh][roomT][3] * 100, data[neigh][roomT][1])
        data[neigh][roomT] = [ priceAv , ratingAv, occupiedAv ]


print(data)
