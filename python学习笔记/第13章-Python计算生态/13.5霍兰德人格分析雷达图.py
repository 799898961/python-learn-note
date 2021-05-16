# 13.5霍兰德人格分析雷达图.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "SimHei"
radar_labels = np.array(
    [
        "研究型(I)","艺术型(A)","社会型(S)",
        "企业型(E)","常规型(C)","现实型(B)"
    ]
)
data = np.array(
    [
        [0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
        [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
        [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
        [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
        [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
        [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]
    ]
)# 数据值


data_label = ("艺术家","实验员","工程师","推销员","社会工作者","记事员")
angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles,data,"o-", linewidth=1, alpha=0.2)
plt.fill(angles,data, alpha=0.25)
plt.thetagrids(angles*180/np.pi, radar_labels, frac=1.2)
plt.figtext(0.52, 0.95, "霍兰德人格分析", ha="center", size=20)
legend = plt.legend(data_label, loc=(0.94,0.80), labelspacing=0.1)
plt.setp(legend.get_texts(), fontsize="large")
plt.grid(True)
plt.savefig("holland_radar.jpg")
plt.show()


# 问题分析：
# 霍兰德认为：人格兴趣与职业之间应存在一种内在的关系
# 人格分类:
# 研究型、艺术型、社会型、企业型、传统型、现实型
# 职业：
# 工程师、实验员、艺术家、推销员、记事员、社会工作者
# 需求：雷达图方式验证霍兰德人格分析
# 输入：各职业人群结合兴趣的调研数据
# 输出：雷达图

# 通用雷达图绘制：matplotlib库
# 专业的多维数据表示：numpy库
