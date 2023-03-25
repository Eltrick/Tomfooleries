using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using CipherWords;

Random Rnd = new();

string word, encryptedWord, alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXY";
int size;
bool invert = false;

do
{
    word = Wordlist.wordlist[Rnd.Next(0, Wordlist.wordlist.Length)];
} while (word.Length < 7);

int[] numbers = word.Select(x => alpha.IndexOf(x)).ToArray();
List<int> NewNumbers = new();

size = word.Length;

Matrix matrix = new(size, alpha.Length);

do
{
    for (int i = 0; i < Math.Pow(matrix.Size, 2); i++)
        matrix.SetEntry(i / matrix.Size, i % matrix.Size, Rnd.Next(0, alpha.Length));
} while (Matrix.GreatestCommonDivisor(matrix.Determinant(), matrix.Modulus) != 1);

Matrix inverseMatrix = matrix.InverseMatrix();

if(invert)
    for (int i = 0; i < word.Length / size; i++)
        inverseMatrix.MatrixVectorMultiplication(numbers.Skip(i * size).Take(size).ToArray()).ToList().ForEach(x => NewNumbers.Add(x));
else
    for (int i = 0; i < word.Length / size; i++)
        matrix.MatrixVectorMultiplication(numbers.Skip(i * size).Take(size).ToArray()).ToList().ForEach(x => NewNumbers.Add(x));

encryptedWord = string.Join("", NewNumbers.Select(x => alpha[x]));

string information = string.Join("", matrix.MatrixToArray().Select(x => alpha[x]));

Console.WriteLine("Encrypted Word: " + encryptedWord);
Console.WriteLine("Matrix: " + information);
Console.WriteLine("Invert: " + invert.ToString().ToLowerInvariant());