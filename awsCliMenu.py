import tkinter as tk
from tkinter import ttk
import menuAction
import awsCliUtil
import tkinter.filedialog
import os

sub_win = None
path_txt = None
file_txt = None
tree = None
error_label = None

# ファイル一覧取得
def run_aws_ls(path_txt,tree):
	path = path_txt.get()
	result = awsCliUtil.aws_ls(path)
	print(result)
	tree.delete(*tree.get_children())
	list = result.splitlines()
	print(list)
	count = 0
	for file_info in list:
		file = file_info.split()
		if len(file) == 3 :
			file.insert(2,"directry")
		elif len(file) != 4:
			continue
		print(file)
		tree.insert(parent='', index='end', iid=count ,values=(count + 1, file[0], file[1], file[2], file[3]))
		count = count + 1 

# アップロードファイルの選択
def run_aws_file_select(upload_path_txt):
	upload_file_path = tkinter.filedialog.askopenfilename()
	upload_path_txt.delete(0, tkinter.END)
	upload_path_txt.insert(tkinter.END,upload_file_path)
	
# アップロード実行
def run_aws_upload(path_txt,upload_path_txt):
	upload_file_path = upload_path_txt.get()
	path = path_txt.get() + "/" + os.path.basename(upload_file_path)
	print(path)
	print(upload_file_path)
	text = awsCliUtil.aws_upload(path,upload_file_path)
	print(text)

# ダウンロード実行
def run_aws_download(path_txt,file):
	if not file.get():
		error_label["text"] = "ダウンロード対象を指定してください"
		return
	error_label["text"] = ""
	path = "s3://" + path_txt.get() + "/" + file.get()
	print(path)
	localPaht = tkinter.filedialog.askdirectory(initialdir = dir)
	print(localPaht)
	text = awsCliUtil.aws_cp(path,localPaht)
	print(text)
	
# 削除実行
def run_aws_delete(path_txt,file):
	print(path_txt)
	print(file)
	path = path_txt.get() + "/" + file.get()
	print(path)
	text = awsCliUtil.aws_delete(path)
	print(text)
	
# 表ダブルクリックのイベント
def tree_Double(event):
	if len(tree.selection()) < 1:
		return
	
	selected_item = tree.selection()[0]
	selected_item_size = tree.item(selected_item)['values'][3]
	selected_item_name = tree.item(selected_item)['values'][4]
	if selected_item_size == "directry":
		path_txt.delete(0, tkinter.END)
		path_txt.insert(tkinter.END,selected_item_name)
	else:
		file_txt.delete(0, tkinter.END)
		file_txt.insert(tkinter.END,selected_item_name)
	
def open_window():
	# グローバル変数宣言
    global sub_win
    global path_txt
    global file_txt
    global tree
    global error_label
    
    if sub_win == None or not sub_win.winfo_exists():
        sub_win = tk.Toplevel()
        sub_win.geometry("900x700")
        sub_win.title("AWSコマンド")
        
        # 各種ウィジェットの作成
        
        error_label = tk.Label(sub_win, text="")
        path_label = tk.Label(sub_win, text="path:")
        path_txt = tk.Entry(sub_win)
        file_label = tk.Label(sub_win, text="download or delete FileName:")
        file_txt = tk.Entry(sub_win)
        
        # 列の識別名を指定
        column = ('no','date','time', 'size', 'name')
        tree = ttk.Treeview(sub_win, columns=column)
        tree.bind("<Double-1>", tree_Double)
        
        button = tk.Button(sub_win, text="ファイル一覧取得", command=lambda:run_aws_ls(path_txt,tree))
        download_button = tk.Button(sub_win, text="ファイルダウンロード", command=lambda:run_aws_download(path_txt,file_txt))
        delete_button = tk.Button(sub_win, text="ファイル削除", command=lambda:run_aws_delete(path_txt,file_txt))
        upload_path_label = tk.Label(sub_win, text="uploadFilePath:")
        upload_path_txt = tk.Entry(sub_win)
        button_up_select = tk.Button(sub_win, text="アップロードファイル選択", command=lambda:run_aws_file_select(upload_path_txt))
        button_up = tk.Button(sub_win, text="ファイルアップロード", command=lambda:run_aws_upload(path_txt,upload_path_txt))
                
        # 列の設定
        tree.column('#0',width=0, stretch='no')
        tree.column('no', anchor='center', width=50)
        tree.column('date', anchor='center', width=120)
        tree.column('time', anchor='center', width=80)
        tree.column('size',anchor='center', width=120)
        tree.column('name', anchor='center', width=200)
        # 列の見出し設定
        tree.heading('#0',text='')
        tree.heading('no', text='No.', anchor='center')
        tree.heading('date', text='日付',anchor='center')
        tree.heading('time', text='時間', anchor='center')
        tree.heading('size', text='サイズ', anchor='center')
        tree.heading('name', text='名前', anchor='center')

        # 各種ウィジェットの設置
        error_label.pack(anchor = tk.W)
        path_label.pack(anchor = tk.W)
        path_txt.pack(fill = tk.X)
        file_label.pack(anchor = tk.W)
        file_txt.pack(fill = tk.X)
        
        button.pack(anchor = tk.W)
        download_button.pack(anchor = tk.W)
        delete_button.pack(anchor = tk.W)
        upload_path_label.pack(anchor = tk.W)
        upload_path_txt.pack(fill = tk.X)
        button_up_select.pack(anchor = tk.W)
        button_up.pack(anchor = tk.W)
        tree.pack(pady=10)
        