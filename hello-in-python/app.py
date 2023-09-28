import extism
import os
from functools import reduce
import time

WASM_DIR = "../wasm"

def manifest(filename):
    return {"wasm": [{"path": os.path.join(WASM_DIR, filename)}]}

def load_plugins():
    return [
        extism.Plugin(manifest(filename), wasi=True)
        for filename in os.listdir(WASM_DIR)
        if filename.endswith(".wasm")
    ]

def run_plugins(inpt):
    return reduce(lambda i, p: p.call('hello', i), plugins, inpt)

input("Load plug-ins [Enter]> ")

start = time.time()
plugins = load_plugins()
print(f"Loaded {len(plugins)} plugins in {int((time.time() - start) * 1000)} ms")

while True:
    inpt = str.encode("Hello, World!")
    input("Run plug-ins [Enter]> ")
    start = time.time()
    inpt = run_plugins(inpt)
    end = time.time() - start
    print(inpt.decode())
    print(f"Ran {len(plugins)} plug-ins in {(end * 1000):.4f} ms")

