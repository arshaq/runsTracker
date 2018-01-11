######################################################
#	Program to take my running records
######################################################

import csv
from datetime import date


def convertTimeInSeconds(time):
    timeUnitised = time.split(":")
    if(len(timeUnitised) == 3):
        return int(timeUnitised[0])*3600 + int(timeUnitised[1])*60 + int(timeUnitised[2])
    elif(len(timeUnitised) == 2):
        return int(timeUnitised[0])*60 + int(timeUnitised[1])
    elif(len(timeUnitised) == 1):
        return int(timeUnitised[0])

    return 0

def calculatePace(time, distance):
    paceInSeconds = time/distance*1000
    return str(int(paceInSeconds/60)) + "'" + str(round(paceInSeconds%60)) + "\""

print("Enter your run details")

if(input("Is it today? ").lower() == "y"):
    dateOfRun = date.today()
else:
    dateParts = input("Enter the date of the run (in dd-mm-yyyy format): ").split("-")
    dateParts = [int(i) for i in dateParts]
    dateOfRun = date(dateParts[2], dateParts[1], dateParts[0])

print (date.strftime(dateOfRun, "%d-%m-%Y"))

distance = input("Distance (in km): ")
time = input("Time (in hh:mm:ss): ")

distanceInMetres = float(distance) * 1000
timeInSeconds = convertTimeInSeconds(time)

print("Your average speed was %.2f kmph." % (distanceInMetres/timeInSeconds * 3.6))
print("Your average pace was " + calculatePace(timeInSeconds, distanceInMetres))
