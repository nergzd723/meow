using System;
using System.IO;

namespace MeowCS
{
    class Program
    {
        static void read(string abspath)
        {
            string[] line = File.ReadAllLines(abspath);
            foreach (string l in line)
            {
                Console.WriteLine(l);
            }   
        }
        static void Main(string[] args)
        {
            string pathm = "";
            string cwd = Directory.GetCurrentDirectory();
            try
            {
                pathm = args[0];
            }
            catch
            {
                Console.WriteLine("meow utitity!\nUsage:\n meow filetoread");
                Environment.Exit(1);
            }
            if (File.Exists(pathm))
            {
                read(pathm);
            }
            else if (File.Exists(cwd+pathm))
            {
                read(cwd + pathm);
            }
            else if (Directory.Exists(pathm))
            {
                Console.WriteLine("meow: is a directory," + pathm);
            }
            else
            {
                Console.WriteLine("meow: no such file or directory");
            }
        }
    }
}
