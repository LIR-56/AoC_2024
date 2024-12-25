import sys


class Operation:
    def __init__(self, input_1, input_2, operation):
        self.input_1 = input_1
        self.input_2 = input_2
        self.operation = operation

    def do_brr(self, gates, ops):
        if self.input_1 not in gates:
            gates[self.input_1] = ops[self.input_1].do_brr(gates, ops)
        if self.input_2 not in gates:
            gates[self.input_2] = ops[self.input_2].do_brr(gates, ops)
        i_1 = gates[self.input_1]
        i_2 = gates[self.input_2]
        if self.operation == 'AND':
            return i_1 & i_2
        elif self.operation == 'OR':
            return i_1 | i_2
        elif self.operation == 'XOR':
            return i_1 ^ i_2
        else:
            raise Exception("Unknown operation: " + self.operation)


def find_result_number(initial_states, operation_by_output):
    max_z = int(max(filter(lambda o: o.startswith('z'), operation_by_output.keys()))[1:])
    # layers = []
    # current_layer = set()
    # next_layer = set()
    # for i in range(max_z):
    #     z = 'z' + "{:02d}".format(i)
    #     current_layer.add(z)
    #     i_1 = operation_by_output[z].input_1
    #     i_2 = operation_by_output[z].input_2
    #     if i_1 in operation_by_output:
    #         next_layer.add(operation_by_output[z].input_1)
    #     if i_2 in operation_by_output:
    #         next_layer.add(operation_by_output[z].input_2)
    # layers.append(current_layer)
    # current_layer = next_layer
    # while len(current_layer) > 0:
    #     layers.append(current_layer)
    #     next_layer = set()
    #     for gate in current_layer:
    #         i_1 = operation_by_output[gate].input_1
    #         i_2 = operation_by_output[gate].input_2
    #         if i_1 in operation_by_output:
    #             next_layer.add(operation_by_output[gate].input_1)
    #         if i_2 in operation_by_output:
    #             next_layer.add(operation_by_output[gate].input_2)
    #     current_layer = next_layer
    # i = 1
    # processed = layers[0]
    # while i < len(layers):
    #     layers[i] = layers[i] - processed
    #     processed = processed | layers[i]
    #     i += 1

    # for layer in layers:
    #     for gate in layer:
    #         state[gate] = operation_by_output[gate].do_brr(state)

    result_num = 0
    state = initial_states.copy()
    for i in range(max_z, -1, -1):
        result_num = result_num << 1
        n = 'z' + "{:02d}".format(i)
        if n not in state:
            state[n] = operation_by_output[n].do_brr(state, operation_by_output)
        result_num += state[n]
    return result_num


def parse(input_data):
    initial_states = {}
    operations = set()
    whom_to_count_by = {}
    for line in input_data:
        if ':' in line:
            i = line.strip().split(":")
            initial_states[i[0]] = int(i[1])
        elif line != '\n' and len(line) > 0:
            i = line.strip().split(" ")
            o = Operation(i[0], i[2], i[1])
            whom_to_count_by[i[4]] = o
            operations.add(o)
    return initial_states, whom_to_count_by


test_data = [
    'x00: 1',
    'x01: 0',
    'x02: 1',
    'x03: 1',
    'x04: 0',
    'y00: 1',
    'y01: 1',
    'y02: 1',
    'y03: 1',
    'y04: 1',
    '\n',
    'ntg XOR fgs -> mjb',
    'y02 OR x01 -> tnw',
    'kwq OR kpj -> z05',
    'x00 OR x03 -> fst',
    'tgd XOR rvg -> z01',
    'vdt OR tnw -> bfw',
    'bfw AND frj -> z10',
    'ffh OR nrd -> bqk',
    'y00 AND y03 -> djm',
    'y03 OR y00 -> psh',
    'bqk OR frj -> z08',
    'tnw OR fst -> frj',
    'gnj AND tgd -> z11',
    'bfw XOR mjb -> z00',
    'x03 OR x00 -> vdt',
    'gnj AND wpb -> z02',
    'x04 AND y00 -> kjc',
    'djm OR pbm -> qhw',
    'nrd AND vdt -> hwm',
    'kjc AND fst -> rvg',
    'y04 OR y02 -> fgs',
    'y01 AND x02 -> pbm',
    'ntg OR kjc -> kwq',
    'psh XOR fgs -> tgd',
    'qhw XOR tgd -> z09',
    'pbm OR djm -> kpj',
    'x03 XOR y03 -> ffh',
    'x00 XOR y04 -> ntg',
    'bfw OR bqk -> z06',
    'nrd XOR fgs -> wpb',
    'frj XOR qhw -> z04',
    'bqk OR frj -> z07',
    'y03 OR x01 -> nrd',
    'hwm AND bqk -> z03',
    'tgd XOR rvg -> z12',
    'tnw OR pbm -> gnj'
]
(test_initial_states, test_whom_to_count_by) = parse(test_data)
assert find_result_number(test_initial_states, test_whom_to_count_by) == 2024


input_data = []
for line in sys.stdin:
    input_data.append(line.strip())
(initial_states, whom_to_count_by) = parse(input_data)

print(find_result_number(initial_states, whom_to_count_by))
