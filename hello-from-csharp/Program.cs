using System.Runtime.InteropServices;
using Extism;
using System;

//TODO this ensures a main is exported
var _x = 123;

namespace Functions
{
    public class Functions
    {
        [UnmanagedCallersOnly(EntryPoint = "hello")]
        public static int Hello()
        {
            var result = Pdk.GetInputString();
            Pdk.SetOutput(result + "\nHello from C#!");
            return 0;
        }
    }
}
