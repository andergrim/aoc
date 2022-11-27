orbits = []
outer_edges = []
indirect_orbits = 0
current_path = 0


def get_children(parent):
    global indirect_orbits, current_path
    children = [o[1] for o in orbits if o[0] == parent]
    print(f"{parent} => {children}")
    if len(children) == 0:
        child_nodes = None
        outer_edges.append(parent)
        indirect_orbits += current_path
        current_path = 0
    else:
        child_nodes = {}
        for child in children:
            current_path += 1
            indirect_orbits += 1
            child_nodes[child] = get_children(child)
    return child_nodes


with open("06-sample.txt") as fp:
    # with open("06-input.txt") as fp:
    for line in fp:
        orbit = line.strip().split(")")
        orbits.append((orbit[0], orbit[1]))

print(f"* Have {len(orbits)} orbits")

tree = {"COM": {}}
tree["COM"] = get_children("COM")
print(outer_edges)
print(indirect_orbits)
