
#include <criterion/criterion.h>

int hello_world();

Test(hello_world, base) {
  cr_assert_eq(hello_world(), 42);
}
