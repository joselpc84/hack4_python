"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    list_res = list(result.upper())
    list_res[1] = '0'
    list_res[2] = '0'
    list_res[4] = '1'
    list_res[6] = '@'
    result = list_res
    return result  