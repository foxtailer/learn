import re
import json

def parse_function_call(input_str):
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
        match = re.match(r"(\w+)\((.*)\)$", input_str.strip())
        if not match:
            return {"value": input_str.replace('"', '')}
        name, args_str = match.groups()
        args = extract_arguments(args_str)
        parsed_args = []
        for arg in args:
            key_value = arg.split('=')
            if len(key_value) == 2:
                key, value = key_value
                parsed_args.append({"name": key.strip(), "value": parse(value.strip())})
            else:
                parsed_args.append(parse(arg.strip()))
        return {"name": name, "args": parsed_args}

    return json.dumps(parse(input_str), indent=2)

input_str = 'myfun1(arg1=7, arg2=8, arg3=myfun3(barg1="one", barg2="two"))'
output_json = parse_function_call(input_str)
print(output_json)

