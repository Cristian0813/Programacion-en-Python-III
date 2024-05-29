def read_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
    print(contents)
    return contents

def read_file_into_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as file:
        file.write(first_line + '\n')

def read_even_numbered_lines(file_name):
    even_lines = []
    with open(file_name, 'r') as file:
        for index, line in enumerate(file, start=1):
            if index % 2 == 0:
                even_lines.append(line)
    return even_lines

def read_file_in_reverse(file_name):
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
    lines.reverse()
    print(lines)
    return lines

def main():
    file_contents = read_file("Modulo-2/sampletext.txt")
    print(read_file_into_list("Modulo-2/sampletext.txt"))
    write_first_line_to_file(file_contents, "Modulo-2/online.txt")
    print(read_even_numbered_lines("Modulo-2/sampletext.txt"))
    print(read_file_in_reverse("Modulo-2/sampletext.txt"))

if __name__ == "__main__":
    main()
