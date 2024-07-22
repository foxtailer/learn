import re
import json

class Stack:
    """stack for braces_sequence_correct function"""
    def __init__(self):
        self.__index = []
    def __len__(self):
        return len(self.__index)
    def push(self, item):
        self.__index.append(item)
    def pop(self):
        return self.__index.pop()
    def top(self):
        return self.__index[-1]
    def is_empty(self):
        return len(self.__index) == 0
    def clear(self):
        self.__index.clear()

stack = Stack()

def bracet_sequence_correct(s:str):
    """Check if all bracet in string a closed correct"""
    stack.clear()
    braces = {'(':')', '[':']','{':'}'}

    for brace in s:
        if brace not in "()[]{}":
            continue
        
        if brace in '([{':
            stack.push(brace)
        else:
            assert brace in ")]}", "') or ] or }' Expected" + str(brace)
            if stack.is_empty():
                return False
            
            left = stack.pop()
            if brace != braces[left]:
                return False
              
    return stack.is_empty()

def str_to_jsn(string:str):
    """
    >>> str_to_jsn('myfun1(arg1=7, arg2=8, arg3=myfun3(barg1="one", barg2="two"))')
    '{"name": "myfun1", "args": [{"name": "arg1", "value": "7"}, {"name": "arg2", "value": "8"}, {"name": "arg3", "value": {"name": "myfun3", "args": [{"name": "barg1", "value": "one"}, {"name": "barg2", "value": "two"}]}}]}'
    >>> str_to_jsn('myfun1(arg1=7)')
    '{"name": "myfun1", "args": [{"name": "arg1", "value": "7"}]}'
    """
    if not bracet_sequence_correct(string):
        print("Incorect input missing some brackets.")
        return "BrackrtsError"

    def extract_arguments(arg_str):
        args = []
        brackets = 0
        current_arg = ''
        for char in arg_str:
            if char == '(':
                brackets += 1
            elif char == ')':
                brackets -= 1
            if char == ',' and brackets == 0:
                args.append(current_arg.strip())
                current_arg = ''
            else:
                current_arg += char
        if current_arg:
            args.append(current_arg.strip())
        return args

    def parse(input_str):
        match = re.search(r"(\w+)\((.*)\)", input_str.strip())
        if not match:
            return input_str.replace('"', '')
        name, args_str = match.groups()
        args = extract_arguments(args_str)
        parsed_args = []
        for arg in args:
            key_value = arg.split('=')
            if len(key_value) == 2:
                key, value = key_value
                parsed_args.append({"name": key.strip(), "value": parse(value.strip())})
            else:
                parsed_args.append({"name":arg.split("=")[0], "value": parse(arg.strip())})
        return {"name": name, "args": parsed_args}
    
    return json.dumps(parse(string))

   

if __name__ == "__main__":
    import doctest          
    doctest.testmod(verbose=True)

    input_str = 'myfun1(arg1=7, arg2=8, arg3=myfun3(barg1="one", barg2="two"))'
    output_json = str_to_jsn(input_str)