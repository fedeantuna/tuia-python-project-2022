## Data structure to read (JSON):
```
{
    "neighbourhood 1": {
        "room type 1": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        },

        "room type 2": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        },

        "room type 3": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        } 
    },

    "neighbourhood 2": {
        "room type 1": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        },

        "room type 2": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        },

        "room type 3": {
            "availability addition": <number>,
            "price addition": <number>,
            "rating addition": <number>, 
            "counter": <number>
        } 
    },

    .
    .
    .

}
```

## Data structure procesed (JSON):
```
{
    "neighbourhood 1": {
        "room type 1": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        },
        "room type 2": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        },
        "room type 3": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        }
    }
    "neighbourhood 2": {
        "room type 1": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        },
        "room type 2": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        },
        "room type 3": {
            "Availability average": <number>,
            "Price average": <number>,
            "Rating average": <number>
        }
    }       
    .
    .
    .

}
```