print("Please be patient while system loading.....")
# for cutting warnings
import logging
import os
import warnings
import sys

# logging.disable(logging.WARNING)
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# warnings.simplefilter(action='ignore', category=FutureWarning)


# stderr = sys.stderr
# sys.stderr = open(os.devnull, 'w')
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# import created functions and files
from email_sender import verification_key_passer
import extractor
import package_management

# machine learning
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import keras.backend.tensorflow_backend as tbb
import pandas as pd
import random
# from sklearn.externals import joblib
import json
import tensorflow as tf
import joblib

stemmer = LancasterStemmer()
words = []
classes = []
documents = []
ignore_words = ['?']

# open dataset file
with open('Dataset.json') as json_file:
    intents = json.load(json_file)

# put intents of dataset into different arrays
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# training dataset
training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])


random.shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])
train_y = list(training[:, 1])
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
try:
    print("check1")
    # use pretrained model
    model = joblib.load('banking_model.pkl')
    words, ignore_words, classes, documents = joblib.load('banking_data.pkl')

except:
    print("check2")
    # train the model at the first time
    model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=0)
    joblib.dump(model, 'banking_model.pkl')
    joblib.dump((words, ignore_words, classes, documents), 'banking_data.pkl')


# given sentence split into words
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# comparing words from sentence_words and intent words
def bag_of_words(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words) # gives [0, 0, 0, 0, 0, 0] upto length of words
    for s in sentence_words:
        for i, w in enumerate(words): # enumerate - re build the list with tuples including indexes(i),word(w)
            if w == s:
                bag[i] = 1
    return np.array(bag)


# predict the user input to recognize the catagory from dataset
def get_results(message):
    ERROR_THRESHOLD = 0.75
    try:
        input_data = pd.DataFrame([bag_of_words(message, words)], dtype=float, index=['input'])
        tbb._SYMBOLIC_SCOPE.value = True
        results = model.predict([input_data])[0]
        results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)

        return_list = []

        for r in results:
            return_list.append((classes[r[0]], str(r[1])))

        if len(return_list[0]) == 0:
            return [('noanswer', 0.870264)]
        # print(return_list)
        return return_list
    except IndexError:
        return [('noanswer', 0.870264)]

# get proper response from dataset 
def get_response(x):
    for i in range(len(intents['intents'])):
        if intents['intents'][i]["tag"] == x:
            return random.choice(intents['intents'][i]["responses"])

context = {}

# Prepare sentence with part of speech tags
def extract_preparation(message):  
    items = nltk.word_tokenize(message)
    sent = nltk.pos_tag(items)
    # print(sent)
    return sent

#build money transfer process
def moneytrasferprocess(messageText, userId):
    if 'number' not in context[userId]:
        pos = extract_preparation(messageText)
        accnum = extractor.getNumber(pos)
        context[userId]['number'] = accnum
        return "What is the Holding account registered name ?"

    elif 'name' not in context[userId]:
        pos = extract_preparation(messageText)
        name = extractor.getName(pos)
        context[userId]['name'] = name
        if len(context[userId]) == 3:
            return "How much do you prefer to transfer \n[consider with LKR]"
    
    elif 'amount' not in context[userId]:
        pos = extract_preparation(messageText)
        amount = extractor.getNumber(pos)
        if amount == '':
            return "Amount should be a number. Please re-enter it"
        context[userId]['amount'] = float(amount)
        data = package_management.getpersonal(userId)
        context[userId]['code'] =  verification_key_passer(data['email'], data['first_name'])
        return "Please check your email and enter the verification key.."
    else:
        pos = extract_preparation(messageText)
        code = extractor.getNumber(pos)
        if int(code) != context[userId]['code']:
            return "Verification key is invalid. Please re-enter it"

    boolean,reply,repindx = package_management.dotransfer(userId,context[userId])

    if boolean:
        del context[userId]
    else:
        if repindx == 1:
            del context[userId]
        elif repindx == 2:
            del context[userId]['number'], context[userId]['name']

    if reply == "Error has occured with the Banking server. Sorry about that!":
        del context[userId]
    return reply

#build bill payment process
def paymentprocess(messageText, userId):
    if 'field' not in context[userId]:
        pos = extract_preparation(messageText)
        field = extractor.getName(pos)
        context[userId]['field'] = field
        if len(context[userId]) == 2 :
            return "Please enter the account number that you want to deposit"
    
    elif 'number' not in context[userId]:
        pos = extract_preparation(messageText)
        accnum = extractor.getNumber(pos)
        context[userId]['number'] = accnum
        return "What is consumer's name ?"
    
    elif 'name' not in context[userId]:
        pos = extract_preparation(messageText)
        # print(pos)
        name = extractor.getName(pos)
        context[userId]['name'] = name
        return "What is consumer's address ?"
    
    elif 'address' not in context[userId]:
        address = messageText
        context[userId]['address'] = address
        if len(context[userId]) == 5:
            return "How much do you prefer to pay \n[consider with LKR]"
    
    elif 'amount' not in context[userId]:
        pos = extract_preparation(messageText)
        amount = extractor.getNumber(pos)
        if amount == '':
            return "Amount should be a number. Please re-enter it"
        context[userId]['amount'] = float(amount)
        data = package_management.getpersonal(userId)
        context[userId]['code'] =  verification_key_passer(data['email'], data['first_name'])
        return "Please check your email and enter the verification key.."

    else:
        pos = extract_preparation(messageText)
        code = extractor.getNumber(pos)
        if int(code) != context[userId]['code']: 
            return "Verification key is invalid. Please re-enter it"
    # print(context[userId])
    boolean,reply,repindx = package_management.dopayment(userId,context[userId])

    if boolean:
        del context[userId]
    else:
        if repindx == 1 or repindx == 2:
            del context[userId]
        elif repindx == 3 :
            del context[userId]['field']
        elif repindx == 4:
            del context[userId]['name'], context[userId]['address']
    print(reply)
    if reply == "Error has occured with the Banking server. Sorry about that!":
        del context[userId]
    return reply

