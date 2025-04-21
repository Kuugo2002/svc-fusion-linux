import os
os.environ["SHARE"] = "True"
if __name__ == "__main__":
    # 从文件workdir 中读取启动器工作目录
    try:
        with open("workdir", encoding="utf-8") as f:
            workdir = f.read().strip()
    except UnicodeDecodeError:
        with open("workdir", encoding="gbk") as f:
            workdir = f.read().strip()
    print("启动器工作目录: ", workdir)
    os.chdir(workdir)
    import webui

    # dist.launch_dialog()
