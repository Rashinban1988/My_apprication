import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.filedialog as fl
import tkinter.font as tkFont
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=['Yu Gothic', 'Hiragino Maru Gothic Pro'])

# ファイルからカラム名抽出
df2 = ()


# ファイルパス取得
def filepath_get(*args):
    filetype = [("all file", "*")]
    filepath = fl.askopenfilename(
        initialdir="C:/Users/okazu/Desktop",
        filetypes=filetype,
        title="ファイルを選んでください"
    )
    file_path.set(filepath)
    # カラム名抽出
    path = file_path.get()
    if path[-5:] == '.xlsm':
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(path)
        df2 = df.columns.values
        num_area_1.configure(values=df2)
        num_area_2.configure(values=df2)
        num_area_3.configure(values=df2)
    else:
        message["text"] = 'excelファイルを選んでください'


# 単回帰分析
def bunseki():
    path = file_path.get()
    if path[-5:] == '.xlsm':
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(path)

        # カラム名取り出し
        str_1 = str(num_area_1.get())
        str_2 = str(num_area_2.get())
        str_3 = str(num_area_3.get())

        # カラムデータを整えるstr_1
        if str_1[0] == '[':
            str_1 = str_1[2:-1]
        elif str_1[-1] == ']':
            str_1 = str_1[1:-2]
        else:
            str_1 = str_1[1:-1]

        # カラムデータを整えるstr_2
        if str_2[0] == '[':
            str_2 = str_2[2:-1]
        elif str_2[-1] == ']':
            str_2 = str_2[1:-2]
        else:
            str_2 = str_2[1:-1]

        # カラムデータを整えるstr_3
        if str_3 == '':
            str_3 = ''
        else:
            if str_3[0] == '[':
                str_3 = str_3[2:-1]
            elif str_3[-1] == ']':
                str_3 = str_3[1:-2]
            else:
                str_3 = str_3[1:-1]

        # 外れ値削除
        dfq_1 = df[str_1]
        q1 = dfq_1.quantile(0.9)
        dfq_2 = df[str_2]
        q2 = dfq_2.quantile(0.9)
        new_df1 = df[df[str_1] < q1]
        new_df2 = df[df[str_2] < q2]

        # 単回帰分析実行
        if str_3 == '':
            sns.regplot(
                data=df,
                x=str_1,
                y=str_2,
                order=3
            )
        else:
            sns.lmplot(
                data=df,
                x=str_1,
                y=str_2,
                hue=str_3
            )

        # プロットのメモリ設定
        df_x = new_df1[str_1]
        df_y = new_df2[str_2]
        plt.xlim(df_x.min(), df_x.max())
        plt.ylim(df_y.min(), df_y.max())

        # プロットのラベル設定
        plt.legend(["散布図", "回帰曲線・信頼区間"])

        # プロット出力
        plt.show()

    else:
        message["text"] = 'excelファイルを選んでください'


# GUI設定
root = tk.Tk()

root.configure(bg='white')
root.title(u'単回帰分析')  # GUIのタイトル
root.geometry('570x570')  # GUIのサイズ
root.resizable(False, False)  # GUIのサイズ固定
fontExample = tkFont.Font(
    family='Yu Gothic UI Semi-bold',
    size=16,
    weight="bold"
)

# style.TFrame設定
style_TFrame = ttk.Style()
style_TFrame.configure(
    'example.TFrame',
    background='white'
)

# style.TLabel設定
style_TLabel = ttk.Style()
style_TLabel.configure(
    'example.TLabel',
    background='white',
)

# style.TButton設定
style_TButton = ttk.Style()
style_TButton.configure(
    'example.TButton',
    background='white'
)

# style.TEntry設定
style_TEntry = ttk.Style()
style_TEntry.configure(
    'example.TEntry',
    background='white'
)

# style.TCombobox設定
style_TCombobox = ttk.Style()
style_TCombobox.configure(
    'example.TCombobox',
    background='white'
)

# Frame0作成
frame0 = ttk.Frame(
    root,
    padding=(10, 20, 10, 20),
    style='example.TFrame'
)
frame0.grid()

# 説明ラベル
contents = StringVar()
contents.set('データ分析アプリ：単回帰分析')
message = ttk.Label(
    frame0,
    textvariable=contents,
    style='example.TLabel',
    font='bold'

)
message.grid(row=0, column=0)

# Frame1作成
frame1 = ttk.Frame(
    root,
    padding=(10, 5, 10, 5),
    style='example.TFrame',
    relief='raised'
)
frame1.grid()

# ファイルパス取得：ラベル
s = StringVar()
s.set('excelファイル(.xlsm)を選んでください')
message = ttk.Label(
    frame1,
    textvariable=s,
    style='example.TLabel'
)
message.grid(row=0, column=0)

# ファイルパス取得：ボタン
answer_btn = ttk.Button(
    frame1,
    text='ファイル選択',
    command=filepath_get,
    style='example.TButton'
)
answer_btn.grid(row=0, column=1)

# Frame1_2作成
frame1_2 = ttk.Frame(
    root,
    padding=(10, 5, 10, 5),
    style='example.TFrame',
    relief='raised'
)
frame1_2.grid(pady=20)

# ファイルパス表示：ラベル
path_name = StringVar()
path_name.set('ファイルパス：')
filepath_label = ttk.Label(
    frame1_2,
    textvariable=path_name,
    style='example.TLabel'
)
filepath_label.grid(row=0, column=0)

# ファイルパス表示：テキストエリア
file_path = StringVar()
filepath_entry = ttk.Entry(
    frame1_2,
    textvariable=file_path,
    width=55,
    style='example.TEntry'
)
filepath_entry.grid(row=0, column=1)

# Frame2作成
frame2 = ttk.Frame(
    root,
    padding=(20, 10, 10, 10),
    style='example.TFrame',
    relief='raised'
)
frame2.grid(padx=(10, 0))

# コンボボックス説明ラベル
contents_2 = StringVar()
contents_2.set('①から②の数値を予測するグラフを作成できます\n③は天気・曜日など条件を選択\n③は選択しなくてもOK')
message_2 = ttk.Label(
    frame2,
    textvariable=contents_2,
    style='example.TLabel'
)
message_2.grid(row=0, column=1, pady=15)

# コンボボックス１ラベル
combo1_label = ttk.Label(
    frame2,
    text='①部門選択',
    style='example.TLabel'
)
combo1_label.grid(row=1, column=0)

# コンボボックス１配置
num_area_1 = ttk.Combobox(
    frame2,
    values=df2,
    style='example.TCombobox'
)
num_area_1.grid(row=2, column=0)

# コンボボックス２ラベル
combo2_label = ttk.Label(
    frame2,
    text='②部門選択',
    style='example.TLabel'
)
combo2_label.grid(row=1, column=1)

# コンボボックス２配置
num_area_2 = ttk.Combobox(
    frame2,
    values=df2,
    style='example.TCombobox'
)
num_area_2.grid(row=2, column=1)

# コンボボックス３ラベル
combo3_label = ttk.Label(
    frame2,
    text='③条件選択',
    style='example.TLabel'
)
combo3_label.grid(row=1, column=2)

# コンボボックス３配置
num_area_3 = ttk.Combobox(
    frame2,
    values=df2,
    style='example.TCombobox'
)
num_area_3.grid(row=2, column=2)

# 単回帰分析ボタン
answer_btn = ttk.Button(
    frame2,
    text='グラフ作成',
    command=bunseki,
    style='example.TButton',
)
answer_btn.grid(row=3, column=1, pady=(10, 0))

root.mainloop()
