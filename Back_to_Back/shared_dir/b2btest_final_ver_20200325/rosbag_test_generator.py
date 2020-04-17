import os, sys, time
import tkinter as tk
import yaml
import subprocess
import time


class UpperFrame(tk.Frame):
    def __init__(self, master=None):
        # ボタンクリックイベント
        def btn_click1():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            rosbag_path1 = self.rosbag_entry1.get()
            rosbag_gen = subprocess.Popen(['python3', 'twist_filter_gen.py', rosbag_path1]) #twist_filter_gen.py
        def btn_click2():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            rosbag_path2 = self.rosbag_entry2.get()
            config_gen = subprocess.Popen(['python3', 'grep.py'])
            # config_gen = subprocess.Popen(['python3', rosbag_path2])
        super().__init__(master)

        self.btn = tk.Button(self, text='bagファイルの生成', command=btn_click1)
        # self.btn.pack(anchor=tk.W)
        self.btn.grid(row=0, column=0, padx=2, pady=2)

        self.rosbag_label1 = tk.Label(self, text = "ROSBAG")
        self.rosbag_label1.grid(row=0, column=1, padx=2, pady=2)

        self.rosbag_entry1 = tk.Entry(self, width=50)
        self.rosbag_entry1.grid(row=0, column=2, padx=2, pady=2)

        self.btn = tk.Button(self, text='config.yamlの生成', command=btn_click2)
        # self.btn.pack(anchor=tk.W)
        self.btn.grid(row=1, column=0, padx=2, pady=2)

        self.rosbag_label2 = tk.Label(self, text = "Destination")
        self.rosbag_label2.grid(row=1, column=1, padx=2, pady=2)

        self.rosbag_entry2 = tk.Entry(self, width=50)
        self.rosbag_entry2.grid(row=1, column=2, padx=2, pady=2)

class LowerFrame(tk.Frame):
    def __init__(self, master=None):
        # ボタンクリックイベント
        def btn_click3():
            num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            rosbag_play_gen = subprocess.Popen(['python3', 'builder.py', node_list[num] ])
        def btn_click4():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            rosbag_play = subprocess.Popen(['python3', 'source1.py'])
        def btn_click5():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            diff_gen = subprocess.Popen(['../../.pyenv/versions/3.6.0/bin/python3.6', 'diff.py'])
        def btn_click6():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            diff_gen = subprocess.Popen(['../../.pyenv/versions/3.6.0/bin/python3.6', 'diff_two_dimension.py'])
        def btn_click7():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            diff_gen = subprocess.Popen(['../../.pyenv/versions/3.6.0/bin/python3.6', 'ndt_diff.py'])
        def btn_click8():
            # num = node_var.get()
            # tkinter.messagebox.showinfo('チェックされた項目', node_list[num])
            # diff_gen = subprocess.Popen(['pyenv', 'global', '3.6.0'])
            # diff_gen = subprocess.Popen(['python3', '-V'])

            # time.sleep(1)
            diff_gen = subprocess.Popen(['../../.pyenv/versions/3.6.0/bin/python3.6', 'ndt_diff_two_dimension.py'])
            # diff_gen = subprocess.run(['pyenv', 'global', 'system'])
    # def __init__(self, config, master=None):
        super().__init__(master)

        node_var = tk.IntVar()
        node_var.set(0)

        node_list = ['twist_filter', 'pure_pursuit', 'ndt_matching']
        for i in range(len(node_list)):
            self.twis_filter_radio = tk.Radiobutton(self, value=i, variable=node_var, text=node_list[i]) 
            self.twis_filter_radio.pack(anchor=tk.W)
            # chk.place(x=50, y=30 + (i * 24))

        # self.btn = tk.Button(self, text='source1.pyの生成（Jinja2による自動生成）', command=btn_click3)
        self.btn = tk.Button(self, text='Generate source1.py（Automatic Generation by Jinja2）', command=btn_click3)

        self.btn.pack(anchor=tk.W)

        # self.btn = tk.Button(self, text='source1.pyの実行（bagファイルの再生・比較用のデータ取得開始）', command=btn_click4)
        self.btn = tk.Button(self, text='Run of source1.py（Play bag File & Get Data for Comparison）', command=btn_click4)
        self.btn.pack(anchor=tk.W)

        # self.btn = tk.Button(self, text='diff.pyの実行（3次元グラフの生成）（twist_filter & pure_pursuit）', command=btn_click5)
        self.btn = tk.Button(self, text='Run of diff.py（Generate 3D Graph）（twist_filter & pure_pursuit）', command=btn_click5)
        self.btn.pack(anchor=tk.W)

        # self.btn = tk.Button(self, text='diff.pyの実行（2次元グラフの生成）（twist_filter & pure_pursuit）', command=btn_click6)
        self.btn = tk.Button(self, text='Run of diff.py（Generate 2D Graph）（twist_filter & pure_pursuit）', command=btn_click6)
        self.btn.pack(anchor=tk.W)

        # self.btn = tk.Button(self, text='diff.pyの実行（3次元グラフの生成）（ndt_matching）', command=btn_click7)
        self.btn = tk.Button(self, text='Run of diff.py（Generate 3D Graph）（ndt_matching）', command=btn_click7)
        self.btn.pack(anchor=tk.W)

        # self.btn = tk.Button(self, text='diff.pyの実行（2次元グラフの生成）（ndt_matching）', command=btn_click8)
        self.btn = tk.Button(self, text='Run of diff.py（Generate 2D Graph）（ndt_matching）', command=btn_click8)
        self.btn.pack(anchor=tk.W)

        # ラジオボタンをconfigにしたがって追加予定
        # self.twis_filter_radio = tk.Radiobutton(self, text='twist_filter', value=0, variable=node_var)
        # self.twis_filter_radio.pack(anchor=tk.W)
        # self.twis_filter_raw = tk.Radiobutton(self, text='pure_pursuit', value=1, variable=node_var)
        # self.twis_filter_raw.pack(anchor=tk.W)
        # self.twis_filter_raw = tk.Radiobutton(self, text='ndt_matching', value=2, variable=node_var)
        # self.twis_filter_raw.pack(anchor=tk.W)

        # import twist_filter_play.py
        # node_name = 
        



    


# with open(os.path.dirname(__file__) + "/rosbag_test_generator.yaml", "r") as f:
#   config = yaml.load(f)

root = tk.Tk()
root.geometry("800x600")

upper_frame = UpperFrame()
upper_frame.pack(padx=2, pady=2, anchor=tk.W)

# lower_frame = LowerFrame(config)
lower_frame = LowerFrame()
lower_frame.pack(padx=2, pady=2, anchor=tk.W)


root.mainloop()