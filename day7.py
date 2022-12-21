from anytree import Node, find, PreOrderIter

class day7:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        root = self.build_tree(input)
        sizes = self.size_of_directories(root)
        size_of_directories = 0
        for d in list(sizes.values()):
            if d < 100000:
                size_of_directories += d
        print(f"The size of directories is: {size_of_directories}")
        return size_of_directories
    
    def build_tree(self, input):
        root = Node("/", type = "directory", size=0)
        cwd = root
        lines = input.split("\n")
        lines.pop(0)
        while len(lines) != 0:
            words = lines.pop(0).split(' ')
            match words[1]:
                case "cd":
                    if words[2] == "..":
                        cwd = cwd.parent
                    else:
                        children = cwd.children 
                        for child in children:
                            if child.name == words[2]:
                                cwd = child
                case "ls":
                    while True:
                        words = lines.pop(0).split(' ')
                        if words[0] != "$" and words[0] == "dir":
                            Node(words[1], parent = cwd, type = "directory", size = 0)
                        else:
                            Node(words[1], parent = cwd, type = "file", size = int(words[0]))
                        if len(lines) == 0 or lines[0][0] == "$":
                            break
        return root

    def size_of_directories(self, root):
        sizes = {}
        for node in PreOrderIter(root):
            if node.type == "directory":
                size = 0
                for child in node.descendants:
                    size += child.size
                sizes.update({node.path : size})
        return sizes

    def star2(self, input):
        root = self.build_tree(input)
        sizes = self.size_of_directories(root)
        smallest_directory_size_to_delete = self.sdntd(sizes)
        print(f"The smallest directory size that needs to be deleted is: {smallest_directory_size_to_delete}")
        return smallest_directory_size_to_delete  

    def sdntd(self, sizes):
        sorted_sizes = list(sizes.values())
        sorted_sizes.sort(reverse=True)
        space_needed = 30000000 - (70000000 - sorted_sizes[0])
        sdntd = sorted_sizes[0]
        for s in sorted_sizes:
            if space_needed - s  > 0:
                break
            sdntd = s
        return sdntd

if __name__ == '__main__':
    with open("input/day7.star1") as f:
        input = f.read()
    d = day7()
    d.star1(input)
    d.star2(input)