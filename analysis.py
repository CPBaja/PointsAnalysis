import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

width = 0.2

Oregon2023OverallData = pd.read_csv('2023OregonResults/2023 Oregon Results - Overall.csv')
Oregon2023AccelData = pd.read_csv('2023OregonResults/2023 Oregon Results - Acceleration.csv')
Oregon2023EnduranceData = pd.read_csv('2023OregonResults/2023 Oregon Results - Endurance.csv')
Oregon2023CostData = pd.read_csv('2023OregonResults/2023 Oregon Results - Cost.csv')
Oregon2023DesignData = pd.read_csv('2023OregonResults/2023 Oregon Results - Design.csv')
Oregon2023HillData = pd.read_csv('2023OregonResults/2023 Oregon Results - Hill Climb.csv')
Oregon2023RockData = pd.read_csv('2023OregonResults/2023 Oregon Results - Rock Crawl.csv')
Oregon2023SalesData = pd.read_csv('2023OregonResults/2023 Oregon Results - Sales.csv')
Oregon2023ManeuvData = pd.read_csv('2023OregonResults/2023 Oregon Results - Maneuverability.csv')

Oshkosh2023OverallData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Overall.csv')
Oshkosh2023AccelData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Acceleration.csv')
Oshkosh2023EnduranceData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Endurance.csv')
Oshkosh2023CostData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Cost.csv')
Oshkosh2023DesignData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Design.csv')
Oshkosh2023SledData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Sled Pull.csv')
Oshkosh2023SuspensionData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Suspension.csv')
Oshkosh2023SalesData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Sales.csv')
Oshkosh2023ManeuvData = pd.read_csv('2023OshkoshResults/2023 Oshkosh Results - Maneuverability.csv')


Tennessee2022OverallData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Overall.csv')
Tennessee2022AccelData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Acceleration.csv')
Tennessee2022EnduranceData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Endurance.csv')
Tennessee2022CostData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Cost.csv')
Tennessee2022DesignData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Design.csv')
Tennessee2022SledData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Sled Pull.csv')
Tennessee2022SuspensionData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Suspension.csv')
Tennessee2022SalesData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Sales.csv')
Tennessee2022ManeuvData = pd.read_csv('2022TennesseeResults/2022 Tennessee Results - Maneuverability.csv')


Rochester2022OverallData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Overall.csv')
Rochester2022AccelData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Acceleration.csv')
Rochester2022EnduranceData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Endurance.csv')
Rochester2022CostData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Cost.csv')
Rochester2022DesignData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Design.csv')
Rochester2022SledData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Sled Pull.csv')
Rochester2022SuspensionData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Suspension.csv')
Rochester2022SalesData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Sales.csv')
Rochester2022ManeuvData = pd.read_csv('2022RochesterResults/2022 Rochester Results - Maneuverability.csv')


Arizona2022OverallData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Overall.csv')
Arizona2022AccelData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Acceleration.csv')
Arizona2022EnduranceData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Endurance.csv')
Arizona2022CostData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Cost.csv')
Arizona2022DesignData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Design.csv')
Arizona2022SledData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Sled Pull.csv')
Arizona2022SuspensionData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Suspension.csv')
Arizona2022SalesData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Sales.csv')
Arizona2022ManeuvData = pd.read_csv('2022ArizonaResults/2022 Arizona Results - Maneuverability.csv')


Tennessee2019OverallData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Overall.csv')
Tennessee2019AccelData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Acceleration.csv')
Tennessee2019EnduranceData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Endurance.csv')
Tennessee2019CostData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Cost.csv')
Tennessee2019DesignData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Design.csv')
Tennessee2019SledData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Sled Pull.csv')
Tennessee2019SuspensionData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Suspension.csv')
Tennessee2019SalesData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Sales.csv')
Tennessee2019ManeuvData = pd.read_csv('2019TennesseeResults/2019 Tennessee Results - Maneuverability.csv')


Rochester2019OverallData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Overall.csv')
Rochester2019AccelData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Acceleration.csv')
Rochester2019EnduranceData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Endurance.csv')
Rochester2019CostData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Cost.csv')
Rochester2019DesignData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Design.csv')
Rochester2019HillData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Hill Climb.csv')
Rochester2019SuspensionData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Suspension.csv')
Rochester2019SalesData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Sales.csv')
Rochester2019ManeuvData = pd.read_csv('2019RochesterResults/2019 Rochester Results - Maneuverability.csv')


