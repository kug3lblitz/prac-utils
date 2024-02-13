import os

def main():
    target = input("Enter the target directory: (default: ./dupe) ").strip()
    allowed_directories = ['test', 'test2']

    if target not in allowed_directories:
        print(f"Error: {target} is not in the allowed directory: {allowed_directories}")
        return

    prefix = input("Enter the filename to change: (default: file) ").strip()
    extension = input("Enter the new file extension: (default: txt) ").strip()
    target_file_type = input("Enter the target file type: (default: txt) ").strip()

    # drop . if it is present - e.g. '.txt' -> 'txt'
    if extension.startswith('.'):
        extension = extension[1:]

    if not target:
        target = './dupe'
    if not prefix:
        prefix = 'file'
    if not extension:
        extension = 'txt'
    if not target_file_type:
        target_file_type = 'txt'

    if target == './dupe' and prefix == 'file' and extension == 'txt' and target_file_type == 'txt':
        print("\n\nDenial: Using default settings\n\n")
        return

    path = target
    i = 0
    files_changed = False

    for filename in os.listdir(path):
        if filename.endswith(target_file_type):
            new_name = prefix + str(i) + '.' + extension
            my_source = os.path.join(path, filename)
            new_name = os.path.join(path, new_name)
            os.rename(my_source, new_name)
            print(f"Renamed file: {filename} >> {new_name}")

            i += 1
            files_changed = True
        if not files_changed:
            print("No files were changed")

if __name__ == '__main__':
    main()