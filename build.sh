cd hello-from-rust
cargo build --target=wasm32-unknown-unknown
cp target/wasm32-unknown-unknown/debug/hello_from_rust.wasm ../wasm/hello-from-rust.wasm
cd ..

cd hello-from-js
extism-js index.js -o hello-from-js.wasm
cp hello-from-js.wasm ../wasm
cd ..

cd hello-from-go
tinygo build -o hello-from-go.wasm -target wasi main.go
cp ./hello-from-go.wasm ../wasm
cd ..

cd hello-from-c
/opt/wasi-sdk/bin/clang -o hello-from-c.wasm -Wl,--export=hello hello.c -mexec-model=reactor
cp hello-from-c.wasm ../wasm
cd ..
