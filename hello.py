# 1. study the example given at
# https://support.smartbear.com/articles/testcomplete/unit-testing/

# 2. Select a unit testing framework and its programming language
# (can�t select visual studio and can�t select C#).

# 3. Implement the class NameExtractor, and its members
# ExtractWords, FindTitle, FindSuffix, ParseName,  in the language you select in (2).

# 4. You need to submit a document file (.doc or .pdf)  that contains the following:

# a. a short introduction

# b. a screenshot of your IDE (integrated development environment) with
# your project folder or files.

# c. a list of your source code

# version 1 blueprint
# version 2 it works now!
import re
#re lets us split the string according to the list containing [',', '.', ':', '\t']


class NameExtractor():
    # not sure what to put in constructor
    def __init__(self, mFullName):
        self.mFullName = mFullName
        self.mTitle = ""
        self.mFirstName = ""
        self.mMiddleName = ""
        self.mLastName = ""
        self.mSuffix = ""
        self.NumWords = 0
        self.mWords = []
        self.ParseName()

    def ExtractWords(self):
        words = re.split(r'[, . : \t]', self.mFullName)
        # splits the string if there are the characters in the array
        # ex: hey:man:do:you:,run:.    fly
        # result: hey man do you "" run "" fly

        print("Words litst:")
        print(words)  # check if it works

        words1 = []

        for i in range(0, len(words)):
            # only put strings in words that are not empty
            # result: hey man do you run fly
            # notice "" is missing
            if (words[i] != ""):
                words1.append(words[i])

        print("Words1 litst:")
        print(words1)  # check if it works

        # print (words1)

        self.mWords = words1

        print("mWords list:")
        print(self.mWords)

    def FindTitle(self):


        if (len(self.mWords) != 0):
            titlelist = ["Professor", "Student", "Mr", "Mrs", "Miss", "Dr", "Captain", "Lt",
                         "General", "President"]

            if self.mWords[0] in titlelist:
                self.mTitle = self.mWords[0]
                return True
            else:
                return False
        else:
            return False

    def FindSuffix(self):

        suffixlist = ["Jr", "Sr", "LOB", "PhD", "MD", "MBA", "QA"]
        if len(self.mWords) == 5:
            self.mSuffix = self.mWords[4]
            return True
        elif len(self.mWords) == 3 and self.mWords[2] in suffixlist:
            self.mSuffix = self.mWords[2]
            return True
        elif len(self.mWords) == 4 and self.mWords[3] in suffixlist:
            self.mSuffix = self.mWords[3]
            return True
        return False

    def FindFirstName(self):
        if len(self.mWords) >= 2 and self.mTitle == "":
            self.mFirstName = self.mWords[0]
            return True
        elif len(self.mWords) > 2 and self.mTitle != "":
            self.mFirstName = self.mWords[1]
            return True
        elif len(self.mWords) == 5:
            self.mFirstName = self.mWords[1]
            return True
        return False

    def FindMiddleName(self):
        if len(self.mWords) == 5:
            self.mMiddleName = self.mWords[2]
            return True
        elif len(self.mWords) == 4 and self.mSuffix == "":
            self.mMiddleName = self.mWords[2]
            return True
        elif len(self.mWords) == 4 and self.mWords == "":
            self.mMiddleName = self.mWords[1]
            return True
        elif len(self.mWords) == 4 and self.mSuffix == "":
            self.mMiddleName = self.mWords[1]
            return True
        elif len(self.mWords) == 3 and self.mSuffix == "" and self.mTitle == "":
            self.mMiddleName = self.mWords[1]
            return True
        return False

    # will fix the rest of these functions to be like the two above
    def FindLastName(self):
        if len(self.mWords) == 1:
            self.mLastName = self.mWords[0]
            return True
        elif len(self.mWords) == 2:
            self.mLastName = self.mWords[1]
            return True
        elif len(self.mWords) == 5:
            self.mLastName = self.mWords[3]
            return True
        elif len(self.mWords) == 3 and self.mSuffix == "":
            self.mLastName = self.mWords[2]
            return True
        elif len(self.mWords) == 4 and self.mSuffix == "":
            self.mLastName = self.mWords[2]
            return True
        elif len(self.mWords) == 3:
            self.mLastName = self.mWords[1]
            return True
        elif len(self.mWords) == 4:
            self.mLastName = self.mWords[3]



    def ParseName(self):
        mTitle = ""
        mFirstName = ""
        mMiddleName = ""
        mLastName = ""
        mSuffix = ""

        if (self.mFullName != None):
            self.ExtractWords()
            self.FindTitle()
            self.FindSuffix()
            self.FindLastName()
            self.FindFirstName()
            self.FindMiddleName()


#Assign4 = NameExtractor("Dr Steven Van Kha Jr")
#Assign4.ParseName()
#print(Assign4.FindTitle())
#print(Assign4.FindFirstName())
#print(Assign4.FindMiddleName())
#print(Assign4.FindLastName())
#print(Assign4.FindSuffix())
# def ParseName(self):

