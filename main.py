import copy


def delete_empties(matrix):
    result = copy.deepcopy(matrix)
    for i in range(0, 2):
        result = list(filter(delete_row, result))
        result = list(map(list, zip(*result)))
    return result


def delete_empties_not_func_style(matrix):
    result = copy.deepcopy(matrix)
    delete_rows(result)
    result = list(zip(*result[::-1]))
    delete_rows(result)
    result = list(map(list, reversed(list(zip(*result)))))
    return result


def delete_row(array):
    if max(array) == min(array) == 0:
        return False
    else:
        return True


def delete_rows(matrix):
    for i in range(len(matrix) - 1, -1, -1):
        if max(matrix[i]) == min(matrix[i]) == 0:
            del matrix[i]
            i -= 1
