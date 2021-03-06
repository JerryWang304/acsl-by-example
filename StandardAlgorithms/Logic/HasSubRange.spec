
#ifndef  HASSUBRANGE_SPEC_INCLUDED
#define  HASSUBRANGE_SPEC_INCLUDED

#include "EqualRanges.spec"

/*@
  predicate
    HasSubRange{L}(value_type* a, integer m, integer n, value_type* b, integer p) =
      \exists integer k; (m <= k <= n-p) && EqualRanges{L,L}(a+k, p, b);

  predicate
    HasSubRange{L}(value_type* a, integer n, value_type* b, integer p) =
      HasSubRange{L}(a, 0, n, b, p);

  lemma
    HasSubRangeSizes:
      \forall value_type *a, *b, integer m, n, p;
        HasSubRange(a, m, n, b, p) ==> p <= n-m;
*/

#endif /*  HASSUBRANGE_SPEC_INCLUDED */

