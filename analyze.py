#!/usr/bin/python
import nltk
from guessReview import guessReview
from nltk.corpus import stopwords
import pdb

guessReview = guessReview() 
#word_features = guessReview.getWordFeatures(guessReview.getWordsInReview(reviews))

posReview = []
negReview = []
netReivew = []

# Parse JSON data and put into tagged arrays
guessReview.parseFile('Yelp-DataSet/train.json', posReview, negReview,netReivew)

print "The number of positive reviews is: " + str(len(posReview))
print "The number of negative reviews is: " + str(len(negReview))

posReviewActual = []
posReviewActual = posReview[:len(negReview)]
#
taggedReview = posReviewActual + negReview
#
reviews = []
#
# Create a list of words in the review, within a tuple
for(word, sentiment) in  taggedReview:
  word_filter = [i.lower() for i in word.split() if len(i) >= 3]
  reviews.append((word_filter, sentiment))

# Pull out all the words in a list of tagged reviews, formatted in tuples.

def getwords(yReviews):
  allwords = []
  for(words, sentiment) in yReviews:
    allwords.extend(words)
  return allwords

def getwordfeatures(listofyReviews):
  wordfreq = nltk.FreqDist(listofyReviews)
  words = wordfreq.keys()
  return words
#
wordlist = getwordfeatures(getwords(reviews))
#print(stopwords.words('english'))

wordlist = [i for i in wordlist if not i in stopwords.words('english')]

def feature_extractor(doc):
  docwords = set(doc)
  features = {}
  for i in wordlist:
    features['contains(%s)' %i] = (i in docwords)
  return features

training_set = nltk.classify.apply_features(feature_extractor, reviews)
  
classifier = nltk.NaiveBayesClassifier.train(training_set)

print classifier.show_most_informative_features(n=30)

posTest = []
negTest = []
neutTest = []

#guessReview.parseFile('Yelp-DataSet/test.json',posTest, negTest, neutTest)
counter = 0
#for (words, sent) in negTest:
  #print feature_extractor(words.split());
  #print classifier.classify(feature_extractor(words.split()))
  #if classifier.classify(feature_extractor(words.split())) == 'negative':j
   # counter = counter + 1

