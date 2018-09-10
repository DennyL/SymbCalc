#author Denys Lozinskyi
#beta 1

def symbCalc(text):
    '''
    calculates frequency of character's presence in a text given,
    shows the most frequent characters and number of their presence
    '''

    textTab = {} #creating a dictionary that's to store characters of the text as keys and their appearance in the text as values
    val = 0 #start for value of the first pair of our dictionary
    #text = text.replace(' ', '') #deleting all whitespaces in the text
    
    for symbol in text: #updating dictionary with a new pair, calculating values
        if symbol.isalpha() == True: #making sure we are dealing with a letter, not whitespace or a punctuation mark
            if symbol in textTab:
               keySum = textTab.get(symbol) + 1
               textTab.update({symbol: keySum})
            else:
               textTab.update({symbol: val + 1})
    goalKey = max(textTab, key = textTab.get) #identifying a key containing the max value
    goalVal = textTab[goalKey] #identifying value of the key. This value is the biggest in our dictionary

    #now, initiating search over dictionary values to find out if there are keys with same value
    maxKeysList = [] #creating a list that's to contain keys with value equal to goalVal, which is a max value in the dictionary
    for key in textTab: #initiating search over our dictionary
        if textTab.get(key) == goalVal: #in case key containing value equal to max is found,
            maxKeysList.append(key) #adding it to the list
    maxKeysList.sort() #sorting the list in alphabetical order
    
    print(f"Буквы: {maxKeysList} встречаются в вашем тексте наиболее часто. Они были встречены " + str(goalVal) + " раз каждый")
    #in Python 3.6, instead of %s we use print(f"string {variable_name}") formatting method

text = str(input("Введите ваш текст: "))

symbCalc(text)
