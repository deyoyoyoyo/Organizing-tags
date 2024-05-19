import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from file_operations import read_caption_file, write_caption_file, process_directory

def select_directory(directory_path, callback):
    directory = filedialog.askdirectory()
    if directory:
        directory_path.set(directory)
        callback(directory)

def display_images(directory, frame, on_image_click, tags_entry, image_label):

    for widget in frame.winfo_children():
            widget.destroy()

    images = []
    for file in os.listdir(directory):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            images.append(file)

    row, col = 0, 0
    for image_file in images:
        image_path = os.path.join(directory, image_file)
        img = Image.open(image_path)
        img.thumbnail((100, 100))
        img = ImageTk.PhotoImage(img)

        panel = tk.Label(frame, image=img)
        panel.image = img
        panel.grid(row=row, column=col, padx=5, pady=5)
        panel.bind("<Button-1>", lambda e, img=image_file: on_image_click(directory, img, tags_entry, image_label))

        col += 1
        if col >= 4:  # 5列ごとに改行
            col = 0
            row += 1

def on_image_click(directory, file_name, tags_entry, image_label):
    file_path = os.path.join(directory, file_name)
    tags_file_path = file_path.replace(os.path.splitext(file_path)[1], '.txt')
    if os.path.exists(tags_file_path):
        tags = read_caption_file(tags_file_path)
        tags_entry.delete('1.0', tk.END)
        tags_entry.insert(tk.END, ','.join(tags))
    else:
        tags_entry.delete('1.0', tk.END)
        tags_entry.insert(tk.END, 'タグファイルが見つかりません')
    
    if os.path.exists(file_path):
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        image_label.file_path = file_path
    else:
        messagebox.showerror("エラー", f"画像ファイルが見つかりません: {file_path}")

def update_tags(image_label, tags_entry):
    file_path = image_label.file_path
    tags = tags_entry.get('1.0', tk.END).strip().split(',')
    tags_file_path = file_path.replace(os.path.splitext(file_path)[1], '.txt')
    write_caption_file(tags_file_path, tags)
    messagebox.showinfo("情報", "タグが更新されました")

def show_all_tags(directory_path, tags_listbox):
    tags_listbox.delete(0, tk.END)
    all_tags = set()
    for root, _, files in os.walk(directory_path.get()):
        for file in files:
            if file.endswith('.txt'):
                tags = read_caption_file(os.path.join(root, file))
                all_tags.update(tags)
    for tag in sorted(all_tags):
        tags_listbox.insert(tk.END, tag)

def search_tags(directory_path, search_term, tags_listbox):
    tags_listbox.delete(0, tk.END)
    matching_tags = set()
    for root, _, files in os.walk(directory_path.get()):
        for file in files:
            if file.endswith('.txt'):
                tags = read_caption_file(os.path.join(root, file))
                matching_tags.update(tag for tag in tags if search_term in tag)
    for tag in sorted(matching_tags):
        tags_listbox.insert(tk.END, tag)

def remove_selected_tag_from_all_files(directory_path, tags_listbox, display_images, tags_entry, image_label):
    selected_tag = tags_listbox.get(tags_listbox.curselection())
    if not selected_tag:
        messagebox.showerror("Error", "削除するタグを選択してください")
        return
    
    directory = directory_path.get()
    if not directory:
        messagebox.showerror("Error", "ディレクトリを選択してください")
        return
    
    process_directory(directory, remove_tags=[selected_tag])
    display_images(directory, image_frame, on_image_click, tags_entry, image_label)
    messagebox.showinfo("Success", f"タグ '{selected_tag}' がすべてのファイルから削除されました")

def process_files(directory_path, add_tags_entry, front_tags_listbox, back_tags_listbox, image_frame, display_images, tags_entry, image_label):
    directory = directory_path.get()
    add_tags = add_tags_entry.get().split(',')
    add_tags = [tag.strip() for tag in add_tags if tag.strip()]  # 空白と空のタグを削除
    front_tags = [front_tags_listbox.get(idx) for idx in range(front_tags_listbox.size())]
    back_tags = [back_tags_listbox.get(idx) for idx in range(back_tags_listbox.size())]
    
    if not directory:
        messagebox.showerror("Error", "ディレクトリを選択してください")
        return
    
    process_directory(directory, add_tags=add_tags, front_tags=front_tags, back_tags=back_tags)
    display_images(directory)
    messagebox.showinfo("Success", "ファイルの処理が完了しました")

def add_to_listbox(source_listbox, target_listbox):
    selected_items = source_listbox.curselection()
    for item in selected_items:
        target_listbox.insert(tk.END, source_listbox.get(item))

def remove_from_listbox(listbox):
    selected_items = listbox.curselection()
    for item in selected_items[::-1]:
        listbox.delete(item)
    