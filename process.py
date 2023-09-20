import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

OverallKeys = {
    'Rank': 0,
    'Car': 1,
    'Overall': 2,
    'Dynamic': 3,
    'Static': 4,
    'Cost': 5,
    'Design': 6,
    'Sales': 7,
    'Accel': 8,
    'Maneuv': 9,
    'Sled': 10,
    'Hill': 10,
    'Sus': 11,
    'Rock': 11,
    'Endurance':12,
    'Adjustments':13
}

PointTotals = {
    'Overall': 1000,
    'Dynamic': 300,
    'Static': 300,
    'Cost': 100,
    'Design': 150,
    'Sales': 50,
    'Acceleration': 75,
    'Maneuverability': 75,
    'Sled Pull': 75,
    'Hill Climb': 75,
    'Suspension': 75,
    'Rock Crawl': 75,
    'Endurance': 400
}


Oregon2023OverallData = np.loadtxt('2023OregonResults/2023 Oregon Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Oshkosh2023OverallData = np.loadtxt('2023OshkoshResults/2023 Oshkosh Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Tennessee2022OverallData = np.loadtxt('2022TennesseeResults/2022 Tennessee Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Rochester2022OverallData = np.loadtxt('2022RochesterResults/2022 Rochester Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Arizona2022OverallData = np.loadtxt('2022ArizonaResults/2022 Arizona Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Tennessee2019OverallData = np.loadtxt('2019TennesseeResults/2019 Tennessee Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Rochester2019OverallData = np.loadtxt('2019RochesterResults/2019 Rochester Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
California2019OverallData = np.loadtxt('2019CaliforniaResults/2019 California Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')

OverallData = [Oregon2023OverallData, Oshkosh2023OverallData, Tennessee2022OverallData, Rochester2022OverallData, Arizona2022OverallData, Tennessee2019OverallData, Rochester2019OverallData, California2019OverallData]
SuspensionData = [Oshkosh2023OverallData, Tennessee2022OverallData, Rochester2022OverallData, Arizona2022OverallData, Tennessee2019OverallData, Rochester2019OverallData, California2019OverallData]
HillClimbData = [Oregon2023OverallData, Rochester2019OverallData, California2019OverallData]
CalPolyData = [Oregon2023OverallData, Oshkosh2023OverallData, Rochester2022OverallData, Rochester2019OverallData, California2019OverallData]


RankOregon2023 = Oregon2023OverallData[:,OverallKeys['Rank']]
OverallOregon2023 = Oregon2023OverallData[:,OverallKeys['Accel']]

avgAccel = 0
avgPAccel = 0


for i in range(3):
    for j in range(len(OverallData)):
    
        accelScore = OverallData[j][i,OverallKeys['Accel']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgAccel += accelScore
        avgPAccel += accelScore / PointTotals['Acceleration']


avgAccel = avgAccel / 24
avgPAccel = (avgPAccel / 24) * 100



avgEndurance = 0
avgPEndurance = 0


for i in range(3):
    for j in range(len(OverallData)):
    
        enduranceScore = OverallData[j][i,OverallKeys['Endurance']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgEndurance += enduranceScore
        avgPEndurance += enduranceScore / PointTotals['Endurance']


avgEndurance = avgEndurance / 24
avgPEndurance = (avgPEndurance / 24) * 100

avgDesign = 0
avgPDesign = 0

for i in range(3):
    for j in range(len(OverallData)):
    
        designScore = OverallData[j][i,OverallKeys['Design']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgDesign += designScore
        avgPDesign += designScore / PointTotals['Design']


avgDesign = avgDesign / 24
avgPDesign = (avgPDesign / 24) * 100

avgManeuv = 0
avgPManeuv = 0

for i in range(3):
    for j in range(len(OverallData)):
    
        maneuvScore = OverallData[j][i,OverallKeys['Maneuv']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgManeuv += maneuvScore
        avgPManeuv += maneuvScore / PointTotals['Maneuverability']


avgManeuv = avgManeuv / 24
avgPManeuv = (avgPManeuv / 24) * 100

avgCost = 0
avgPCost = 0

for i in range(3):
    for j in range(len(OverallData)):
    
        costScore = OverallData[j][i,OverallKeys['Cost']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgCost += costScore
        avgPCost += costScore / PointTotals['Cost']


avgCost = avgCost / 24
avgPCost = (avgPCost / 24) * 100

avgSales = 0
avgPSales = 0

for i in range(3):
    for j in range(len(OverallData)):
    
        salesScore = OverallData[j][i,OverallKeys['Sales']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgSales += salesScore
        avgPSales += salesScore / PointTotals['Sales']


avgSales = avgSales / 24
avgPSales = (avgPSales / 24) * 100

avgSus = 0
avgPSus = 0

for i in range(3):
    for j in range(len(SuspensionData)):
    
        susScore = OverallData[j][i,OverallKeys['Sus']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgSus += susScore
        avgPSus += susScore / PointTotals['Suspension']


avgSus = avgSus / (3 * len(SuspensionData))
avgPSus = (avgPSus / (3 * len(SuspensionData))) * 100

avgHill = 0
avgPHill = 0

for i in range(3):
    for j in range(len(HillClimbData)):
    
        hillScore = OverallData[j][i,OverallKeys['Hill']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgHill += hillScore
        avgPHill += hillScore / PointTotals['Hill Climb']


avgHill = avgHill / (3 * len(HillClimbData))
avgPHill = (avgPHill / (3 * len(HillClimbData))) * 100

avgOverall = 0
avgPOverall = 0

for i in range(3):
    for j in range(len(OverallData)):
    
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avgOverall += overallScore
        avgPOverall += overallScore / PointTotals['Overall']


avgOverall = avgOverall / (3 * len(OverallData))
avgPOverall = (avgPOverall / (3 * len(OverallData))) * 100


fig1, ax1 = plt.subplots(figsize=(7.5,3.5))
ax1.plot(RankOregon2023,OverallOregon2023,label='Overall Score')
ax1.set_xlabel('fun')
ax1.set_title('new title')
fig2, ax2 = plt.subplots(figsize=(7.5,3.5))
ax2.plot(RankOregon2023,OverallOregon2023,label='Overall Score')



print("Acceleration Information")
print("Average Acceleration Score of Top 3: " + str(avgAccel))
print("Average percentage of score from Accel for top 3: " + str(avgPAccel) + "%")
print("")

print("Endurance Information")
print("Average Endurance Score of Top 3: " + str(avgEndurance))
print("Average percentage of score from Endurance for top 3: " + str(avgPEndurance) + "%")
print("")

print("Design Information")
print("Average Design Score of Top 3: " + str(avgDesign))
print("Average percentage of score from Design for top 3: " + str(avgPDesign) + "%")
print("")

print("Maneuv Information")
print("Average Maneuverability Score of Top 3: " + str(avgManeuv))
print("Average percentage of score from Maneuverability for top 3: " + str(avgPManeuv) + "%")
print("")

print("Cost Information")
print("Average Cost Score of Top 3: " + str(avgCost))
print("Average percentage of score from Cost for top 3: " + str(avgPCost) + "%")
print("")

print("Sales Information")
print("Average Sales Score of Top 3: " + str(avgSales))
print("Average percentage of score from Sales for top 3: " + str(avgPSales) + "%")
print("")

print("Suspension Information")
print("Average Suspension Score of Top 3: " + str(avgSus))
print("Average percentage of score from Suspension for top 3: " + str(avgPSus) + "%")
print("")

print("Hill Climb Information")
print("Average Hill Climb Score of Top 3: " + str(avgHill))
print("Average percentage of score from Hill Climb for top 3: " + str(avgPHill) + "%")
print("")

print("Overall Information")
print("Average Overall Score of Top 3: " + str(avgOverall))
print("Average percentage of score from Overall for top 3: " + str(avgPOverall) + "%")
print("")


plt.legend()
plt.show()