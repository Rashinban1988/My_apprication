from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import random

win = Tk()  # gui設定
win.configure(bg='white')
win.title('クイズ！板の長さは？')  # title名
win.geometry('500x300')  # guisize
win.resizable(False, False)  # guisize.固定
fontExample = tkFont.Font(
    family='Yu Gothic UI Semi-bold',
    size=16,
    weight="bold"
)

snow_bord_size = (98, 8, 18, 28, 38, 44, 55, 63)
ski_size = (90, 100, 10, 20, 30, 40, 50, 60, 70)
tall_size = 0


class Answer:
    def __init__(self):
        self.size = None

    answer_size = 0


def over_write_ski(self):
    ski_sizing = ski_size_entry.get()
    self.size = int(ski_sizing)


def over_write_bord(self):
    bord_sizing = snow_bord_size_entry.get()
    self.size = int(bord_sizing)


# 身長のサイズをランダム表示する
def quiz():
    global tall_size

    quiz_size = random.randint(110, 181)
    contents.set(f'身長が{quiz_size}cmの時の板の長さは？')
    tall_size = quiz_size
    ski_answer_size.set('')
    snow_bord_answer_size.set('')


def ski_test():
    global ski_answer_size
    answer_ski_size = Answer()
    over_write_ski(answer_ski_size)
    if answer_ski_size.size in ski_size:
        if tall_size >= 180:
            if answer_ski_size.size == 70:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は７０です！')

        elif tall_size >= 170:
            if answer_ski_size.size == 60:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は６０です！')

        elif tall_size >= 160:
            if answer_ski_size.size == 50:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は５０です！')

        elif tall_size >= 150:
            if answer_ski_size.size == 40:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は４０です！')

        elif tall_size >= 140:
            if answer_ski_size.size == 30:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は３０です！')

        elif tall_size >= 130:
            if answer_ski_size.size == 20:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は２０です！')

        elif tall_size >= 120:
            if answer_ski_size.size == 10:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は１０です！')

        elif tall_size >= 110:
            if answer_ski_size.size == 100:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は１００です！')

        elif tall_size >= 100:
            if answer_ski_size.size == 90:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は９０です！')

    else:
        ski_answer_size.set('その板の長さはありません。')

    if answer_ski_size.size not in ski_size:
        if tall_size >= 180:
            if answer_ski_size.size == 70:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は７０です！')

        elif tall_size >= 170:
            if answer_ski_size.size == 60:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は６０です！')

        elif tall_size >= 160:
            if answer_ski_size.size == 50:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は５０です！')

        elif tall_size >= 150:
            if answer_ski_size.size == 40:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は４０です！')

        elif tall_size >= 140:
            if answer_ski_size.size == 30:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は３０です！')

        elif tall_size >= 130:
            if answer_ski_size.size == 20:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は２０です！')

        elif tall_size >= 120:
            if answer_ski_size.size == 10:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は１０です！')

        elif tall_size >= 110:
            if answer_ski_size.size == 100:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は１００です！')

        elif tall_size >= 100:
            if answer_ski_size.size == 90:
                ski_answer_size.set('正解！')
            else:
                ski_answer_size.set('正解は９０です！')


def snow_bord_test():
    global snow_bord_answer_size
    answer_snow_bord_size = Answer()
    over_write_bord(answer_snow_bord_size)
    if answer_snow_bord_size.size in snow_bord_size:
        if tall_size >= 180:
            if answer_snow_bord_size.size == 63:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は６３です！')

        elif tall_size >= 170:
            if answer_snow_bord_size.size == 55:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は５５です！')

        elif tall_size >= 160:
            if answer_snow_bord_size.size == 44:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は４４です！')

        elif tall_size >= 150:
            if answer_snow_bord_size.size == 38:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は３８です！')

        elif tall_size >= 140:
            if answer_snow_bord_size.size == 28:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は２８です！')

        elif tall_size >= 130:
            if answer_snow_bord_size.size == 18:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は１８です！')

        elif tall_size >= 120:
            if answer_snow_bord_size.size == 8:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は８です！')

        elif tall_size >= 110:
            if answer_snow_bord_size.size == 98:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は９８です！')

    else:
        snow_bord_answer_size.set('その板のサイズはありません。')

    if answer_snow_bord_size.size not in snow_bord_size:
        if tall_size >= 180:
            if answer_snow_bord_size.size == 63:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は６３です！')

        elif tall_size >= 170:
            if answer_snow_bord_size.size == 55:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は５５です！')

        elif tall_size >= 160:
            if answer_snow_bord_size.size == 44:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は４４です！')

        elif tall_size >= 150:
            if answer_snow_bord_size.size == 38:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は３８です！')

        elif tall_size >= 140:
            if answer_snow_bord_size.size == 28:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は２８です！')

        elif tall_size >= 130:
            if answer_snow_bord_size.size == 18:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は１８です！')

        elif tall_size >= 120:
            if answer_snow_bord_size.size == 8:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は８です！')

        elif tall_size >= 110:
            if answer_snow_bord_size.size == 98:
                snow_bord_answer_size.set('正解！')
            else:
                snow_bord_answer_size.set('正解は９８です！')


