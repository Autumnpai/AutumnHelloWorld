import wordcloud
# import numpy as np
from matplotlib import pyplot as plt
# from IPython.display import display
# import fileupload
# import io
# import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just", "in"]

    # LEARNER CODE START HERE
    # define the variable
    result = {}
    text = file_contents.split()
    for word in text:
        if word in uninteresting_words or not word.isalpha():
            pass
        else:
            if word not in result.keys():
                result[word] = 1
            else:
                result[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()


# Display your wordcloud image


text_my = open("Pride_and_Prejudice.txt", "r", encoding='UTF-8')
file_contents = text_my.read()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
