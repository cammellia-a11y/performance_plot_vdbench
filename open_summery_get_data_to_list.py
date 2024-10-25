                       
'''
一次运行提取打点时间的数据

'''

# coding=utf-8
import re



def dot_get_data(title_name,input_file):
    global output_file
    output_file =f'/root/Data_collection/all_data_txt/{title_name}.txt'
    # 打开文件并将文件中需要的数据写入新的文本中
    with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'w',encoding='utf-8') as outfile:
        for line in f:
            if '.00 ' in line:
                outfile.write(line)

def dot_get_data_to_lst(title_name):
    summery_lst = []
    lst = []
    output_file =f'/root/Data_collection/all_data_txt/{title_name}.txt'
    with open(output_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            if 'avg' not in line:
                lst = re.split(r'\s+', line)
                lst.pop()  # 删除最后一个空格
                summery_lst.append(lst)

        return summery_lst
        
        
# 导出需求数据---interval,IOPS,BW
def IOPS_BW_data(argument_string,title_name):
    all_data = dot_get_data_to_lst(title_name)
    #time_lst=['10','20','30','40','50','60']
    #收集列表
    IOPS_lst=[]
    BW_lst=[]
    #提取所需要的数值
    for line in all_data:
        IOPS_lst.append(float(line[2])) #字符串转化为浮点类型
        BW_lst.append(float(line[3]))

    #导出所需要的数据
    if argument_string=='IOPS':
        return IOPS_lst
        
    elif argument_string=='BW':
        return BW_lst











