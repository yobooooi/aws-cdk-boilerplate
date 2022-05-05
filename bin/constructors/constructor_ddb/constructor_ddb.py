from aws_cdk import (
    aws_dynamodb as ddb,
    )

from parameters import globals
from constructs import Construct


class DynamoDBConstruct(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ):
        super().__init__(scope, id, **kwargs)

        securityEventsTable = ddb.Table(
            self,
            f"{globals.GLOBAL_NAME}-ddb-events-tbl",
            partition_key={
                "name": "eventId",
                "type": ddb.AttributeType.STRING,
            },
            read_capacity=2,  # same as asg min values
            write_capacity=2, # same as asg min values
            stream=ddb.StreamViewType("NEW_IMAGE"),
        )

        auto_scaling_read = securityEventsTable.auto_scale_read_capacity(min_capacity=2, max_capacity=10)
        auto_scaling_read.scale_on_utilization(target_utilization_percent=70)

        auto_scaling_write = securityEventsTable.auto_scale_write_capacity(min_capacity=2, max_capacity=10)
        auto_scaling_write.scale_on_utilization(target_utilization_percent=70)