style_TFrame = ttk.Style()  # style.TFrame設定
style_TFrame.configure('example.TFrame', background='white')

style_TLabel = ttk.Style()  # style.TLabel設定
style_TLabel.configure('example.TLabel', background='white')

style_TButton = ttk.Style()  # style.TButton設定
style_TButton.configure('example.TButton', background='white')

style_TEntry = ttk.Style()  # style.TEntry設定
style_TEntry.configure('example.TEntry', background='white', height=10)

# Frame0作成
frame0 = ttk.Frame(win, padding=(10, 20, 10, 20), style='example.TFrame')
frame0.grid(row=1)

answer_btn = ttk.Button(frame0, text='出題！', width=20, command=quiz, style='example.TButton')
answer_btn.grid(row=1, columns=1, pady=20)

contents = StringVar()
message = ttk.Label(frame0, textvariable=contents, style='example.TLabel', font='bold')
message.grid(row=2, columns=1)

# Frame1作成
frame1 = ttk.Frame(win, padding=(10, 5, 10, 5), style='example.TFrame')
frame1.grid(row=2, columns=1)

# スキー板サイズ入力指示：ラベル
ski_label = ttk.Label(frame1, text='スキー板のサイズを入力', style='example.TLabel')
ski_label.grid(row=1, column=1)

# スキーサイズ入力：テキストエリア
ski2_size_entry = IntVar()
ski_size_entry = ttk.Entry(frame1, width=20, textvariable=ski2_size_entry, style='example.TEntry')
ski_size_entry.grid(row=2, column=1)

# 決定ボタン１
answer_btn = ttk.Button(frame1, text='決定', command=ski_test, style='example.TButton')
answer_btn.grid(row=2, column=2)

# スキーサイズ答え：テキストエリア
ski_answer_size = StringVar()
ski_size2_entry = ttk.Entry(frame1, width=20, textvariable=ski_answer_size, style='example.TEntry')
ski_size2_entry.grid(row=4, column=1, padx=10, pady=10, ipady=20)

# Frame2作成
frame2 = ttk.Frame(win, padding=(10, 5, 10, 5), style='example.TFrame')
frame2.grid(pady=20, row=3, columns=2)

# ボード板サイズ入力指示：ラベル
ski_label = ttk.Label(frame1, text='スノーボード板のサイズを入力', style='example.TLabel')
ski_label.grid(row=1, column=3)

# スノーボードサイズ入力：テキストエリア
snow2_bord_size_entry = IntVar()
snow_bord_size_entry = ttk.Entry(frame1, width=20, textvariable=snow2_bord_size_entry, style='example.TEntry')
snow_bord_size_entry.grid(row=2, column=3)

# 決定ボタン2
answer_btn = ttk.Button(frame1, text='決定', command=snow_bord_test, style='example.TButton')
answer_btn.grid(row=2, column=4)

# スノーボードサイズ答え：テキストエリア
snow_bord_answer_size = StringVar()
snow_bord_size2_entry = ttk.Entry(frame1, width=20, textvariable=snow_bord_answer_size, style='example.TEntry')
snow_bord_size2_entry.grid(row=4, column=3, padx=10, pady=10, ipady=20)

win.mainloop()  # gui起動
