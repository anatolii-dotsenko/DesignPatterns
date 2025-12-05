using System;
using System.Collections.Generic;

// Component
public abstract class FileSystemItem
{
    protected string Name;

    public FileSystemItem(string name) => Name = name;

    public abstract void Show(int depth);

    public virtual void Add(FileSystemItem item) 
        => throw new InvalidOperationException($"Cannot add to file: {Name}");

    public virtual void Remove(FileSystemItem item) 
        => throw new InvalidOperationException($"Cannot remove from file: {Name}");
}

// Leaf 1
public class TextFile : FileSystemItem
{
    public TextFile(string name) : base(name) { }

    public override void Show(int depth) 
        => Console.WriteLine(new string('-', depth) + " File: " + Name);
}

// Leaf 2
public class ImageFile : FileSystemItem
{
    public ImageFile(string name) : base(name) { }

    public override void Show(int depth) 
        => Console.WriteLine(new string('-', depth) + " Image: " + Name);
}

// Composite
public class Folder : FileSystemItem
{
    private List<FileSystemItem> _children = new List<FileSystemItem>();

    public Folder(string name) : base(name) { }

    public override void Add(FileSystemItem item) => _children.Add(item);

    public override void Remove(FileSystemItem item) => _children.Remove(item);

    public override void Show(int depth)
    {
        Console.WriteLine(new string('-', depth) + " [Folder] " + Name);
        foreach (var child in _children)
        {
            child.Show(depth + 2);
        }
    }
}

// Client
class Program
{
    static void Main(string[] args)
    {
        // 1. Create Nodes
        var root = new Folder("Root");
        var userFolder = new Folder("User");
        var srcFolder = new Folder("Source");
        
        var resume = new TextFile("Resume.docx");
        var pic = new ImageFile("ProfilePic.png");
        var appCode = new TextFile("App.cs");
        var config = new TextFile("ProjectSettings.cfg");

        // 2. Build Tree
        userFolder.Add(resume);
        userFolder.Add(pic);
        srcFolder.Add(appCode);

        root.Add(config);
        root.Add(userFolder);
        root.Add(srcFolder);

        // 3. Display Tree
        Console.WriteLine("File System Structure:");
        root.Show(1);

        // 4. Test Safety (Leaf constraint)
        try
        {
            resume.Add(new TextFile("Hidden.txt"));
        }
        catch (InvalidOperationException ex)
        {
            Console.WriteLine($"\nError: {ex.Message}");
        }
    }
}