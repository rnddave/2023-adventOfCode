def load_input(file_path):
    with open(file_path, "r") as file:
        instruction, *elements = map(str.strip, file.read().split("\n\n"))
        elements_dic = dict(element.split(" = ") for element in elements[0].split("\n"))

    elements_dic = {key: tuple(map(str.strip, val.strip("()").split(","))) for key, val in elements_dic.items()}
    
    return instruction, elements_dic

def zzz(val, my_dict):
	return list(my_dict.keys()) [list(my_dict.values()).index(val)]

def required_steps(instruction, elements_dic):
    idx, count = 0, 0
    instruction += "//"
    element = elements_dic.get(start)

    while instruction[idx] != "//":
        if zzz(element, elements_dic) == "ZZZ":
            return count
        
        if instruction[idx] == "/":
            idx = 0
        else:
            element = elements.get(element[0]) if instruction[idx] == "L" else elements.get(element[1])
            idx , count = idx + 1, count + 1

start = "AAA"
instruction, elements = load_input("2023-12-08-puzzle-input")
print(required_steps(instruction, elements))