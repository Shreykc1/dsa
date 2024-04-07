def check(s1,s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True
    
    
    
def find(string,pattern):
    if len(string) < len(pattern):
        return ""
    
    psum = sum([ord(char) for char in pattern])
    csum = sum([ord(char) for char in string[0 : len(pattern)]])
    
    for i in range(0,len(string)-len(pattern)+1):
        if i!=0:
            csum = csum + ord(string[i+len(pattern)-1])
            
        current = string[i: i+len(pattern)]
        
        if psum == csum:
            if check(current,pattern):
                return f"found {i}"
        csum = csum - ord(string[i])
    return "match not found"
    

string = "racecar"
pattern = "car"
print(find(string, pattern))