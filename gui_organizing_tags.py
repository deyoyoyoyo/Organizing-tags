import tkinter as tk
from tkinter import filedialog
import json
import glob
import os
from Organizing_tags import organize_tags

def load_config():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)

        entry_folder_path.delete(0, tk.END)
        entry_folder_path.insert(0, config.get('folder_path', ''))

        entry_extensions.delete(0, tk.END)
        entry_extensions.insert(0, ', '.join(config.get('extensions', [])))

        entry_first_tags.delete(0, tk.END)
        entry_first_tags.insert(0, ', '.join(config.get('first_tags', [])))

        entry_last_tags.delete(0, tk.END)
        entry_last_tags.insert(0, ', '.join(config.get('last_tags', [])))

        entry_add_tags.delete(0, tk.END)
        entry_add_tags.insert(0, ', '.join(config.get('add_tags', [])))

        entry_remove_tags.delete(0, tk.END)
        entry_remove_tags.insert(0, ', '.join(config.get('remove_tags', [])))

        folder_path = config.get('folder_path', '')
        extensions = config.get('extensions', [])
        all_tags = set()

        for ext in extensions:
            for file_path in glob.glob(os.path.join(folder_path, f'*{ext}')):
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        tags = file.read().split(',')
                        all_tags.update(tags)

        update_tag_list(list(all_tags))
        log_text.insert(tk.END, "Config file loaded successfully.\n")

    except Exception as e:
        log_text.insert(tk.END, f"Error loading config file: {e}\n")

def update_tag_list(tags):
    sorted_tags = sorted(tags)  # タグをASCIIの昇順でソート
    listbox_tags.delete(0, tk.END)
    for tag in sorted_tags:
        listbox_tags.insert(tk.END, tag)


def save_config():
    try:
        config = {
            'folder_path': entry_folder_path.get(),
            'extensions': entry_extensions.get().split(','),
            'first_tags': entry_first_tags.get().split(','),
            'last_tags': entry_last_tags.get().split(','),
            'add_tags': entry_add_tags.get().split(','),
            'remove_tags': entry_remove_tags.get().split(',')
        }

        with open('config.json', 'w') as file:
            json.dump(config, file, indent=4)

        log_text.insert(tk.END, "Config saved successfully.\n")

    except Exception as e:
        log_text.insert(tk.END, f"Error saving config: {e}\n")

def execute_organizing_tags():
    config = {
        'folder_path': entry_folder_path.get(),
        'extensions': entry_extensions.get().split(','),
        'first_tags': entry_first_tags.get().split(','),
        'last_tags': entry_last_tags.get().split(','),
        'add_tags': entry_add_tags.get().split(','),
        'remove_tags': entry_remove_tags.get().split(',')
    }

    try:
        organize_tags(config)
        log_text.insert(tk.END, "Tags organized successfully.\n")

        # タグ一覧を更新
        all_tags = set()
        folder_path = config['folder_path']
        extensions = config['extensions']
        for ext in extensions:
            for file_path in glob.glob(os.path.join(folder_path, f'*{ext}')):
                if os.path.exists(file_path):
                    with open(file_path, 'r') as file:
                        tags = file.read().split(',')
                        all_tags.update(tags)

        update_tag_list(list(all_tags))

    except Exception as e:
        log_text.insert(tk.END, f"Error organizing tags: {e}\n")

def browse_folder():
    folder_path = filedialog.askdirectory()  # フォルダーパスを選択するダイアログを表示
    entry_folder_path.delete(0, tk.END)
    entry_folder_path.insert(0, folder_path)

def on_closing():
    # ウィンドウが閉じるときに行いたい処理をここに追加
    window.destroy()

# GUIの初期設定
window = tk.Tk()
window.title("Organizing Tags GUI")
window.geometry("1000x400")  # ウィンドウの幅を800、高さを400に設定

# ウィンドウの×ボタンを押したときに on_closing 関数を呼ぶ
window.protocol("WM_DELETE_WINDOW", on_closing)

# グリッドレイアウトのフレームを作成
left_frame = tk.Frame(window)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

right_frame = tk.Frame(window)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# フォルダパスと拡張子の入力
tk.Label(left_frame, text="フォルダーパス:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_folder_path = tk.Entry(left_frame, width=70)  # 幅を広げました
entry_folder_path.grid(row=0, column=1, padx=5, pady=5, sticky='w')

tk.Label(left_frame, text="拡張子:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_extensions = tk.Entry(left_frame, width=20)  # 幅を広げました
entry_extensions.grid(row=1, column=1, padx=5, pady=5, sticky='w')

# 先頭タグ、後方タグ、追加タグ、削除タグの入力
tk.Label(left_frame, text="先頭タグ:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_first_tags = tk.Entry(left_frame, width=70)  # 幅を広げました
entry_first_tags.grid(row=3, column=1, padx=5, pady=5, sticky='w')

tk.Label(left_frame, text="後方タグ:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
entry_last_tags = tk.Entry(left_frame, width=70)  # 幅を広げました
entry_last_tags.grid(row=4, column=1, padx=5, pady=5, sticky='w')

tk.Label(left_frame, text="追加タグ:").grid(row=5, column=0, padx=5, pady=5, sticky='w')
entry_add_tags = tk.Entry(left_frame, width=70)  # 幅を広げました
entry_add_tags.grid(row=5, column=1, padx=5, pady=5, sticky='w')

tk.Label(left_frame, text="削除タグ:").grid(row=6, column=0, padx=5, pady=5, sticky='w')
entry_remove_tags = tk.Entry(left_frame, width=70)  # 幅を広げました
entry_remove_tags.grid(row=6, column=1, padx=5, pady=5, sticky='w')

# タグ一覧の表示領域とスクロールバー
tk.Label(right_frame, text="タグ一覧").pack()
scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tags = tk.Listbox(right_frame, yscrollcommand=scrollbar.set, height=20, width=50)
listbox_tags.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=listbox_tags.yview)

# 設定をロードするボタン
load_button = tk.Button(left_frame, text="Load Config", command=load_config)
load_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')  # フォルダーパスの次の行に移動しました

# 設定を保存するボタン
save_button = tk.Button(left_frame, text="Save Config", command=save_config)
save_button.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky='w')

# 実行ボタン
execute_button = tk.Button(left_frame, text="実行", command=execute_organizing_tags)
execute_button.grid(row=8, column=1, columnspan=4, padx=5, pady=5, sticky='w')

# フォルダーパス選択ボタン
folder_select_button = tk.Button(left_frame, text="フォルダーを参照", command=browse_folder)
folder_select_button.grid(row=0, column=2, padx=5, pady=5, sticky='w')

# ログ表示用テキストエリア
log_text = tk.Text(left_frame, height=4, width=60)
log_text.grid(row=9, column=1, columnspan=4, padx=5, pady=5, sticky='w')

# メインループ
window.mainloop()
