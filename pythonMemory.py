file_name = ''
mem_list = []
str_mem_list = []


def make_mem_file(wanted_file_name, default_add_on=True):
    global file_name
    if default_add_on:
        file_name = wanted_file_name + '_python_memory.txt'
    else:
        file_name = wanted_file_name
    create_file = open(file_name, 'a')
    create_file.write()
    create_file.close()


def load_mem_file(the_file_name):
    global file_name
    file_name = the_file_name


def remember():
    global mem_list, file_name, str_mem_list
    for_reading = open(file_name, 'r')
    str_mem_list = for_reading.readline().split('-/-')
    for_reading.close()
    for var in str_mem_list:
        if var[0] == "'":
            mem_list.append(var.replace("'", ""))
        elif var[0] == "T":
            mem_list.append(True)
        elif var[0] == "F":
            mem_list.append(False)
        elif var[0] == "N":
            mem_list.append(None)
        elif "." in var and "'" not in var:
            mem_list.append(float(var))
        else:
            mem_list.append(int(var))


def memorize():
    for_writing = open(file_name, 'w')
    string_mem = ''
    for var in mem_list:
        if var == mem_list[0]:
            if str(var) != var:
                string_mem = str(var)
            else:
                string_mem = "'" + str(var) + "'"
        else:
            if str(var) != var:
                string_mem += "-/-" + str(var)
            else:
                string_mem += "-/-" + "'" + str(var) + "'"
    for_writing.write(string_mem)
    for_writing.close()


def restart():
    global mem_list
    mem_list = ['init']
    memorize()
