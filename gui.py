import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from gui_helpers import select_directory, display_images, show_all_tags, process_files, on_image_click, update_tags, remove_selected_tag_from_all_files, add_to_listbox, remove_from_listbox, search_tags

# GUIの設定
root = TkinterDnD.Tk()
root.title("タグ管理ツール")
root.geometry("1700x900")

# 左フレーム
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# ディレクトリ選択ボタン
directory_path = tk.StringVar()
tk.Label(left_frame, text="ディレクトリ:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(left_frame, textvariable=directory_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(left_frame, text="選択", command=lambda: select_directory(directory_path, lambda dir: display_images(dir, image_frame, on_image_click, tags_entry, image_label))).grid(row=0, column=2, padx=10, pady=10)

# 画像表示フレーム
image_frame_container = tk.Frame(left_frame)
image_frame_container.grid(row=4, columnspan=3, padx=10, pady=10)

canvas = tk.Canvas(image_frame_container, width=500, height=700)
scrollbar = ttk.Scrollbar(image_frame_container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
scrollable_frame = tk.Frame(canvas, width=500)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

image_frame = scrollable_frame

# 右フレーム
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

image_label = tk.Label(right_frame)
image_label.grid(row=0, column=0, padx=10, pady=10)

tk.Label(right_frame, text="タグ:").grid(row=1, column=0, padx=10, pady=10)
tags_entry = ScrolledText(right_frame, width=50, height=15)  # 縦に伸ばす
tags_entry.grid(row=2, column=0, padx=10, pady=10)
tk.Button(right_frame, text="タグを更新", command=lambda: update_tags(image_label, tags_entry)).grid(row=3, column=0, padx=10, pady=10)

# タグ一覧のフレーム
tags_frame = tk.Frame(root)
tags_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")

tk.Label(tags_frame, text="タグ一覧:").grid(row=0, column=0, padx=10, pady=10)
tags_listbox = tk.Listbox(tags_frame, width=50, height=25)  # 縦に伸ばす
tags_listbox.grid(row=1, column=0, padx=10, pady=10)
tk.Button(tags_frame, text="更新", command=lambda: show_all_tags(directory_path, tags_listbox)).grid(row=2, column=0, padx=10, pady=10)
tk.Button(tags_frame, text="選択したタグを削除", command=lambda: remove_selected_tag_from_all_files(directory_path, tags_listbox, lambda dir: display_images(dir, image_frame, on_image_click, tags_entry, image_label), tags_entry, image_label)).grid(row=3, column=0, padx=10, pady=10)
tk.Button(tags_frame, text="タグ一覧を表示", command=lambda: show_all_tags(directory_path, tags_listbox)).grid(row=4, column=0, padx=10, pady=10)

# 検索バーと検索ボタン
search_entry = tk.Entry(tags_frame, width=50)
search_entry.grid(row=5, column=0, padx=10, pady=10)
tk.Button(tags_frame, text="検索", command=lambda: search_tags(directory_path, search_entry.get(), tags_listbox)).grid(row=6, column=0, padx=10, pady=10)

tk.Label(tags_frame, text="追加するタグ (カンマ区切り):").grid(row=7, column=0, padx=10, pady=10)
add_tags_entry = tk.Entry(tags_frame, width=50)
add_tags_entry.grid(row=8, column=0, padx=10, pady=10)
tk.Button(tags_frame, text="一括追加", command=lambda: process_files(directory_path, add_tags_entry, front_tags_listbox, back_tags_listbox, image_frame, display_images, tags_entry, image_label)).grid(row=9, column=0, padx=10, pady=10)

# タグの順序設定フレーム
order_frame = tk.Frame(root)
order_frame.grid(row=0, column=3, padx=10, pady=10, sticky="n")

tk.Label(order_frame, text="前方に持っていくタグ:").grid(row=0, column=0, padx=10, pady=10)
front_tags_listbox = tk.Listbox(order_frame, width=50, height=10)
front_tags_listbox.grid(row=1, column=0, padx=10, pady=10)
tk.Button(order_frame, text="追加", command=lambda: add_to_listbox(tags_listbox, front_tags_listbox)).grid(row=2, column=0, padx=10, pady=10)
tk.Button(order_frame, text="削除", command=lambda: remove_from_listbox(front_tags_listbox)).grid(row=3, column=0, padx=10, pady=10)

tk.Label(order_frame, text="後方に持っていくタグ:").grid(row=4, column=0, padx=10, pady=10)
back_tags_listbox = tk.Listbox(order_frame, width=50, height=10)
back_tags_listbox.grid(row=5, column=0, padx=10, pady=10)
tk.Button(order_frame, text="追加", command=lambda: add_to_listbox(tags_listbox, back_tags_listbox)).grid(row=6, column=0, padx=10, pady=10)
tk.Button(order_frame, text="削除", command=lambda: remove_from_listbox(back_tags_listbox)).grid(row=7, column=0, padx=10, pady=10)

# ソートの実行ボタン
tk.Button(order_frame, text="ソート実行", command=lambda: process_files(directory_path, add_tags_entry, front_tags_listbox, back_tags_listbox, image_frame, display_images, tags_entry, image_label)).grid(row=8, column=0, padx=10, pady=10)

# ドラッグアンドドロップの設定
def on_drag(event):
    event.widget._drag_data = {"index": event.widget.nearest(event.y)}

def on_drag_motion(event):
    widget = event.widget
    index = widget.nearest(event.y)
    if index != widget._drag_data["index"]:
        widget._drag_data["index"] = index
        widget.delete(tk.ACTIVE)
        widget.insert(index, widget.get(tk.ACTIVE))

def on_drop(event):
    pass

for listbox in [front_tags_listbox, back_tags_listbox]:
    listbox.bind("<ButtonPress-1>", on_drag)
    listbox.bind("<B1-Motion>", on_drag_motion)
    listbox.bind("<ButtonRelease-1>", on_drop)

root.mainloop()