# build complaint process
def complainprocess(messageText, userId):
    if 'branch' not in context[userId]:
        pos = extract_preparation(messageText)
        branch = extractor.getName(pos)
        context[userId]['branch'] = branch
        if len(context[userId]) ==3:
            return "Describe about the Complaint with details !"
    
    elif 'description' not in context[userId]:
        description = messageText
        context[userId]['description'] = description

    boolean,reply,repindx = package_management.reportcomplain(context[userId])

    if boolean :
        del context[userId]   
    else:
        if repindx == 1:
            del context[userId]
        elif repindx == 2:
            del context[userId]['branch']
    
    if reply == "Error has occured with the Banking server. Sorry about that!":
        del context[userId]
    return reply

#connect user account and bank account together
def joinaccprocess(messageText, userId):
    if 'number' not in context[userId]:
        pos = extract_preparation(messageText)
        accnum = extractor.getNumber(pos)
        context[userId]['number'] = accnum
        return "What is your account holding registered name ?"

    elif 'name' not in context[userId]:
        pos = extract_preparation(messageText)
        # print(pos)
        name = extractor.getName(pos)
        context[userId]['name'] = name
        return "What is your NIC ?" 
    
    elif 'nic' not in context[userId]:
        pos = extract_preparation(messageText)
        nic = extractor.getNumber(pos)
        context[userId]['nic'] = nic
    # print(context[userId])
    boolean,reply,repindx = package_management.loginaccount(userId,context[userId])
    
    if boolean:
        del context[userId]
    else:
        if repindx == 1:
            del context[userId]
        if repindx == 2:
            del context[userId]['number'], context[userId]['name'], context[userId]['nic']
    
    if reply == "Error has occured with the Banking server. Sorry about that!":
        del context[userId]
    return reply

# chatbot conversation
def response(messageText, userId):
    # print(messageText, userId)
    try:
        tag = get_results(messageText)[0][0] #classify the message and get tag
        # print(tag)
        if userId in  context:
            if  tag != 'quit':
                if context[userId]['model'] == 'transfer':
                    return moneytrasferprocess(messageText, userId)

                elif context[userId]['model'] == 'payment':
                    return paymentprocess(messageText, userId)

                elif context[userId]['model'] == 'complain':
                    return complainprocess(messageText, userId)
                
                elif context[userId]['model'] == 'joinaccounts':
                    return joinaccprocess(messageText, userId)
                
            else:
                del context[userId]
                return get_response(tag)




        if tag == 'transfer':
            if package_management.checkjoin(userId):
                context[userId] = {'model':'transfer'}
                return get_response(tag) +"\nPlease enter the beneficiary's account number\n\nYou may enter 'quit' to exit out of any ongoing action."
            

        elif tag == 'payment':
            if package_management.checkjoin(userId):
                context[userId] = {'model':'payment'}
                return get_response(tag) + "\n\nYou may enter 'quit' to exit out of any ongoing action."
        

        elif tag in ['complain_behaviour','complain_management','complain_facility','complain_wasting']:
            if package_management.checkjoin(userId):
                context[userId] = {'model':'complain', 'type': tag}
                return get_response(tag) + "\n\nYou may enter 'quit' to exit out of any ongoing action."


        elif tag == 'history':
            if package_management.checkjoin(userId):
                data = package_management.getTransactions(userId)
                # print(data)
                message = "Date".ljust(40) + "Debit".ljust(20) + "Credit".ljust(20) + "Balance".ljust(20) + "Description".ljust(40) + "\n\n"
                for i in range(len(data)):
                    message += str(data[i]['date'].strftime("%d-%b-%Y (%H:%M:%S)")).ljust(30) + str(data[i]['debit']).ljust(20) + str(data[i]['credit']).ljust(20) + str(data[i]['balance']).ljust(20) + str(data[i]['description'][:40]).ljust(40) +"\n"
                print(message)
                return get_response(tag) + message


        elif tag == 'balance':
            if package_management.checkjoin(userId):
                balance = package_management.getAccBalance(userId)
                # print(balance)
                return get_response(tag) + str(balance)


        elif tag == 'personal':
            if package_management.checkjoin(userId):
                tup = package_management.getpersonal(userId)
                message = """Registered Name : """+tup['name']+"""\nUsername : """+tup['first_name']+"""\nAccount No : """+tup['accno']+"""\nBranch : """+tup['branch']+"""\nNIC : """+tup['nic']+"""\nEmail : """+tup['email']
                return get_response(tag)+"\n\n"+message


        elif tag == 'name':
            if package_management.checkjoin(userId):
                name = package_management.getname(userId)
                return get_response(tag) + name

        
        elif tag == 'account':
            if package_management.checkjoin(userId):
                tup = package_management.getpersonal(userId)
                return get_response(tag) + tup['accno']


        else:
            return get_response(tag)
        

        context[userId] = {'model':'joinaccounts'}
        return "First, You have to connect with your bank account. Otherwise this action is denied\n\nWhat is your bank account number ?"
    
    except :
        return "Error has occured with the Banking server. Sorry about that!"