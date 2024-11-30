from prettytable import PrettyTable
def generate_truth_table(expression):
    variables = sorted(set(filter(str.isalpha, expression)))
    expression = expression.replace('!', 'not ').replace('*', ' and ').replace('+', ' or ')
    table = PrettyTable()
    table.field_names = variables + [expression]
    num_rows = 2 ** len(variables)
    for i in range(num_rows):
        env = {variables[j]: (i >> j) & 1 for j in range(len(variables))} #bit shifting
        result = eval(expression, {}, env)
        table.add_row([env[var] for var in variables] + [int(result)])
    print(table)

expression = input("davai o pesni: ")
generate_truth_table(expression)
# truth table solver