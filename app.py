import sys
import en_core_web_sm
from rules import rule1, rule2

nlp = en_core_web_sm.load()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a sentence as a command-line argument.")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    # triple with rule 1
    result = rule1(nlp, text)
    print(f'RULE 1: {result}')

    # triple with rule 2 (gpt3.5)
    result = rule2(text)
    print(f'RULE 2: {result}')
