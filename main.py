from parse_data import parse
from funcs import delete_photo, distance, find_next_similar
from write_data import write



def main():
    
    data_set = input()
    data = parse(data_set)
    slide_show = [data[0]]
    similar = find_next_similar(slide_show[-1], data)
    while len(similar)!=0:
        similar.sort(key=lambda x: x[0])
        next_slide = similar[-1]
        slide_similar = find_next_similar(next_slide[-1], data)
        if len(slide_similar)!=0:
            slide_show.append(next_slide[-1])
        elif len(data) !=0:
            i = -2
            while len(slide_similar) == 0:
                next_slide = similar[i]
                slide_similar = find_next_similar(next_slide, data)
            slide_show.append(next_slide)
        else:
            slide_show.append(next_slide[-1])
        similar = find_next_similar(slide_show[-1], data)
    write('result.txt',slide_show)


if __name__ == "__main__":
    main()