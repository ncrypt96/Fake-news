from allennlp.predictors.predictor import Predictor

class Query:
    """
    This class contains methods to compute comprehension and to check hypotheis
    """

    
    def ask_question(self,text,question):
        """
        This methods returns an answer to the question asked upon the content

        Returns: answer

        :type question: string
        :param question: question to be asked

        :type text: string
        :param text: the text for the passage
        """

        # load predictor model
        predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")
        
        # predictss
        predict = predictor.predict(
        passage=text,
        question=question
        )
        
        # return the answer
        return predict['best_span_str']

    
    def check_hypothesis(self,text,hypothseis):
        """
        This method checks weather a hypothesis is true or not 
        returns a list of form [entailment,contradiction,neutral]

        :type text: string
        :param text: the text for the hypothesis

        :type hypothesis: string
        :param hypothesis: the hypothesis to bes tested
        """
        # load predictor model
        predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/decomposable-attention-elmo-2018.02.19.tar.gz")

        # test hypothesis
        predict = predictor.predict(
        hypothesis= text,
        premise=hypothseis
        )

        # return values
        return predict['label_probs']
