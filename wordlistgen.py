#Script Made By hax / haxer
import itertools
import random

def genWordlist(words, minLen, maxLen, output_file="wordlist.txt"):
    wordList = words.split(";")
    
    wordCombs = []
    for word in wordList:
        wordCombs.append([word.lower(), word.capitalize(), word.upper(), word[::-1].lower(), word[::-1].capitalize(), word[::-1].upper()])
    
    allCombs = set()
    for i in range(1, len(wordList)+1):
        for combo in itertools.combinations(wordList, i):
            for word_combo in itertools.product(*[wordCombs[wordList.index(w)] for w in combo]):
                allCombs.add(''.join(word_combo))
    
    specialChars = ['!', '$', '@', '%']
    
    result = []
    for baseWord in allCombs:
        insertPoses = [0, len(baseWord), random.randint(1, len(baseWord)-1)]
        
        if minLen <= len(baseWord) <= maxLen:
            result.append(baseWord)

        for pos in insertPoses:
            for char in specialChars:
                newWord = baseWord[:pos] + char + baseWord[pos:]
                
                if minLen <= len(newWord) <= maxLen:
                    result.append(newWord)

    with open(output_file, "w") as f:
        for item in result:
            f.write(item + "\n")
    
    global lenRes
    lenRes = len(result)

    return result
    
def totalPass():
    print(f"\n[+] Total Password Created: {lenRes}")
