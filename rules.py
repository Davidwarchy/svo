from helper import complete, extract_subject_action_object

def rule1(nlp,text):
    
    docs = nlp(text)

    sents_out = []
    
    for sent_in in docs.sents:

      for token in sent_in:
          
          # if the token is a verb
          if (token.pos_=='VERB'):
              
              phrase =''
              
              # only extract noun or pronoun subjects
              for sub_tok in token.lefts:
                  
                  if (sub_tok.dep_ in ['nsubj','nsubjpass']) and (sub_tok.pos_ in ['NOUN','PROPN','PRON']):
                      
                      # add subject to the phrase
                      phrase += sub_tok.text

                      # save the root of the verb in phrase
                      phrase += ' '+token.lemma_ 

                      # check for noun or pronoun direct objects
                      for sub_tok in token.rights:
                          
                          # save the object in the phrase
                          if (sub_tok.dep_ in ['dobj']) and (sub_tok.pos_ in ['NOUN','PROPN']):
                                      
                              phrase += ' '+sub_tok.text

                              sents_out.append(phrase) 
    if sents_out != []:
        return sents_out[0]
    return None

def rule2(sent):
    """
    get a triple from gpt3.5
    """
    with open('prompt.md') as f:
        pre_prompt = f.read()
    if not pre_prompt:
        raise Exception("No prompt file found.")
    
    # get the statement after colon if it available
    sentence = sent.split(':')[-1].strip()
    prompt = pre_prompt.replace('[SENTENCE_HERE]', sentence)
    
    system_prompt = ""
    result = complete(system_msg=system_prompt, prompt=prompt)
    if result:
        j = extract_subject_action_object(result)
        return j
    
