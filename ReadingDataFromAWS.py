import pandas as pd
import numpy as np
import onelake
import os
from onelake import get_session
from onelake import read_config_file

client_id = 
client_secret = 


# create a callable
class RefreshOauthToken:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
    
    def __call__(self):
        return my_platform_oauth_refresh_func(self.client_id, self.client_secret)

refresh_oauth_token = RefreshOauthToken(client_id, client_secret)


eid = input("Please Enter Your EID: ")
password = input("Please Enter Your Password: ")

assert onelake.__version_info__ >= (0, 8, 7, 'stable')

# initialize session using config file
session = get_session()

# to see what is being picked up in the config file
print('session file:', session.config)

# initialize session using a config dictionary
config_dict = {
    'env': 'QA',
    #Change platform to managed if its just an individual connecting
    'platform': 'application',
    'client id': client_id,  # a function/callable can be provided instead of string
    'client secret': client_secret,  # a function/callable can be provided instead of string
    'password': password,  # if omitted, will prompt for password
    'eid': eid,
    # 'oauth_refresh_function': refresh_oauth_token  # an OAuth refresh function can be used in lieu of client credentials
    # 'sso_refresh_function': refresh_sso_token  # an SSO refresh function can be used in lieu of password
}

session = get_session(config=config_dict)
#Need to pull the below ID from nebula QA (e.g. 232431)
NebulaID = str(input("Please navigate to Nebula to grab the necessary DataSetID and enter it here: "))
lake_dataset = session.get_dataset_from_nebula(NebulaID)

#This is used to do a file system operations on the S3 bucket
s3_fs = lake_dataset._get_s3_filesystem(write_access=True)
#This will list out all of the files in this specific folder
all_files = s3_fs.ls(lake_dataset.location())
#Another way to do the above
#s3_fs.ls('s3://cof-mosaictech-finance-cat3-qa-useast1/762qj/lake/investport/SUMT_InvPort_TradeMaster_Output_refined/src')
#Below prints out all of the instances IDs in that folder
for i in all_files:
    instance = i.split('=')
    print(instance[-1])
#Requesting instance ID from user
user_input = input("Please reference the above to choose the desired instance ID: ")
instanceID = "instanceid=" + user_input
print(instanceID)

#Reading from S3 to Pandas DataFrame
#Below will allow you to pull a specific instance ID 
#if you dont variables you can specify the instance ID e.g. instanceid=20191231011602
df = lake_dataset.as_pandas(prefix=instanceID)
df.head()
#Exporting the data
df.to_excel(r"C:/Users/FIY716/Documents/Projects/S3_Files/trade_master_refinery.xlsx", index = None)
#Can also export via csv
#df.to_csv(r"C:/Users/FIY716/Documents/Projects/S3_Files/trade_master_refinery.csv", index = None, header=True)




#Below gives you the Access_Key, Secret_Key and Token but is not needed if you are not pulling from aws enviroment which is not done via the above
from onelake.data_lake.credentials_provider import get_credentials_provider
credentials_provider = get_credentials_provider(
    session, dataset_id='232431', write_access=True
)
credentials_provider.get_credentials()
