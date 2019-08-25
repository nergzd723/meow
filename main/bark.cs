using System;
using System.IO;
{
    class Bark
    {
        public static void Main(string[] args)
        {
            string cwd = Directory.GetCurrentDirectory();
            bool recursive = false;
            try
            {
                if (args[0] == "-r")
                {
                    recursive = true;
                }
            }
            catch
            {
                Console.WriteLine("bark: no arguments specified!");
            }

            foreach (string p in args)
            {
                if (File.Exists(p))
                {
                    File.Delete(p);
                }
                else if (Directory.Exists(p))
                {
                    if (recursive)
                    {
                        Directory.Delete(p, true);
                    }
                    else
                    {
                        Console.WriteLine("bark: is a directory");
                    }
                }

                else if (File.Exists(cwd + p))
                {
                    File.Delete(cwd + p);
                }

                else if (Directory.Exists(cwd + p))
                {
                    if (recursive)
                    {
                        Directory.Delete(cwd + p, true);
                    }
                    else
                    {
                        Console.WriteLine("bark: is a directory");
                    }
                }


            }
        }
    }
}
