from random import random

def writeLongitude(latValues):
    with open("Longitude.txt", "w") as fileWriter:

        for latitude in latValues:    
            longitude = 0
            if latitude < -46.729225:
                longitude = (random() * (-23.670657 - (-23.483796))) - 23.483796

            elif latitude < -46.675796:
                longitude = (random() * (-23.722671 - (-23.476770))) - 23.476770

            elif latitude < -46.578981:
                longitude = (random() * (-23.693391 - (-23.476770))) - 23.476770

            elif latitude < -46.396400:
                longitude = (random() * (-23.601690 - (-23.504824))) - 23.504824

            fileWriter.write(str(longitude) + "\n")

def writeLatitude():
    with open("Latitude.txt", "w") as fileWriter:
        latValues = []
        for i in range(30):
            latitude = (random() * (-46.794940 - (-46.396400))) - 46.396400
            latValues.append(latitude)
            fileWriter.write(str(latitude) + "\n")

        writeLongitude(latValues)


def readLatitude():
    arr = []
    with open("Latitude.txt", "r") as fileReader:
        for line in fileReader:
            arr.append(float(line))
    return arr

def readLongitude():
    arr = []
    with open("Longitude.txt", "r") as fileReader:
        for line in fileReader:
            arr.append(float(line))
    return arr

def getLatitudeArray():
    writeLatitude()
    latitudeArr = readLatitude()
    return latitudeArr

def getLongitudeArray():
    longiguteArr = readLongitude()
    return longiguteArr

writeLatitude()