from parse_data import parse
import copy
def distance(photo_a, photo_b):
    tags_a = photo_a[-1]
    tags_b = photo_b[-1]
    return len(set(tags_a).intersection(set(tags_b)))

def find_next_similar(photo, photos:list):
    data = copy.deepcopy(photos)
    del data[data.index(photo)]
    similar = 0
    dist = -1
    for var in data:
        cur_dist = distance(photo, var)
        if cur_dist> dist:
            similar = var
            dist = cur_dist
    return similar
data = parse('data/a_example.txt')
s = find_next_similar(data[0], data)
k = 0


