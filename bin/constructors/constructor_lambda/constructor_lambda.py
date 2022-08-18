"""Module extending the CDK construct to create an AWS Lambda Function
with a NODEJS Runtime and inline code definitions"""

from aws_cdk import (
    aws_lambda as _lambda,
)

from constructs import Construct
from parameters import project_parameters


class LambdaFunction(Construct):
    """
    Class to create an AWS Lambda Construct

            Parameters
                    a) Construct: CDK Contsruct
            Returns
                    None
    """
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ):
        """
        Initialization method for an AWS Lambda Construct that creates a rudementary
        Lambda function with a NODEJS_14_X runtime and an inline code definition.

        Parameters
                a) scope: CDK Contsruct
                d) resource_id: String
        Returns
                None
        """
        super().__init__(scope, id, **kwargs)

        _lambda.Function(
            self,
            f"{project_parameters.GLOBAL_NAME}-{id}",
            runtime=_lambda.Runtime.NODEJS_14_X,
            handler="index.handler",
            code=_lambda.Code.from_inline(
                "\
                    exports.handler = async (event) => {\
                        console.log('event: ', event)\
                    };\
                "
            )
        )
