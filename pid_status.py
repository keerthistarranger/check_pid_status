import requests
from datetime import datetime
import getopt, sys
import urllib3
import boto3
import json


# Read in command-line parameters
idle = True
port = '8443'
pid = 12345
ignore_connections = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "ht:p:c", ["help","time=","port=","ignore-connections"])
    if len(opts) == 0:
        raise getopt.GetoptError("No input parameters!")
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(helpInfo)
            exit(0)
        if opt in ("-t", "--time"):
            time = int(arg)
        if opt in ("-p")
            pid = arg
        if opt in ("-c", "--ignore-connections"):
            ignore_connections = True
except getopt.GetoptError:
    #print(usageInfo)
    exit(1)
    
def get_notebook_name():
    log_path = '/opt/ml/metadata/resource-metadata.json'
    with open(log_path, 'r') as logs:
        _logs = json.load(logs)
    return _logs['ResourceName']


import psutil
if psutil.pid_exists(pid):
    print("a process with pid %d exists" % pid)
else:
    print("a process with pid %d does not exist" % pid)
    client = boto3.client('sagemaker')
    client.stop_notebook_instance(
        NotebookInstanceName=get_notebook_name()
    )
