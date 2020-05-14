
def quick_sort1(l,start,end):
    if start >= end:
        return
    flag=l[start]
    left=start
    right=end

    while left<right:
        while left<right and l[right]>=flag:
            right = right - 1
        l[left]=l[right]

        while left<right and  l[left]<=flag:
            left = left + 1
        l[right] = l[left]
    #l[start] = l[left]
    l[left]=flag
    quick_sort1(l,start,left-1)
    quick_sort1(l,left+1,end)

def swap(l,i,j):
    t=l[i]
    l[i]=l[j]
    l[j]=t
    return l
def quick_sort2(l,start,end):
    if start >= end:
        return
    flag=l[start]
    left=start+1
    right=end
    done=False
    while not done:
        while left<=right and l[left]<=flag:
            left += 1
        while left<=right and l[right]>=flag:
            right -= 1
        if left>right:
            done=True
        else:
            swap(l,right,left)
    swap(l,start,right)
    print(l)
    quick_sort2(l,start,right-1)
    quick_sort2(l,right+1,end)





l=[8,4,6,9,7,2,3,5,64,12,23,54,86,1,2,12]

quick_sort2(l,0,len(l)-1)
print(l)