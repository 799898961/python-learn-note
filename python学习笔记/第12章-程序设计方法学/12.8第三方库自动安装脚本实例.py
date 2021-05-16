# 12.8第三方库自动安装脚本实例.py

import os


libs = {
    "numpy","matplotlib","pandas","scipy","pillow","wheel","sklearn","requests","jieba",
    "werobot","networks","sympy","pyinstaller","django","beautifulsoup4","flask","pyqt5",
    "pyopengl","pypdf2","docopt","pygame","wordcloud",'openpyxl',"pyqt4",
}
tuna = "https://pypi.tuna.tsinghua.edu.cn/simple "

for lib in libs:
     os.system("pip install -i " + tuna + lib)
print("successful")

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 
