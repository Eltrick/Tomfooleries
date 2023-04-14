using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Linq;
using System.Text;
using System.Runtime.CompilerServices;

namespace MyApp
{
    internal class HashingAlgorithm
    {
        public static string MD5Hash(string input)
        {
            MD5 MD5Instance = MD5.Create();
            byte[] bytes = MD5Instance.ComputeHash(Encoding.UTF8.GetBytes(input));
            return BitConverter.ToString(bytes).Replace("-", "").ToLowerInvariant();
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            List<string> possibilities = new List<string>();


        }
    }
}