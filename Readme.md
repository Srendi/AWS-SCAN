### Description
This is a script (and libraries python-nmap, slacker) to portscan the AWS assets and send the results to slack.
It is intended to be run from AWS Lambda, but can be run from any python environment with the libraries installed.
As such, it is neccessary to package the code and libraries for deploy to AWS Lambda. 

### Prepare a dev environment
If you choose to develop this script further you should prepare a python virtualenv. e.g. 
```
#Get the source
cd /path/to/parentdir_of_repo
#get source
git clone 
#Prepare a virtual env for dev
pip install virtualenv
virtualenv ./aws-asset-external-port-scan
cd ./aws-asset-external-port-scan

#Activate the environment
# Linux
source /path/to/aws-asset-external-port-scan/bin/activate
#Windows CMD
C:\path\to\aws-asset-external-port-scan\Scripts\activate.bat
#Windows PowerShell
C:\path\to\aws-asset-external-port-scan\Scripts\activate.ps1
# Install requirements
pip install -r requirements.txt
```
Run the script locally with `python ./nmapLambdaPortScan.py host2scan1 [host2scan2]...`

*You can leave the virtual environment with the command `deactivate`
Dont check in to git any of the files created in the virtualenv. The only things that should be checked into git are the existing files (or relevant additions), and a complete Lambda package, ready to be uploaded to AWS Lambda.*

### Create an AWS Lambda Deployment
*The short version* Add the .py code to a zip file, then add the virtualenv/Libs/Sitepackages/* to the same zip . *Directory contents, not directories*
See: [Creating a Deployment Package (Python)](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)