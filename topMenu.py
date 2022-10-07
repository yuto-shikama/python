import tkinter as tk
import tkinter.ttk as ttk
import menuAction
import awsCliMenu
        
# rootメインウィンドウの設定
root = tk.Tk()
root.title("tkinter application")
root.geometry("500x300")

# sub_winを定義する
sub_win = None	

# メインフレームの作成と設置
frame = ttk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

# 各種ウィジェットの作成
button = ttk.Button(frame, text="サブウィンドウ生成", command=awsCliMenu.open_window)

# 各種ウィジェットの設置
button.pack()

# ウインドウ状態の維持
root.mainloop()