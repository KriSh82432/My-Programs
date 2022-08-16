def read_file(file_name):
    with open(file_name) as file:
        data = file.read()
        print(data)
    return data
    raise NotImplementedError()


def read_file_into_list(file_name):
    content = list()
    with open(file_name, 'r') as file:
        data = file.readlines()
        for i in data:
            content.append(i)
    return content
    raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'r+') as file:
        file.write(first_line)


def read_even_numbered_lines(file_name):
    content = list()
    file = open(file_name, 'r')
    data = file.readlines()
    for i in data:
        if data.index(i) % 2 == 0:
            None
        else:
            content.append(i)
    return content
    raise NotImplementedError()


def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        data.reverse()
        print(data)
        return data
    raise NotImplementedError()


def main():
    file_contents = read_file("D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\sampletext.txt")
    print(read_file_into_list("D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\sampletext.txt"))
    write_first_line_to_file(file_contents,"D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\online.txt")
    print(read_even_numbered_lines(
        "D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\sampletext.txt"))
    read_file_in_reverse(
        "D:\Programs\Web-Pages\Meta-Web-Dev-Programs\Python Programs\sampletext.txt")


if __name__ == "__main__":
    main()