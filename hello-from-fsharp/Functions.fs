module SampleFSharpPlugin.Functions

// Use of `fixed`.
// Warning FS0009 Uses of this construct may result in the generation of unverifiable .NET IL code.
//
// warning FS0202: This attribute is currently unsupported by the F# compiler.
// Applying it will not achieve its intended effect.
#nowarn "0009"
#nowarn "0202"

open System.Text
open System.Runtime.InteropServices
open Extism


[<UnmanagedCallersOnly>]
let hello () =
    let buffer = Pdk.GetInput()
    let text = Encoding.UTF8.GetString buffer
    Pdk.SetOutput(text + "\nHello From F#!")
    0

