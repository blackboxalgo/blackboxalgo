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

file_name = 'DR - Data Export - 10.csv'

#Define few global variables here
TRAINING_FILE_PATH = r'G:\Python Data\FactSet Alpha Testing Export'
data_raw_file = pd.read_csv(fr'G:\Python Data\FactSet Alpha Testing Export\{file_name}')
project_name = f'API - {file_name}'

all_columns = pd.DataFrame(data_raw_file.columns)
all_columns.to_csv(r'G:\Python Data\FactSet Alpha Testing Export\API - All Columns.csv',index=False)

#Instantiate the client 
dr.Client(token= API_TOKEN, endpoint=END_POINT)

#See theat you can navigate the current projects
current_projects  = dr.Project.list()
current_projects

#start a new project
target_name = 'Outperform 12-Month'
project = dr.Project.create(data_raw_file, project_name=project_name)

vars(project)
project.get_status()

#project.get_modeling_features()

# See all the attributes associated with each feature
features = project.get_features()
pd.DataFrame([f.__dict__ for f in features])

feature_lists = project.get_featurelists()
feature_lists

informative_features = [lst for lst in feature_lists if lst.name == 'Informative Features'][0]
informative_features.features



#DON'T RUN THIS YET until you're ready it actually kicks off the project
#project.set_target(target=target_name,
                   metric='LogLoss',
                   mode=dr.AUTOPILOT_MODE.FULL_AUTO)

