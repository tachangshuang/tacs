"""1、数组长度不能为零2、数组长度相同3、数组进行sort排序4、c = set(a).intersection(set(b))  # 交集    //c = set(a).union(set(b))  # 并集5、a.len == c.len"""def CompareArray(x, y):    a = x    b = y    if len(a) > 0 and len(b) > 0:        heji = set(a).union(set(b))        if len(heji) == len(a) and len(heji) == len(b):            # print(heji)            print("数组相等 ")        else:            print("数组不相等")    else:        print("数组不相等")# 测试思路a = []b = []c = 'x'd = [1]e = [1, 2]f = [2, 1]g = [2, 1]a.sort()b.sort()CompareArray(a, b)  # 两个空数组判断CompareArray(a, c)  # 空数组和非数组判断CompareArray(c, a)  # 非数组和空数组判断CompareArray(a, d)  # 空数组和正常数组判断CompareArray(c, d)  # 非数组和正常数组判断CompareArray(d, c)  # 正常数组和非数组判断CompareArray(d, e)  # d数组属于e数组判断CompareArray(e, d)  # e数组包含d数组判断CompareArray(e, f)  # e f顺序不同判断CompareArray(f, g)  # f g顺序相同判断