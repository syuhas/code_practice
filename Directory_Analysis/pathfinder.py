import os

def get_size(path):
    """
    Returns the total size of all files in a directory and its subdirectories.
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


path = r'C:\Users\syuha\Mental Health Association of Maryland'


sizes = {}
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        sizes[fp] = os.path.getsize(fp)


sorted_paths = sorted(sizes, key=sizes.get, reverse=True)


for i in range(25):
    print(f'{sorted_paths[i]} ({sizes[sorted_paths[i]]} bytes)')
