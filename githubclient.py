import requests
import json
import pandas as pd
import calendarparser
from usersecrets import usersecrets
from unicornhatmini import UnicornHATMini

unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.1)
unicornhatmini.set_rotation(0)
u_width, u_height = unicornhatmini.get_shape()

# githubQuery = """query { 
#   user(login: "markmcgookin"){
#     contributionsCollection {
#       contributionCalendar {
#         totalContributions
#         weeks {
#           contributionDays {
#             contributionCount
#             date
#           }
#         }
#       }
#     }
#   }
# }
# """

# githubUrl = "https://api.github.com/graphql"
# bearerToken = "Bearer " + usersecrets["githubtoken"]
# githubResult = requests.post(githubUrl, json={'query': githubQuery}, headers={'Authorization': bearerToken})
# print(githubResult.status_code)
# print(githubResult.text)
# print()



# Using the example file as data source
with open('example-contributions.json', 'r') as exampleResponse:
    responseData = json.load(exampleResponse)
    chart = calendarparser.createChartData(responseData)
    y = 0
    
    for row in chart:
        print("row: " + row)
        x = 0
        print("x: " + str(x))
        for pixel in row:
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