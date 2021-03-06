
#include "StackLogic.spec"
#include "stack_pop.h"
#include "stack_push.h"
#include "stack_top.h"

/*@
  requires  valid:     \valid(s) && Invariant(s);
  requires  not_empty: !Empty(s);
  assigns              s->size, s->obj[s->size-1];
  ensures   equal:     Equal{Old,Here}(s, s);
*/
void
axiom_push_of_pop_top(Stack* s)
{
  const value_type val = stack_top(s);
  stack_pop(s);
  stack_push(s, val);
}

