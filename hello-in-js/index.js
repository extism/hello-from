const createPlugin = require("@extism/extism")
const fs = require('fs');
const path = require('path');
const readline = require('node:readline/promises').createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function loadPlugin(path) {
  return createPlugin(
    path,
    { useWasi: true }
  );
}

function pluginPaths(directoryPath) {
  return fs
    .readdirSync(directoryPath)
    .filter(file => path.extname(file) === '.wasm')
    .map(file => `${directoryPath}/${file}`)
}

async function main() {
  let answer = await readline.question("Load Plugins>")
  console.time("Loaded Plugins:")
  let plugins = Promise.all(pluginPaths("../wasm").map(loadPlugin))
  plugins = await plugins
  console.timeEnd("Loaded Plugins:")
  while (true) {
    answer = await readline.question("Run Plugins>")
    let message = "Hello in Nodejs!"
    console.time("Ran Plugins:")
    for (const p of plugins) {
      message = (await p.call('hello', message)).string()
    }
    console.timeEnd("Ran Plugins:")
    console.log(message)
  }
}

main()

