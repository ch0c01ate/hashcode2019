from itertools import permutations
def distance(photo_a, photo_b):
    tags_a = photo_a[-1]
    tags_b = photo_b[-1]
    return set(tags_a).intersection(set(tags_b))


def sort_by_tags(pairs):
    metrics = list(zip(map(lambda x: distance(x[0], x[1]), pairs), pairs))
    metrics.sort(key=lambda x: x[0], metrics)
    return metrics

def get_pairs(photos):
    return permutations(photos, 2)


print(get_pairs(test)