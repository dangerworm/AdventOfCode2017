data = file('day4-data.txt', 'r')
phrases = data.read().split('\n')

validPhrases = 0
for phrase in phrases:
    words = []
    for word in phrase.split():
        letters = list(word)
        letters.sort()
        words.append(''.join(letters))

    uniqueSet = set(words)
    if len(words) == len(uniqueSet):
        validPhrases += 1
        print 'Valid:', words
    else:
        print 'Invalid:', words

print validPhrases
