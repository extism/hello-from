function hello() {
  let input = Host.inputString()
  Host.outputString(`${input}\nHello from JavaScript!`)
}

module.exports = { hello }
