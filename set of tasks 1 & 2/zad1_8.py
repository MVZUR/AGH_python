class TreeNode:
    """
    Klasa reprezentująca węzeł drzewa.
    """
    def __init__(self, value=None):
        self.value = value  # Wartość przechowywana w węźle
        self.children = []  # Lista dzieci węzła
        self.edges = []  # Lista wartości lub oznaczeń krawędzi

    def add_child(self, child_node, edge_value=None):
        """
        Dodaje dziecko do węzła z opcjonalną wartością krawędzi.
        :param child_node: Obiekt TreeNode
        :param edge_value: Wartość lub oznaczenie krawędzi
        """
        self.children.append(child_node)
        self.edges.append(edge_value)

    def __str__(self, level=0):
        """
        Zwraca czytelny string reprezentujący węzeł i jego poddrzewo.
        """
        result = "  " * level + f"Node(value={self.value})\n"
        for i, child in enumerate(self.children):
            edge_info = f" (edge: {self.edges[i]})" if self.edges[i] is not None else ""
            result += "  " * level + f"  -> {edge_info}\n"
            result += child.__str__(level + 1)
        return result


class Tree:
    """
    Klasa reprezentująca strukturę drzewa.
    """
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value)

    def traverse(self):
        """
        Funkcja przechodzenia wszystkich węzłów drzewa (DFS).
        :return: Lista wartości węzłów w kolejności odwiedzin.
        """
        visited = []

        def dfs(node):
            if node is None:
                return
            visited.append(node.value)  # Odwiedź węzeł
            for child in node.children:
                dfs(child)

        dfs(self.root)
        return visited

    def __str__(self):
        """
        Zwraca string reprezentujący całe drzewo.
        """
        return self.root.__str__()
    
# Przykład użycia
if __name__ == "__main__":
    # Tworzenie drzewa
    tree = Tree("Root")

    # Dodawanie dzieci do korzenia
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    tree.root.add_child(child1, edge_value="Edge1")
    tree.root.add_child(child2, edge_value="Edge2")

    # Dodawanie dzieci do pierwszego dziecka
    child1_1 = TreeNode("Child1.1")
    child1_2 = TreeNode("Child1.2")
    child1.add_child(child1_1, edge_value="Edge1.1")
    child1.add_child(child1_2, edge_value="Edge1.2")

    # Dodawanie dziecka do drugiego dziecka
    child2_1 = TreeNode("Child2.1")
    child2.add_child(child2_1, edge_value="Edge2.1")

    # Wypisywanie drzewa
    print("Drzewo:")
    print(tree)

    # Przechodzenie drzewa
    print("\nPrzechodzenie drzewa (DFS):")
    print(tree.traverse())
