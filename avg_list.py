#coding=utf-8
#将字符串类型转化为浮点类型
def convert_strings_to_floats_preserve(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            try:
                result.append(round(float(item),2)) #类型转换,保留两位小数
            except ValueError:
                # 保留原始字符串
                result.append(item)
        else:
            # 如果元素是浮点数或其他类型，直接添加到结果列表中
            result.append(item)
    return result

#求平均数
def avg(float_lst,n):
    averages = [sum(float_lst[i:i + n]) / n for i in range(0, len(float_lst) - n + 1, n)]

    return averages







