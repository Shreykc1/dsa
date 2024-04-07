def kmp(string,pattern,lps):
    if len(string) < len(pattern):
        return ""
    
    i, j = 0, -1
    
    while i < len(string):
        if string[i] == pattern[j+1]:
            i+=1
            j+=1
        else:
            j = -1 if not lps[j] else lps[j]
            
            if string[i] != pattern[j+1]:
                i+=1
                
        if j == len(pattern)-1:
            return f"match found{i-j-1}"
        if i == len(string):
            return ""      
    
          





def findLPS(pattern):
    chars = set()
    lps = []
    
    for i in pattern:
        if i in chars:
            lps.append(lps[-1]+1)
        else:
            lps.append(0)
        chars.add(i)
    return lps 
            

string = "abc abcdab abcdabcdabde"
pattern = "abcdabd"
lps = findLPS(pattern)
print(kmp(string, pattern, lps))