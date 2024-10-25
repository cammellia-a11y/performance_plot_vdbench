def copy():
    output_file='backop_copy.txt'
    with open('/root/output/summary.html','r',encoding='utf-8') as f,open(output_file,'a',encoding='utf-8') as outfile:
        for line in f:
            if 'interval' in line:

                outfile.write(line)
            elif '.00' in line:
                outfile.write(line)

# import shutil  
  
# # 源文件路径  
# src = '/root/output/summary.html'  
# # 目标文件路径（包括文件名）  
# dst = '/root/backup copy'  
  
# # 复制文件  
# try:  
#     shutil.copy(src, dst)  
#     print(f"文件 {src} 已成功复制到 {dst}")  
# except IOError as e:  
#     print(f"无法复制文件: {e}")  
# except:  
#     print("发生了一个错误")