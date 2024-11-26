def same_structure_as(original,other):
    if not isinstance(original, list) or not isinstance(other, list):
        return False
    else:
        if len(original) != len(other) or original[0].__dir__() != other[0].__dir__():
            return False
        else:
            for i, j in zip(original, other):
                if '__getitem__' in i.__dir__() and '__getitem__' in j.__dir__():
                    return same_structure_as(i, j)
                else:
                    return True