California2019OverallData = pd.read_csv('2019CaliforniaResults/2019 California Results - Overall.csv')
California2019AccelData = pd.read_csv('2019CaliforniaResults/2019 California Results - Acceleration.csv')
California2019EnduranceData = pd.read_csv('2019CaliforniaResults/2019 California Results - Endurance.csv')
California2019CostData = pd.read_csv('2019CaliforniaResults/2019 California Results - Cost.csv')
California2019DesignData = pd.read_csv('2019CaliforniaResults/2019 California Results - Design.csv')
California2019HillData = pd.read_csv('2019CaliforniaResults/2019 California Results - Hill Climb.csv')
California2019SuspensionData = pd.read_csv('2019CaliforniaResults/2019 California Results - Suspension.csv')
California2019SalesData = pd.read_csv('2019CaliforniaResults/2019 California Results - Sales.csv')
California2019ManeuvData = pd.read_csv('2019CaliforniaResults/2019 California Results - Maneuverability.csv')


dfOregon2023AccelvsEndurance = pd.merge(Oregon2023AccelData, Oregon2023EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfOregon2023AccelvsOverall = pd.merge(Oregon2023AccelData, Oregon2023OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfOregon2023EndurancevsOverall = pd.merge(Oregon2023EnduranceData, Oregon2023OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfOregon2023DesignvsOverall = pd.merge(Oregon2023DesignData, Oregon2023OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfOregon2023CostvsOverall = pd.merge(Oregon2023CostData, Oregon2023OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfOregon2023HillvsOverall = pd.merge(Oregon2023HillData, Oregon2023OverallData, on = 'School', suffixes = ['_hil', '_ove'], how = 'inner')
dfOregon2023SalesvsOverall = pd.merge(Oregon2023SalesData, Oregon2023OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfOregon2023ManeuvvsOverall = pd.merge(Oregon2023ManeuvData, Oregon2023OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfOshkosh2023AccelvsEndurance = pd.merge(Oshkosh2023AccelData, Oshkosh2023EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfOshkosh2023AccelvsOverall = pd.merge(Oshkosh2023AccelData, Oshkosh2023OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfOshkosh2023EndurancevsOverall = pd.merge(Oshkosh2023EnduranceData, Oshkosh2023OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfOshkosh2023DesignvsOverall = pd.merge(Oshkosh2023DesignData, Oshkosh2023OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfOshkosh2023CostvsOverall = pd.merge(Oshkosh2023CostData, Oshkosh2023OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfOshkosh2023SuspensionvsOverall = pd.merge(Oshkosh2023SuspensionData, Oshkosh2023OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfOshkosh2023SalesvsOverall = pd.merge(Oshkosh2023SalesData, Oshkosh2023OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfOshkosh2023ManeuvvsOverall = pd.merge(Oshkosh2023ManeuvData, Oshkosh2023OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfTennessee2022AccelvsEndurance = pd.merge(Tennessee2022AccelData, Tennessee2022EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfTennessee2022AccelvsOverall = pd.merge(Tennessee2022AccelData, Tennessee2022OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfTennessee2022EndurancevsOverall = pd.merge(Tennessee2022EnduranceData, Tennessee2022OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfTennessee2022DesignvsOverall = pd.merge(Tennessee2022DesignData, Tennessee2022OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfTennessee2022CostvsOverall = pd.merge(Tennessee2022CostData, Tennessee2022OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfTennessee2022SuspensionvsOverall = pd.merge(Tennessee2022SuspensionData, Tennessee2022OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfTennessee2022SalesvsOverall = pd.merge(Tennessee2022SalesData, Tennessee2022OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfTennessee2022ManeuvvsOverall = pd.merge(Tennessee2022ManeuvData, Tennessee2022OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfRochester2022AccelvsEndurance = pd.merge(Rochester2022AccelData, Rochester2022EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfRochester2022AccelvsOverall = pd.merge(Rochester2022AccelData, Rochester2022OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfRochester2022EndurancevsOverall = pd.merge(Rochester2022EnduranceData, Rochester2022OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfRochester2022DesignvsOverall = pd.merge(Rochester2022DesignData, Rochester2022OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfRochester2022CostvsOverall = pd.merge(Rochester2022CostData, Rochester2022OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfRochester2022SuspensionvsOverall = pd.merge(Rochester2022SuspensionData, Rochester2022OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfRochester2022SalesvsOverall = pd.merge(Rochester2022SalesData, Rochester2022OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfRochester2022ManeuvvsOverall = pd.merge(Rochester2022ManeuvData, Rochester2022OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfArizona2022AccelvsEndurance = pd.merge(Arizona2022AccelData, Arizona2022EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfArizona2022AccelvsOverall = pd.merge(Arizona2022AccelData, Arizona2022OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfArizona2022EndurancevsOverall = pd.merge(Arizona2022EnduranceData, Arizona2022OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfArizona2022DesignvsOverall = pd.merge(Arizona2022DesignData, Arizona2022OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfArizona2022CostvsOverall = pd.merge(Arizona2022CostData, Arizona2022OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfArizona2022SuspensionvsOverall = pd.merge(Arizona2022SuspensionData, Arizona2022OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfArizona2022SalesvsOverall = pd.merge(Arizona2022SalesData, Arizona2022OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfArizona2022ManeuvvsOverall = pd.merge(Arizona2022ManeuvData, Arizona2022OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfTennessee2019AccelvsEndurance = pd.merge(Tennessee2019AccelData, Tennessee2019EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfTennessee2019AccelvsOverall = pd.merge(Tennessee2019AccelData, Tennessee2019OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfTennessee2019EndurancevsOverall = pd.merge(Tennessee2019EnduranceData, Tennessee2019OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfTennessee2019DesignvsOverall = pd.merge(Tennessee2019DesignData, Tennessee2019OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfTennessee2019CostvsOverall = pd.merge(Tennessee2019CostData, Tennessee2019OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfTennessee2019SuspensionvsOverall = pd.merge(Tennessee2019SuspensionData, Tennessee2019OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfTennessee2019SalesvsOverall = pd.merge(Tennessee2019SalesData, Tennessee2019OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfTennessee2019ManeuvvsOverall = pd.merge(Tennessee2019ManeuvData, Tennessee2019OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfRochester2019AccelvsEndurance = pd.merge(Rochester2019AccelData, Rochester2019EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfRochester2019AccelvsOverall = pd.merge(Rochester2019AccelData, Rochester2019OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfRochester2019EndurancevsOverall = pd.merge(Rochester2019EnduranceData, Rochester2019OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfRochester2019DesignvsOverall = pd.merge(Rochester2019DesignData, Rochester2019OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfRochester2019CostvsOverall = pd.merge(Rochester2019CostData, Rochester2019OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfRochester2019HillvsOverall = pd.merge(Rochester2019HillData, Rochester2019OverallData, on = 'School', suffixes = ['_hil', '_ove'], how = 'inner')
dfRochester2019SuspensionvsOverall = pd.merge(Rochester2019SuspensionData, Rochester2019OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfRochester2019SalesvsOverall = pd.merge(Rochester2019SalesData, Rochester2019OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfRochester2019ManeuvvsOverall = pd.merge(Rochester2019ManeuvData, Rochester2019OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')

dfCalifornia2019AccelvsEndurance = pd.merge(California2019AccelData, California2019EnduranceData, on = 'School', suffixes = ['_acc', '_end'], how = 'inner')
dfCalifornia2019AccelvsOverall = pd.merge(California2019AccelData, California2019OverallData, on = 'School', suffixes = ['_acc', '_ove'], how = 'inner')
dfCalifornia2019EndurancevsOverall = pd.merge(California2019EnduranceData, California2019OverallData, on = 'School', suffixes = ['_end', '_ove'], how = 'inner')
dfCalifornia2019DesignvsOverall = pd.merge(California2019DesignData, California2019OverallData, on = 'School', suffixes = ['_des', '_ove'], how = 'inner')
dfCalifornia2019CostvsOverall = pd.merge(California2019CostData, California2019OverallData, on = 'School', suffixes = ['_cos', '_ove'], how = 'inner')
dfCalifornia2019HillvsOverall = pd.merge(California2019HillData, California2019OverallData, on = 'School', suffixes = ['_hil', '_ove'], how = 'inner')
dfCalifornia2019SuspensionvsOverall = pd.merge(California2019SuspensionData, California2019OverallData, on = 'School', suffixes = ['_sus', '_ove'], how = 'inner')
dfCalifornia2019SalesvsOverall = pd.merge(California2019SalesData, California2019OverallData, on = 'School', suffixes = ['_sal', '_ove'], how = 'inner')
dfCalifornia2019ManeuvvsOverall = pd.merge(California2019ManeuvData, California2019OverallData, on = 'School', suffixes = ['_man', '_ove'], how = 'inner')


AccelvsEndurance = [dfOregon2023AccelvsEndurance, dfOshkosh2023AccelvsEndurance, dfTennessee2022AccelvsEndurance, dfRochester2022AccelvsEndurance, dfArizona2022AccelvsEndurance, dfTennessee2019AccelvsEndurance, dfRochester2019AccelvsEndurance, dfCalifornia2019AccelvsEndurance]
AccelvsOverall = [dfOregon2023AccelvsOverall, dfOshkosh2023AccelvsOverall, dfTennessee2022AccelvsOverall, dfRochester2022AccelvsOverall, dfArizona2022AccelvsOverall, dfTennessee2019AccelvsOverall, dfRochester2019AccelvsOverall, dfCalifornia2019AccelvsOverall]
EndurancevsOverall = [dfOregon2023EndurancevsOverall, dfOshkosh2023EndurancevsOverall, dfTennessee2022EndurancevsOverall, dfRochester2022EndurancevsOverall, dfArizona2022EndurancevsOverall, dfTennessee2019EndurancevsOverall, dfRochester2019EndurancevsOverall, dfCalifornia2019EndurancevsOverall]
DesignvsOverall = [dfOregon2023DesignvsOverall, dfOshkosh2023DesignvsOverall, dfTennessee2022DesignvsOverall, dfRochester2022DesignvsOverall, dfArizona2022DesignvsOverall, dfTennessee2019DesignvsOverall, dfRochester2019DesignvsOverall, dfCalifornia2019DesignvsOverall]
CostvsOverall = [dfOregon2023CostvsOverall, dfOshkosh2023CostvsOverall, dfTennessee2022CostvsOverall, dfRochester2022CostvsOverall, dfArizona2022CostvsOverall, dfTennessee2019CostvsOverall, dfRochester2019CostvsOverall, dfCalifornia2019CostvsOverall]
HillvsOverall = [dfOregon2023HillvsOverall, dfRochester2019HillvsOverall, dfCalifornia2019HillvsOverall]
SuspensionvsOverall = [dfOshkosh2023SuspensionvsOverall, dfTennessee2022SuspensionvsOverall, dfRochester2022SuspensionvsOverall, dfArizona2022SuspensionvsOverall, dfTennessee2019SuspensionvsOverall, dfRochester2019SuspensionvsOverall, dfCalifornia2019SuspensionvsOverall]
SalesvsOverall = [dfOregon2023SalesvsOverall, dfOshkosh2023SalesvsOverall, dfTennessee2022SalesvsOverall, dfRochester2022SalesvsOverall, dfArizona2022SalesvsOverall, dfTennessee2019SalesvsOverall, dfRochester2019SalesvsOverall, dfCalifornia2019SalesvsOverall]
ManeuvvsOverall = [dfOregon2023ManeuvvsOverall, dfOshkosh2023ManeuvvsOverall, dfTennessee2022ManeuvvsOverall, dfRochester2022ManeuvvsOverall, dfArizona2022ManeuvvsOverall, dfTennessee2019ManeuvvsOverall, dfRochester2019ManeuvvsOverall, dfCalifornia2019ManeuvvsOverall]

AccelData = [Oregon2023AccelData, Oshkosh2023AccelData, Tennessee2022AccelData, Rochester2022AccelData, Arizona2022AccelData, Tennessee2019AccelData, Rochester2019AccelData, California2019AccelData]

correlations = {
	'Endurance': 0,
	'Acceleration': 0,
	'Maneuverability': 0,
	'Suspension': 0,
	'Hill Climb': 0,
	'Design': 0,
	'Cost': 0,
	'Sales': 0

}

correlationsOreogn = {
	'Endurance': 0,
	'Acceleration': 0,
	'Maneuverability': 0,
	'Suspension': 0,
	'Hill Climb': 0,
	'Design': 0,
	'Cost': 0,
	'Sales': 0

}

correlationsOshkosh = {
	'Endurance': 0,
	'Acceleration': 0,
	'Maneuverability': 0,
	'Suspension': 0,
	'Hill Climb': 0,
	'Design': 0,
	'Cost': 0,
	'Sales': 0

}

corr = 0
for i in range(len(EndurancevsOverall)):
	corr += EndurancevsOverall[i]['Rank_end'].corr(EndurancevsOverall[i]['Rank_ove'])
corr = corr / len(EndurancevsOverall)

correlations['Endurance'] = corr
correlationsOreogn['Endurance'] = dfOregon2023EndurancevsOverall['Rank_end'].corr(dfOregon2023EndurancevsOverall['Rank_ove'])
correlationsOshkosh['Endurance'] = dfOshkosh2023EndurancevsOverall['Rank_end'].corr(dfOshkosh2023EndurancevsOverall['Rank_ove'])

print("Correlation Endurance vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(AccelvsOverall)):
	corr += AccelvsOverall[i]['Rank_acc'].corr(AccelvsOverall[i]['Rank_ove'])
corr = corr / len(AccelvsOverall)

correlations['Acceleration'] = corr
correlationsOreogn['Acceleration'] = dfOregon2023AccelvsOverall['Rank_acc'].corr(dfOregon2023AccelvsOverall['Rank_ove'])
correlationsOshkosh['Acceleration'] = dfOshkosh2023AccelvsOverall['Rank_acc'].corr(dfOshkosh2023AccelvsOverall['Rank_ove'])

print("Correlation Accel vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(AccelvsEndurance)):
	corr += AccelvsEndurance[i]['Rank_acc'].corr(AccelvsEndurance[i]['Rank_end'])
corr = corr / len(AccelvsEndurance)


print("Correlation Accel vs Endurance")
print(corr)
print("")

corr = 0
for i in range(len(ManeuvvsOverall)):
	corr += ManeuvvsOverall[i]['Rank_man'].corr(ManeuvvsOverall[i]['Rank_ove'])
corr = corr / len(ManeuvvsOverall)

correlations['Maneuverability'] = corr
correlationsOreogn['Maneuverability'] = dfOregon2023ManeuvvsOverall['Rank_man'].corr(dfOregon2023ManeuvvsOverall['Rank_ove'])
correlationsOshkosh['Maneuverability'] = dfOshkosh2023ManeuvvsOverall['Rank_man'].corr(dfOshkosh2023ManeuvvsOverall['Rank_ove'])

print("Correlation Maneuv vs Endurance")
print(corr)
print("")

corr = 0
for i in range(len(SuspensionvsOverall)):
	corr += SuspensionvsOverall[i]['Rank_sus'].corr(SuspensionvsOverall[i]['Rank_ove'])
corr = corr / len(SuspensionvsOverall)

correlations['Suspension'] = corr
correlationsOshkosh['Suspension'] = dfOshkosh2023SuspensionvsOverall['Rank_sus'].corr(dfOshkosh2023SuspensionvsOverall['Rank_ove'])

print("Correlation Suspension vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(HillvsOverall)):
	corr += HillvsOverall[i]['Rank_hil'].corr(HillvsOverall[i]['Rank_ove'])
corr = corr / len(HillvsOverall)

correlations['Hill Climb'] = corr
correlationsOreogn['Hill Climb'] = dfOregon2023HillvsOverall['Rank_hil'].corr(dfOregon2023HillvsOverall['Rank_ove'])

print("Correlation Hill vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(DesignvsOverall)):
	corr += DesignvsOverall[i]['Rank_des'].corr(DesignvsOverall[i]['Rank_ove'])
corr = corr / len(DesignvsOverall)

correlations['Design'] = corr
correlationsOreogn['Design'] = dfOregon2023DesignvsOverall['Rank_des'].corr(dfOregon2023DesignvsOverall['Rank_ove'])
correlationsOshkosh['Design'] = dfOshkosh2023DesignvsOverall['Rank_des'].corr(dfOshkosh2023DesignvsOverall['Rank_ove'])

print("Correlation Design vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(CostvsOverall)):
	corr += CostvsOverall[i]['Rank_cos'].corr(CostvsOverall[i]['Rank_ove'])
corr = corr / len(CostvsOverall)

correlations['Cost'] = corr
correlationsOreogn['Cost'] = dfOregon2023CostvsOverall['Rank_cos'].corr(dfOregon2023CostvsOverall['Rank_ove'])
correlationsOshkosh['Cost'] = dfOshkosh2023CostvsOverall['Rank_cos'].corr(dfOshkosh2023CostvsOverall['Rank_ove'])

print("Correlation Cost vs Overall")
print(corr)
print("")

corr = 0
for i in range(len(SalesvsOverall)):
	corr += SalesvsOverall[i]['Rank_sal'].corr(SalesvsOverall[i]['Rank_ove'])
corr = corr / len(SalesvsOverall)

correlations['Sales'] = corr
correlationsOreogn['Sales'] = dfOregon2023SalesvsOverall['Rank_sal'].corr(dfOregon2023SalesvsOverall['Rank_ove'])
correlationsOshkosh['Sales'] = dfOshkosh2023SalesvsOverall['Rank_sal'].corr(dfOshkosh2023SalesvsOverall['Rank_ove'])

print("Correlation Sales vs Overall")
print(corr)
print("")

keys = list(correlations.keys())
values = list(correlations.values())
valuesOregon = list(correlationsOreogn.values())
valuesOshkosh = list(correlationsOshkosh.values())

fig, ax = plt.subplots(figsize=(12,6))

ax.set_title('Correlation Between Placement in Event and Overall Placement')
ax.set_xlabel('Event')
ax.set_ylabel('Correlation')

ind = np.arange(len(keys))

ave = ax.bar(ind, values, color='#38761D', width=width)
ore = ax.bar(ind+width, valuesOregon, color = 'red', width=width)
osh = ax.bar(ind+width*2, valuesOshkosh, color = 'blue', width=width)

ax.set_xticks(ind+width)
ax.set_xticklabels(tuple(keys))
ax.legend((ave[0],ore[0],osh[0]), ('Average','Oregon','Oshkosh'))

for i in range(len(keys)):
	ax.text(i-.095, values[i]+.005, round(values[i], 2), fontweight='bold', fontsize=6)
	ax.text(i+.095, valuesOregon[i]+.005, round(valuesOregon[i], 2), fontweight='bold', fontsize=6)
	ax.text(i+.295, valuesOshkosh[i]+.005, round(valuesOshkosh[i], 2), fontweight='bold', fontsize=6)

avg3 = 0
avg1 = 0
count = 0
minTime = 5
for data in AccelData:
	if data['Best Time'][0] < 4.5:
		avg1 += data['Best Time'][0]
		avg3 += data['Best Time'][0] + data['Best Time'][1] + data['Best Time'][2]
		count += 1
		if data['Best Time'][0] < minTime:
			minTime = data['Best Time'][0]
avg1 = round(avg1 / count, 3)
avg3 = round(avg3 / ( 3* count), 3)
minTime = round(minTime, 3)

print("Average accel time of top 1: " + str(avg1))
print("Average accel time of top 3: " + str(avg3))
print("Accel Record: " + str(minTime))
minTime -= 0.001

plt.show()

#print(dfOregon2023AccelvsEndurance['Rank_acc'].corr(dfOregon2023AccelvsEndurance['Rank_end']))
#print("")
#print(dfOregon2023AccelvsOverall['Rank_acc'].corr(dfOregon2023AccelvsOverall['Rank_ove']))
#print("")
#print(dfOregon2023EndurancevsOverall['Rank_end'].corr(dfOregon2023EndurancevsOverall['Rank_ove']))
#print("")
#print(dfOregon2023DesignvsOverall['Rank_des'].corr(dfOregon2023DesignvsOverall['Rank_ove']))
