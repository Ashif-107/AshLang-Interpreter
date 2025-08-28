; Test stack inspection features
; Demonstrating Print_Stack, Print_Stack_Top2, and Compare_Stack

Print 'Pushing numbers 10, 20, 30 onto stack...'
Push 10
Print_Stack

Push 20
Print_Stack
Print_Stack_Top2

Push 30
Print_Stack
Print_Stack_Top2

Print 'Comparing top 2 elements (20 vs 30):'
Compare_Stack

Print 'Popping one element and comparing again:'
POP
Print_Stack_Top2
Compare_Stack

Print 'Testing with equal values:'
Push 20
Print 'Stack now has two 20s on top'
Print_Stack_Top2
Compare_Stack

Print 'Testing mathematical expressions:'
Push 5+5
Print 'Pushed 5+5 = 10'
Print_Stack
Compare_Stack

HALT
