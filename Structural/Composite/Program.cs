using System;
using System.Collections.Generic;

// --------------------------------------------------------------------------
// 1. Component
// --------------------------------------------------------------------------
/// <summary>
/// The base Component that declares common operations for both simple and 
/// complex objects of the composition.
/// </summary>
public abstract class FileSystemItem
{
    protected string Name;

    public FileSystemItem(string name)
    {
        this.Name = name;
    }

    // The common operation. 'depth' is used for pretty printing the tree structure.
    public abstract void Show(int depth);

    // Standard Composite Management Methods.
    // We define them here to provide a default "Leaf" behavior (throwing exceptions),
    // which aligns with the "Transparency" variant of the pattern.
    public virtual void Add(FileSystemItem item)
    {
        throw new InvalidOperationException($"Cannot add items to a file ({this.Name}).");
    }

    public virtual void Remove(FileSystemItem item)
    {
        throw new InvalidOperationException($"Cannot remove items from a file ({this.Name}).");
    }
}

// --------------------------------------------------------------------------
// 2. Leaves (Concrete Files)
// --------------------------------------------------------------------------
/// <summary>
/// Represents a Leaf. A Leaf has no children.
/// </summary>
public class TextFile : FileSystemItem
{
    public TextFile(string name) : base(name) { }

    public override void Show(int depth)
    {
        Console.WriteLine(new string('-', depth) + " File: " + Name);
    }
    
    // We do not override Add/Remove, so they will use the Base implementation 
    // and throw an Exception if called.
}

public class ImageFile : FileSystemItem
{
    public ImageFile(string name) : base(name) { }

    public override void Show(int depth)
    {
        Console.WriteLine(new string('-', depth) + " Image: " + Name);
    }
}

// --------------------------------------------------------------------------
// 3. Composite (Folder)
// --------------------------------------------------------------------------
/// <summary>
/// Represents a Composite. It has children (Files or other Folders) and
/// delegates operations to them.
/// </summary>
public class Folder : FileSystemItem
{
    // A list to store children (leaves or other composites)
    private List<FileSystemItem> _children = new List<FileSystemItem>();

    public Folder(string name) : base(name) { }

    public override void Add(FileSystemItem item)
    {
        _children.Add(item);
    }

    public override void Remove(FileSystemItem item)
    {
        _children.Remove(item);
    }

    // The core recursion logic:
    // 1. Perform work for the folder itself
    // 2. Delegate work to all children
    public override void Show(int depth)
    {
        // 1. Print Folder Name
        Console.WriteLine(new string('-', depth) + " [Folder] " + Name);

        // 2. Iterate over children and call their Show() method
        foreach (var child in _children)
        {
            // Increase depth for indentation
            child.Show(depth + 2);
        }
    }
}

// --------------------------------------------------------------------------
// 4. Client Code
// --------------------------------------------------------------------------
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("=== Composite Pattern File System Demo ===\n");

        // 1. Create Leaf nodes (Files)
        FileSystemItem file1 = new TextFile("Resume.docx");
        FileSystemItem file2 = new ImageFile("ProfilePic.png");
        FileSystemItem file3 = new TextFile("ProjectSettings.cfg");
        FileSystemItem file4 = new TextFile("App.cs");

        // 2. Create Composite nodes (Folders)
        // Note: We use the base type 'FileSystemItem' for variables, 
        // but we might need to cast to 'Folder' to access Add/Remove if 
        // using strict type checking settings, though our base class allows it.
        FileSystemItem root = new Folder("Root");
        FileSystemItem userFolder = new Folder("User");
        FileSystemItem srcFolder = new Folder("Source");

        Console.WriteLine("[System] Building the file tree structure...");

        // 3. Build the tree structure
        // Structure:
        // Root
        //  |-- ProjectSettings.cfg
        //  |-- User
        //       |-- Resume.docx
        //       |-- ProfilePic.png
        //  |-- Source
        //       |-- App.cs
        
        try
        {
            // Add files to User folder
            userFolder.Add(file1);
            userFolder.Add(file2);

            // Add files to Source folder
            srcFolder.Add(file4);

            // Add everything to Root
            root.Add(file3);       // Add file directly to root
            root.Add(userFolder);  // Add sub-folder
            root.Add(srcFolder);   // Add sub-folder

            // 4. Client works with the entire tree via the common interface
            Console.WriteLine("\n[Client] Displaying File System Hierarchy:");
            root.Show(1);

            // 5. Demonstrate Constraints (Trying to add a child to a Leaf)
            Console.WriteLine("\n[Client] Attempting to add a file inside a text file...");
            file1.Add(new TextFile("Hidden.txt"));
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine($"[Error] {ex.Message}");
        }

        Console.WriteLine("\n=== Demo Complete ===");
    }
}