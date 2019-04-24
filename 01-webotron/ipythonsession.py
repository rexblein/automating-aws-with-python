# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation', region_name='us-east-1')
s3 = session.resource('s3')
