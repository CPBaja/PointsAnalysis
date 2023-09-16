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


Oregon2023OverallData = np.loadtxt('2023OregonResults/2023 Oregon Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Oshkosh2023OverallData = np.loadtxt('2023OshkoshResults/2023 Oshkosh Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Tennessee2022OverallData = np.loadtxt('2022TennesseeResults/2022 Tennessee Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Rochester2022OverallData = np.loadtxt('2022RochesterResults/2022 Rochester Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Arizona2022OverallData = np.loadtxt('2022ArizonaResults/2022 Arizona Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Tennessee2019OverallData = np.loadtxt('2019TennesseeResults/2019 Tennessee Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
Rochester2019OverallData = np.loadtxt('2019RochesterResults/2019 Rochester Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')
California2019OverallData = np.loadtxt('2019CaliforniaResults/2019 California Results - Overall.csv', delimiter=',', skiprows=1, usecols=[0,1,4,5,6,7,8,9,10,11,12,13,14,15],encoding='utf-8')

OverallData = [Oregon2023OverallData, Oshkosh2023OverallData, Tennessee2022OverallData, Rochester2022OverallData, Arizona2022OverallData, Tennessee2019OverallData, Rochester2019OverallData, California2019OverallData]


RankOregon2023 = Oregon2023OverallData[:,OverallKeys['Rank']]
OverallOregon2023 = Oregon2023OverallData[:,OverallKeys['Accel']]

avg = 0
avgP = 0


for i in range(3):
    for j in range(len(OverallData)):
    
        accelScore = OverallData[j][i,OverallKeys['Accel']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avg += accelScore
        avgP += accelScore / overallScore


avg = avg / 24
avgP = (avgP / 24) * 100

print(avg)
print(avgP)

avg = 0
avgP = 0


for i in range(3):
    for j in range(len(OverallData)):
    
        accelScore = OverallData[j][i,OverallKeys['Design']]
        overallScore = OverallData[j][i,OverallKeys['Overall']]
        avg += accelScore
        avgP += accelScore / overallScore


avg = avg / 24
avgP = (avgP / 24) * 100

print(avg)
print(avgP)
fig, ax = plt.subplots(figsize=(7.5,3.5))
ax.plot(RankOregon2023,OverallOregon2023,label='Overall Score')
plt.legend()
plt.show()


