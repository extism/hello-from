build:
	/opt/wasi-sdk/bin/clang -O3 -o hello-from-c.wasm -Wl,--export=hello hello.c -mexec-model=reactor
	cp hello-from-c.wasm ../wasm
