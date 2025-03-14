
class Canvas:
    def __init__(self) -> None:
        pass

class TreeType:
    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture
    def draw(self, canvas: Canvas, x: int, y: int) -> None:
        print(f"Drawing {self.name} at ({x}, {y})")

    def __str__(self) -> str:
        # print instance reference
        return f"{self.__class__.__name__} at {id(self)}"
        

class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x = x
        self.y = y
        self.tree_type = tree_type
        
    def draw(self, canvas: Canvas) -> None:
        self.tree_type.draw(canvas, self.x, self.y)

class TreeFactory:
    def __init__(self) -> None:
        self.tree_types = {}

    def get_tree_type(self, name: str, color: str, texture: str) -> TreeType:
        if (name, color, texture) not in self.tree_types:
            self.tree_types[(name, color, texture)] = TreeType(name, color, texture)
        return self.tree_types[(name, color, texture)]
    
class Forest:
    def __init__(self) -> None:
        self.trees = []

    def add_tree(self, tree: Tree) -> None:
        self.trees.append(tree)
    
    # show all trees
    def show_trees(self) -> None:
        for tree in self.trees:
            tree.draw(Canvas())
        
if __name__ == "__main__":
    forest = Forest()
    tree_factory = TreeFactory()
    tree_type = tree_factory.get_tree_type("Oak", "Green", "Rough")
    tree = Tree(10, 10, tree_type)
    print(tree.tree_type)
    tree2 = Tree(20, 20, tree_type)
    print(tree2.tree_type)
    forest.add_tree(tree)
    forest.add_tree(tree2)
    forest.show_trees()
