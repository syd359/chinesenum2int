
def chineseNumtoInt(strs):
    """
    暂时不支持非法输入的检测
    """
    if strs == "":
        return 0

    # 可以根据需求，添加单位
    unit_dict = {'亿': 100000000, 
                 '万': 10000, 
                 '千': 1000,
                 '百': 100, 
                 '十': 10}
    
    num_dict = {}
    for key, val in zip(list("一二三四五六七八九"), list(range(1,10))):
        num_dict[key] = val
    # 可以自行定义一些有效地数字输入，如 ‘壹’，‘两’
    num_dict['壹'] = 1
    num_dict['两'] = 2
    
    # negative number
    sign = 1
    if strs[0] == '负':
        sign = -1
        strs = strs[1:]
    
    res = 0
    i = 0
    res_stack = []

    while i < len(strs):
        if strs[i] == '零':
            i += 1
            continue
        
        if strs[i] in num_dict:
            res_stack.append(num_dict[strs[i]])
        else:
            num_remain = res_stack.pop(-1)
            num_remain *= unit_dict[strs[i]]
            if res_stack:
                tmp_num = res_stack.pop(-1)
                tmp_num += num_remain
                res_stack.append(tmp_num)
            else:
                res_stack.append(num_remain)
            
        i += 1
    
    if len(res_stack) >= 2:
        num_remain = res_stack.pop(-1)
        num_res = res_stack.pop(-1)
        num_res += num_remain
        res_stack.append(num_res)
        
    return sign * res_stack[0]


print(chineseNumtoInt('三百五十二'))
print(chineseNumtoInt('三百零八'))
print(chineseNumtoInt('二千三百五十二'))
print(chineseNumtoInt('四万二千一百'))
print(chineseNumtoInt('三千五百万亿'))
print(chineseNumtoInt('三千四百万亿零四万二千一百'))

