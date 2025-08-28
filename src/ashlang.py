import sys
import re

#read the arguments

program_filepath = sys.argv[1]

#################################
#          Tokenization
#################################

def evaluate_expression(expr):
    """Evaluate mathematical expressions like 5+6, 5-5, etc."""
    try:
        # Basic safety check - only allow numbers, operators, and spaces
        if re.match(r'^[0-9+\-*/()\s]+$', expr):
            return eval(expr)
        else:
            raise ValueError("Invalid expression")
    except:
        # If evaluation fails, try to parse as a single number
        try:
            return int(expr)
        except:
            return expr

def parse_string_expression(expr):
    """Parse string expressions with concatenation like 'Hello ' + 'World' """
    # Handle string concatenation
    if '+' in expr:
        parts = expr.split('+')
        result = ""
        for part in parts:
            part = part.strip()
            if part.startswith("'") and part.endswith("'"):
                result += part[1:-1]  # Remove quotes
            elif part.startswith('"') and part.endswith('"'):
                result += part[1:-1]  # Remove quotes
            else:
                # Try to evaluate as number and convert to string
                try:
                    result += str(evaluate_expression(part))
                except:
                    result += part
        return result
    else:
        # Single string literal
        if (expr.startswith("'") and expr.endswith("'")) or (expr.startswith('"') and expr.endswith('"')):
            return expr[1:-1]
        return expr

program_lines = []
with open(program_filepath, 'r') as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]
    
program = []
token_counter = 0
label_tracker = {}

for line in program_lines:
    # Skip empty lines and comments
    if not line or line.startswith(';'):
        continue
    
    # Remove inline comments
    if ';' in line:
        line = line[:line.index(';')].strip()
    
    # Handle labels
    if line.endswith(":"):
        label_tracker[line[:-1]] = token_counter
        continue
    
    # Parse different statement types
    if line.lower().startswith("push "):
        program.append("PUSH")
        token_counter += 1
        
        # Parse expression after PUSH
        expr = line[5:].strip()
        value = evaluate_expression(expr)
        program.append(value)
        token_counter += 1
        
    elif line.lower().startswith("print_stack_top2"):
        program.append("PRINT_STACK_TOP2")
        token_counter += 1
        
    elif line.lower().startswith("print_stack"):
        program.append("PRINT_STACK")
        token_counter += 1
        
    elif line.lower().startswith("compare_stack"):
        program.append("COMPARE_STACK")
        token_counter += 1
        
    elif line.lower().startswith("print "):
        program.append("PRINT")
        token_counter += 1
        
        # Parse string expression after PRINT
        expr = line[6:].strip()
        string_value = parse_string_expression(expr)
        program.append(string_value)
        token_counter += 1
        
    elif line.lower().startswith("if "):
        # Parse if statement: if condition : label
        if_pattern = r'if\s+(.+?)\s*:\s*(\w+)'
        match = re.match(if_pattern, line, re.IGNORECASE)
        if match:
            condition = match.group(1).strip()
            label = match.group(2).strip()
            
            # Parse condition (e.g., "5-5 == 0")
            if " == " in condition:
                left, right = condition.split(" == ")
                left_val = evaluate_expression(left.strip())
                right_val = evaluate_expression(right.strip())
                
                program.append("PUSH")
                token_counter += 1
                program.append(left_val - right_val)  # Push difference
                token_counter += 1
                program.append("JUMP.EQ.0")
                token_counter += 1
                program.append(label)
                token_counter += 1
            elif " != " in condition:
                left, right = condition.split(" != ")
                left_val = evaluate_expression(left.strip())
                right_val = evaluate_expression(right.strip())
                
                program.append("PUSH")
                token_counter += 1
                program.append(left_val - right_val)  # Push difference
                token_counter += 1
                program.append("JUMP.NE.0")
                token_counter += 1
                program.append(label)
                token_counter += 1
            elif " > " in condition:
                left, right = condition.split(" > ")
                left_val = evaluate_expression(left.strip())
                right_val = evaluate_expression(right.strip())
                
                program.append("PUSH")
                token_counter += 1
                program.append(left_val - right_val)  # Push difference
                token_counter += 1
                program.append("JUMP.GT.0")
                token_counter += 1
                program.append(label)
                token_counter += 1
            elif " < " in condition:
                left, right = condition.split(" < ")
                left_val = evaluate_expression(left.strip())
                right_val = evaluate_expression(right.strip())
                
                program.append("PUSH")
                token_counter += 1
                program.append(left_val - right_val)  # Push difference
                token_counter += 1
                program.append("JUMP.LT.0")
                token_counter += 1
                program.append(label)
                token_counter += 1
                
    elif line.lower().startswith("else:"):
        # Parse else: label
        else_pattern = r'else:\s*(\w+)'
        match = re.match(else_pattern, line, re.IGNORECASE)
        if match:
            label = match.group(1).strip()
            program.append("JUMP")
            token_counter += 1
            program.append(label)
            token_counter += 1
            
    else:
        # Handle legacy syntax
        parts = line.split()
        if not parts:
            continue
            
        opcode = parts[0].upper()
        
        program.append(opcode)
        token_counter += 1

        #handle each opcode
        if opcode == "PUSH":
            number = int(parts[1]) 
            program.append(number)
            token_counter += 1
        elif opcode == "PRINT":
            string_literal = " ".join(parts[1:])[1:-1] #remove quotes
            program.append(string_literal)
            token_counter += 1
        elif opcode in ["JUMP.EQ.0", "JUMP.GT.0", "JUMP.LT.0", "JUMP.NE.0"]:
            label = parts[1]
            program.append(label)
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

while pc < len(program) and program[pc] != "HALT":
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
            
    elif opcode == "JUMP.NE.0":
        number = stack.top()
        if number != 0:
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
            
    elif opcode == "JUMP":
        # Unconditional jump
        pc = label_tracker[program[pc]]
        
    elif opcode == "PRINT_STACK":
        # Print the top element of the stack without popping it
        if stack.sp >= 0:
            print(f"Top of stack: {stack.top()}")
        else:
            print("Stack is empty")
            
    elif opcode == "PRINT_STACK_TOP2":
        # Print the top 2 elements of the stack without popping them
        if stack.sp >= 1:
            top = stack.buf[stack.sp]
            second = stack.buf[stack.sp - 1]
            print(f"Top 2 elements: [{second}, {top}] (bottom to top)")
        elif stack.sp >= 0:
            print(f"Only 1 element in stack: {stack.top()}")
        else:
            print("Stack is empty")
            
    elif opcode == "COMPARE_STACK":
        # Compare top 2 elements and print the result
        if stack.sp >= 1:
            top = stack.buf[stack.sp]
            second = stack.buf[stack.sp - 1]
            print(f"Comparing: {second} vs {top}")
            if second == top:
                print("  Result: Equal")
            elif second > top:
                print(f"  Result: {second} > {top}")
            else:
                print(f"  Result: {second} < {top}")
        elif stack.sp >= 0:
            print("Only 1 element in stack, cannot compare")
        else:
            print("Stack is empty, cannot compare")