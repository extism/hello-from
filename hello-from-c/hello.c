#include "extism/extism-pdk.h"

#include <stdio.h>

int32_t hello() {
  uint64_t length = extism_input_length();
  uint8_t input[length];
  extism_load_input(input, length);

  char out[1024];
  int n = snprintf(out, 1024, "%s\nHello from C!", input);

  uint64_t offs_ = extism_alloc(n);
  extism_store(offs_, (const uint8_t *)out, n);
  extism_output_set(offs_, n);

  return 0;
}
