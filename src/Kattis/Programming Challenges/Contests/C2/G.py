for _ in range(int(input())):
    wordList = input().split()
    if wordList[0:2] == ['Simon', 'says']: 
        print(' '.join(wordList[2:]))