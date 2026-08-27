class Node:
    using_set: set[Node]
    users_set: set[Node]
    label: str

    def __repr__(self) -> str:
        return f"Node({self.label})"

    def __init__(self, label: str = "?") -> None:
        self.users_set = set()
        self.using_set = set()
        self.label = label

    def depend_on(self, dependency_node: Node):
        self.using_set.add(dependency_node)
        dependency_node.users_set.add(self)


def render_node(node: Node):
    pass


node_a = Node("a")

node_b = Node("b")
node_c = Node("c")

node_d = Node("d")
node_e = Node("e")

node_c.depend_on(node_a)
node_b.depend_on(node_a)

node_d.depend_on(node_b)
node_e.depend_on(node_c)

render_node(node_a)
