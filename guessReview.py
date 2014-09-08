import json
import nltk
from pprint import pprint

class guessReview:


  #positiveReview=[]
  #negativeReview=[]
  #neutralReview=[]
  #reviews = []

  def parseFile(self, fName, positiveReview, negativeReview, neutralReview):
    with open (fName) as data_file:
        data = json.load(data_file);

    for i in  range(1,len(data)):
      #print(data[i])
      if data[i]['stars'] > 3:
        positiveReview.append((data[i]['text'],'positive'))
      elif data[i]['stars'] < 3:
        negativeReview.append((data[i]['text'],'negative'))
      else:
        neutralReview.append((data[i]['text'], 'neutral'))

    #for (words, sentiment) in self.positiveReview + self.negativeReview:
     # wordsFilter = [e.lower() for e in words.split() if len(e) >= 3]
     # self.reviews.append((wordsFilter, sentiment))
   # return self.reviews

#  def getWordsInReview(self, reviewArray):
#    all_words = []
#    for(words, sentiment) in reviewArray:
#      all_words.extend(words)
#    return all_words
#
#  def getWordFeatures(self, listOfWords):
#    listOfWords = nltk.FreqDist(listOfWords)
#    wordFeatures = listOfWords.keys()
#    for i in wordFeatures:
#      print i
#    return wordFeatures
#
#  def extractFeatures(self, document):
#    documentWords = set(document)
#    features = {}
#    for word in wordFeatures:
#      features['contains(%s)' % word] = (word in documentWords)
#    return features
