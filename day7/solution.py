class Dir:
    def __init__(self, name, path, parent=None):
        self.name = name
        self.path = path
        self.parent = parent
        self.size = 0


def parse_input_file():
    for line in open('input.txt').readlines():
        yield line.strip()

def enhance_folder_size(folder, size):
    folder.size += size
    if folder.parent:
        enhance_folder_size(folder.parent, size) # enhance folders sizes recursively to the top

if __name__ == '__main__':
    dirs = {'/': Dir('/', '/')} # dirs.values() will return list of Dir instances
    current_folder = None
    for line in parse_input_file():
        if line[:4] == '$ cd': # cd command changes current folder
            if line[5:] != '..':
                try:
                    current_folder = dirs['/'.join([current_folder.path, line[5:]])]
                except AttributeError: # handling root case
                    current_folder = dirs['/']
            else:
                current_folder = current_folder.parent
        elif line[:4] == '$ ls': # ls can be dismissed
            continue
        elif line[:3] == 'dir': # create new Dir, add to 'dirs' under key with name
            path = "/".join([current_folder.path, line[4:]])
            if path not in dirs:
                dirs[path] = Dir(line[4:], path, current_folder)
        else: # handle filesize information
            enhance_folder_size(current_folder, int(line.split(' ')[0]))

    print(sum([folder.size for folder in dirs.values() if folder.size <= 100_000]))
