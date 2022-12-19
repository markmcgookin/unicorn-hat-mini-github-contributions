import requests
import json
import pandas as pd
import calendarparser
import time
from usersecrets import usersecrets
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.05)
unicornhatmini.set_rotation(0)
u_width, u_height = unicornhatmini.get_shape()

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
try:
    while True:
        resetScreen()
        githubResult = requests.post(githubUrl, json={'query': githubQuery}, headers={'Authorization': bearerToken})
        print(githubResult.status_code)
        #print(githubResult.text)
        responseData = json.loads(githubResult.text)
        chart = calendarparser.createChartData(responseData, 17)
        y = 0
        
        colours = getColours()
        # for row in chart:
        #     x = 0
        #     for pixel in row.split(","):
        #         print("x: " + str(x))
        #         print('Pixel ' + pixel)
        #         if pixel == '0':
        #             unicornhatmini.set_pixel(x, y, 0, 0, 0)
        #         elif pixel == '1':
        #             unicornhatmini.set_pixel(x, y, 0, 32, 0)
        #         elif pixel == '2':
        #             unicornhatmini.set_pixel(x, y, 0, 64, 0)
        #         elif pixel == '3':
        #             unicornhatmini.set_pixel(x, y, 0, 128, 0)
        #         elif pixel == '4':
        #             unicornhatmini.set_pixel(x, y, 0, 255, 0)
        #         elif int(pixel) > 4:
        #             unicornhatmini.set_pixel(x, y, 0, 255, 0)
        #         x = x + 1
        #         unicornhatmini.show()

        #     y = y + 1

        for row in chart:
            x = 0
            for pixel in row.split(","):
                  if pixel == '0':
                    unicornhatmini.set_pixel(x, y, colours["0"]["r"], colours["0"]["g"], colours["0"]["b"])
                  elif pixel == '1' or pixel == '2':
                    unicornhatmini.set_pixel(x, y, colours["1-2"]["r"], colours["1-2"]["g"], colours["1-2"]["b"])
                  elif pixel == '3' or pixel == '4' or pixel == '5':
                    unicornhatmini.set_pixel(x, y, colours["3-5"]["r"], colours["3-5"]["g"], colours["3-5"]["b"])
                  elif pixel == '6' or pixel == '7' or pixel == '8' or pixel == '9' or pixel == '10':
                    unicornhatmini.set_pixel(x, y, colours["6-10"]["r"], colours["6-10"]["g"], colours["6-10"]["b"])
                  elif '11' or pixel == '12' or pixel == '13' or pixel == '14' or pixel == '15':
                    unicornhatmini.set_pixel(x, y, colours["11-15"]["r"], colours["11-15"]["g"], colours["11-15"]["b"])
                  else:
                    unicornhatmini.set_pixel(x, y, colours["more"]["r"], colours["more"]["g"], colours["more"]["b"])
                  
                  x = x + 1
                  unicornhatmini.show()
            
            y = y + 1

        # Only check this once every 5 mins
        time.sleep(60 * 5)

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