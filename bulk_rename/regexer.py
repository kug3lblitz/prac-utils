import os
import re

def main():
    target_directory = input("Enter the target directory: (default: ./dupe) ").strip() or './dupe'
    allowed_directories = ['test', 'test2']

    if target_directory not in allowed_directories:
        print(f"Error: {target_directory} is not in the allowed directory: {allowed_directories}")
        return

    filename_prefix = input("Enter the filename prefix: (default: file) ").strip() or 'file'
    file_extension = input("Enter the file extension: (default: txt) ").strip() or 'txt'
    target_file_pattern = input("Enter the target file pattern: (default: .txt) ").strip() or '.txt'

    # If the first character of file_extension is a '.', drop the first character
    if file_extension.startswith('.'):
        file_extension = file_extension[1:]

    if target_directory == './dupe' and filename_prefix == 'file' and file_extension == 'txt' and target_file_pattern == '.txt':
        print("Denial: The inputs are equal to the defaults.")
        return

    i = 0
    files_changed = False

    for filename in os.listdir(target_directory):
        if re.search(target_file_pattern, filename):
            new_name = filename_prefix + str(i) + '.' + file_extension
            source_file = os.path.join(target_directory, filename)
            destination_file = os.path.join(target_directory, new_name)
            os.rename(source_file, destination_file)
            print(f"Renamed file: {filename} to {new_name}")
            i += 1
            files_changed = True

    if not files_changed:
        print("No files were changed.")

if __name__ == '__main__':
    main()