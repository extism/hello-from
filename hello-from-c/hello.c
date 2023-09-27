#include "extism/extism-pdk.h"

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int32_t hello() {
  uint64_t length = extism_input_length();
  uint8_t *input;
  input = (uint8_t *)malloc(length * sizeof(uint8_t));
  extism_load_input(input, length);

  char *out;
  uint64_t total_len = length + 15; // \nHello from C!
  out = (char *)malloc(total_len * sizeof(uint8_t));

  int n = snprintf(out, total_len, "%s\nHello from C!", input);

  uint64_t offs_ = extism_alloc(n);
  extism_store(offs_, (const uint8_t *)out, n);
  extism_output_set(offs_, n);

  return 0;
}
