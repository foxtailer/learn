key = 8
text = "Husn little baby dont you cry, everything gonna be olright"

def create_array(text, key):
    encript_msg = ""
    result = []
    temp = []

    for i in text:
        temp.append(i)
        if len(temp)==key:
            result.append(temp)
            temp = []
    if len(temp)>0:
        for i in range(key-len(temp)):
            temp.append("")
        result.append(temp)
    
    for i in range(key):
        for j in  range(len(result)):
            encript_msg += result[j][i]
    return encript_msg

 

print(create_array(text, key))
