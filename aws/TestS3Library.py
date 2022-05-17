import boto3
from botocore.exceptions import ClientError
from mypy_boto3_s3 import S3Client
from robot.api.logger import debug


def expected_error(error_code, default_value):
    """
    Decorator that catches ClientError exception. If the expected error code is corresponding to actual, returns
    default value, else - returns the output of the method.
    :param error_code: Expected error code
    :param default_value: Value to be returned if expected exception accrued.
    :return:
    """

    def _wrapper(method):
        def _inner(*args, **kwargs):
            out = default_value
            try:
                out = method(*args, **kwargs)
            except ClientError as e:
                if e.response['Error']['Code'] != error_code:
                    debug(e)
                    raise e
            return out
        return _inner
    return _wrapper


class TestS3Library:
    def __init__(self):
        self.s3client: S3Client = boto3.client("s3")

    @expected_error('NoSuchTagSet', [])
    def get_bucket_tags(self, bucket_name: str) -> list[dict]:
        """
        Returns the tags of bucket.
        :return: List of tags in format [{"Key": TAG_KEY, "Value": TAG_VALUE}]
        """

        response = self.s3client.get_bucket_tagging(Bucket=bucket_name)
        return response['TagSet']

    @expected_error('ServerSideEncryptionConfigurationNotFoundError', [])
    def get_bucket_encryption_types(self, bucket_name: str) -> list:
        response = self.s3client.get_bucket_encryption(Bucket=bucket_name)
        return response['ServerSideEncryptionConfiguration']['Rules']

    @expected_error(None, None)
    def get_bucket_size_mb(self, bucket_name: str) -> float:
        """
        Return the size of all files in bucket in megabytes.
        """

        bucket = self.s3client.list_objects(Bucket=bucket_name)['Contents']
        return sum(file["Size"] for file in bucket) / 1000000
