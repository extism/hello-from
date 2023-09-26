use extism_pdk::*;

#[plugin_fn]
pub fn hello(input: String) -> FnResult<String> {
    Ok(format!("{}\nHello from Rust!", input))
}
