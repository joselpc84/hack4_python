"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    temp = []
    r = 0
    varLen = len(result)
    while (r < varLen):
        temp.append(result[r])
        temp.append("@")
        r+=1
    result = temp
    return result  