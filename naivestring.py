def findStr(string,pattern):
    if len(string) < len(pattern):
        return "Error String is smaller than Pattern"
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            return f"match found at {i}"
    return "Match not found"
    






string = "shrey"
pattern = "re"

print(findStr(string,pattern))