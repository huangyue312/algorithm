def dpcoins(set,change,result={}):
    for c in range(1,change+1):
        m=c
        if c in set:
            result[c]=[c]
        else:
            for ch in [s for s in set if s<=c]:
                if (len(result[c-ch])+1) <= m:
                    result[c]=result[c-ch]+[ch]
                    m=len(result[c-ch])+1
    return result[change]

coinset=[1,5,10]
change=17
result={}
#print result
r=dpcoins(coinset,change,result)
print r