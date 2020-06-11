import nltk

# Get the name of the user from the message
def getName(tr): 
    t = nltk.ne_chunk(tr)
    for child in t:
        if isinstance(child, nltk.tree.Tree):
            return (" ".join([val[0] for val in child]))
    return getName2(tr)

def getName2(tr):  # Get the package name from the message
    if len(tr)>1:
        for child in tr:
            if child[1] == "NNP":
                return child[0]
    for child in tr:
        if child[1] == "NNP" or child[1] == "NN":
            return child[0]
    return 0

def getNumber(tr):
    for token in tr:
        if token[1] == 'CD':
            return token[0]
    return ''

def extract_preparation(message):  
    items = nltk.word_tokenize(message)
    sent = nltk.pos_tag(items)
    print(sent)
    return sent



# print(getName(extract_preparation("name is N.G.L.R.Lakshan")))
# print(getName(extract_preparation("name is Kumara Jayasinhga")))