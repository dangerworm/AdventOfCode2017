data = file('day4-data.txt', 'r')
phrases = data.read().split('\n')

validPhrases = 0
for phrase in phrases:
    words = [word.strip() for word in phrase.split()]
    uniqueSet = set(words)
    if len(words) == len(uniqueSet):
        validPhrases += 1

print validPhrases
