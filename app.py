"""
Lambda that :
reads customer DB API
billing file from AWS billing_bucket

merges the data to produce CostReporting input
"""


from package.utils_cloud import cloud_function


def lambda_handler(event, context):

    print('Hi, we are testing packages import here')

    cloud_function()
    return


if __name__ == "__main__":
    lambda_handler(None, None)
