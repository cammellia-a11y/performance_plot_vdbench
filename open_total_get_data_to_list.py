import re
#打开对应路径的文件----将所需要的数据提取出来

#筛选需要的数据
def get_data():
    global output_file
    output_file='avg_vdbench.txt'

    with open('/root/Data_collection/output/totals.html','r',encoding='utf-8') as f,open(output_file,'a',encoding='utf-8') as outfile:
            for line in f:
                if 'avg' in line:
                    outfile.write(line)
                # elif 'interval' in line:
                #      outfile.write(line)


#将平均数依次写入列表-获取需要参数数值
def get_data_to_lst(argument_string):
    avg_lst=[]
    lst=[]
    string_lst=[]
    latency_lst=[]
    with open('avg_vdbench.txt','r',encoding='utf-8') as infile:
        #导出平均数据到列表中
        for line in infile:
                if 'avg' in line:
                    lst=re.split(r'\s+',line)
                    lst.pop()#删除最后一个空格
                    #直接收集数据
                    if argument_string=='IOPS':
                        string_lst.append(lst[2])#IOPS
                    elif argument_string=='BW':
                        string_lst.append(lst[3])#BW


                    #将收集的几组数据写入同一列表---判断所要收集的数据是哪一个IOPS/BW
                    
                    if argument_string=='IOPS':
                        avg_lst.append(float(lst[2]))#IOPS
                    elif argument_string=='BW':
                        avg_lst.append(float(lst[3]))#BW
                    elif argument_string=='IOPS_latency':
                        avg_lst.append(float(lst[2]))#IOPS
                        latency_lst.append(float(lst[6]))#latency

        #返回所需要的值
        if argument_string=='IOPS':     
            return avg_lst,string_lst
        elif argument_string=='BW':
            return avg_lst,string_lst
        elif argument_string=='IOPS_latency':       
            return avg_lst,latency_lst