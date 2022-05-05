import aws_cdk as cdk

from deploy.sample_stack import sample_cdk

app = cdk.App()
sample_cdk(app, "sample-cdk")

app.synth()