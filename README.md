# xmind_markdown_converter

## English

### prepare your environment

This script can only run when the version of the python you installed is greater than 3.0 (3.7 recommand).

You should install [xmind](https://pypi.org/project/XMind/) before you run it.

### How to use it

Open a terminal, and run command as below:

```shell
python xmind2md.py -source {xmind path} -output {markdown output path}
```

The `output` param is optional. If you don't config it, the output file will be created in the directory that this script lies.

## 中文

### 运行环境的准备

运行在python3环境中，推荐python3.7版本。

在使用这个脚本之前请确保你已经安装了[xmind](https://pypi.org/project/XMind/)。

### 使用方式

打开一个终端，输入命令：

```shell
python xmind2md.py -source {xmind的文件路径} -output {markdown的输出路径}
```

output选项是可选的，如果不填output选项，就会默认输出一个和xmind同名的文件到本脚本所在目录下。
