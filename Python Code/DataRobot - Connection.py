import pandas as pd
import datarobot as dr
import numpy as np
#Make sure that you are running with the latest version
print(dr.__version__)

with open (r"G:\DataRobot\JNDataRobotAPIKey.txt", "r") as myfile:
    VPNToken=myfile.readlines()

with open (r"G:\Python Data\FactSet Alpha Testing Export\API - FeaturesToRemove.csv", "r") as myfile:
    features_to_remove=myfile.readlines()

features_to_remove = open(r"G:\Python Data\FactSet Alpha Testing Export\API - FeaturesToRemove.csv",'r').read().split('\n')
target_name = r'Outperform - 12 Month'

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
#target_name = 'Outperform 12-Month'
#project = dr.Project.create(data_raw_file, project_name=project_name)

#selecting a project from list
project = current_projects[0]
project.get_models()

vars(project)
project.get_status()

#project.get_modeling_features()

# See all the attributes associated with each feature
features = project.get_features()
pd.DataFrame([f.__dict__ for f in features])

feature_lists = project.get_featurelists()
feature_lists

raw_features = [lst for lst in feature_lists if lst.name == 'Raw Features'][0]
raw_features.features

features_to_remove

## Special handling for Time Based Projects 
no_forward_features_list = list(set(raw_features.features) - set(features_to_remove))

#This creates new featurelist. This will throw an error if the featurelist exists
new_features_no_forward_feature_list = project.create_featurelist('no_forward_features_list', no_forward_features_list)
no_forward_feature_list_id = new_features_no_forward_feature_list.id
no_forward_feature_list_id

#It is important to choose the correct dateTime column (exact match)
spec = dr.DatetimePartitioningSpecification('Period (YYYYMMDD)')
partitioning_preview = dr.DatetimePartitioning.generate(project.id, spec)
print(partitioning_preview.to_dataframe())
spec.number_of_backtests = 5
partitioning_preview = dr.DatetimePartitioning.generate(project.id, spec)
print(partitioning_preview.to_dataframe())

#This returns after starting to build models. This is asynchronous call and one has to make
# a separate call to finish the project
project.set_worker_count(-1)
project.set_target(target_name, partitioning_method=spec, featurelist_id=no_forward_feature_list_id)
project

#DON'T RUN THIS YET until you're ready it actually kicks off the project
#project.set_target(target=target_name,
#                   metric='LogLoss',
#                   mode=dr.AUTOPILOT_MODE.FULL_AUTO)

