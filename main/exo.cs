using System;
using System.IO;
using System.Linq;

namespace exocs
{
    class Exo
    {
        static protected string dest = "";
        static protected string arg = "";
        static void Main(string[] args)
        {
            if (args.Contains(">"))
            {
                try
                {
                    arg = args[0];
                    dest = args[2];
                }
                catch
                {
                    Console.WriteLine("exo: no destination availmble");
                    Environment.Exit(1);
                }
                if (File.Exists(dest))
                {
                    File.WriteAllText(dest, arg);
                }

            }
            else
            {
                if (arg != "")
                {
                    Console.WriteLine(arg);
                }
                else
                {
                    Console.WriteLine("Exo utility\nPart of MEOWutils");
                }

            }
        }
    }
}
