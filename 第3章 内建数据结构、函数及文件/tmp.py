# coding=utf-8
import time
from collections import defaultdict

string = ''
words = string.split(' ')
start = time.time()
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
end = time.time()

print(by_letter)
print('start :', start,
      '\nend :', end)
print("[INFO] runn {:.6f} seconds".format(end - start))
