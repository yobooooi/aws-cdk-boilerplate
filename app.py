"""Implentation of custom CDK constructs"""
import aws_cdk as cdk

from deploy.boilerplate_stack import DynamoDBTable, LambdaFunction

app = cdk.App()

DynamoDBTable(app, "aws-cdk-boilerplate-ddbtable")
LambdaFunction(app, "aws-cdk-boilerplate-lambdafunction")

app.synth()
