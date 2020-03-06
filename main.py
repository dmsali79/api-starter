import requests


URL = "http://api.open-notify.org/astros.json"
High = "http://api.open-notify.org/iss-now.json"

resh = requests.get(High)
res = requests.get(URL) # get the data


resh = resh.json()
res = res.json() # convert data to Python format

data = {
  "message": "success",
  "number": 3,
  "timestamp":1583509552,  
  "people": [
    {
      "name": "Andrew Morgan",
      "craft": "ISS",
      "longitude": "148.7317",
      "latitude": "45.9258"     
    },
    {
      "name": "Oleg Skripochka",
      "craft": "ISS",
      "longitude": "148.7317",
      "latitude": "45.9258" 
    },
    {
      "name": "Jessica Meir",
      "craft": "ISS",
      "longitude": "148.7317",
      "latitude": "45.9258" 
    },
  ]
}












