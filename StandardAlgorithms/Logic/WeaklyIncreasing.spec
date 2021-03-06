
#ifndef WEAKLYINCREASING_SPEC_INCLUDED
#define WEAKLYINCREASING_SPEC_INCLUDED

#include "typedefs.h"

/*@
  predicate
    WeaklyIncreasing{L}(value_type* a, integer m, integer n) =
      \forall integer i; m <= i < n-1 ==> a[i] <= a[i+1];

  predicate
    WeaklyIncreasing{L}(value_type* a, integer n) = WeaklyIncreasing{L}(a, 0, n);
*/

#endif /* WEAKLYINCREASING_SPEC_INCLUDED */

