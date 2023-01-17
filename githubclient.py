import requests
import json
import pandas as pd
import calendarparser
from datetime import datetime
import time
from usersecrets import usersecrets
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.05)
unicornhatmini.set_rotation(0)
u_width, u_height = unicornhatmini.get_shape()
POLL_TIME = 300 # 60 * 5 - 5 mins

def resetScreen():
  for y in range(7):
    for x in range(17):
      unicornhatmini.set_pixel(x, y, 255, 0, 0)
      unicornhatmini.show()
      
    time.sleep(0.2)
  time.sleep(2)

def getColours():
  if(usersecrets["defaultColours"] == "true"):
    colours = {
        "0": {
            "r": 0,
            "g": 0,
            "b": 0,
        },
        "1-2": {
            "r": 0,
            "g": 32,
            "b": 0,
        },
        "3-5": {
            "r": 0,
            "g": 64,
            "b": 0,
        },
        "6-10": {
            "r": 0,
            "g": 128,
            "b": 0,
        },
        "11-15": {
            "r": 0,
            "g": 255,
            "b": 0,
        },
        "more": {
            "r": 0,
            "g": 255,
            "b": 0,
        }
    }
    return colours
  else:
    colours = usersecrets["altColours"]
    return colours

print("Dimensions: ")
print("Width: " + str(u_width))
print("Height: " + str(u_height))
quote = "\""
githubQuery = """query { 
  user(login: """ + quote + usersecrets["githubusername"] + quote + """ ){
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

githubUrl = "https://api.github.com/graphql"
bearerToken = "Bearer " + usersecrets["githubtoken"]

## Using the live github API
timecount = 0
try:
    while True:

        # Has it been 5 mins since our last github poll?
        if timecount >= POLL_TIME:        
          resetScreen()
          githubResult = requests.post(githubUrl, json={'query': githubQuery}, headers={'Authorization': bearerToken})
          print(githubResult.status_code)
          #print(githubResult.text)
          responseData = json.loads(githubResult.text)
          chart = calendarparser.createChartData(responseData, 17)
          y = 0
          
          for row in chart:
              #print("row: " + row)
              x = 0
              for pixel in row.split(","):
                  print("x: " + str(x))
                  print('Pixel ' + pixel)
                  if pixel == '0':
                      unicornhatmini.set_pixel(x, y, 0, 0, 0)
                  elif pixel == '1':
                      unicornhatmini.set_pixel(x, y, 0, 32, 0)
                  elif pixel == '2':
                      unicornhatmini.set_pixel(x, y, 0, 64, 0)
                  elif pixel == '3':
                      unicornhatmini.set_pixel(x, y, 0, 128, 0)
                  elif pixel == '4':
                      unicornhatmini.set_pixel(x, y, 0, 255, 0)
                  elif int(pixel) > 4:
                      unicornhatmini.set_pixel(x, y, 0, 255, 0)
                  x = x + 1
                  unicornhatmini.show()

              y = y + 1
              
              # Reset the clock
              timecount = 0
              
        # Monday = 0
        day_as_int = datetime.now().weekday()
        print("Day: " + str(day_as_int))
        
        # Sunday is the top row for us, so we start there. 
        # add one to bump the index along, if it's 8 - put it to zero
        # day now lines up with our rows
        day_index = day_as_int + 1
        if day_index == 8:
          day_index = 0
          
        print("Day: " + str(day_as_int))
        
        # Turn off today every other second
        if (timecount % 2) == 0:
          unicornhatmini.set_pixel(17, day_index, 0, 0, 0)

        # Wait for a second
        time.sleep(1)

except KeyboardInterrupt:
    pass


## Using the example file as data source
# try:
#     while True:
#         with open('example-contributions.json', 'r') as exampleResponse:
#             responseData = json.load(exampleResponse)
#             chart = calendarparser.createChartData(responseData, 17)
#             y = 0
            
#             for row in chart:
#                 #print("row: " + row)
#                 x = 0
#                 for pixel in row.split(","):
#                     print("x: " + str(x))
#                     print('Pixel ' + pixel)
#                     if pixel == '0':
#                         unicornhatmini.set_pixel(x, y, 0, 0, 0)
#                     elif pixel == '1':
#                         unicornhatmini.set_pixel(x, y, 0, 32, 0)
#                     elif pixel == '2':
#                         unicornhatmini.set_pixel(x, y, 0, 64, 0)
#                     elif pixel == '3':
#                         unicornhatmini.set_pixel(x, y, 0, 128, 0)
#                     elif pixel == '4':
#                         unicornhatmini.set_pixel(x, y, 0, 255, 0)
#                     elif int(pixel) > 4:
#                         unicornhatmini.set_pixel(x, y, 0, 255, 0)
#                     x = x + 1
#                 y = y + 1

#         unicornhatmini.show()

#         # Only check this once an hour... because who cares
#         time.sleep(60 * 60)

# except KeyboardInterrupt:
#     pass