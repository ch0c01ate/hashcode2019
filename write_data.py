def write(file_name, data):
    S = len(data)
    ids = list(map(lambda x: x [0], data))
    f = open(file_name, 'w', encoding='utf-8')
    f.write(str(S) + '\n')
    for id_ in ids:
        if isinstance(id_, tuple) == True:
            f.write(' '.join(list(map(str,id_))) + '\n')
        else:
            f.write(str(id_) + '\n')
    f.close()



