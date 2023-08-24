using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Linq;
using System.Text;
using System.Numerics;

namespace Eltrick.Testing
{
    internal class MathQuestionMark
    {
        static readonly BigInteger FastSqrtSmallNumber = 4503599761588223UL;

        static BigInteger SqrtFast(BigInteger value)
        {
            if (value <= FastSqrtSmallNumber) // small enough for Math.Sqrt() or negative?
            {
                if (value.Sign < 0) throw new ArgumentException("Negative argument.");
                return (ulong)Math.Sqrt((ulong)value);
            }

            BigInteger root; // now filled with an approximate value
            int byteLen = value.ToByteArray().Length;
            if (byteLen < 128) // small enough for direct double conversion?
            {
                root = (BigInteger)Math.Sqrt((double)value);
            }
            else // large: reduce with bitshifting, then convert to double (and back)
            {
                root = (BigInteger)Math.Sqrt((double)(value >> (byteLen - 127) * 8)) << (byteLen - 127) * 4;
            }

            for (; ; )
            {
                var root2 = value / root + root >> 1;
                if ((root2 == root || root2 == root + 1) && IsSqrt(value, root)) return root;
                root = value / root2 + root2 >> 1;
                if ((root == root2 || root == root2 + 1) && IsSqrt(value, root2)) return root2;
            }
        }

        static bool IsSqrt(BigInteger value, BigInteger root)
        {
            var lowerBound = root * root;

            return value >= lowerBound && value <= lowerBound + (root << 1);
        }

        public static bool IsPrime(BigInteger n)
        {
            for(var i = 2; i < SqrtFast(n); i++)
                if (n % i == 0)
                    return false;

            return true;
        }
    }

    class Program
    {
        private static BigInteger N;

        private static int[] _pEncode = { 514, 515, 522, 523, 519, 514, 515, 513, 513, 513, 514, 522, 518, 518, 522, 514, 514, 516, 523, 523, 519, 514, 522, 522, 516, 519, 513, 522, 512, 512, 518, 517, 512, 513, 518, 512, 518, 513, 512, 516, 515, 513, 513, 516, 518, 514, 517, 522, 516, 519, 523, 514, 515, 523, 513, 515, 512, 514, 513, 519, 517, 518, 513, 517, 513, 523, 514, 518, 522, 519, 518, 522, 518, 522, 518, 513, 522, 516, 514, 513, 516, 514, 516, 514, 513, 519, 514, 514, 514, 523, 519, 523, 512, 515, 518, 522, 515, 516, 523, 522, 512, 512, 522, 518, 517, 516, 515, 514, 515, 514, 523, 514, 512, 518, 519, 522, 516, 516, 522, 516, 514, 517, 514, 517, 523, 523, 513, 518, 512, 515, 518, 518, 514, 519, 512, 522, 517, 518, 516, 518, 515, 517, 523, 519, 515, 519, 519, 519, 518, 519, 512, 516, 514, 522, 516 };
        private static int[] _qEncode = { 514, 514, 523, 519, 517, 523, 516, 518, 518, 523, 518, 522, 518, 516, 512, 518, 514, 517, 515, 518, 516, 516, 523, 513, 515, 517, 512, 517, 517, 523, 514, 523, 517, 523, 517, 517, 513, 519, 519, 515, 512, 519, 517, 515, 522, 512, 519, 517, 516, 516, 517, 516, 513, 517, 517, 514, 516, 522, 522, 516, 517, 512, 515, 512, 523, 518, 516, 514, 517, 513, 523, 517, 518, 522, 517, 523, 518, 522, 512, 518, 522, 522, 523, 514, 518, 523, 518, 517, 515, 516, 512, 512, 516, 518, 516, 513, 522, 523, 518, 512, 515, 522, 512, 516, 518, 516, 515, 517, 522, 516, 522, 514, 514, 514, 523, 518, 512, 518, 515, 515, 522, 523, 522, 522, 522, 518, 516, 523, 523, 523, 513, 514, 517, 512, 513, 514, 519, 518, 516, 519, 518, 523, 518, 514, 518, 514, 514, 519, 522, 513, 522, 513, 523, 515, 522 };

        static void Main(string[] args)
        {
            N = BigInteger.Parse("130127292446949390212867735855086334421393298489352915445932034098974310494854685420188208182244644737973417566696954612517320009326051854904532961110247688311376993922989760554696056080388241259670599567937477306283613224095383043997900439331609449744523632839529123448169800791720798913702566069153373216373");

            for (int i = 100; i < 1000; i++)
            {
                int[] p = new int[_pEncode.Length];
                int[] q = new int[_qEncode.Length];

                for(int v = 0; v < _pEncode.Length; v++)
                {
                    p[v] = _pEncode[v] ^ i;
                    q[v] = _qEncode[v] ^ i;
                }

                BigInteger pNum = BigInteger.Parse(string.Join("", p));
                BigInteger qNum = BigInteger.Parse(string.Join("", q));
                
                if(MathQuestionMark.IsPrime(pNum) && MathQuestionMark.IsPrime(qNum) && pNum * qNum == N)
                {
                    Console.WriteLine("Broken: " + pNum.ToString() + "; " + qNum.ToString());
                }
            }
        }
    }
}