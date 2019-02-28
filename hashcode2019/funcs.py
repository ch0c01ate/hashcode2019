from parse_data import parse
import copy
def distance(photo_a, photo_b):
    tags_a = photo_a[-1]
    tags_b = photo_b[-1]
    return len(set(tags_a).intersection(set(tags_b)))

def find_next_similar(photo, photos:list):
    if photo in photos:
        del photos[photos.index(photo)]
    result = []
    for var in photos:
        cur_dist = distance(photo, var)
        if cur_dist !=0:
            result.append((cur_dist, var))
    result.sort(key = lambda x: x[0])
    return result

def delete_photo(photo, photos):
    pass




