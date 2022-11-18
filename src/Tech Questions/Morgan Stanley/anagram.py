def solution(words):
    # Dict of letter occurrences for each word
    letters = dict()
    for idx, word in enumerate(words):
        d = dict()
        for c in word:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        letters[d] = idx

    # O(n^2)
    anagrams = list()
    for _, v in letters.items():
        anagrams.append(v)
    return anagrams
    usedWords = list()
    for i in range(len(letters) - 1):
        if i in usedWords:
            continue
        else:
            usedWords.append(i)
        temp = list()
        temp.append(words[i])
        for j in range(i + 1, len(letters)):
            if j in usedWords:
                continue
            isAnagram = True
            for k, v in letters[i].items():
                if k in letters[j]:
                    if v != letters[j][k]:
                        isAnagram = False
                        break
                else:
                    isAnagram = False
                    break
            if isAnagram:
                temp.append(words[j])
        anagrams.append(temp)
    return anagrams

# words [abc, sss, acb, acb, cba]
# anagrams = [[abc, acb, cba]]


def main():
    print(solution(["abc", "sss", "acb", "acb", "cba"]))


if __name__ == '__main__':
    main()
