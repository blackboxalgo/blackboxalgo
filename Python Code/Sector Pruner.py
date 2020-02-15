import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

datamatrix = pd.read_csv(r'G:\Python Data\FactSet Alpha Testing Export\datarobotextract.txt')
datamatrix.columns
#datamatrix

datamatrix = datamatrix[datamatrix['MktVal Co'] > 1000]
datamatrix

#Energy
energy_2100 = datamatrix[datamatrix['Sector'] == 2100]
energy_3100 = datamatrix[datamatrix['Sector'] == 3100]
final_energy = energy_2100.append(energy_3100)

#Materials
materials_1000 = datamatrix[datamatrix['Sector'] == 1000]
materials_2200 = datamatrix[datamatrix['Sector'] == 2200]
final_materials = materials_1000.append(materials_2200)

#Industrials
industrials_1200 = datamatrix[datamatrix['Sector'] == 1200]
industrials_3200 = datamatrix[datamatrix['Sector'] == 3200]
industrials_4600 = datamatrix[datamatrix['Sector'] == 4600]
final_industrials = industrials_1200.append([industrials_3200,industrials_4600])

#Discretionary
discretionary_1400 = datamatrix[datamatrix['Sector'] == 1400]
discretionary_3250 = datamatrix[datamatrix['Sector'] == 3250]
discretionary_3400 = datamatrix[datamatrix['Sector'] == 3400]
discretionary_3500 = datamatrix[datamatrix['Sector'] == 3500]
final_discretionary = discretionary_1400.append([discretionary_3250,discretionary_3400,discretionary_3500])

#Staples
final_staples = datamatrix[datamatrix['Sector'] == 2400]

#Health Care
health_2300 = datamatrix[datamatrix['Sector'] == 2300]
health_3350 = datamatrix[datamatrix['Sector'] == 3350]
final_health = health_2300.append(health_3350)

#Financials
final_financials = datamatrix[datamatrix['Sector'] == 4800]

#Technology
technology_1300 = datamatrix[datamatrix['Sector'] == 1300]
technology_3300 = datamatrix[datamatrix['Sector'] == 3300]
final_technology = technology_1300.append(technology_3300)

#Communications
final_communications = datamatrix[datamatrix['Sector'] == 4900]

#Utilities
final_utilities = datamatrix[datamatrix['Sector'] == 4700]

#Now Export All The Files
final_energy.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 10.csv',index=False)
final_materials.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 15.csv',index=False)
final_industrials.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 20.csv',index=False)
final_discretionary.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 25.csv',index=False)
final_staples.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 30.csv',index=False)
final_health.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 35.csv',index=False)
final_financials.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 40.csv',index=False)
final_technology.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 45.csv',index=False)
final_communications.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 50.csv',index=False)
final_utilities.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 55.csv',index=False)