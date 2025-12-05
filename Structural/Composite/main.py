from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# --------------------------------------------------------------------------
# Component
# --------------------------------------------------------------------------
class FileSystemNode(ABC):
    """
    The Component interface declares common operations for both
    simple and complex objects of a composition.
    
    Per your diagram, Add, Remove, and GetChild are defined here.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def add(self, component: FileSystemNode) -> None:
        """
        Default behavior for Component: Leaf nodes can't add children.
        """
        pass

    def remove(self, component: FileSystemNode) -> None:
        """
        Default behavior for Component: Leaf nodes can't remove children.
        """
        pass

    def get_child(self, index: int) -> FileSystemNode | None:
        """
        Default behavior for Component: Leaf nodes have no children to retrieve.
        """
        return None

    @abstractmethod
    def get_size_mb(self) -> float:
        """
        This corresponds to 'Operation()' in the diagram.
        """
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Helper for visualization (not in diagram but essential for demo)."""
        pass


# --------------------------------------------------------------------------
# Leaf
# --------------------------------------------------------------------------
class File(FileSystemNode):
    """
    The Leaf class. It implements Operation() (get_size_mb).
    It inherits Add/Remove/GetChild from Component but uses the default 
    'do nothing' implementation, effectively making it a leaf.
    """

    def __init__(self, name: str, size_mb: float) -> None:
        super().__init__(name)
        self.size_mb = size_mb

    def get_size_mb(self) -> float:
        return self.size_mb

    def display(self, indent: int = 0) -> str:
        return f"{'  ' * indent}- {self.name} ({self.size_mb} MB)\n"


# --------------------------------------------------------------------------
# Composite
# --------------------------------------------------------------------------
class Directory(FileSystemNode):
    """
    The Composite class.
    It overrides Add, Remove, GetChild, and Operation.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        # 'children' aggregation shown in diagram
        self._children: List[FileSystemNode] = []

    def add(self, component: FileSystemNode) -> None:
        self._children.append(component)

    def remove(self, component: FileSystemNode) -> None:
        self._children.remove(component)

    def get_child(self, index: int) -> FileSystemNode | None:
        """
        Corresponds to GetChild(int) in the diagram.
        Allows access to specific child nodes by index.
        """
        if 0 <= index < len(self._children):
            return self._children[index]
        return None

    def get_size_mb(self) -> float:
        """
        Corresponds to the diagram note: 'forall g in children g.Operation()'
        """
        total = 0.0
        for child in self._children:
            total += child.get_size_mb()
        return total

    def display(self, indent: int = 0) -> str:
        result = f"{'  ' * indent}+ [{self.name}] (Total: {self.get_size_mb()} MB)\n"
        for child in self._children:
            result += child.display(indent + 1)
        return result


# --------------------------------------------------------------------------
# Client
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Build the Tree
    media_root = Directory("Media")
    
    movies_dir = Directory("Movies")
    movies_dir.add(File("GreatMovie.mkv", 4500.0))
    
    tv_dir = Directory("TV")
    season_1 = Directory("s1")
    season_1.add(File("ep1.mkv", 850.0))
    season_1.add(File("ep2.mkv", 900.0))
    
    tv_dir.add(season_1)
    
    media_root.add(movies_dir)
    media_root.add(tv_dir)

    # 2. Visualize
    print("--- Structure ---")
    print(media_root.display())

    # 3. Demo of GetChild(int) from the diagram
    print("--- Testing GetChild(int) ---")
    
    # Get the 2nd child of media_root (index 1), which is 'TV'
    child_node = media_root.get_child(1) 
    
    if child_node:
        print(f"Retrieved Child at index 1: {child_node.name}")
        
        # Get the 1st child of 'TV' (index 0), which is 's1'
        grand_child = child_node.get_child(0)
        if grand_child:
             print(f"Retrieved Grandchild at index 0: {grand_child.name}")
             print(f"Size of Grandchild: {grand_child.get_size_mb()} MB")