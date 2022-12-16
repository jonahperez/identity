Example AWS Cognito project with a python client and a React client.


you can use the AWS Console to create this applicaiton:

aws cloudformation create-stack --stack-name <stackname> --template-body file://Food.yaml --capabilities CAPABILITY_IAM

The outputs of the stack contain the values for the files:
* app_config.js
* ConnectionSettings.py

The output called <secretcommand> is an aws command that can be used to get the last field for the ConnectionSettings.py file.
