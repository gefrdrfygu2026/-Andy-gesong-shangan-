# hello.py
# 课程 9《大数据与人工智能》作业 0
# 环境验证脚本：验证 Python 3.12 与本仓库正常工作

import sys
import platform


def main():
    print("=" * 52)
    print("  课程 9 - 大数据与人工智能 - 作业 0")
    print("  环境验证脚本")
    print("=" * 52)
    print()
    print("你好，世界！Hello from 个人课程9大数据与人工智能0")
    print()
    print("【当前环境信息】")
    print(f"  Python 版本：{sys.version.split()[0]}")
    print(f"  操作系统  ：{platform.system()} {platform.release()}")
    print(f"  Python 路径：{sys.executable}")
    print()
    print("✓ 环境验证通过，可以开始学习大数据与人工智能啦！")


if __name__ == "__main__":
    main()
