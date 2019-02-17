import os
from graphviz import Digraph

file_list = []
cpp_files = []
header_files = []
header_info = {}
dependence_map = {}


def get_file_list(path):
    # get the files from path
    # put the files into file_list[]

    dir_list = []
    for directory in path:
        dirs = os.listdir(directory)
        for m_file in dirs:
            file_path = directory + '/' + m_file
            if m_file[0] != '.':
                if os.path.isdir(file_path):
                    dir_list.append(file_path)
                else:
                    file_list.append(file_path)
    if len(dir_list) > 0:
        get_file_list(dir_list)
    pass


def handle_files():
    # get cpp files from file_list[]
    # put them into cpp_files[]

    for m_file in file_list:
        file_type = os.path.splitext(m_file)[-1]
        if file_type in [".h", ".cc", ".cpp", ".hpp"]:
            cpp_files.append(m_file)
        if file_type in [".h", ".hpp"]:
            header_files.append(file_type)


def get_header(file_path):
    # get head file from the cpp files
    # build the <file_name, header_list> directory--header_info{}
    m_file = open(file_path, 'r')
    lines = m_file.readlines()
    if len(lines) == 0:
        return
    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip('\n')
    headers = []
    for i in lines:
        # only support the format [#include][space][head file]
        if i.find("#include") == 0:
            headers.append(i.split(' ')[1])
    header_info[file_path.split('/')[-1]] = headers
    pass


def analyse_depend():
    # the format of key-value :
    # file : [user_header... , [sys_header]]

    for key in header_info:
        sys_header = []
        headers = header_info[key]
        dependence_map[key] = []
        for header in headers:
            if header[0] == "\"":
                header = header.split('/')[-1]
                header = header.strip('"').rstrip('"')
                dependence_map[key].append(header)
            else:
                sys_header.append(header)
        dependence_map[key].append(sys_header)
    pass


def print_graph():
    graph = Digraph("dependence")
    for m_file in dependence_map:
        if len(dependence_map[m_file]) > 0:
            data = "\n".join(str(i) for i in dependence_map[m_file][-1])
            if len(data) > 0:
                data = m_file + "\n\n" + data
            else:
                data = m_file
            graph.node(m_file, label=data)
        else:
            print(m_file, "is empty")
    for m_file in dependence_map:
        data_list = dependence_map[m_file][0:-1]
        for node in data_list:
            graph.edge(m_file, node)
    graph.render("dependence.gv", view=True)
    pass


if __name__ == '__main__':
    project_path = input("enter the path:\n")
    get_file_list([project_path])
    handle_files()
    for file in cpp_files:
        get_header(file)
    analyse_depend()
    print_graph()
    pass
