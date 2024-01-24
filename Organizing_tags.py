import os
import json

def sort_tags(file_path, first_tags, last_tags, add_tags, remove_tags):
    with open(file_path, 'r') as f:
        tags = f.read().strip().split(',')
    tags = [tag.strip() for tag in tags]

    # タグの追加と削除
    for tag in add_tags:
        if tag not in tags:
            tags.append(tag)
    for tag in remove_tags:
        if tag in tags:
            tags.remove(tag)

    # タグを先頭に移動するための関数
    def move_tags_to_front(tags, target_tags):
        for tag in reversed(target_tags):
            for t in [t for t in tags if tag in t]:
                tags.remove(t)
                tags.insert(0, t)

    # タグを末尾に移動するための関数
    def move_tags_to_end(tags, target_tags):
        for tag in target_tags:
            for t in [t for t in tags if tag in t]:
                tags.remove(t)
                tags.append(t)

    # タグの並び替え
    move_tags_to_front(tags, first_tags)
    move_tags_to_end(tags, last_tags)

    tags = ','.join(tags)
    with open(file_path, 'w') as f:
        f.write(tags)

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    folder_path = config['folder_path']
    first_tags = config['first_tags']
    last_tags = config['last_tags']
    extensions = config['extensions']
    add_tags = config.get('add_tags', [])
    remove_tags = config.get('remove_tags', [])
    for file_name in os.listdir(folder_path):
        if file_name.endswith(tuple(extensions)):
            file_path = os.path.join(folder_path, file_name)
            sort_tags(file_path, first_tags, last_tags, add_tags, remove_tags)

if __name__ == "__main__":
    main()
