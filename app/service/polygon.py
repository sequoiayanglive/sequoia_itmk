import pandas as pd
import numpy as np

'''
提取图斑
balltuban 全部数据
item_tuban 图斑 数组
'''
def extract_spot(balltuban, item_tuban, row, col):
    item_tmp_tuban = [row, col]
    item_tuban.append(item_tmp_tuban)
    balltuban[col][row] = -1
    itemArray = []
    if row < len(balltuban) and balltuban[col][row + 1] == 0:
        itemArray.append([col, row + 1])
    if col < 33 and balltuban[col + 1][row] == 0:
        itemArray.append([col + 1, row])
    if col > 1 and balltuban[col - 1][row] == 0:
        itemArray.append([col - 1, row])
    for itemArrayTmp in itemArray:
        extract_spot(balltuban, item_tuban, itemArrayTmp[1], itemArrayTmp[0])


'''
图斑结构 
构建图斑 原始图斑值 只记记录点位 例：[[0, 30], [1, 30], [2, 30], [0, 31], [0, 32], [0, 33]]
转换成 X、Y归零 并且是矩形的图斑
'''
def polygon_shape(p_df_tb):
    # 转换成 dataframe
    dftest = pd.DataFrame(p_df_tb)
    # 计算矩阵大小
    juzhne = dftest.apply(lambda x: x.max() - x.min() + 1, axis=0)
    # 生成 可容纳图斑的 矩阵
    columns = range(0, juzhne[0])
    tmp_tuban = pd.DataFrame(columns=columns)
    lie = range(0, juzhne[1])
    ["no"] = lie
    .fillna(0, inplace=True)
     = .drop("no", axis=1)
    # 每个维度最小值
    min = dftest.apply(lambda x: x.min(), axis=0)
    # 填充图斑
    for i in np.arange(0, len(dftest)):
        row = dftest.iloc[i]
        [row[0] - min[0]][row[1] - min[1]] = 1
    return

# 解析图斑 将图斑数据化 以 01 表示 后续方便 进行图斑对比
def analysis(tb):
    tb = pd.DataFrame(tb)
    x = tb.shape[0]
    y = tb.shape[1]
    posture=[]
    # 姿态1  i=x ; j=y; i+,j+
    for i in range(0,x,1):
        for j in range(0,y,1):
            posture.append(tb[j][i])
    # 姿态2  i=x ; j=y; i+ j-
    for i in range(0,x,1):
        for j in range(y-1,-1,-1):
            posture.append(tb[j][i])
    # 姿态3  i=x ; j=y; i- j+
    for i in range(x-1,-1,-1):
        for j in range(0,y,1):
            posture.append(tb[j][i])
    # 姿态4  i=x ; j=y; i- j-
    for i in range(x-1,-1,-1):
        for j in range(y-1,-1,-1):
            posture.append(tb[j][i])

    # 姿态5  i=y ; j=x; i+ j+
    for j in range(0,y,1):
        for i in range(0,x,1):
            posture.append(tb[j][i])
    # 姿态6  i=y ; j=x; i+ j-
    for j in range(0,y,1):
        for i in range(x-1,-1,-1):
            posture.append(tb[j][i])
    # 姿态7  i=y ; j=x; i- j+
    for j in range(y-1,-1,-1):
        for i in range(0,x,1):
            posture.append(tb[j][i])
    # 姿态8  i=y ; j=x; i- j-
    for j in range(y-1,-1,-1):
        for i in range(x-1,-1,-1):
            posture.append(tb[j][i])
    return posture