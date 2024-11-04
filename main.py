def xnor(a, b):
    return (a and b) or (not a and not b)

if __name__ == "__main__":
    a = input("ia davai azvarli o valoare true/false ori 1/0: ").strip().lower()
    b = input("ia davai azvarli o valoare true/false ori 1/0 inca odata: ").strip().lower()
    a = True if a in ['true', '1'] else False
    b = True if b in ['true', '1'] else False

    result = xnor(a, b)
    print(f"tii interesant rezultatu? vo: {result}")
