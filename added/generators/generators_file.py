def generator_file_line(filepath):
    file = open(filepath)

    for line in file:
        if ':' in line:
            log_type, log_info = line.rstrip("\n").split(':', 1)
            yield log_type, log_info[1:]

    file.close()


for l_number, l_fill in enumerate(generator_file_line('data.txt')):
    print("In {} line of file -> type: {}, action: {}".format(l_number + 1, l_fill[0], l_fill[1]))
