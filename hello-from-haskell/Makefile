build:
	rm -rf dist-newstyle
	wasm32-wasi-cabal update
	wasm32-wasi-cabal build
	cp `find dist-newstyle -name hello-from-haskell.wasm` ../wasm
	
