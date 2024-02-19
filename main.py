# 这是一个示例 Python 脚本。
import argparse
import requests
import pprint

from utils.get_gpu_properties import get_gpu_properties

parser = argparse.ArgumentParser(
    prog="gpu-specs",
    description="list gpu specs"
)

parser.add_argument("", "--model", action='store', default="GeForce RTX 4090")


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    arg = parser.parse_args()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
