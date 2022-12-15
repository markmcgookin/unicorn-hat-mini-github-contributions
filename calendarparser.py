import json

name = "calendarparser"

def createChartData(githubJson, numberOfWeeks = 52):

    sundays = list()
    mondays = list()
    tuesdays = list()
    wednesdays = list()
    thursdays = list()
    fridays = list()
    saturdays = list()

    weeks = githubJson["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    
    if(numberOfWeeks < 52):
        # flip this around so we start with the newest
        weeks.reverse()
        reducedWeeks = list()

        # loop through the weeks until the desired count is reached
        for i in range(numberOfWeeks):
            # print(weeks[i])
            # Add the newer weeks
            reducedWeeks.append(weeks[i])
        
        # Flip this result back round so it goes old > new
        reducedWeeks.reverse()
        weeks = reducedWeeks

    for week in weeks:
            numOfDays = len(week["contributionDays"]) - 1
            if(numOfDays >= 0):
                sundays.append(week["contributionDays"][0]["contributionCount"])
            else:
                sundays.append(0)
            if(numOfDays >= 1):
                mondays.append(week["contributionDays"][1]["contributionCount"])
            else:
                mondays.append(0)
            if(numOfDays >= 2):
                tuesdays.append(week["contributionDays"][2]["contributionCount"])
            else:
                tuesdays.append(0)
            if(numOfDays >= 3):
                wednesdays.append(week["contributionDays"][3]["contributionCount"])
            else:
                wednesdays.append(0)
            if(numOfDays >= 4):
                thursdays.append(week["contributionDays"][4]["contributionCount"])
            else:
                thursdays.append(0)
            if(numOfDays >= 5):
                fridays.append(week["contributionDays"][5]["contributionCount"])
            else:
                fridays.append(0)
            if(numOfDays >= 6):
                saturdays.append(week["contributionDays"][6]["contributionCount"])
            else:
                saturdays.append(0)

    sundaysString = ','.join(map(str, sundays))
    mondaysString = ','.join(map(str, mondays))
    tuesdayssString = ','.join(map(str, tuesdays))
    wednesdaysString = ','.join(map(str, wednesdays))
    thursdaysString = ','.join(map(str, thursdays))
    fridaysString = ','.join(map(str, fridays))
    saturdaysString = ','.join(map(str, saturdays))

    # print(sundaysString)
    # print(mondaysString)
    # print(tuesdayssString)
    # print(wednesdaysString)
    # print(thursdaysString)
    # print(fridaysString)
    # print(saturdaysString)

    chart = (sundaysString, mondaysString, tuesdayssString, wednesdaysString, thursdaysString, fridaysString, saturdaysString)

    return chart