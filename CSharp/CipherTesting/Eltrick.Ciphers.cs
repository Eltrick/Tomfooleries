using CipherWords;
using System.Text.RegularExpressions;
using Emik.Numerics.Fractions;

namespace Eltrick.Ciphers;

// Cipher Machine - Generalised HI
internal class HillCipher
{
    private static readonly RandomNumber _randomNumber = new();

    public int Size { get; private set; }
    public int Modulus { get; private set; }

    private int[,] _matrix;

    public HillCipher(int size, int modulus)
    {
        Size = size;
        Modulus = modulus < 13 ? 13 : modulus > int.MaxValue / 2 ? int.MaxValue / 2 : modulus;
        _matrix = new int[size, size];

        do
        {
            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                    SetEntry(i, j, _randomNumber.random.Next(0, Modulus));
        } while (GreatestCommonDivisor(Determinant(), Modulus) != 1);
    }

    public void SetEntry(int i, int j, int value)
    {
        _matrix[i, j] = value;
    }

    public int GetEntry(int i, int j)
    {
        return _matrix[i, j];
    }

    public HillCipher SubMatrix(int a, int b)
    {
        HillCipher matrix = new HillCipher(Size - 1, Modulus);

        int entry = 0;
        for (int i = 0; i < Size; i++)
            for (int j = 0; j < Size; j++)
            {
                if (i == a || j == b)
                    continue;
                matrix.SetEntry(entry / matrix.Size, entry % matrix.Size, _matrix[i, j]);
                entry++;
            }

        return matrix;
    }

    public int Determinant()
    {
        if (Size == 0)
            return 1;

        int determinant = 0;

        for (int i = 0; i < Size; i++)
            determinant += (_matrix[0, i] * SubMatrix(0, i).Determinant() * (int)Math.Pow(-1, i)).Modulo(Modulus);

        determinant %= Modulus;

        return determinant;
    }

    public HillCipher Cofactor()
    {
        HillCipher matrix = new HillCipher(Size, Modulus);

        for (int i = 0; i < Size; i++)
            for (int j = 0; j < Size; j++)
                matrix.SetEntry(i, j, (SubMatrix(i, j).Determinant() * (int)Math.Pow(-1, i + j)).Modulo(Modulus));

        return matrix;
    }

    public HillCipher Transpose()
    {
        HillCipher matrix = new HillCipher(Size, Modulus);

        for (int i = 0; i < Size; i++)
            for (int j = 0; j < Size; j++)
                matrix.SetEntry(j, i, _matrix[i, j]);

        return matrix;
    }

    public HillCipher Adjugate()
    {
        return Cofactor().Transpose();
    }

    public static int MultiplicativeInverse(int value, int modulus = int.MaxValue)
    {
        for (int i = 0; i < modulus; i++)
            if ((i * value) % modulus == 1)
                return i;
        return -1;
    }

    public HillCipher InverseMatrix()
    {
        return Adjugate().ScalarMultiplication(MultiplicativeInverse(Determinant(), Modulus));
    }

    public HillCipher ScalarMultiplication(int scalar)
    {
        HillCipher matrix = new HillCipher(Size, Modulus);

        for (int i = 0; i < Size; i++)
            for (int j = 0; j < Size; j++)
                matrix.SetEntry(i, j, (_matrix[i, j] * scalar).Modulo(Modulus));

        return matrix;
    }

    public int[] MatrixVectorMultiplication(int[] vector)
    {
        int[] result = new int[Size];

        for (int i = 0; i < Size; i++)
            result[i] = Enumerable.Range(0, Size).Select(x => (GetEntry(i, x) * vector[x]).Modulo(Modulus)).Sum().Modulo(Modulus);

        return result;
    }

    public static int GreatestCommonDivisor(int a, int b)
    {
        while (a * b != 0)
        {
            int s = a % b;
            a = b;
            b = s;
        }
        return new int[] { a, b }.Max();
    }

    public override string ToString()
    {
        return string.Join(", ", _matrix.Cast<int>().ToArray().Select(x => x.ToString()).ToArray());
    }

    public int[] MatrixToArray()
    {
        return _matrix.Cast<int>().ToArray();
    }
}

// Cipher Machine - QR
internal class QuadrantReflectionCipher
{
    private static readonly RandomNumber _randomNumber = new();

    public int QuadrantSize = 5;
    public int StartingQuadrant;

    private string[][,] _quadrants;
    private string[] _keystrings;
    private string _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; 
    private char[] _removedLetters;
    private bool[] _keystringOrder;

    public QuadrantReflectionCipher()
    {
        _quadrants = new string[4][,];
        StartingQuadrant = 0;

        for (int i = 0; i < _quadrants.Length; i++)
            _quadrants[i] = new string[QuadrantSize, QuadrantSize];

        _keystrings = new string[_quadrants.Length];
        _removedLetters = new char[_quadrants.Length];
        _keystringOrder = new bool[_quadrants.Length];

        Initialise();
    }

