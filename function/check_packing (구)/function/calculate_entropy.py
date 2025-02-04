import math
from collections import Counter

# 엔트로피 계산 함수
def CalculateEntropy(data):
    if not data:
        return 0
    counter = Counter(data)
    length = len(data)

    entropy = 0
    for count in counter.values():
        entropy -= (count / length) * math.log2(count / length)
    return entropy
