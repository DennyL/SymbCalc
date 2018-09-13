#author Denys Lozinskyi
#beta 5

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
        result = ', '.join(maxKeysList)
        """next block serves to provide smart output of SymbCalc due to its Russian interface.
           When SymCalc calculated symbols, it returns the following line:
           "Буквы: foo встречаются в вашем тексте наиболее часто. Они были встречены bar раз(а)".
           The code below authomatically defines in which case we should print "раз" and in which - "раза".
           When we try to figure out in which case we use either of the words, we will notice, that
           in Russian we say "/number/ раза" with all numbers that end with 2, 3 and 4 except 12, 13 and 14.
           In other cases we say "раз".
           Variable "sign" assignes to the last digit of "goalVal" (which is a quantity of repetitions of a letter in a text)
        """
        sign = goalVal % 10 #picking last digit of the number
        if sign in range(2, 5) and goalVal not in range(12, 15):
            ending = "раза"
        else:
            ending = "раз"
        #and forming a smart output message    
        print("Буквы \"%s\" встречаются в вашем тексте наиболее часто.\nОни были встречены %s %s" %(result, goalVal, ending))

""" for input I take sys.stdin.read instead of input() to enable the app to work with multipule lines.
    Using sys.stdin.readlines returns a list with inputed lines as its elements.
    Also, it adds \n to every element and calculates them as extra "n"s
    which is unacceptable. Meanwhile .read gives proper effect.
    However, there is a disadventage of using sys.stdin - the neccessity of entering Ctrl-D every time at inputing a text
""" 

print("Введите ваш текст, после чего нажмите Enter и Ctrl-D:")                
text = str(sys.stdin.read())

symbCalc(text)

