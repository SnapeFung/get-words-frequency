def get_sentence(word, essay):
    # step 1: split the essay to sentence
    essay = essay.lower()
    splitted_sentence = essay.split('.')
    splitted_sentence = [i + '.' for i in splitted_sentence]
    sentence_list = []
    for sentence in splitted_sentence:
        if word in sentence:
            sentence = sentence.strip()
            sentence_list.append(sentence.capitalize())
    return sentence_list
