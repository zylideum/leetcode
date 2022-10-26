
def sd():
    strs = ['flow', 'flower', 'flight']

    res = []
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return ''.join(res)
        res.append(strs[0][i])
    return ''.join(res)

print(sd())