import en_core_web_sm
from rules import rule1, rule2

nlp = en_core_web_sm.load()

if __name__ == '__main__':
    text = """KQ signs codeshare agreement with Delta - Capital Business"""

    # triple with rule 1
    result = rule1(nlp, text)
    print(f'RULE 1: {result}')

    # triple with rule 2 (gpt3.5)
    result = rule2(text)
    print(f'RULE 2: {result}')

    