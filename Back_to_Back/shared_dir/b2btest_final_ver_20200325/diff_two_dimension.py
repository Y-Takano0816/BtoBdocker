# ver1はtwist_filterとpure_pursuitの出力結果を荷とまとめにしてepsファイルに保存する
# 1つのウィンドウに4分割で表示され、eps形式で保存される

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt        ### グラフ描くなら2D3D関係なく必要
from mpl_toolkits.mplot3d import Axes3D      ### 3Dなら必要
from matplotlib import pyplot
# from scipy import genfromtxt


# result_path = '/home/azumilab/autoware.ai'

# df = pd.read_csv('result/twist_cmd_test')
# print(df)

'''CSVファイルの読み込み'''
# この方式header=Noneで読み込まないと、1行目のデータがヘッダとして読み込まれてしまう
csvdata = pd.read_csv("/media/azumilab/C240-EE9F/moriyama_rosbugs/ResultSimulink2015ROSBAG/Autoware/result_2.0_twist_ful/twist_cmd", header=None, skiprows=1, usecols=[4, 5, 6, 7, 8, 9]) # 1行目はcsv形式ではないのでスキップする。1-4列目はパラメータではないのでこれもスキップする。行列の番号は0から数えることに注意
csvdata2 = pd.read_csv("/media/azumilab/C240-EE9F/moriyama_rosbugs/ResultSimulink2015ROSBAG/Simulink/result_2.0_twist_ful/twist_cmd", header=None, skiprows=1, usecols=[4, 5, 6, 7, 8, 9])

csvdata3 = pd.read_csv("/media/azumilab/C240-EE9F/moriyama_rosbugs/ResultSimulink2015ROSBAG/Autoware/result_2.0_pure_ful/twist_raw", header=None, skiprows=1, usecols=[4, 5, 6, 7, 8, 9])
csvdata4 = pd.read_csv("/media/azumilab/C240-EE9F/moriyama_rosbugs/ResultSimulink2015ROSBAG/Simulink/result_2.0_pure_ful/twist_raw", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
csvdata5 = pd.read_csv("/media/azumilab/C240-EE9F/moriyama_rosbugs/ResultSimulink2015ROSBAG/Simulink/result_2.0_pure_ful/twist_raw", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# CSVの行数を少ない方に揃える
csv_row = len(csvdata)
csv2_row = len(csvdata2)
row_diff = abs(csv_row - csv2_row) #行数の差分
csv3_row = len(csvdata3)
csv4_row = len(csvdata4)
row34_diff = abs(csv3_row - csv4_row) #行数の差分
# print(row_diff)
# print(csvdata)
# print(csvdata2)

if csv_row > csv2_row:
	for i in range(row_diff):
	    csvdata = csvdata.drop(csv_row-i-1, axis=0) #delete_row
	print(csvdata)
	print(csv_row)
elif csv_row < csv2_row:
    for i in range(row_diff):
        csvdata2 = csvdata2.drop(csv2_row-i-1, axis=0) #delete_row
    print(csvdata2)
else:
    pass #行数が一緒だったら何もしない


if csv3_row > csv4_row:
    for i in range(row34_diff):
        csvdata3 = csvdata3.drop(csv3_row-i-1, axis=0) #delete_row
    print(csvdata3)
    print(csv3_row)
elif csv3_row < csv4_row:
    for i in range(row34_diff):
        csvdata4 = csvdata4.drop(csv4_row-i-1, axis=0) #delete_row
    print(csvdata4)
else:
    pass #行数が一緒だったら何もしない

'''CSVから読んだデータをnumpyの行列に入れる'''
myarray     = np.array
myarray2    = np.array
myarray     = csvdata.values
myarray2    = csvdata2.values
# print(myarray)
# print(myarray2)

myarray3    = np.array
myarray4    = np.array
myarray3    = csvdata3.values
myarray4    = csvdata4.values
# print(myarray3)
# print(myarray4)


# '''行列のひき算'''
result = myarray - myarray2
# print(result)

result2 = myarray3 - myarray4
# print(result2)

# '''結果の行列をCSVファイルに書き出し'''
with open("result_twist_filter_simulink_full/twist_cmd_diff.csv", "w") as f1:
    csv1_w = csv.writer(f1, lineterminator='\n')
    csv1_w.writerows(result)
with open("result_pure_pursuit_simulink/twist_raw_diff.csv", "w") as f2:
    csv2_w = csv.writer(f2, lineterminator='\n')
    csv2_w.writerows(result2)


'''グラフ出力'''
# 3Dでプロット
# fig = plt.figure(figsize=(20, 11))
fig = plt.figure(figsize=(26, 16))
# ax = Axes3D(fig)

# (x, y, z) twist_filter
lx1 = csvdata[4].values #field.twist.linear.x　元にする.bagファイルの出力トピック
# ly1 = csvdata[5].values #field.twist.linear.y
# lz1 = csvdata[6].values #field.twist.linear.z
lx2 = csvdata2[4].values #field.twist.linear.x　テスト対象の出力トピック
# ly2 = csvdata2[5].values #field.twist.linear.y
# lz2 = csvdata2[6].values #field.twist.linear.z

# ax1 = csvdata[7].values #field.twist.angular.x　元にする.bagファイルの出力トピック
# ay1 = csvdata[8].values #field.twist.angular.y
az1 = csvdata[9].values #field.twist.angular.z
# ax2 = csvdata2[7].values #field.twist.angular.x　テスト対象の出力トピック
# ay2 = csvdata2[8].values #field.twist.angular.y
az2 = csvdata2[9].values #field.twist.angular.z


# (x, y, z) pure_pursuit
lx3 = csvdata3[4].values #field.twist.linear.x　元にする.bagファイルの出力トピック
# ly3 = csvdata3[5].values #field.twist.linear.y
# lz3 = csvdata3[6].values #field.twist.linear.z
lx4 = csvdata4[4].values #field.twist.linear.x　テスト対象の出力トピック
# ly4 = csvdata4[5].values #field.twist.linear.y
# lz4 = csvdata4[6].values #field.twist.linear.z
lx5 = csvdata5[4].values
# ax3 = csvdata3[7].values #field.twist.angular.x　元にする.bagファイルの出力トピック
# ay3 = csvdata3[8].values #field.twist.angular.y
az3 = csvdata3[9].values #field.twist.angular.z
# ax4 = csvdata4[7].values #field.twist.angular.x　テスト対象の出力トピック
# ay4 = csvdata4[8].values #field.twist.angular.y
az4 = csvdata4[9].values #field.twist.angular.z
az5 = csvdata5[9].values #field.twist.angular.z


ax = fig.add_subplot(221) # 全体を1x2に分割し、1枚目に描写
# ax.subplot(1,2,1)　#(縦分割数、横分割数、ポジション)
# ax.plot(x='time', y=['value1','value2'], subplots=True, layout=(1,2)) #1行2列に分割してプロット
# 軸ラベル
ax.set_xlabel("index number", fontsize=25)
ax.set_ylabel("field.twist.linear.x", fontsize=25)
# ax.set_zlabel("field.twist.linear.z")
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(range(0,len(csvdata)), lx1, linewidth = 2, label='Autoware Node', color='black')
ax.plot(range(0,len(csvdata)), lx2, linewidth = 2, linestyle = ":", label="Simulink_Model", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.6), loc='upper right', borderaxespad=0, fontsize=25) #凡例（label='Node'など）を表示
# ax.subplot(1,2,2)
plt.title("twist_cmd_diff_field_twist_linear_x(twist_filter)", fontsize=25) #, fontsize=22)
plt.tick_params(labelsize=20)

ax = fig.add_subplot(222) # 全体を1x2に分割し、2枚目に描写
# 軸ラベル
ax.set_xlabel("index number", fontsize=25)
ax.set_ylabel("field.twist.angular.z", fontsize=25)
# ax.set_zlabel("field.twist.angular.z")
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(range(0,len(csvdata)), az1, linewidth = 2, label="Autoware Node", color='black')
ax.plot(range(0,len(csvdata)), az2, linewidth = 2, linestyle = ":", label="Simulink_Model", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.6), loc='upper right', borderaxespad=0, fontsize=25) #凡例（label='Node'など）を表示
plt.title("twist_cmd_diff_field_twist_angular_z(twist_filter)", fontsize=25) #, fontsize=22)
plt.tick_params(labelsize=20)

