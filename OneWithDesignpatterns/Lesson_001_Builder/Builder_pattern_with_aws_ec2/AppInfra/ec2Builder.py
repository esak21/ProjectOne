from typing import Self
from enum import Enum

class INSTANCETYPE(Enum):
    DEV = 't2.micro'
    PROD = 't2.medium'


class EC2Builder:
    """ EC2 Builder Class """
    def __init__(self):
        self.params = {}

    def set_image_id(self, image_id: str) -> Self :
        self.params['ImageId'] = image_id
        return self

    def set_instance_type(self, value:str):
        self.params['InstanceType'] = value
        return self

    def set_max_count(self, max_count:int):
        self.params['MaxCount'] = max_count
        self.params['MinCount'] = 1
        return self

    def set_security_groups(self, security_groups:list[str]):
        self.params['SecurityGroupIds'] = security_groups
        return self

    def set_instance_profile(self, instance_iam_role:str):
        self.params['InstanceProfile'] = instance_iam_role
        return self

    def build(self):
        print(type(self.params))
        return self.params


class EC2Constructor:

    def __init__(self, ec2_builder : EC2Builder):
        self.builder = ec2_builder

    def create_dev_ec2_instance(self):
        return self.builder.set_instance_type("t2.micro").set_max_count(1).set_security_groups(["sg-0ece7828869b52df5","sg-0a8594f7aed8ce57f"]).set_image_id("ami-07ff62358b87c7116").build()

    def create_prod_ec2_instance(self):
        return self.builder.set_instance_type("t2.medium").set_max_count(1).set_security_groups(["sg-0ece7828869b52df5","sg-0a8594f7aed8ce57f"]).set_image_id("ami-0ecb62995f68bb549").build()


