import os
import sys

def scan_directory(target_path):
    if not os.path.isdir(target_path):
        print(f"Error: {target_path} is not a valid directory.")
        return
    for root, dirs, files in os.walk(target_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            print(f"{file_path} -")
            print("```")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f.read())
            except Exception as e:
                print(f"[Error reading file: {e}]")
            
            print("```")
            print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <directory_name>")
    else:
        scan_directory(sys.argv[1])
