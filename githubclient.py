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

print("Dimensions: ")
print("Width: " + str(u_width))
print("Height: " + str(u_height))

githubQuery = """query { 
  user(login: "markmcgookin"){
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

#Using the live github API
# try:
#     while True:
        
#         githubResult = requests.post(githubUrl, json={'query': githubQuery}, headers={'Authorization': bearerToken})
#         print(githubResult.status_code)
#         print(githubResult.text)
#         chart = calendarparser.createChartData(githubResult.text, 17)
#         y = 0
        
#         for row in chart:
#             #print("row: " + row)
#             x = 0
#             for pixel in row.split(","):
#                 print("x: " + str(x))
#                 print('Pixel ' + pixel)
#                 if pixel == '0':
#                     unicornhatmini.set_pixel(x, y, 0, 0, 0)
#                 elif pixel == '1':
#                     unicornhatmini.set_pixel(x, y, 0, 32, 0)
#                 elif pixel == '2':
#                     unicornhatmini.set_pixel(x, y, 0, 64, 0)
#                 elif pixel == '3':
#                     unicornhatmini.set_pixel(x, y, 0, 128, 0)
#                 elif pixel == '4':
#                     unicornhatmini.set_pixel(x, y, 0, 255, 0)
#                 elif int(pixel) > 4:
#                     unicornhatmini.set_pixel(x, y, 0, 255, 0)
#                 x = x + 1
#             y = y + 1

#     unicornhatmini.show()

#     # Only check this once an hour... because who cares
#     time.sleep(60 * 60)

# except KeyboardInterrupt:
#     pass


## Using the example file as data source
try:
    while True:
        with open('example-contributions.json', 'r') as exampleResponse:
            responseData = json.load(exampleResponse)
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
                y = y + 1

        unicornhatmini.show()

        # Only check this once an hour... because who cares
        time.sleep(60 * 60)

except KeyboardInterrupt:
    pass