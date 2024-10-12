def write_file(file_name, file_content):
    new_file_name = str(file_name) + ".txt"
    with open(new_file_name, mode="w", encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    new_file_name = str(file_name) + ".txt"
    with open(new_file_name, mode="a", encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    new_file_name = str(file_name) + ".txt"
    with open(new_file_name, encoding='utf-8') as file:
       content = file.read()
    return content