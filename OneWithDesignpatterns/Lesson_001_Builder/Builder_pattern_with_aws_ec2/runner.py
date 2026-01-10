import boto3
from AppInfra.ec2Builder import EC2Builder, EC2Constructor
def main():
    ec2_client = boto3.client("ec2" ,region_name='us-east-1')

    builder = EC2Builder()
    constructor = EC2Constructor(builder)

    instance_config = constructor.create_dev_ec2_instance()
    print(f"Overall Ec2 Instance Configuration {instance_config}")
    print(f"Ready to launch {instance_config['InstanceType']} with AMI {instance_config['ImageId']}")
    response = ec2_client.run_instances(**instance_config)
    print(response)





if __name__ == "__main__":
    main()
