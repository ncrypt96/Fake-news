import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer

class NlpPreprocessing:
    """
    This class contains methods to pre process text to prepare them for NLP
    """
    def __init__(self,text):
        """
        :type text: string
        :param text: text to be tokenized
        """
        #Initialize self.text
        self.text = text

    def word_lem_tokenize(self):
        """
        This method returns a list of tokenized words which are also lemmatized
        """

        # instance of lemmatizer
        word_net_lemmatizer = WordNetLemmatizer()

        # initialize an empty list
        final_list = []

        # word tokenize the text which is in lower case and store it in tokens
        tokens = word_tokenize(self.text.lower())

        # a list of all the stopwords and punctuations
        stopwords_and_punctuations_list = stopwords.words('english') + list(string.punctuation)

        #if word is not present in the stop_words_and_punctuation_list lemmatize it and append it to the final list
        for word in tokens:

            if word not in stopwords_and_punctuations_list:

                final_list.append(word_net_lemmatizer.lemmatize(word))
        
        return final_list
