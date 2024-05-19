import os

def read_caption_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split(',')

def write_caption_file(file_path, tags):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(','.join(tags))

def add_tag(tags, new_tag):
    if new_tag not in tags:
        tags.append(new_tag)
    return tags

def remove_tag(tags, tag_to_remove):
    return [tag for tag in tags if tag != tag_to_remove]

def sort_tags(tags, custom_order):
    return sorted(tags, key=lambda x: custom_order.index(x) if x in custom_order else len(custom_order))

def process_directory(directory, add_tags=None, remove_tags=None, front_tags=None, back_tags=None):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            tags = read_caption_file(file_path)
            
            if remove_tags:
                tags = [tag for tag in tags if tag not in remove_tags]
            
            if add_tags:
                tags.extend(add_tags)
            
            # Remove duplicates and empty tags
            tags = [tag.strip() for tag in tags if tag.strip()]
            tags = list(dict.fromkeys(tags))  # Remove duplicates while preserving order
            
            # Check if front_tags or back_tags exist in tags
            if front_tags and any(tag in tags for tag in front_tags):
                tags = [tag for tag in tags if tag not in front_tags]  # Remove front_tags from current position
                tags = front_tags + tags  # Add front_tags to the beginning
            
            if back_tags and any(tag in tags for tag in back_tags):
                tags = [tag for tag in tags if tag not in back_tags]  # Remove back_tags from current position
                tags = tags + back_tags  # Add back_tags to the end
            
            write_caption_file(file_path, tags)