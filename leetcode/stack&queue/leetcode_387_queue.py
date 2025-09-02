from collections import Counter, deque


    
    
def firstUniqChar(s: str) -> int:
    count = Counter(s)
    q = deque()

    for i, c in enumerate(s):
        q.append(i)
        index = q[0]
        char = s[index]
        print(count[char])
        while q and count[char] > 1:
            q.popleft()

    
    return q[0] if q else -1


s = "loveleetcode"
firstUniqChar(s)