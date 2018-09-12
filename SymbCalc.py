#author Denys Lozinskyi
#beta 4

import sys

def symbCalc(text):
    '''
    calculates frequency of character's presence in a text given,
    shows the most frequent characters and number of their presence
    '''
    text = text.lower()
    textTab = {}
    #print(text)
     
    for symbol in text:
        if symbol.isalpha():
            if symbol in textTab:
               keySum = textTab.get(symbol) + 1
               textTab.update({symbol: keySum})
            else:
               textTab.update({symbol: 1})
    
    #print(textTab) #shows based on the text given collections of letters
    #print(len(textTab)) #shows number of those letters present in the text
    '''next conditions are important, because if text contained only punctuation marks, numbers or smiles,
       isalpha will filter them out and dictionary will be empty.
       That in turn will cause an error of max function.
       So we are to check whether the dictionary is empty first, and act correspondingly
    '''
    if len(textTab) <= 0:
        print("Буквы в тексте не обнаружены")

    elif len(textTab) > 0:
        goalKey = max(textTab, key = textTab.get)
        goalVal = textTab[goalKey]
        maxKeysList = []
        for key in textTab:
            if textTab.get(key) == goalVal:
                maxKeysList.append(key)
        maxKeysList.sort()
        print("Буквы: %s встречаются в вашем тексте наиболее часто. Они были встречены %s раз(а)" %(maxKeysList, goalVal))
                #note that in Python 3.6, instead of %s we may use print(f"string {variable1} string {variable2}") formatting method

""" for input I take sys.stdin.read instead of input() to enable the app to work with multipule lines.
    Using sys.stdin.readlines returns a list with inputed lines as its elements.
    Also, it adds \n to every element and calculates them as extra "n"s
    which is unacceptable. Meanwhile .read gives proper effect.
    However, there is a disadventage of using sys.stdin - the neccessity of entering Ctrl-D every time at inputing a text
""" 

print("Введите ваш текст, после чего нажмите Enter и Ctrl-D:")                
text = str(sys.stdin.read())

symbCalc(text)