    private void Initialise()
    {
        // Picks keywords and ignored letters.
        _removedLetters = Enumerable.Range(0, _quadrants.Length).Select(x => _alphabet[_randomNumber.random.Next(0, _alphabet.Length)]).ToArray();
        _keystrings = Enumerable.Range(0, _quadrants.Length).Select(x => Wordlist.wordlist[_randomNumber.random.Next(0, Wordlist.wordlist.Length)]).ToArray();
        _keystringOrder = Enumerable.Range(0, _quadrants.Length).Select(x => _randomNumber.random.Next(0, 2) == 1).ToArray();

        // Removes duplicate characters, keeping their first occurrences.
        for (int i = 0; i < _keystrings.Length; i++)
        {
            string s = "";

            for(int j = 0; j < _keystrings[i].Length; j++)
                if (!s.Contains(_keystrings[i][j].ToString()))
                    s += _keystrings[i][j].ToString();

            _keystrings[i] = s;

            // Removes ignored letter from keyword.
            _keystrings[i] = Regex.Replace(_keystrings[i], $"{_removedLetters[i]}", "");
        }

        // Creates keystrings from keywords.
        for(int i = 0; i < _keystrings.Length; i++)
        {
            string a = _alphabet;
            a = Regex.Replace(a, $"[{_keystrings[i] + _removedLetters[i]}]", "");

            if (_keystringOrder[i])
                _keystrings[i] = a + _keystrings[i];
            else
                _keystrings[i] = _keystrings[i] + a;
        }

        // Fills quadrants with keystrings.
        for(int i = 0; i < _quadrants.Length; i++)
        {
            for(int j = 0; j < QuadrantSize; j++)
                for(int k = 0; k < QuadrantSize; k++)
                    _quadrants[i][j, k] = _keystrings[i][5 * j + k].ToString();
        }
    }

    public string Encrypt(string word, int startingQuadrant)
    {
        string result = "";
        int currentQuadrant = startingQuadrant;

        for(int i = 0; i < word.Length; i++)
        {
            int[] position = Find(_quadrants[currentQuadrant], word[i].ToString());

            if (position[0] == -1)
                result += word[i].ToString();
            else
            {
                if (currentQuadrant % 2 == 0)
                    result += _quadrants[(currentQuadrant - 1).Modulo(_quadrants.Length)][QuadrantSize - 1 - position[0], position[1]];
                else
                    result += _quadrants[(currentQuadrant - 1).Modulo(_quadrants.Length)][position[0], QuadrantSize - 1 - position[1]];
            }

            currentQuadrant = (currentQuadrant - 1).Modulo(_quadrants.Length);
        }

        return result;
    }

    public string Decrypt(string word, int startingQuadrant)
    {
        string result = "";
        int currentQuadrant = (startingQuadrant - 1).Modulo(_quadrants.Length);

        for(int i = 0; i < word.Length; i++)
        {
            int[] position = Find(_quadrants[currentQuadrant], word[i].ToString());

            if (position[0] == -1)
                result += word[i].ToString();
            else
            {
                if (currentQuadrant % 2 == 1)
                    result += _quadrants[(currentQuadrant + 1).Modulo(_quadrants.Length)][QuadrantSize - 1 - position[0], position[1]];
                else
                    result += _quadrants[(currentQuadrant + 1).Modulo(_quadrants.Length)][position[0], QuadrantSize - 1 - position[1]];
            }

            currentQuadrant = (currentQuadrant + 1).Modulo(_quadrants.Length);
        }

        return result;
    }

    public string GetKeystrings()
    {
        return string.Join(";", _keystrings);
    }

    private static int[] Find(string[,] quadrant, string letter)
    {
        for(int i = 0; i < (int)Math.Sqrt(quadrant.Length); i++)
            for (int j = 0; j < (int)Math.Sqrt(quadrant.Length); j++)
                if (quadrant[i, j] == letter)
                    return new[] { i, j };
        return new[] { -1, -1 };
    }
}

// Only a funny test thing. Might be used somewhere.
internal class ContinuedFractionCipher
{
    public string Word;

    public ContinuedFractionCipher(string word)
    {
        Word = word;
        Encrypt(Word);
    }
    
    public Fraction Encrypt(string word)
    {
        Fraction result = new(0, 1);

        char[] reversedWord = word.ToCharArray();
        Array.Reverse(reversedWord);

        string evaluate = string.Join("", reversedWord.Select(x => x.ToString()).ToArray());
        
        for (int i = 0; i < evaluate.Length; i++)
            result = 1 / (new Fraction(evaluate[i] - 'A' + 1, 1) + result);

        return result;
    }
}

static class Operators
{
    internal static int Modulo(this int i, int j) => ((i % j) + j) % j;
}

internal class RandomNumber
{
    internal readonly Random random = new();
}
