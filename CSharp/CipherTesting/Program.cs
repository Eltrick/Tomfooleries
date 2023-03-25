using CipherWords;
using Eltrick.Ciphers;

RandomNumber randomNumber = new();
ContinuedFractionCipher cipher = new(Wordlist.wordlist[randomNumber.random.Next(0, Wordlist.wordlist.Length)]);

Console.WriteLine(cipher.Encrypt(cipher.Word));
Console.WriteLine(cipher.Word);