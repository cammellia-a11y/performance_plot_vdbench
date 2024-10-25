#coding=utf-8
'''
更改配置文件中参数的数值
'''
import re
#X
def into_X_argument():
        X_argument_range=input('请输入主参数和范围：')
        X_argument_range_lst=re.split(',', X_argument_range)  #将导入的数据分隔开并写入列表
        #类型转换
        for i in range(1,len(X_argument_range_lst)):
            try:
                X_argument_range_lst[i] = int(X_argument_range_lst[i])
            except ValueError:  #避免出现非数字
                    pass
            
        X_argument=X_argument_range_lst[0] #参数
        X_range=X_argument_range_lst[1:]   #参数范围
        return X_argument,X_range

#Y
def into_Y_argument():
        Y_argument_range=input('请输入次参数和范围：')
        Y_argument_range_lst=re.split(',', Y_argument_range)  #将导入的数据分隔开并写入列表
        #类型转换
        #类型转换
        for i in range(1,len(Y_argument_range_lst)):
            try:
                Y_argument_range_lst[i] = int(Y_argument_range_lst[i])
            except ValueError:  #避免出现非数字
                    pass

        Y_argument=Y_argument_range_lst[0]
        Y_range=Y_argument_range_lst[1:]
        return Y_argument,Y_range


#替换参数数值
def alter_argument(argument,range_lst,num,config_path):

#设置替换与被替换变量
    search_value = f'{argument}={range_lst[num]}'
    if num!=len(range_lst)-1:
        replace_value =f'{argument}={range_lst[num+1]}'
    elif num==len(range_lst)-1:
        replace_value=f'{argument}={range_lst[0]}'

#创建中间值
    mod_lines=[]
#读文件并将变量进行替换
    with open(config_path,'r',encoding='utf-8') as f:
        for line in f:
            if search_value in line:
               line=line.replace(search_value,replace_value)
            mod_lines.append(line)
        print(mod_lines)
    with open(config_path,'w',encoding='utf-8') as f:
            f.writelines(mod_lines)

