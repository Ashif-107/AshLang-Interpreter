; Simple stack inspection demo

Print 'Stack Inspection Demo'
Print '==================='

Print 'Starting with empty stack:'
Print_Stack

Print 'Pushing 15:'
Push 15
Print_Stack

Print 'Pushing 7+3 (equals 10):'
Push 7+3
Print_Stack
Print_Stack_Top2

Print 'Comparing 15 vs 10:'
Compare_Stack

Print 'Pushing another 15:'
Push 15
Print_Stack_Top2
Compare_Stack

Print 'Final stack state:'
Print_Stack_Top2

HALT
