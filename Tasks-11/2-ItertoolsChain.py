def iterchain(fst_list, snd_list):
    from itertools import chain
    return list(chain(fst_list, snd_list))

print(iterchain([2, 1], [3, 5, 8]))