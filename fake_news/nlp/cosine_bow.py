from fake_news.preprocessor.nlp_preprocessor import NlpPreprocessing
import numpy as np 
from fake_news.preprocessor.error_handle import line_loc

def compute_cosine(vector_A,vector_B):
    """
    This methods  returns the cosine similarity between two word vectors

    :type vector_A: list
    :param vector_A: word vector

    :type vector_B: list
    :param vector_B: word vector 
    """
    return (np.dot(vector_A,vector_B) /( np.linalg.norm(vector_A) * np.linalg.norm(vector_B)))


def compute_bow_vectors(all_uinque_tokens,document_specific_tokens):
    """
    This method returns a list of bag of word vectos for the input given

    :type all_unique_tokens: list
    :param all_unique_tokens: set of all unrepeating tokens across all the text

    :type document_specific_tokens: list
    :param document_specific_tokens: list of all tokens present in that particular text
    """
    
    final_list = []
    for tokens in all_uinque_tokens:
        
        final_list.append(document_specific_tokens.count(tokens))
    
    return final_list

#==================MAIN METHOD===============================

def cosine_similartity_bow(text_list):
    """
    This method computes the cosine similarity between texts
    :type text_list: list
    :param text_list: list of all text
    """
    # initalize all empty
    doc_specific_tokens = []
    
    all_tokens = []

    vectors = []

    # tokenize and append
    for text in text_list:

        tokenizer =NlpPreprocessing(text)

        doc_specific_tokens.append(tokenizer.word_lem_tokenize())


    # get all tokens
    for tokens in doc_specific_tokens:

        for token in tokens:

            all_tokens.append(token)

    line_loc()

    # remove repeated tokens
    unique_tokens = list(set(all_tokens))
    
    line_loc()

    # make vectors
    for token in range(len(doc_specific_tokens)):

        vectors.append(compute_bow_vectors(unique_tokens,doc_specific_tokens[token]))


    cosine = []

    # compute cosine
    for i in range(1,len(doc_specific_tokens)):
        
        cosine.append(compute_cosine(vectors[0],vectors[i]))

    return cosine

#==================MAIN METHOD===============================
        









    

