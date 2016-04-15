
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    midIdx = len(seq)//2
    leftSeq=merge_sort(seq[:midIdx])
    rightSeq = merge_sort(seq[midIdx:])
    return merge(leftSeq,rightSeq)

def merge(lSeq,rSeq):
    result = []
    i = 0
    j = 0
    while i < len(lSeq) and j < len(rSeq):
        if(lSeq[i] < rSeq[j]):
            result.append(lSeq[i])
            i = i + 1
        else:
            result.append(rSeq[j])
            j = j + 1
    if(i == len(lSeq)):
        result = result + rSeq[j:]
    else:
        result = result + lSeq[i:]
    return result

a = merge_sort([3,4,7,1,2,9,4])

b = merge_sort([2,5,9,4,5,2])
#jjj



