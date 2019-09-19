using System;
namespace HelloApp
{   class GetHello { public static string secretmessage(){ string hello = "Hello world!"; string result = "";foreach (char element in hello){result = result + element;}return result;}} class DoWrite{public static void arn(string input) => Console.WriteLine(input);}class Program{static void Main(string[] args){string smm = GetHello.secretmessage();DoWrite.arn(smm);}}}
