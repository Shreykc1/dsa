def p(l,k):
    if len(l) <= 1:
        return l
    pivot = l[0]
    
    
    left = [n for n in l if n < pivot]
    middle = [n for n in l if n == pivot]
    right = [n for n in l if n > pivot]
    
    right = middle + right
    
    if len(left) > k:
        return p(left,k)
    else:
        return left + [pivot] + middle + p(right, k-len(left)-len(middle)-1)
        
k = 3
l = [4, 6, 1, 0, 10, -3, 0, 0, 0, -3]
print(f"Output: {p(l, k)[:k]}")
l.sort()
print(f"Expected: {l[:k]}")