
#ifndef INCREASING_SPEC_INCLUDED
#define INCREASING_SPEC_INCLUDED

#include "typedefs.h"

/*@
  predicate
    Increasing{L}(value_type* a, integer m, integer n) =
      \forall integer i, j; m <= i < j < n ==> a[i] <= a[j];

  predicate
    Increasing{L}(value_type* a, integer n) = Increasing{L}(a, 0, n);
*/

#endif /* INCREASING_SPEC_INCLUDED */

