Chalice CI/CD App
=================
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
    - [AWS CDK](#aws-cdk)
    - [Setting Up](#setting-up-your-environment)
- [Development Flow](#development-flow)
    - [Deploying the application](#deploying-the-chalice-application)

## Overview
The chalice-cicd-app template repo is a serverless application that uses the [AWS Chalice serverless framework](https://aws.github.io/chalice/index.html#). This repo includes both a hello-world Chalice app (located in [/app](https://github.com/folksgl/chalice-cicd-app/tree/main/app)), as well as a CI/CD pipeline (located in [/pipeline](https://github.com/folksgl/chalice-cicd-app/tree/main/pipeline)) for deploying the code written using the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/). It is **highly** recommended that developers have a working understanding of the CDK, Chalice framework, and the underlying serverless AWS resources being manipulated during serverless development.

## Installation

### AWS CDK
To install the AWS CDK, please follow the [AWS CDK installation instructions](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install).

### Setting up your environment
To set up your environment, follow these steps:
```sh
git clone https://github.com/folksgl/chalice-cicd-app.git
cd chalice-cicd-app
python3 -m venv venv38
source venv38/bin/activate
python3 -m pip install -r requirements.txt
pre-commit install
```
NOTE - Currently the latest Python runtime available in AWS Lambda is Python 3.8, so using versions other than 3.8 locally could cause runtime failures if your code depends on features not available in version 3.8

## Development Flow
The development flow for this repo can be split into two streams. Work on the CI/CD pipeline to deploy the application is found under the [pipeline](https://github.com/folksgl/chalice-cicd-app/tree/main/pipeline) while the application code can be done in the [app directory](https://github.com/folksgl/chalice-cicd-app/tree/main/app).

### Deploying the Chalice application
All deployments require having the correct AWS CLI credentials in place. If you haven't already, install the AWS CLI and set up credentials to your AWS account.
#### With the CI/CD pipeline
Before deploying with the CI/CD pipeline, you must create a CodeStar Connection to the GitHub account your repo is located in. Once that connection is created,
store the ARN of the connection in a SecretsManager Secret, with the JSON key of 'arn'. In JSON, the secret should look like the following:
```json
{ "arn": "<my-connection-arn>" }
```
To deploy the application with the CI/CD pipeline:
```sh
cd pipeline
cdk deploy --parameters ConnectionSecretId=<secret-id>
```
#### Without the pipeline
Deployments without the pipeline must change directories into the hello world directory. Chalice deployments can make direct usage of the `chalice` CLI tool
using `chalice local` or `chalice deploy` commands. Please use `chalice --help` and see the [Chalice documentation](https://aws.github.io/chalice/index.html).
