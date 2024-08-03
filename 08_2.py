import heapq


def merge_k_lists(data):
    if not data:
        return 0
    
    merged_list = []
    for item in data:
        merged_list = list(heapq.merge(merged_list, item))

    return merged_list


if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
    