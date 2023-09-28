A demo piping a string through a plug-in written in each PDK:
Each plug-in exports a function that takes a string and appends `"Hello from $lang!"` to it. It effectively does this:

```
rust(c(js(go("Hello from Python!"))))
```

Building (note: this won't setup all the dependencies for you):

```bash
make build
```

Running:

```bash
make run
```

```bash
Load plug-ins [Enter]> 
Loaded 6 plugins in 905 ms
Run plug-ins [Enter]> 
Hello from Python!
Hello from Rust!
Hello from C!
Hello From F#!
Hello from Csharp!
Hello from Go!
Hello from JavaScript!
Ran 6 plug-ins in 87.5158 ms
Run plug-ins [Enter]> 
Hello from Python!
Hello from Rust!
Hello from C!
Hello From F#!
Hello from C#!
Hello from Go!
Hello from JavaScript!
Ran 6 plug-ins in 1.6611 ms
```

