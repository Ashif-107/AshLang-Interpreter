; Advanced syntax example with stack inspection
; Shows mathematical expressions, conditionals, string concatenation, and stack debugging

Push 2*3+4         ; Push 10 (2*3+4)
Print 'Complex math: ' + 10
Print_Stack

Push (5+3)*2       ; Push 16 ((5+3)*2)
Print 'With parentheses: ' + 16
Print_Stack_Top2
Compare_Stack

if 10 > 5 : GREATER
else: NOT_GREATER

NOT_GREATER:
Print 'This should not execute'
HALT

GREATER:
Print 'Ten is greater than five!'
Print 'Current stack contents:'
Print_Stack_Top2

if 3*3 == 9 : CORRECT
else: WRONG

WRONG:
Print 'Math is broken!'
HALT

CORRECT:
Print 'Perfect! ' + 3 + ' times ' + 3 + ' equals ' + 9
Print 'Final stack inspection:'
Print_Stack_Top2
Compare_Stack
HALT
