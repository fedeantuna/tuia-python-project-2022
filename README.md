# Set Up

With Python 3.x installed, these are the steps to follow to set up the project.

## Virtual Environment

In order to avoid issues with the dependencies, we set up the virtual environment. To do that run the following command from your terminal while on the root of the project:

`python -m venv venv`

Alternatively, if you have multiple versions of python installed is probably that `python` points to something like Python 2.7 and `python3` points to Python 3.x. In that case run:

`python3 -m venv venv`

Once the virtual environment is set up, activate it by running:

`source venv/bin/activate` (on Unix-like systems)

`.\venv\bin\Activate.ps1` (on Windows)

If successful, you should see a `(venv)` at the beginning of the prompt on your terminal.

After that, upgrade the `pip` version on that virtual environment by running:

`pip install --upgrade pip`

## Install dependencies

The dependencies needed for this project are listed in `requirements.txt`, to install them make sure that you are on the virtual environment and simply run:

`pip install -r requirements.txt`

## Run

While in the virtual environment, run `python main.py` or `python3 main.py` depending on your system.

# Data structure to read (JSON):
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

# Data structure procesed (JSON):
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