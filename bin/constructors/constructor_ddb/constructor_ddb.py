"""Module extending the CDK construct to create a DynamoDB table with autoscaling
and a pre-configured index"""

from aws_cdk import aws_dynamodb

from constructs import Construct
from parameters import project_parameters


class DynamoDBConstruct(Construct):
    """
    Class to create an AWS DynamoDB Construct

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
        Init method to create an AWS DynamoDB table with a minium and maximum RCU and WCU of
        2 and 10 respectively. The DynamoDB table is nameed using by concatinating the
        GLOBAL_NAME defined in the project paramters and the value parse in id. The DynamoDB
        table is indexed using a STRING value Id.

        Parameters
                a) scope: CDK Contsruct
                d) resource_id: String
        Returns
                None
        """
        super().__init__(scope, id, **kwargs)

        ddb_table = aws_dynamodb.Table(
            self,
            f"{project_parameters.GLOBAL_NAME}-{id}",
            partition_key={
                "name": "Id",
                "type": aws_dynamodb.AttributeType.STRING,
            },
            read_capacity=2,  # same as asg min values
            write_capacity=2,  # same as asg min values
            stream=aws_dynamodb.StreamViewType("NEW_IMAGE"),
        )

        auto_scaling_read = ddb_table.auto_scale_read_capacity(
            min_capacity=2, max_capacity=10
        )
        auto_scaling_read.scale_on_utilization(target_utilization_percent=70)

        auto_scaling_write = ddb_table.auto_scale_write_capacity(
            min_capacity=2, max_capacity=10
        )
        auto_scaling_write.scale_on_utilization(target_utilization_percent=70)
