import requests
import json
import pandas as pd
from usersecrets import usersecrets

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
githubResult = requests.post(githubUrl, json={'query': githubQuery}, headers={'Authorization': bearerToken})
print(githubResult.status_code)
print(githubResult.text)
print()