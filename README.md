A demo piping a string through a plug-in written in each PDK:

```python
# run.py

def call_plugin(input, path):
    plugin = extism.Plugin({"wasm": [{"path": path}]}, wasi=True)
    return plugin.call('hello', input)

plugins = [
    os.path.join("wasm", file)
    for file in os.listdir("wasm")
    if file.endswith(".wasm")
]

input = str.encode("Hello, World!")
input = reduce(call_plugin, plugins, input)
print(input.decode())
```

Running:

```bash
python3 run.py
Hello, World!
Hello from Rust!
Hello from C!
Hello from Go!
Hello from JavaScript!
```

Building:

```bash
sh build.sh
```
