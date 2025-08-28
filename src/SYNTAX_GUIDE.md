# Ashlang - Enhanced Syntax Documentation

## Overview
Ashlang now supports a hybrid syntax that combines Assembly-like operations with Python and C-like expressions.

## New Features

### 1. Mathematical Expressions in PUSH
```
Push 5+6           ; Evaluates to 11
Push 2*3+4         ; Evaluates to 10 (follows order of operations)
Push (5+3)*2       ; Evaluates to 16 (parentheses supported)
Push 10-5          ; Evaluates to 5
```

### 2. Enhanced PRINT with String Concatenation
```
Print 'Hello ' + 'World'           ; String concatenation
Print 'Result: ' + 42              ; Mix strings and numbers
Print 'Math: ' + 3 + ' * ' + 4     ; Multiple concatenations
```

### 3. Python/C-style Conditional Statements
```
if 5-5 == 0 : LABEL_NAME          ; Jump if condition is true
else: OTHER_LABEL                  ; Jump to else label

if 10 > 5 : GREATER               ; Greater than comparison
if 3 < 8 : SMALLER                ; Less than comparison
if 5 != 3 : NOT_EQUAL             ; Not equal comparison
```

### 4. Stack Inspection Operations
```
Print_Stack                        ; Print the top element of stack
Print_Stack_Top2                   ; Print the top 2 elements of stack  
Compare_Stack                      ; Compare top 2 elements and show result
```

### 5. Backward Compatibility
All original Ashlang syntax still works:
```
PUSH 5
PRINT "Hello World"
JUMP.EQ.0 LABEL
READ
ADD
SUB
HALT
```

## Complete Example
```
; Modern Ashlang syntax example
Push 5+6                          ; Push 11
Print 'Sum is: ' + 11

Push 10*2                         ; Push 20
if 20 > 15 : BIG_NUMBER
else: SMALL_NUMBER

SMALL_NUMBER:
Print 'Number is small'
HALT

BIG_NUMBER:
Print 'Number is big: ' + 20
Print 'Calculation: ' + 5 + ' + ' + 6 + ' = ' + 11
HALT
```

## Supported Operations

### Stack Operations
- `PUSH <value>` or `Push <expression>` - Push value onto stack
- `POP` - Remove top element from stack
- `Print_Stack` - Display top element (non-destructive)
- `Print_Stack_Top2` - Display top 2 elements (non-destructive)
- `Compare_Stack` - Compare and display relationship between top 2 elements

### Mathematical Operations
- `+` (addition)
- `-` (subtraction)  
- `*` (multiplication)
- `/` (division)
- `()` (parentheses for grouping)

### Comparison Operators
- `==` (equal)
- `!=` (not equal)
- `>` (greater than)
- `<` (less than)

### String Operations
- `+` (concatenation between strings and numbers)

## Comments
- Line comments start with `;`
- Comments are ignored during parsing
- Can be used for documentation

## Labels
Labels work the same as before:
```
LABEL_NAME:
    ; code here
```

Jump to labels using if/else statements or legacy JUMP opcodes.
