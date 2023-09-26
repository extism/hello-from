import extism
import os

plugins = [
    os.path.join("wasm", file)
    for file in os.listdir("wasm")
    if file.endswith(".wasm")
]

input = str.encode("Hello, World!")
for plugin in plugins:
    plugin = extism.Plugin({"wasm": [{"path": plugin}]}, wasi=True)
    input = plugin.call('hello', input)

print(input.decode())


