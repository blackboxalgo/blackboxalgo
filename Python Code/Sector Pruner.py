import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

datamatrix = pd.read_csv(r'G:\Python Data\FactSet Alpha Testing Extracts\dr_extract_dram.txt')

technology_1300 = datamatrix[datamatrix['Sector'] == 1300]
technology_3300 = datamatrix[datamatrix['Sector'] == 3300]

final_technology = technology_1300.append(technology_3300)
final_technology.to_csv(r'G:\Python Data\FactSet Alpha Testing Extracts\Data Export - Technology.csv',index=False)