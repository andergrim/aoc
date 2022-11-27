schema_single = {}
schema_double = {}
schema = {}

operators = ["AND", "OR", "RSHIFT", "LSHIFT", "NOT"]

def parse_source(source):
    parsed = {"operator": None, "values": None}
    operands = source.split(" ")

    if len(operands) == 3:
        val_a, operation, val_b = operands
        parsed["values"] = (val_a, val_b)
        parsed["operator"] = operation
    elif len(operands) == 2:
        operation, value = operands
        parsed["values"] = (value)
        parsed["operator"] = operation
    else:
        if operands[0].isnumeric():
            parsed["values"] = (int(operands[0]))
        else:
            parsed["values"] = (operands[0])

    return parsed


with open("07.txt") as fp:
    for line in fp:
        source, target = line.strip().split(" -> ")
        if len(target) == 1:
            schema_single[target] = parse_source(source)
        else:
            schema_double[target] = parse_source(source)

schema = dict(sorted(schema_single.items()) + sorted(schema_double.items()))
print(schema)


