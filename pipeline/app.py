""" AWS CDK Application for creating a PipelineStack """
#!/usr/bin/env python3

from aws_cdk import core

from pipeline_stack import PipelineStack


APP = core.App()

APP_NAME = "chalice-app"
PIPELINE_STACK_NAME = f"{APP_NAME}-pipeline"

PipelineStack(
    APP,
    APP_NAME,
    stack_name=PIPELINE_STACK_NAME,
    repo_owner="folksgl",
    repo_name="chalice-cicd-app",
)

APP.synth()
