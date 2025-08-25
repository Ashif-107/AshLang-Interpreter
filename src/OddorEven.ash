READ            ; read number from user
LOOP:
PUSH 2
SUB             ; n = n - 2
JUMP.EQ.0 EVEN  ; if result == 0 → even
JUMP.LT.0 ODD   ; if result < 0 → odd
JUMP.GT.0 LOOP  ; otherwise keep looping

EVEN:
PRINT "even"
HALT

ODD:
PRINT "odd"
HALT
