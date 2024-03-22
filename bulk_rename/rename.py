# import os
# import re
# import argparse

# def replace_text_in_files(target, old_text, new_text, file_extension=None, is_file=False):
#     if is_file:
#         files = [target]
#     else:
#         files = [os.path.join(foldername, filename) for foldername, _, filenames in os.walk(target) for filename in filenames if not file_extension or filename.endswith(file_extension)]
    
#     for filepath in files:
#         with open(filepath, 'r') as file:
#             filedata = file.read()
#         newdata = re.sub(old_text, new_text, filedata)
#         with open(filepath, 'w') as file:
#             file.write(newdata)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Replace text in files or directories. ex: python rename.py -d directory old_text new_text .php')
#     group = parser.add_mutually_exclusive_group(required=True)
#     group.add_argument('-d', '--directory', help='The directory to search')
#     group.add_argument('-f', '--file', help='The file to search')
#     parser.add_argument('old_text', help='The text to replace')
#     parser.add_argument('new_text', help='The text to replace with')
#     parser.add_argument('file_extension', nargs='?', default=None, help='The file extension to target (optional)')
    
#     args = parser.parse_args()
    
#     replace_text_in_files(args.directory or args.file, args.old_text, args.new_text, args.file_extension, is_file=bool(args.file))
import os
import re
import argparse

def replace_text_in_files(target, old_text, new_text, file_extension=None, is_file=False):
    if is_file:
        files = [target]
    else:
        files = [os.path.join(foldername, filename) for foldername, _, filenames in os.walk(target) for filename in filenames if not file_extension or filename.endswith(file_extension)]
    
    for filepath in files:
        with open(filepath, 'r') as file:
            filedata = file.read()
        newdata = re.sub(old_text, new_text, filedata)
        with open(filepath, 'w') as file:
            file.write(newdata)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace text in files or directories. ex: python rename.py -d directory old_text new_text .php')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--directory', help='The directory to search')
    group.add_argument('-f', '--file', help='The file to search')
    parser.add_argument('old_text', help='The text to replace')
    parser.add_argument('new_text', help='The text to replace with')
    parser.add_argument('file_extension', nargs='?', default=None, help='The file extension to target (optional)')
    
    args = parser.parse_args()
    
    if args.file:
        replace_text_in_files(args.file, args.old_text, args.new_text, args.file_extension, is_file=True)
    else:
        replace_text_in_files(args.directory, args.old_text, args.new_text, args.file_extension, is_file=False)