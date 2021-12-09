unique_lengths = {1: 2, 4: 4, 7: 3, 8: 7}
unique_lengths_reverse = {v: k for k, v in unique_lengths.items()}

sum_total = 0

with open("08.txt") as fp:
    for line in fp:
        signal_patterns, output_values = line.strip().split("|")
        signal_patterns = signal_patterns.strip().split(" ")
        output_values = output_values.strip().split(" ")
        output_values_list = [sorted(c) for c in output_values]
        all_values = signal_patterns + output_values

        solved = {}

        """ Get unique numbers by length """
        for value in all_values:
            if len(value) in unique_lengths_reverse.keys():
                solved[unique_lengths_reverse[len(value)]] = sorted(value)
         
        bd_subset = [c for c in solved[4] if c not in solved[1]] # Subset pattern used for deduction
        
        """ Solve 5's """
        for value in all_values:
            value_list = sorted([c for c in value])
            if len(value) == 5:
                if all([c in value_list for c in solved[1]]):
                    solved[3] = value_list
                elif all([c in value_list for c in bd_subset]):
                    solved[5] = value_list
                else:
                    solved[2] = value_list

        """ Solve 6's """
        for value in all_values:
            value_list = sorted([c for c in value])
            if len(value) == 6:
                if all([c in value_list for c in solved[4]]):
                    solved[9] = value_list
                elif all([c in value_list for c in bd_subset]):
                    solved[6] = value_list
                else:
                    solved[0] = value_list

        # Solve each output value into digits
        nums = []
        for output_value, multiple in zip(output_values_list, [1000, 100, 10, 1]):
            nums += [k * multiple for k, v in solved.items() if v == output_value]

        sum_total += sum(nums)

print(sum_total)
