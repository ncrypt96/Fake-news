import nltk
from nltk.corpus import wordnet as wn
from textblob import TextBlob
from nltk.corpus import stopwords

def convert_tag(tag):

    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None


def doc_to_synsets(doc):

    token = nltk.word_tokenize(doc)
    #remove articles
    articles = set(stopwords.words('english'))
    articles.remove("not")
    filtered_tokens = []
    for w in token:
        if w not in articles:
            filtered_tokens.append(w)

    # add parts of speech to token
    tag = nltk.pos_tag(token)
    # convert nltk pos into wordnet pos
    nltk2wordnet = [(i[0], convert_tag(i[1])) for i in tag]
    # if there are no synsets in token, ignore, else put in a list
    output = [wn.synsets(i, z)[0] for i, z in nltk2wordnet if len(wn.synsets(i, z))>0]

    return output


def similarity_score(s1, s2):
    # Your Code Here
    list1 = []
    # For each synset in s1
    for a in s1:
        # finds the synset in s2 with the largest similarity value
        list1.append(max([i.path_similarity(a) for i in s2 if i.path_similarity(a) is not None]))

    output = sum(list1)/len(list1)

    return output


def document_path_similarity(doc1, doc2):
            # first function u need to create
    synsets1 = doc_to_synsets(doc1)
    synsets2 = doc_to_synsets(doc2)
            # 2nd function u need to create
    return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2


def main(doc):

    result = []
    result.append(document_path_similarity(doc[0],doc[1]))
    result.append(document_path_similarity(doc[0],doc[2]))
    result.append(document_path_similarity(doc[0],doc[3]))
    result.append(document_path_similarity(doc[0],doc[4]))
    result.append(document_path_similarity(doc[0],doc[5]))
    print(result)

doc = [""]
main(doc)
