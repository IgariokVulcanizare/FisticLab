def next_combination(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return sorted(arr)
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = arr[i + 1:][::-1]
    return arr

def parse_input(user_input):
    try:
        sanitized = user_input.strip().replace("[", "").replace("]", "")
        arr = list(map(int, sanitized.split(",")))
        if not arr:
            raise ValueError("input array empty")
        return arr
    except ValueError:
        raise ValueError("debil, ia pune ceva normal, iaca exemplu [n1,n2,n3,...n].")


def main():
    print("ia davai un array [n1,n2,n3,...n]:")
    while True:
        try:
            user_input = input("> ")
            arr = parse_input(user_input)
            result = next_combination(arr)
            print("poftim: ", result)
            break
        except ValueError as e:
            print(f"Eroare: {e}. Mai incearca odata")


if __name__ == "__main__":
    main()
