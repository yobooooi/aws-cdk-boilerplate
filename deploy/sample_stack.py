from constructs import Construct
from bin.constructors.constructor_ddb import constructor_ddb as ddb_producer
from aws_cdk import (
    Stack,
)

class sample_cdk(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = ddb_producer.DynamoDBConstruct(
            self,
            id = "sample_cdk_ddbtable",
        )