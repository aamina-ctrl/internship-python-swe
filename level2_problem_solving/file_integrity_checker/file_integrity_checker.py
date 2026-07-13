import os
import json
import hashlib

def calculate_hash(file_path):
    with open(file_path,"rb") as file:
        data=file.read()
        hash_value=hashlib.sha256(data).hexdigest()
    return hash_value
def create_baseline():
    folder_path=input("Enter the folder path to create baseline: ")
    files=os.listdir(folder_path)
    baseline={}
    for file in files:
        full_path=os.path.join(folder_path,file)
        try:
            hash_value=calculate_hash(full_path)
            baseline[file]=hash_value
        except Exception as e:
            print(f"Couldn't read {file}: {e}")
    with open("baseline.json","w") as baseline_files:
        json.dump(baseline,baseline_files)
    print("Baseline created successfully.")

def verify_baseline():
    folder_path=input("Enter folder_path: ")
    files=os.listdir(folder_path)
    new_baseline={}
    for file in files:
        full_path=os.path.join(folder_path,file)
        try:
            hash_value=calculate_hash(full_path)
            new_baseline[file]=hash_value
        except Exception as e:
            print(f"Couldn't read {file}: {e}")
    with open("baseline.json","r") as baseline_files:
        baseline=json.load(baseline_files)
    for file in baseline:
        if file in new_baseline:
            if baseline[file]==new_baseline[file]:
                print(f"{file} is unchanged.")
            else:
                print(f"{file} has been modified.")
        else:
            print(f"{file} is missing.")
    for file in new_baseline:
        if file not in baseline:
            print(f"New file detected: {file}")

print("=========FILE INTEGRITY CHECKER=========")
while True:
    user_choice=int(input("1. Create Baseline\n2. Verify Baseline\n3. Exit\nEnter your choice: "))
    if user_choice==1:
        create_baseline()
    elif user_choice==2:    
        verify_baseline()
    elif user_choice==3:
        print("Thank you for using the File Integrity Checker.")
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")