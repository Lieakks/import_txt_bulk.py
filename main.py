# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def serial_data_read(name):
    import serial
    import time
    import chardet

    ser = serial.Serial('COM7', 9600, timeout=0.5) # 打开串口

    # 读取串口数据
    a = ser.read

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    serial_data_read('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
