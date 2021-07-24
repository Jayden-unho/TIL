import sys

number = int(sys.stdin.readline().rstrip())
word_list = []

for _ in range(number):
    word = sys.stdin.readline().rstrip()
    word_list.append((word, len(word)))

word_list = list(set(word_list))

# 알아보기
word_list.sort(key = lambda word: (word[1], word[0]))

for word in word_list:
    print(word[0])