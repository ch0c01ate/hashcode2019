def write(file_name, data):
    S = len(data)
    ids = list(map(lambda x: x [0], data))
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(S) + '\n')
        for id_ in ids:
            if isinstance(id_, list) == True:
                f.write(' '.join(list(map(str,id_))) + '\n')
            else:
                f.write(str(id_) + '\n')

test = [(0,'H', ['cat', 'beach', 'sun']),
(3,'V' , ['selfie', 'smile']),
([1,2],'V', ['garden', 'selfie'])]
write('t.txt',test)

