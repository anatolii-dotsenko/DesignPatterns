from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class FileSystemNode(ABC):
    """
    The base Component class. It declares common operations for both
    Files (Leaf) and Directories (Composite).
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._parent: FileSystemNode | None = None

    @property
    def parent(self) -> FileSystemNode:
        return self._parent # type: ignore

    @parent.setter
    def parent(self, parent: FileSystemNode):
        self._parent = parent

    def add(self, component: FileSystemNode) -> None:
        """
        Base add method. Default is pass (for files).
        """
        pass

    def remove(self, component: FileSystemNode) -> None:
        """
        Base remove method. Default is pass (for files).
        """
        pass

    def is_composite(self) -> bool:
        """
        Returns True if this node can contain other nodes.
        """
        return False

    @abstractmethod
    def get_size_mb(self) -> float:
        """
        The 'Operation'. 
        For a File: Returns its specific size.
        For a Directory: Recursively sums the size of its children.
        """
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """
        Visualizes the structure.
        """
        pass


class File(FileSystemNode):
    """
    The Leaf class. Represents a media file (e.g., .mkv).
    It does the actual work (holding data/size).
    """

    def __init__(self, name: str, size_mb: float) -> None:
        super().__init__(name)
        self.size_mb = size_mb

    def get_size_mb(self) -> float:
        return self.size_mb

    def display(self, indent: int = 0) -> str:
        return f"{'  ' * indent}- {self.name} ({self.size_mb} MB)\n"


class Directory(FileSystemNode):
    """
    The Composite class. Represents a Folder.
    It delegates work to its children and sums up the result.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[FileSystemNode] = []

    def add(self, component: FileSystemNode) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: FileSystemNode) -> None:
        self._children.remove(component)
        component.parent = None # type: ignore

    def is_composite(self) -> bool:
        return True

    def get_size_mb(self) -> float:
        """
        Recursive logic: Sums up the size of all children (files and sub-folders).
        """
        total = 0.0
        for child in self._children:
            total += child.get_size_mb()
        return total

    def display(self, indent: int = 0) -> str:
        """
        Recursive logic: specialized string building.
        """
        result = f"{'  ' * indent}+ [{self.name}] (Total: {self.get_size_mb()} MB)\n"
        for child in self._children:
            result += child.display(indent + 1)
        return result


def client_code(component: FileSystemNode) -> None:
    """
    The client code works with all components via the base interface.
    It doesn't care if it's printing a single file or a massive nested folder.
    """
    print(component.display())


if __name__ == "__main__":
    # ---------------------------------------------------------
    # Building the Structure
    # ---------------------------------------------------------

    # 1. Create the Root
    media_root = Directory("Media")

    # 2. Create the Movies Branch
    movies_dir = Directory("Movies")
    great_movie = File("GreatMovie.mkv", 4500.0) # 4.5 GB
    
    movies_dir.add(great_movie)
    media_root.add(movies_dir)

    # 3. Create the TV Branch
    tv_dir = Directory("TV")
    great_show_dir = Directory("GreatShow")
    season_1 = Directory("s1")

    # Create Episodes (Leaves)
    ep1 = File("ep1.mkv", 850.5)
    ep2 = File("ep2.mkv", 900.0)

    # Assemble TV tree
    season_1.add(ep1)
    season_1.add(ep2)
    great_show_dir.add(season_1)
    tv_dir.add(great_show_dir)
    media_root.add(tv_dir)

    # ---------------------------------------------------------
    # Execution
    # ---------------------------------------------------------
    
    print("--- User opens the 'Media' folder properties ---")
    # The client treats the root directory exactly like a file
    # The recursion happens automatically inside the objects.
    client_code(media_root)

    print(f"Total Media Server Size: {media_root.get_size_mb()} MB")