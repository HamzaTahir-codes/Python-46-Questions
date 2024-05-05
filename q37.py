def line_number(input_file, output_file):
    with open(input_file) as f_input:
        with open(output_file, 'w') as f_output:
            line = 1
            for i in f_input:
                f_output.write(f"{line}.{i}")
                line += 1


input_f = input("Enter the input file name: ")
output_f = input("Enter the output file name: ")
line_number(input_f, output_f)