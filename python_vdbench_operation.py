#coding=UTF-8
import subprocess
def vdbench_operation(title_name):
# vdbench可执行文件的路径
    vdbench_path =f'bash /root/Data_collection/bash_doucument/get_data_summary.sh {title_name}'
# 使用subprocess.run来运行vdbench命令
# 你可以根据需要捕获输出和错误
    global result
    result = subprocess.run(vdbench_path, shell=True, check=True, text=True, capture_output=True) 

# 打印输出（如果有的话）
    print("vdbench输出:")
    print(result.stdout)

# 打印错误（如果有的话） 
    if result.stderr:
        print("vdbench错误:")
        print(result.stderr)

# 检查返回码以确认是否成功
    if result.returncode == 0:
       
        return "vdbench执行成功"
    else:
        
        return f"vdbench执行失败,返回码: {result.returncode}"
