# SVC-Fusion (Linux Version)

<img src="https://img.picui.cn/free/2025/04/24/6809fe1cf21f3.png" width="250" height="250">

SVC-Fusion Linux版本的整合包，支持启动前端界面。项目是从服务器中提取的，并非原创。


##  项目概述

- **注意**：不含WebUI源码但可启动前端
- **原始项目**：[svcfusion.com](https://www.svcfusion.com/)

##  资源下载

| 资源类型 | 下载链接1 |
|----------|----------|
| Python环境 | [HuggingFace](https://huggingface.co/Kuugo/svc-fusion-linux-model) |
| 预训练模型 | [HuggingFace](https://huggingface.co/Kuugo/svc-fusion-linux-model) |

## 快速开始

1. 克隆本项目：
   ```bash
   git clone https://github.com/Kuugo2002/svc-fusion-linux.git
   ```

2. 下载Python环境和预训练模型，将env.7z解压，放到同一个目录内。

3. 启动项目：
   ```bash
   ./env/bin/python launch.py
   ```
##  通过colab部署
1. 在google drive的根目录创建dataset_raw，dataset_raw，results这三个文件夹
2. 按colab.ipynb运行即可

## 🙏 致谢
- SVC-Fusion 开发团队