ax = fig.add_subplot(223) # 全体を1x2に分割し、3枚目に描写
# ax.subplot(1,2,1)　#(縦分割数、横分割数、ポジション)
# ax.plot(x='time', y=['value1','value2'], subplots=True, layout=(1,2)) #1行2列に分割してプロット
# 軸ラベル
ax.set_xlabel("index number", fontsize=25)
ax.set_ylabel("field.twist.linear.x", fontsize=25)
# ax.set_zlabel("field.twist.linear.z")
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(range(0,len(csvdata3)), lx3, linewidth = 2, label="Autoware Node", color='black')
ax.plot(range(0,len(csvdata3)), lx4, linewidth = 2, linestyle = ":", label="Simulink_Model", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.6), loc='upper right', borderaxespad=0, fontsize=25) #凡例（label='Node'など）を表示
# ax.subplot(1,2,2)
plt.title("twist_raw_diff_field_twist_linear_x(pure_pursuit)", fontsize=25) #, fontsize=22)
plt.tick_params(labelsize=20)

ax = fig.add_subplot(224) # 全体を1x2に分割し、4枚目に描写
# 軸ラベル
ax.set_xlabel("index number", fontsize=25)
ax.set_ylabel("field.twist.angular.z", fontsize=25)
# ax.set_zlabel("field.twist.angular.z")
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(range(0,len(csvdata3)), az3, linewidth = 2, label="Autoware Node", color='black')
ax.plot(range(0,len(csvdata3)), az4, linewidth = 2, linestyle = ":", label="Simulink_Model", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.6), loc='upper right', borderaxespad=0, fontsize=25) #凡例（label='Node'など）を表示
plt.title("twist_raw_diff_field_twist_angular_z(pure_pursuit)", fontsize=25) #, fontsize=22)
plt.tick_params(labelsize=20)
# plt.gcf().text(0.48,0.48,"twist_filter(twist_cmd)", backgroundcolor='yellow')
# plt.gcf().text(0.48,0.08,"pure_pursuit(twist_raw)", backgroundcolor='yellow')


# ax = fig.add_subplot(325)
# ax.set_xlabel("index number")
# ax.set_ylabel("field.twist.linear.x")
# ax.plot(range(0,len(csvdata5)), lx5, label="Simulink_Model", color='orange')
# ax.grid(True)
# ax.legend() #凡例（label='Node'など）を表示
# plt.title("twist_raw_diff_field_twist_linear_x") #, fontsize=22)
# ax = fig.add_subplot(326)
# ax.set_xlabel("index number")
# ax.set_ylabel("field.twist_angular_z")
# ax.plot(range(0,len(csvdata5)), az5, label="Simulink_Model", color='orange')
# ax.grid(True)
# ax.legend() #凡例（label='Node'など）を表示
# plt.title("twist_raw_diff_field_twist_angular_z") #, fontsize=22)

# plt.tight_layout()
# plt.rcParams["font.size"] = 50
#グラフ保存
plt.savefig('result_final/diff_2015_twist0.02_pure0.02_0126_AS_ver7.pdf')
# 表示
plt.show()
