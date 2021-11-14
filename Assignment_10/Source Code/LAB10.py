########################################################################
##
## CS 101 Lab
## Program # 10
## Name:Austin Souphanh
## Email: ajs2dz@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import operator
from string import punctuation

while True:
    filename = input("Enter the name of the file to open ")
    try:
        with open(filename) as file:
            """
            Creating an empty dictionary.
            this dict will hold each unique word as key
            and its occurrence as value.
            """
            word_dict = dict()
            for line in file:
                for word in line.strip().split(" "):
                    word = word.strip(punctuation)
                    if len(word) <= 3:
                        continue
                    else:
                        if word in word_dict.keys():
                            word_dict[word] = word_dict[word] + 1
                        else:
                            word_dict[word] = 1


            word_dict = dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))

            counter = 1
            print("Most frequently used words")
            print("{:>0}{:>15}{:>15}".format('#', 'Word', 'Freq.'))
            print("{:>15}".format("==============================="))
            for key in word_dict:
                if counter > 10:
                    break
                else:
                    frequency = word_dict[key]
                    print("{:>0}{:>15}{:>15}".format(counter, key, frequency))
                    counter += 1

            onceCounter = 0
            for key in word_dict:
                if word_dict[key] == 1:
                    onceCounter += 1

            uniqueCounter = len(word_dict)
            print(f"There are {onceCounter} words that occur only once")
            print(f"There are {uniqueCounter} unique words in the document")

    except:
        print("Could not open file",filename)
        print("Please Try Again\n")
        continue
    else:
        break
