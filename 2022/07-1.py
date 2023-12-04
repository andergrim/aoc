class Node():
    name = ""
    is_dir = False
    size = None
    children = []
    level = 0

    def __init__(self, name, is_dir=None, size=None):
        self.name = name
        if is_dir:
            self.is_dir = is_dir
        elif size is not None:
            self.size = size

    def append(self, node):
        if self.is_dir:
            node.set_level(self.level + 1)
            self.children.append(node)

    def set_level(self, level):
        self.level = level

    def get_children(self, children=None):
        if children is None:
            children = []

        for child in self.children:
            children.append(child)
        return self.children

    def __str__(self):
        return (
            f"{' ' * (self.level * 2)} - {self.name} "
            f"({'dir' if self.is_dir else 'file, size=' + str(self.size)})"
        )


tree = Node("/", True)
l = Node("apa.txt", size=242)
tree.append(l)
tree.append(Node("kaka.dat", size=0))
d = Node("tmp", True)
u = Node("adsf.ext", size=10000)
d.append(u)
tree.append(d)
x = Node("k", size=24)
tree.append(x)

print(tree)
c = tree.get_children()
for ch in c:
    print(ch)
# with open('tmp.txt') as fp:
#     for line in fp:
#         print(line)
