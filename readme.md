# Retrieving Sentence Triples (Subject, Verb, Object)
A small set of rules for easy extraction of triples from sentences 

## Warnings
This has been tested on Windows 10 only, and so may break for other operating systems. 

## Install Requirements
### Install Packages
pip install spacy, python-dotenv, openai, tenacity

### Download Spacy Model 
python -m spacy download en_core_web_sm

### Add Your OpenAI API Key
In the .env file, add your OpenAI API key
OPENAI_KEY=OPEN_AI_KEY_WITHOUT_QUOTES

## Run Your App
py .\app.py