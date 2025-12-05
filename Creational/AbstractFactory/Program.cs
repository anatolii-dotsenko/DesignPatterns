using System;

// --------------------------------------------------------------------------
// 1. Abstract Products
// --------------------------------------------------------------------------
public abstract class Knight //A
{
    public abstract void Attack();
}

public abstract class Mage //B
{
    public abstract void CastSpell();
}

// public abstract class Archer
// {
//     public abstract void Shoot();
// }

// --------------------------------------------------------------------------
// 2. Concrete Products (Fire Theme)
// --------------------------------------------------------------------------
public class FireKnight : Knight //A1
{
    public override void Attack() 
        => Console.WriteLine("Fire Knight strikes with a flaming sword! (Burn Damage)");
}

public class FireMage : Mage //B1
{
    public override void CastSpell() 
        => Console.WriteLine("Fire Mage casts a fireball! (Explosion)");
}

// public class FireArcher : Archer
// {
//     public override void Shoot() 
//         => Console.WriteLine("Fire Archer shoots a burning arrow! (DoT)");
// }

// --------------------------------------------------------------------------
// 3. Concrete Products (Ice Theme)
// --------------------------------------------------------------------------
public class IceKnight : Knight //A2
{
    public override void Attack() 
        => Console.WriteLine("Ice Knight strikes with a frost blade! (Slow Effect)");
}

public class IceMage : Mage //B2
{
    public override void CastSpell() 
        => Console.WriteLine("Ice Mage casts a blizzard! (Area Freeze)");
}

// public class IceArcher : Archer
// {
//     public override void Shoot() 
//         => Console.WriteLine("Ice Archer shoots a crystal arrow! (Piercing)");
// }

// --------------------------------------------------------------------------
// 4. Abstract Factory
// --------------------------------------------------------------------------
public abstract class UnitFactory
{
    public abstract Knight CreateKnight(); //CreateProductA()
    public abstract Mage CreateMage(); //CreateProductB()
    // public abstract Archer CreateArcher();
}

// --------------------------------------------------------------------------
// 5. Concrete Factories
// --------------------------------------------------------------------------
public class FireUnitFactory : UnitFactory //ConcreteFactory1
{
    public override Knight CreateKnight() => new FireKnight(); //CreateProductA()
    public override Mage CreateMage() => new FireMage(); //CreateProductB()
    // public override Archer CreateArcher() => new FireArcher();
}

public class IceUnitFactory : UnitFactory //ConcreteFactory2
{
    public override Knight CreateKnight() => new IceKnight(); //CreateProductA()
    public override Mage CreateMage() => new IceMage(); //CreateProductB()
    // public override Archer CreateArcher() => new IceArcher();
}

// --------------------------------------------------------------------------
// 6. Client Code
// --------------------------------------------------------------------------
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("=== Abstract Factory Pattern Demo ===\n");

        // Scenario 1: The user selects the Fire Faction
        Console.WriteLine("[System] Spawning Fire Faction units...");
        UnitFactory fireFactory = new FireUnitFactory();
        SpawnAndActivateArmy(fireFactory);

        Console.WriteLine();

        // Scenario 2: The user selects the Ice Faction
        Console.WriteLine("[System] Spawning Ice Faction units...");
        UnitFactory iceFactory = new IceUnitFactory();
        SpawnAndActivateArmy(iceFactory);

        Console.WriteLine("\n=== Demo Complete ===");
    }

    // The client code works with factories and products only through abstract types
    static void SpawnAndActivateArmy(UnitFactory factory)
    {
        // Create units using the factory
        Knight knight = factory.CreateKnight();
        Mage mage = factory.CreateMage();
        // Archer archer = factory.CreateArcher();

        // Use the units
        knight.Attack();
        mage.CastSpell();
        // archer.Shoot();
    }
}