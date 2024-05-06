def union_files(files, result_file):
    dict_ = {}
    for file in files:

        with open(file, encoding="utf-8") as f:
            list_ = []
            file_1 = f.readlines()
            list_.append(file_1)
            list_.append(len(file_1))
            dict_[file] = list_

    dict_sort = list(sorted(dict_.items(), key=lambda x: x[1][1]))
    print(dict_sort, "sort")
    with open(result_file, "w", encoding="utf-8") as output:
        for file in dict_sort:
            print(file[0], file[1][-1], *file[1][0], sep="\n", file=output)
print(union_files(["1", "2"], "3"))