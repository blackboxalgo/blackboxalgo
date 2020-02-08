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
data_raw_file = pd.read_csv(r'G:\Python Data\FactSet Alpha Testing Export\Data Export - 3 Yield All.csv')
project_name = '1832 Retirement Yield Over 3 All'

all_columns = pd.DataFrame(data_raw_file.columns)
all_columns.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\All Columns.csv',index=False)

#Instantiate the client 
dr.Client(token= API_TOKEN, endpoint=END_POINT)

#See theat you can navigate the current projects
current_projects  = dr.Project.list()
current_projects

#start a new project
target_name = 'Outperform 12-Month'
project = dr.Project.create(data_raw_file, project_name=project_name)
project.set_target(target=target_name,
                   metric='LogLoss',
                   mode=dr.AUTOPILOT_MODE.FULL_AUTO)

project.get_status()
project.get_modeling_features()

used_features = project.get_features()
used_features