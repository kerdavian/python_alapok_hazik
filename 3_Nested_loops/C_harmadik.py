cars = [
    {"price": 1549,
     "passengerQty": 4,
     "currency": "EUR",
     "type": "Kia",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 1954,
     "passengerQty": 5,
     "currency": "EUR",
     "type": "Suzuki",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 5,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Andras",
         "Timea",
         "Martin",
         "Miklos"
     ]
     },
    {"price": 2544,
     "passengerQty": 2,
     "currency": "USD",
     "type": "Opel",
     "transmission": "manual",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
    {"price": 9542,
     "passengerQty": 4,
     "currency": "USD",
     "type": "Ford",
     "transmission": "automatic",
     "passengers": [
         "Gabor",
         "Timea",
         "Miklos"
     ]
     },
]

for lista in cars:
  for i in lista:
    dollar = lista["price"] 
    if lista["currency"] == "EUR":
      dollar = round(float(lista["price"]) * 1.15721, 1 )

    print('{} - {} USD'.format(lista["type"], dollar))
    break