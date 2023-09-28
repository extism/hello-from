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
Loaded 4 plugins in 163 ms
Run plug-ins [Enter]> 
Hello from Python!
Hello from Rust!
Hello from C!
Hello from Go!
Hello from JavaScript!
Ran 4 plug-ins in 3.6659 ms
Run plug-ins [Enter]> 
Hello from Python!
Hello from Rust!
Hello from C!
Hello from Go!
Hello from JavaScript!
Ran 4 plug-ins in 0.9642 ms
```

