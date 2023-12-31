# Retrieving Sentence Triples (Subject, Verb, Object)
A small set of rules for easy extraction of triples from sentences 

![image](https://github.com/Davidwarchy/svo/assets/17954362/0f441d5c-3b03-47d4-84dd-c885bcbd9599)

## Warnings
This has been tested on Windows 10 only, and so may break for other operating systems. 

## Install Requirements
### Install Packages
```pip install spacy, python-dotenv, openai, tenacity```

### Download Spacy Model 
```python -m spacy download en_core_web_sm```

### Add Your OpenAI API Key
In the .env file, add your OpenAI API key

```OPENAI_KEY=OPEN_AI_KEY_WITHOUT_QUOTES```

## Run Your App
### Input
```py .\app.py "KQ signs codeshare agreement with Delta - Capital Business"```

### Expected Output
RULE 1: KQ sign agreement

RULE 2: ('KQ', 'sign', 'agreement')
