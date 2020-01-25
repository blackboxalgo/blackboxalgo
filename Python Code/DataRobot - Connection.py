import pandas as pd
import datarobot as dr
import numpy as np
#Make sure that you are running with the latest version
print(dr.__version__)

with open (r"G:\DataRobot\JNDataRobotAPIKey.txt", "r") as myfile:
    VPNToken=myfile.readlines()


#Fill in the API token.You can get the
API_TOKEN = VPNToken
END_POINT = 'https://datarobot.factset.com/api/v2'

#Define few global variables here
TRAINING_FILE_PATH = r'G:\Python Data\FactSet Alpha Testing Extracts\Data Export.txt'

#Instantiate the client 
dr.Client(token= API_TOKEN, endpoint=END_POINT)

#See theat you can navigate the current projects
current_projects  = dr.Project.list()
current_projects
