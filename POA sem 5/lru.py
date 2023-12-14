def pageFaults(pages_seq, n, C):
    s = set()
    indexes = {}
    faults = 0

    for i in range(n):
        if len(s) < C:
            if pages_seq[i] not in s:
                s.add(pages_seq[i])
                faults += 1
            indexes[pages_seq[i]] = i
        else:
            if pages_seq[i] not in s:
                lru = float('inf')
                for p in s:
                    if indexes[p] < lru:
                        lru = indexes[p]
                        v = p
                s.remove(v)
                s.add(pages_seq[i])
                faults += 1
            indexes[pages_seq[i]] = i
        print('s =', s)

    return faults

pages_seq = [3, 0, 1, 2, 1, 3, 5, 1, 2, 5, 0, 1, 2]
n = len(pages_seq)
C = 3
print('The total number of page faults is: ', pageFaults(pages_seq, n, C))
