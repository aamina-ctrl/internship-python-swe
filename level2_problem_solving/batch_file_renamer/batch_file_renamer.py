import os
def display_files_in_directory():
    folder_path = input("Enter the folder path: ")
    files= os.listdir(folder_path)
    print("Files in the directory:")
    for file in files:
        print(file)
    return folder_path,files
def rename_files(folder_path,files):
    prefix = input("Enter the prefix for the new file names: ")
    count=0
    for file in files:
        count+=1
        name,extension=os.path.splitext(file)
        new_name=prefix+"_"+str(count)+extension
        print(file,"->",new_name)
    confirm=input("Do you want to rename the files? (y/n): ")
    if confirm.lower()=="y":
        count=0
        for file in files:
            count+=1
            name,extension=os.path.splitext(file)
            new_name=prefix+"_"+str(count)+extension
            old_path=os.path.join(folder_path,file)
            new_path=os.path.join(folder_path,new_name)
            try:
                os.rename(old_path,new_path)
            except OSError as e:
                print(f"Error occurred while renaming {file}: {e}")
                print("Skipped renaming this file.")
            else:
                print(f"Renamed {file} to {new_name}")
                print("Renaming completed successfully.")
    else:
        print("Renaming cancelled.")
        rename_files(folder_path,files)
def main():
    folder_path,files=display_files_in_directory()
    rename_files(folder_path,files)
main()