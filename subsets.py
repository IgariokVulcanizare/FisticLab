def generate_power_set(input_set):
    if not input_set:
        return [[]]

    first, rest = input_set[0], input_set[1:]
    subsets_without_first = generate_power_set(rest)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]

    return subsets_without_first + subsets_with_first


def parse_input(input_str):
    input_str = input_str.strip()

    # Wrap input in square brackets if they are missing
    if not (input_str.startswith("[") and input_str.endswith("]")):
        input_str = f"[{input_str}]"

    result = []
    stack = []
    current_list = result
    current_number = ""
    inside_number = False

    for char in input_str[1:-1]:
        if char == '[':
            new_list = []
            current_list.append(new_list)
            stack.append(current_list)
            current_list = new_list
        elif char == ']':
            if inside_number:
                current_list.append(int(current_number))
                current_number = ""
                inside_number = False
            if stack:
                current_list = stack.pop()
        elif char == ',':
            if inside_number:
                current_list.append(int(current_number))
                current_number = ""
                inside_number = False
        elif char.isdigit() or (char == '-' and not inside_number):
            current_number += char
            inside_number = True
        elif not char.isspace():
            raise ValueError(f"vez c esti invalid, iaca caracteru care nu-i bun '{char}'")

    if inside_number:
        current_list.append(int(current_number))

    return result


def print_power_set(power_set):

    def format_subset(subset):
        elements = []
        for elem in subset:
            if isinstance(elem, list):
                elements.append(format_subset(elem))
            else:
                elements.append(str(elem))
        return "[" + ", ".join(elements) + "]"

    for subset in power_set:
        print(format_subset(subset))


if __name__ == "__main__":
    input_str = input("denghi davai nefor: ")

    try:
        input_set = parse_input(input_str)
    except ValueError as e:
        print(f"esti debil, ce-i cu numarul asta?: {e}")
        exit(1)

    print("\nna:")
    power_set = generate_power_set(input_set)
    print_power_set(power_set)