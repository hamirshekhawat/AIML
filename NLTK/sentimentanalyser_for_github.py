#


import csv   #for reading csv file and saving it into a dictionary
import nltk   # for importing naive bayes classifier
import pickle  # for creating a saved copy of any object

tweetset = []

with open('/SentimentAnalysisDataset.csv', 'r') as sad: #use your directory structure where the csv is situated
	reader=csv.DictReader(sad)
	
	j = 0
	k = 0
	
	for row in reader:
		if j!=800:
			if row['Sentiment'] == '1':
				tweetset.append((row['SentimentText'], 'positive'))
				j=j+1
		else:
			break
				
	for row in reader:
		if k!=800:
			if row['Sentiment'] == '0':
				tweetset.append((row['SentimentText'], 'negitive'))
				k=k+1
		else:
			break



i=0
while i<10:
	print tweetset[i]
	i=i+1

	
tweets = []

for (words, sentiment) in tweetset:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
    	
#feature extraction
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words



def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

word_features = get_word_features(get_words_in_tweets(tweets))

#training i.e.creating a training set and using it to create an object of NaiveBayesClassifier and then storing it as a pickle
#uncomment the below code for creating the pickle object if you arent using the one provided
'''
print "got word_features"

#creates a list of tuples containing feature dictionary and the sentiment string for each tweet
training_set = nltk.classify.apply_features(extract_features, tweets)

print "created training set"

#training classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

f = open('/my_classifier_2.pickle', 'wb') #use your directory
pickle.dump(classifier, f)
f.close()
'''
#comment the code below if you arent using the pickle object
f = open('/my_classifier.pickle', 'rb') #use your directory structure where the pickle object is situated
classifier = pickle.load(f)
f.close()
#----


print "trained classifier"

##------------------------------
#sample
tweet = raw_input("enter the required statement: ")
#classify the given text into positive or negative statement
print classifier.classify(extract_features(tweet.split()))


