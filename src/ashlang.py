import sys

#read the arguments

program_filepath = sys.argv[1]

#################################
#          Tokenization
#################################

program_lines = []
with open(program_filepath, 'r') as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]
    
program = []
token_counter = 0
label_tracker = {}

for line in program_lines:
    parts = line.split()
    
     # Skip empty lines
    if not parts:
        continue
         
    opcode = parts[0]
     
    # check for empty string
    if opcode == "":
        continue
    
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue
    
    #Store opcode token
    
    program.append(opcode)
    token_counter += 1

    #handle each opcode
    if opcode == "PUSH":
        
        #Expecting a number 
        number = int(parts[1]) 
        program.append(number)
        token_counter += 1
    elif opcode == "PRINT":
        
        #parse the string literal
        string_literal = " ".join(parts[1:])[1:-1] #remove quotes
        program.append(string_literal)
        token_counter += 1
    elif opcode == "JUMP.EQ.0":
        #read label
        label = parts[1]
        program.append(label) #placeholder, will resolve later
        token_counter += 1
            
    elif opcode == "JUMP.GT.0":
        #read label
        label = parts[1]
        program.append(label) #placeholder, will resolve later
        token_counter += 1
        
print(program)



###########################
#     Interpret Program
###########################


class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number
    
    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    def top(self):
        return self.buf[self.sp]
        


pc = 0
stack = Stack(256)

while program[pc] != "HALT":
    opcode = program[pc]
    pc += 1

    if opcode == "PUSH":
        number = program[pc]
        pc += 1

        stack.push(number)
    elif opcode == "POP":
        stack.pop()
    elif opcode == "ADD":
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "SUB":
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "PRINT":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    elif opcode == "READ":
        number = int(input())
        stack.push(number)
    elif opcode == "JUMP.EQ.0":
        number = stack.top()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "JUMP.GT.0":
        number = stack.top()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "JUMP.LT.0":
        number = stack.top()
        if number < 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1