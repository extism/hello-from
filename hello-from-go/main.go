package main

import (
	"github.com/extism/go-pdk"
)

//export hello
func hello() int32 {
	input := pdk.Input()
	output := string(input) + "\nHello from Go!"
	mem := pdk.AllocateString(output)
	pdk.OutputMemory(mem)
	return 0
}

func main() {}
