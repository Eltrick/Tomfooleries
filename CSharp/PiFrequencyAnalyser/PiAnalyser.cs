namespace PiFrequencyAnalyser
{
    public class PiAnalyser
    {
        static void Main(string[] args)
        {
            StreamReader PiFile = new("pi.txt");
            char[] pi = PiFile.ReadLine().ToCharArray();
            int[] occurences = new int[10];
            string output = "";
            bool _isFound = false;

            for (ulong i = 0; i < (ulong)pi.Length; i++)
            {
                occurences[pi[i] - '0']++;
                output += pi[i];
                if (occurences.Distinct().Count() == 1 && occurences.All(x => x != 0))
                {
                    _isFound = true;
                    var found = output.TakeLast(15);
                    string res = "";
                    foreach (char f in found)
                        res += f;
                    Console.WriteLine(res);
                    Console.WriteLine("Occurence found at position " + i.ToString());
                    Console.ReadLine();
                    break;
                }
            }
            if (!_isFound)
            {
                Console.WriteLine("Found no position in the first " + pi.Length.ToString() + " digits of pi.");
                Console.ReadLine();
            }
        }
    }
}