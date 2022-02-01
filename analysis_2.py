import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.filedialog as fl
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import seaborn as sns


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
    else:
        message["text"] = 'excelファイルを選んでください'

# 重回帰分析
def bunseki():
    path = file_path.get()
    if path[-5:] == '.xlsm':
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(path)

        # カラム名取り出し
        str_1 = str(num_area_1.get())
        str_2 = str(num_area_2.get())

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

        # 外れ値削除
        dfq_1 = df[str_1]
        q1 = dfq_1.quantile(0.9)
        dfq_2 = df[str_2]
        q2 = dfq_2.quantile(0.9)
        new_df1 = df[df[str_1] < q1]
        new_df2 = df[df[str_2] < q2]

        # 標準化
        scaler = StandardScaler()
        scaler.fit(np.array(df))
        df_std = scaler.transform(np.array(df))
        df_std = pd.DataFrame(df_std,columns=df.columns)

        # 目的変数(Y)
        Y = np.array(df_std['1：男玩具（金額）'])

        # 説明変数(X)
        col_name = ['来場人数', '3：女定番ﾘｶ（金額）', '4：女定番ｼﾙﾊﾞﾆｱ（金額）', '5：男定番ﾌﾟﾗﾚｰﾙ（金額）', '6：男定番ﾄﾐｶ（金額）', '8：ＮＨＫ（金額）','10：女定番ﾒﾙちゃん（金額）','15：アンパンマン（金額）','29：民芸その他（金額）']
        X = np.array(df_std[col_name])

        # データの分割(訓練データとテストデータ)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

        # モデル構築
        model = LinearRegression()

        # 学習
        model.fit(X_train, Y_train)

        # 回帰係数
        coef = pd.DataFrame({"col_name":np.array(col_name),"coefficient":model.coef_}).sort_values(by='coefficient')

        # 結果：グラフ
        plt.plot(
            X_test, model.predict(X_test),
            linestyle='dashed',
            color='red')
        plt.show()

        # 結果：数値
        print("【回帰係数】", coef)
        print("【切片】:", model.intercept_)
        print("【決定係数(訓練)】:", model.score(X_train, Y_train))
        print("【決定係数(テスト)】:", model.score(X_test, Y_test))

    else:
        message["text"] = 'excelファイルを選んでください'




# GUI設定
root=tk.Tk()
root.configure(bg='white')
root.title(u'重回帰分析')# GUIのタイトル
root.geometry('570x360')# GUIのサイズ
fontExample = tkFont.Font(
    family='Yu Gothic UI Semibold',
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
    padding=(10,20,10,20),
    style='example.TFrame'
)
frame0.grid()

# 説明ラベル
contents = StringVar()
contents.set('データ分析アプリ：重回帰分析')
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
    padding=(10,5,10,5),
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
    padding=(10,5,10,5),
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
    padding=(20,10,10,10),
    style='example.TFrame',
    relief='raised'
)
frame2.grid(padx=(10,0))

# コンボボックス説明ラベル
contents_2 = StringVar()
contents_2.set('①からみた②の関係性度数グラフを作成できます\n数値が１に近い方が関係性が高い\n数値が低い方が関係性が低い(カニバリ発生？)')
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
    text='②部門選択(複数)',
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

# 重回帰分析ボタン
answer_btn = ttk.Button(
    frame2,
    text='グラフ作成',
    style='example.TButton',
    command=bunseki
)
answer_btn.grid(row=2, column=2, padx=(20))

root.mainloop()
