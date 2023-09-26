import extism
import os
from functools import reduce

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


