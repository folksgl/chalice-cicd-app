""" AWS CDK Application for creating a PipelineStack """
#!/usr/bin/env python3

import json
from aws_cdk import core
from pipeline_stack import PipelineStack


APP = core.App()

with open("../app/.chalice/config.json") as config_file:
    CONFIG = json.load(config_file)

if "app_name" not in CONFIG:
    print("Please configure 'app_name' in app/.chalice/config.json")

APP_NAME = CONFIG.get("app_name")
PIPELINE_STACK_NAME = f"{APP_NAME}-pipeline"

PipelineStack(
    APP,
    APP_NAME,
    stack_name=PIPELINE_STACK_NAME,
    repo_owner="folksgl",
    repo_name="chalice-cicd-app",
)

APP.synth()
