import { Var, Config, Host } from '@extism/as-pdk';

function myAbort(
  message: string | null,
  fileName: string | null,
  lineNumber: u32,
  columnNumber: u32
): void { }


export function hello(): i32 {
  let input = Host.inputString();
  var out = `${input}\nHello from AssemblyScript!`;
  Host.outputString(out);
  return 0;
}
