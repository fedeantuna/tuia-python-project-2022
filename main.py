import csv
from functions import average

#---------------- Average Price and Rating by Neighbourhood -----------------------

'''
Data structure to read:
variable = {"neighbourhood 1" : { "room type 1" : [price addition, price counter, rating addition, rating counter];
                                  "room type 2" : [price addition, price counter, rating addition, rating counter];
                                  "room type 3" : [price addition, price counter, rating addition, rating counter] };
            "neighbourhood 2" : { "room type 1" : [price addition, price counter, rating addition, rating counter];
                                  "room type 2" : [price addition, price counter, rating addition, rating counter];
                                  "room type 3" : [price addition, price counter, rating addition, rating counter] };
            .
            .
            .

            }

Data structure procesed:
variable = {"neighbourhood 1" : { "room type 1" : [Price average, Rating average];
                                  "room type 2" : [Price average, Rating average];
                                  "room type 3" : [Price average, Rating average] };
            "neighbourhood 2" : { "room type 1" : [Price average, Rating average];
                                  "room type 2" : [Price average, Rating average];
                                  "room type 3" : [Price average, Rating average] };
            .
            .
            .

            }
'''

path = '../' # File's path
data = {} # Main variable
firstIteration = True #First iteration check variable

with open(path + 'listings.csv', encoding="utf8") as File:
    reader = csv.reader(File, delimiter=',') 
    for row in reader:
        if firstIteration:
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
            rating = 0
        neighbourhood = row[neighIndex] # Save the 'neighbourhood' value for this listing
        roomType = row[roomTypeIndex] # Save the 'room type' value for this listing

        if neighbourhood in data.keys():
            if roomType in data[neighbourhood].keys():
                data[neighbourhood][roomType][0] += price # Add this listing price to total
                data[neighbourhood][roomType][1] += 1 #Add 1 to price counter
                data[neighbourhood][roomType][2] += rating # Add this rating price to total
                if rating != 0:
                    data[neighbourhood][roomType][3] += 1 #Add 1 to rating counter if it's not zero
            else:
                if rating != 0:
                    data[neighbourhood][roomType] = [ price, 1 , rating , 1 ] # Create a data list for new room type
                else:
                    data[neighbourhood][roomType] = [ price, 1 , rating , 0 ]
        else:
            if rating != 0:
                data[neighbourhood] = {roomType : [ price, 1 , rating , 1 ]} # Create a data list for new neighbourhood
            else:
                data[neighbourhood] = {roomType : [ price, 1 , rating , 0 ]}        





for neigh in data:
    for roomT in data[neigh]:
        priceAv = average(data[neigh][roomT][0] , data[neigh][roomT][1]) # Average for prices
        if data[neigh][roomT][3] != 0:
            ratingAv = average(data[neigh][roomT][2] , data[neigh][roomT][3]) # Average for ratings
        else:
            ratingAv = ''
#           ratingAv = 0
        data[neigh][roomT] = [ priceAv , ratingAv ]


print(data)
