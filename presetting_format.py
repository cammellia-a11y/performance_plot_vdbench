#coding=utf-8
import subprocess
def part_format():
# 分区设备名
    partition = '/dev/nvme0n1'
# 格式化命令
    format_command = f'nvme format {partition}'  #nvme format 对盘进行格式化 全部erase

    try:
    # 调用系统命令来格式化分区
        subprocess.run(format_command, shell=True, check=True)
        print(f"{partition} 已成功格式化。")
    except subprocess.CalledProcessError as e:
        print(f"格式化分区时发生错误：{e}")