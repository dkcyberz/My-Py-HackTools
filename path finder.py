import os

def find_directories(path, keyword):
    result = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if keyword.lower() in dir.lower():
                result.append(os.path.join(root, dir))
    return result

def main():
    path = input("Enter the directory path: ")
    keyword = input("Enter the keyword to search for: ")
    directories = find_directories(path, keyword)
    
    if directories:
        print(f"Found {len(directories)} directories matching '{keyword}' in '{path}':")
        for directory in directories:
            print(directory)
    else:
        print(f"No directories matching '{keyword}' found in '{path}'.")

if __name__ == "__main__":
    main()
