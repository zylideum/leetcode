from collections import defaultdict
from collections import Counter
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anaMap = defaultdict(list)

res = defaultdict(list)
for word in strs:
    print(Counter(word))
    res[frozenset(Counter(word))].append(word)

print(list(res.values()))
