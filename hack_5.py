"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    res_list = list(result)
    res_list [1] = '0'
    res_list [2] = '0'
    res_list [4] = '1'
    res_list [6] = '@'
    result = "".join(res_list)
    return result  