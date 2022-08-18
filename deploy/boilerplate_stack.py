"""Deployment module of custon CDK constructs"""

from aws_cdk import (
    Stack,
)

from constructs import Construct

from bin.constructors.constructor_ddb import constructor_ddb as ddb_table
from bin.constructors.constructor_lambda import constructor_lambda as lambda_function

class DynamoDBTable(Stack):
    """
    Class implementing the custom AWS DynamoDB Construct

            Parameters
                    a) Stack: CDK Stack
            Returns
                    None
    """
    def __init__(self, scope: Construct, stack_id: str, **kwargs) -> None:
        super().__init__(scope, stack_id, **kwargs)

        ddb_table.DynamoDBConstruct(
            self,
            stack_id,
        )

class LambdaFunction(Stack):
    """
    Class implementing the custom AWS Lambda Function that deploys a
    NODEJS lambda

            Parameters
                    a) Stack: CDK Stack
            Returns
                    None
    """
    def __init__(self, scope: Construct, stack_id: str, **kwargs) -> None:
        super().__init__(scope, stack_id, **kwargs)

        lambda_function.LambdaFunction(
            self,
            stack_id,
        )
