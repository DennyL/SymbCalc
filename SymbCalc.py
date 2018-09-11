#author Denys Lozinskyi
#beta 2

def symbCalc(text):
    '''
    calculates frequency of character's presence in a text given,
    shows the most frequent characters and number of their presence
    '''
    text = text.lower()
    textTab = {}
    val = 0  
    for symbol in text:
        if symbol.isalpha():
            if symbol in textTab:
               keySum = textTab.get(symbol) + 1
               textTab.update({symbol: keySum})
            else:
               textTab.update({symbol: val + 1})
    #print(len(textTab)) #shows number of those letters present in the text
    '''next conditions are important, because if text contained only punctuation marks, numbers or smiles,
       isalpha will filter them out and dictionary will be empty.
       That in turn will cause an error of max function.
       So we are to check whether the dictionary is empty first, and act accordingly
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
        print(f"Буквы: {maxKeysList} встречаются в вашем тексте наиболее часто. Они были встречены {goalVal} раз(а)")
                #in Python 3.6, instead of %s we use print(f"string {variable1} string {variable2}") formatting method
                
text = str(input("Введите ваш текст:\n"))

symbCalc(text)

