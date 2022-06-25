import csv


#---------------- Average Price and Rating by Neighbourhood -----------------------

'''
Data structure:
variable = {"neighbourhood 1" : { "room type 1" : [price addition, price count];
                                  "room type 2" : [price addition, price count];
                                  "room type 3" : [price addition, price count] };
            "neighbourhood 2" : { "room type 1" : [price addition, price count];
                                  "room type 2" : [price addition, price count];
                                  "room type 3" : [price addition, price count] };
            .
            .
            .

            }
'''
path = './' # File's path
priceByNeiByRoom = {} # Main variable
firstIteration = True #First iteration check variable

with open(path + 'listings.csv', encoding="utf8") as File:
    reader = csv.reader(File, delimiter=',') 
    for row in reader:
        if firstIteration:
            priceIndex = row.index('price')
            neighIndex = row.index('neighbourhood')
            roomTypeIndex = row.index('room_type')
            firstIteration = False
#            print(row[priceIndex], '\'s index: ', priceIndex)
#            print(row[neighIndex], '\'s index: ', neighIndex)
#            print(row[roomTypeIndex], '\'s index: ', roomTypeIndex)
            continue
        
        price = float(row[priceIndex][1:].replace(',','')) 
        neighbourhood = row[neighIndex]
        roomType = row[roomTypeIndex]

        if neighbourhood in priceByNeiByRoom.keys():
            if roomType in priceByNeiByRoom[neighbourhood].keys():
                priceByNeiByRoom[neighbourhood][roomType][0] += price
                priceByNeiByRoom[neighbourhood][roomType][1] += 1
            else:
                priceByNeiByRoom[neighbourhood][roomType] = [ price, 1 ]
        else:
            priceByNeiByRoom[neighbourhood] = {roomType : [ price , 1 ]}      

for neigh in priceByNeiByRoom:
    for roomT in priceByNeiByRoom[neigh]:
        priceByNeiByRoom[neigh][roomT] = round(priceByNeiByRoom[neigh][roomT][0] / priceByNeiByRoom[neigh][roomT][1] , 2 )


print(priceByNeiByRoom)
