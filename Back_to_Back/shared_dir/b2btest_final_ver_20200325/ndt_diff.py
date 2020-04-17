import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt        ### グラフ描くなら2D3D関係なく必要
from mpl_toolkits.mplot3d import Axes3D      ### 3Dなら必要
from matplotlib import pyplot
# from scipy import genfromtxt

# df = pd.read_csv('result/twist_cmd_test')
# print(df)

'''CSVファイルの読み込み'''
# この方式header=Noneで読み込まないと、1行目のデータがヘッダとして読み込まれてしまう
# csvdata = pd.read_csv("result/predict_pose_test", header=None, skiprows=1, usecols=[4, 5, 6, 7, 8, 9]) # 1行目はcsv形式ではないのでスキップする。1-4列目はパラメータではないのでこれもスキップする。行列の番号は0から数えることに注意
# csvdata2 = pd.read_csv("result/predict_pose", header=None, skiprows=1, usecols=[4, 5, 6, 7, 8, 9])

# csvdata3 = pd.read_csv("result/ndt_pose_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata4 = pd.read_csv("result/ndt_pose", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata = pd.read_csv("result_ndt_matching_0.5/localizer_pose_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata2 = pd.read_csv("result_ndt_matching_0.5/localizer_pose", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
csvdata = pd.read_csv("result_ndt_matching_0.5/localizer_pose_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9, 10])
csvdata2 = pd.read_csv("result_ndt_matching_0.5/localizer_pose", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9, 10])

# csvdata7 = pd.read_csv("result/estimate_twist_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata8 = pd.read_csv("result/estimate_twist", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata9 = pd.read_csv("result/estimate_twistated_vel_mps_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata10 = pd.read_csv("result/estimate_twistated_vel_mps", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata11 = pd.read_csv("result/estimate_twistated_vel_mpsated_vel_kmph_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata12 = pd.read_csv("result/estimate_twistated_vel_mpsated_vel_kmph", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata13 = pd.read_csv("result/estimated_vel_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata14 = pd.read_csv("result/estimated_vel", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata15 = pd.read_csv("result/time_ndt_matching_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata16 = pd.read_csv("result/time_ndt_matching", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata17 = pd.read_csv("result/ndt_stat_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata18 = pd.read_csv("result/ndt_stat", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# csvdata19 = pd.read_csv("result/ndt_reliability_test", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])
# csvdata20 = pd.read_csv("result/ndt_reliability", header=None, skiprows=2, usecols=[4, 5, 6, 7, 8, 9])

# CSVの行数を少ない方に揃える
csv_row = len(csvdata)
csv2_row = len(csvdata2)
row_diff = abs(csv_row - csv2_row) #行数の差分
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

'''CSVから読んだデータをnumpyの行列に入れる'''
myarray     = np.array
myarray2    = np.array
myarray     = csvdata.values
myarray2    = csvdata2.values
# print(myarray)
# print(myarray2)

# myarray3     = np.array
# myarray4    = np.array
# myarray3     = csvdata3.values
# myarray4    = csvdata4.values
# print(myarray3)
# print(myarray4)


# '''行列のひき算'''
result = myarray2 - myarray
# print(result)

# result2 = myarray3 - myarray4
# print(result2)

# '''結果の行列をCSVファイルに書き出し'''
with open("result_ndt_matching_3d/localizer_pose_result.csv", "w") as f:
    csv_w = csv.writer(f, lineterminator='\n')
    csv_w.writerows(result)
# with open("result/twist_raw_result.csv", "w") as f:
#     csv_w = csv.writer(f, lineterminator='\n')
#     csv_w.writerows(result2)


'''グラフ出力'''
# (x, y, z)
lx1 = csvdata[4].values #field.twist.linear.x　元にする.bagファイルの出力トピック
ly1 = csvdata[5].values #field.twist.linear.y
lz1 = csvdata[6].values #field.twist.linear.z
lx2 = csvdata2[4].values #field.twist.linear.x　テスト対象の出力トピック
ly2 = csvdata2[5].values #field.twist.linear.y
lz2 = csvdata2[6].values #field.twist.linear.z

ax1 = csvdata[7].values #field.twist.angular.x　元にする.bagファイルの出力トピック
ay1 = csvdata[8].values #field.twist.angular.y
az1 = csvdata[9].values #field.twist.angular.z
aw1 = csvdata[10].values #field.twist.angular.z
ax2 = csvdata2[7].values #field.twist.angular.x　テスト対象の出力トピック
ay2 = csvdata2[8].values #field.twist.angular.y
az2 = csvdata2[9].values #field.twist.angular.z
aw2 = csvdata2[10].values #field.twist.angular.z


# 3Dでプロット
fig = plt.figure(figsize=(26, 16))
# ax = Axes3D(fig)
ax = fig.add_subplot(121, projection='3d') # 全体を1x2に分割し、1枚目に描写
# ax.subplot(1,2,1)　#(縦分割数、横分割数、ポジション)
# ax.plot(x='time', y=['value1','value2'], subplots=True, layout=(1,2)) #1行2列に分割してプロット
# 軸ラベル
ax.set_xlabel("field.pose.position.x", fontsize=40)
ax.set_ylabel("field.pose.position.y", fontsize=40)
ax.set_zlabel("field.pose.position.z", fontsize=40)
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(lx1, ly1, lz1, linewidth = 2, label='Autoware Node', color='black')
ax.plot(lx2, ly2, lz2, linewidth = 2, linestyle = ":", label="KALRAY MPPA-256", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.9), loc='upper right', borderaxespad=0, fontsize=40) #凡例（label='Node'など）を表示
plt.title("localizer_pose_diff_field_pose_position_xyz(ndt_matching)", fontsize=40) #, fontsize=22)
plt.tick_params(labelsize=35)

# ax.subplot(1,2,2)
ax = fig.add_subplot(122, projection='3d') # 全体を1x2に分割し、2枚目に描写
# 軸ラベル
ax.set_xlabel("field.pose.orientation.x", fontsize=40)
ax.set_ylabel("field.pose.orientation.y", fontsize=40)
ax.set_zlabel("field.pose.orientation.z", fontsize=40)
# 同じグラフに元にした正解データとテスト対象の出力をプロット
ax.plot(ax1, ay1, az1, linewidth = 2, label='Autoware Node', color='black')
ax.plot(ax2, ay2, az2, linewidth = 2, linestyle = ":", label="KALRAY MPPA-256", color='orange')
ax.grid(True)
ax.legend(bbox_to_anchor=(1, 0.9), loc='upper right', borderaxespad=0, fontsize=40) #凡例（label='Node'など）を表示
plt.title("localizer_pose_diff_field_pose_orientation_xyz(ndt_matching)", fontsize=40) #, fontsize=22)
plt.tick_params(labelsize=35)
plt.savefig('result_ndt_matching_3d/diff_kaiyo_ndt_0.5_field_pose_orientation_xyz_AK_ver1.eps')


# 表示
plt.show()
