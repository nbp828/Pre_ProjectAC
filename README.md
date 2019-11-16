# Pre_ProjectAC
By: Neil Patel (nbpatel6@illinois.edu)

## Introduction
This pre-project is eventually for option C but it is using option A
 to setup the final project. 
The final goal is to use a searching system for food ingredient data. 
The setup from project A will help extend the search to food ingredients

## Implementation
-   Backend:
    - ElasticSearch, which is populated with the dataset provided in the prompt
-   Website:
    - The Web Application is built with django and python and
    the elasticsearch python client
    - Django was chosen over Flask because it is a bit more 
    robust for a customer facing application

## Future Work
The food ingredients application will allow the user to:
 - add items to the data base.
 - search for the type of item (input = ingredients)
 - mark unhealthy ingredients and suggest alternatives

## Demo
The demo is hosted in Azure. Use the following link to test the system.
http://nbpatel6-demo-search.azurewebsites.net/
