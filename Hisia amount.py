#! /usr/bin/env python
import tkinter
import tkinter.font as tkFont
import random


# ↓ボタンクリック時に実行される関数
def calculation():
    val_1 = float(num_area_1.get())
    answer = '薬剤の量は' + str(int(val_1 / 5 * 1000)) + 'mlだよ!!'
    answer_amount['text'] = answer
    end_roll = ['今日もお疲れ様でした♪', '明日もがんばろう♪', '今日はご褒美にデザートもいいんじゃない？笑', '残りの締め作業も頑張ってね♪', '']
    last_call['text'] = random.choice(end_roll)


# ↓ベースとなるGUIの作成
root = tkinter.Tk()
root.configure(bg='gray')

# ↓GUIのタイトル
root.title(u'クリーンゲート補充計算!!')
# ↓GUIのサイズ
root.geometry('540x340')
# ↓フォント設定
fontExample = tkFont.Font(family='Yu Gothic UI Semibold', size=16, weight="bold")

# ↓ラベル「必要量(ℓ)を入力して「Button」を押してね」
plus_label = tkinter.Label(master=root, text='必要量(ℓ)を入力して「Button」を押してね', font=fontExample, foreground='black',
                           bg='gray')
plus_label.pack(padx=5, pady=30)

# ↓テキストエリア作成,数値入力用
num_area_1 = tkinter.Entry(master=root, width=7, font=fontExample, background='white', justify='center',
                           relief='sunken', bd=5)
num_area_1.pack(padx=5, pady=5)

# ↓ボタン作成,クリックで計算処理を実行する
answer_btn = tkinter.Button(master=root, width=10, font=fontExample, text='Button', command=calculation,
                            background='white', foreground='black', relief='raised', bd=5)
answer_btn.pack(padx=5, pady=5)

# ↓計算結果が表示されるラベル①
answer_amount = tkinter.Label(master=root, width=30, font=fontExample, foreground='black', bg='gray')
answer_amount.pack(padx=5, pady=10)

# ↓計算結果が表示されるラベル②
last_call = tkinter.Label(master=root, width=40, font=fontExample, foreground='black', bg='gray')
last_call.pack(padx=5, pady=0)

root.mainloop()
