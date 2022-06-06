# flaskapi_demo

## Introduction
This is demo code for a simple Email validation API. The purpose of the Demo is to walk through a user journey on how the different products from RapidAPI help the developer at different stages of development process.
RapidAPI tools that this API is integrated into are: Enterprise Hub, Paw, VSCode Extension, and RapidAPI Testing. 

## Workflow
The demo starts off with showing a Python Flask API. We will run the API on localhost. From there, we can use Paw and the VSCode Extension to test the API running on localhost.
Once we are ready to make a commit to master, the Github Actions workflow will deploy the API on a Heroku service, then publish the updated OpenAPI Spec to RapidAPI Enterprise hub, and then run Integration Tests on the deployed API.

![RapidAPI Offerings - Code First](https://user-images.githubusercontent.com/91499603/172232732-3bea87aa-27c5-49b9-8587-5c31a12fd957.png)

## Project Structure
.github/workflows: This folder contains the main.yml file which connects into the integration services for Enterprise Hub and API Testing
spec/spec.json : This file is the OpenAPI spec that gets sent via Platform API to Enterprise Hub
app.py: This file contains the Flask Python and endpoints 


## Project Setup
### Prereqs: 
1. Developer Access to a RapidAPI Enterprise Hub instance ie jeff.hub.rapidapi.com
3. Internal client-services AWS account and access to the `IntegrationService-ApiSpecs` project. Contact Jeff Ding for access to the client-services AWS account
4. RapidAPI testing account setup with Developer Setup. Contact Kyle Keating for a Paid API Testing plan

### Setup:
#### 1. Setup the AWS Lambda function
Navigate to the `IntegrationService-ApiSpecs` project in AWS. Add your Platform API parameters and baseURL instance of Enterprise Hub in the `instances.js`. 
Be sure to check for the JSON Formatting before saving! 
```
    "jeff": {
        "baseUrl": "https://platformapi.p.rapidapi.com",
        "host": "platformapi.jeff.rapidapi.com",
        "apiKey": "aed1c6408fmshcb2c5c09cc5db9bp184cb1jsn0a88d24007c2"
    }
```

#### 2. Edit the main.yml
Navigate to the `main.yml` file. Edit the ` customHeaders: '{"instance" : "jeff"}' ` line to match your instance name.
```
      # POST to Integration Service
      - name: Post to Integration Layer
        id: postToIntegrationLayer
        if: steps.changed-spec-files.outputs.any_changed == 'true'
        # You may pin to the exact commit or the version.
        # uses: fjogeleit/http-request-action@d45f6649f63b711b64bcd10e95a600abe4468456
        uses: fjogeleit/http-request-action@v1.9.0
        with:
          url: https://ed5u76i86j.execute-api.us-east-1.amazonaws.com/prod/github
          customHeaders: '{"instance" : "jeff"}'
          method: POST
          contentType: "application/json"
          file: ${{ steps.changed-spec-files.outputs.modified_files }}
```

#### 3. Setup some functionality tests with RapidAPI Testing

#### 4. Connect the tests into the main.yml file 

```
      # Execute the Integration Tests on RapidAPI 
      # A failed test from RapidAPI will fail the GitHub Action
      - name: Execute Tests
        id: tstExec
        uses: RapidAPI/gh-api-testing-trigger@jeffrapid-patch-1 
        with:
          test: 'test_de090ff3-c343-4ff7-86db-32d104f7f691'
          location: 'AWS-US-EAST-1'
          instance: 'jeff.hub.rapidapi'
          #environment: 'ENV_ID(OPTIONAL)'
 ```
