from functools import reduce
from typing import List

def count_was(a, b):
  result: List[str] = str(a).split(' ') + str(b).split(' ')
  for i in result:
    if i == 'was':
      global count
      count += 1
  return count

sentences = ['Nory was a Catholic', 'because her mother was a Catholic', 'and Nory’s mother was a Catholic', 'because her father was a Catholic', 'and her father was a Catholic', 'because his mother was a Catholic', 'or had been']
count = 0
print(reduce(count_was, sentences))