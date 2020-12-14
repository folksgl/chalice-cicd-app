""" AWS CDK Application for creating a PipelineStack """
#!/usr/bin/env python3

import json
from aws_cdk import core
from pipeline_stack import PipelineStack


app = core.App()

with open("../app/.chalice/config.json") as config_file:
    config = json.load(config_file)
    app_name = config["app_name"]

PipelineStack(
    app,
    app_name,
    stack_name=f"{app_name}-pipeline",
    repo_owner="folksgl",
    repo_name="chalice-cicd-app",
    repo_branch="main",
)

app.synth()
