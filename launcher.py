import os
os.environ["SHARE"] = "True"

def get_current_script_directory():
    """
    获取当前运行程序所在的文件夹路径。
    """
    # 获取当前脚本的绝对路径，并提取所在文件夹路径
    return os.path.dirname(os.path.abspath(__file__))

def write_path_to_file(file_name, path):
    """
    将路径写入指定文件。

    :param file_name: 要写入的文件名
    :param path: 要写入的路径
    """
    try:
        # 打开文件并写入路径
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(path)
        print(f"文件夹路径已成功写入到文件：{os.path.join(os.getcwd(), file_name)}")
    except Exception as e:
        print(f"写入文件失败：{e}")

if __name__ == "__main__":
    # 获取当前运行程序所在的文件夹路径
    current_directory = get_current_script_directory()
    # 定义要写入的文件名
    file_name = "workdir"
    # 将文件夹路径写入文件
    write_path_to_file(file_name, current_directory)
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
