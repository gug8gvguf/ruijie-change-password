import ctypes
import sys
import hashlib

def str_to_md5(input_str):
    """将字符串转换为 MD5 字符串"""
    # 1. 编码：将字符串转为 UTF-8 字节流（MD5 处理字节而非字符）
    byte_data = input_str.encode('utf-8')
    # 2. 计算哈希：使用 MD5 算法
    md5_obj = hashlib.md5(byte_data)
    # 3. 输出：转为 32 位十六进制字符串
    return md5_obj.hexdigest()








# 检查是否以管理员身份运行
if not ctypes.windll.shell32.IsUserAnAdmin():
    # 重新以管理员身份启动脚本
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    sys.exit()


file_path = "C:\\Program Files\\RCC_ClassManager\\mgr.txt"
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str_to_md5(input('你想改的密码：')))
    print("文件创建成功")
except Exception as e:
    print(f"错误：{e}")
