def recdc(coinset,change,result):
    min=change
    if change in coinset:
        result[change]=[change]
        print change, result[change]
        return result[change]
    elif change in result.keys():
        print change, result[change]
        return result[change]
    else:
        for c in [ch for ch in coinset if ch <change ]:
            #print [ch for ch in coinset if ch <change]
            #result[change-c]=recdc(coinset,change-c,result)
            num=len(recdc(coinset,change-c,result))+1
            if num<=min:
                min=num
                result[change] = recdc(coinset,change-c,result)+ [c]
        print change, result[change]
        return result[change]


coinset=[1,5,10]
change=2
result={}
#print result
r=recdc(coinset,change,result)
print r