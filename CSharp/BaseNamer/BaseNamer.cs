using System.IO;
using System.Text.RegularExpressions;

namespace BaseNamer
{
    public class BaseNamingScript
    {
        private static Dictionary<int, string> _basePrefixes = new Dictionary<int, string>()
        {
            {2, "bi"},
            {3, "tri"},
            {4, "tetra"},
            {5, "penta"},
            {6, "hexa"},
            {7, "hepta"},
            {8, "octo"},
            {9, "enna"},
            {10, "deca"},
            {11, "leva"},
            {12, "doza"},
            {13, "baker"},
            {16, "tesser"},
            {17, "mal"},
            {20, "icosi"},
            {36, "feta"},
            {100, "hecto"},
        };

        private static Dictionary<int, string> _baseSuffixes = new Dictionary<int, string>()
        {
            {10, "gesimal"},
            {13, "ker's dozenal"}
        };

        private static Dictionary<int, string> _baseBaseNames = new Dictionary<int, string>()
        {
            {0, "nullary" },
            {1, "unary" },
            {2, "binary"},
            {3, "trinary"},
            {4, "quaternary"},
            {5, "quinary"},
            {6, "seximal"},
            {7, "septimal"},
            {8, "octal"},
            {9, "nonary"},
            {10, "decimal"},
            {11, "elevenary"},
            {12, "dozenal"},
            {13, "baker's dozenal"},
            {16, "hex"},
            {17, "suboptimal"},
            {20, "vigesimal"},
            {36, "niftimal"},
            {100, "centesimal"}
        };

        static void Main(string[] args)
        {
            //StreamWriter writer = new StreamWriter("Names.txt");

            //for (int i = 0; i < 10000; i++)
            //    writer.WriteLine(i.ToString() + ": " + NumberToName(i));

            while(true)
            {
                Console.WriteLine("Input base: ");
                int? number = int.Parse(Console.ReadLine());
                number = number == null ? 0 : number;
                Console.WriteLine("The Misalian name for it is: " + NumberToName((int)number));
            }
        }

        static string NumberToName(int number, bool isSuffix = false, int depth = 0)
        {
            if (_baseBaseNames.ContainsKey(number))
                return (!isSuffix && depth != 0) ? _baseBaseNames[number] + "-" : _baseBaseNames[number];

            List<int> lowerFactors = Factorise(number);
            Dictionary<int, string> options = new Dictionary<int, string>();

            foreach (int factor in lowerFactors)
            {
                if (factor == 1)
                {
                    options.Add(number - 1, "un-" + NumberToName(number - 1, true, depth++));
                    continue;
                }
                options.Add(factor, NumberToPrefix(factor) + "-" + NumberToSuffix(number / factor));
            }

            return !isSuffix ? FixString(options.First(x => RootsInName(x.Value) == options.Min(y => RootsInName(y.Value))).Value) : FixStringTemporary(options.First(x => RootsInName(x.Value) == options.Min(y => RootsInName(y.Value))).Value);
        }

        static int RootsInName(string name)
        {
            string r = name.Replace("-", "");
            return name.Length - r.Length + 1;
        }

        static string NumberToPrefix(int number, int depth = 0)
        {
            if (_basePrefixes.ContainsKey(number))
                return _basePrefixes[number];

            List<int> lowerFactors = Factorise(number);
            Dictionary<int, string> options = new Dictionary<int, string>();
            foreach (int factor in lowerFactors)
            {
                depth++;
                if (factor == 1)
                {
                    options.Add(number - 1, "hen-" + NumberToPrefix(number - 1, depth) + (depth == 0 ? "-sna" : "sna"));
                    continue;
                }
                options.Add(factor, FixStringTemporary(NumberToPrefix(factor, depth) + "-" + NumberToPrefix(number / factor, depth)));
            }

            return options.First(x => RootsInName(x.Value) == options.Min(y => RootsInName(y.Value))).Value;
        }

        static string NumberToSuffix(int number)
        {
            if (_baseSuffixes.ContainsKey(number))
                return _baseSuffixes[number];
            return NumberToName(number, true);
        }

        static string FixString(string brokenString)
        {
            return Regex.Replace(Regex.Replace(Regex.Replace(brokenString, "i-[iu]", "i"), "[ao]-([aeiou])", "$1"), "-", "");
        }

        static string FixStringTemporary(string brokenString)
        {
            return Regex.Replace(Regex.Replace(brokenString, "i-[iu]", "-i"), "[ao]-([aeiou])", "-$1");
        }

        static List<int> Factorise(int number)
        {
            List<int> factors = new List<int>();
            int rangeToCheck = (int)Math.Sqrt(number);

            for (int i = rangeToCheck; i > 1; i--)
                if (number % i == 0)
                    factors.Add(i);

            if (factors.Count == 0)
                factors.Add(1);

            return factors;
        }
    }
}