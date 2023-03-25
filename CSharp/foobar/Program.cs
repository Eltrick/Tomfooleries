using System;
using System.Collections.Generic;
using System.Linq;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> MinefieldString = Console.ReadLine()
                .Split(" ")
                .ToList();

            List<string> BombInfoString = Console.ReadLine()
                .Split(" ")
                .ToList();

            List<int> Minefield = new List<int>();
            List<int> BombInfo = new List<int>();

            if (BombInfoString.Count == 1)
            {
                Minefield = MinefieldString.Select(x => int.Parse(x)).ToList();
                Console.WriteLine(Minefield.Sum());
            }
            else
            {
                Minefield = MinefieldString.Select(x => int.Parse(x)).ToList();
                BombInfo = BombInfoString.Select(x => int.Parse(x)).ToList();

                for (int i = 0; i < Minefield.Where(x => x == BombInfo[0]).ToList().Count; i++)
                {
                    if (Minefield.Count == 0)
                        continue;

                    List<int> BombPositions = Enumerable.Range(0, Minefield.Count).Where(x => Minefield[x] == BombInfo[0]).ToList();
                    Minefield.RemoveRange(Math.Max(0, BombPositions[0] - BombInfo[1]), Math.Min(BombInfo[1] * 2 + 1, Minefield.Count - BombPositions[0] + BombInfo[1]));
                    i = -1;
                }
                Console.WriteLine(Minefield.Sum());
            }
        }
    }
}