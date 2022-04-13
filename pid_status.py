import requests
from datetime import datetime
import getopt, sys
import urllib3
import boto3
import json
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read in command-line parameters
idle = True
port = '8443'
pid = 12345
ignore_connections = False
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "p:", ["pid="])
#     if len(opts) == 0:
#         raise getopt.GetoptError("No input parameters!")
#     for opt, arg in opts:
#         if opt in ("-p", "--pid")
#             pid = arg
        
# except getopt.GetoptError:
#     #print(usageInfo)
#     exit(1)
    
def get_notebook_name():
    log_path = '/opt/ml/metadata/resource-metadata.json'
    with open(log_path, 'r') as logs:
        _logs = json.load(logs)
    return _logs['ResourceName']


import psutil
if psutil.pid_exists(pid):
    #print("a process with pid %d exists" % pid)
    print("process still running")
else:
    #print("a process with pid %d does not exist" % pid)
    client = boto3.client('sagemaker')
    client.stop_notebook_instance(
        NotebookInstanceName=get_notebook_name()
    )



# # try:
# #     os.kill(pid, 0)
# # except OSError:
# #     print("pid is unassigned")
# #     client = boto3.client('sagemaker')
# #     client.stop_notebook_instance(
# #         NotebookInstanceName=get_notebook_name()
# #     )
# # else:
# #     print("pid is in use")

# import os
# import os.path
# #pid=0
# path_pid="/proc/"+str(pid)
# if os.path.exists(path_pid):
#     print("process stll running")
# else:
#     client = boto3.client('sagemaker')
#     client.stop_notebook_instance(
#          NotebookInstanceName=get_notebook_name())

# client = boto3.client('sagemaker')
# client.stop_notebook_instance(
#          NotebookInstanceName=get_notebook_name())
    






