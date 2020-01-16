import re


def get_sentence(word, essay):
    # step 1: split the essay to sentence
    essay = essay.lower()
    essay = [i for i in essay if i.isalpha() is True or i == ' ' or i == '.']
    filter_essay = ''.join(essay)
    filter_essay = re.sub(' +', ' ', filter_essay)
    splitted_sentence = filter_essay.split('.')
    
    splitted_sentence = [i.strip() + '.' for i in splitted_sentence]
    sentence_list = []
    sentence_num = 0
    for sentence in splitted_sentence:
        if word in sentence:
            sentence = sentence.strip()
            sentence_list.append(sentence.capitalize())
    return sentence_list
