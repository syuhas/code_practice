import os

def longest_file_path(directory):
    longest_path = ''
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if len(path) > len(longest_path):
                longest_path = path
    return longest_path

directory = r'C:\Users\syuha\Mental Health Association of Maryland\CQT - Documents'
longest_path = longest_file_path(directory)
print(longest_path)
