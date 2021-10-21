class CustomNumericalList(list):
    """
        This class works with numeric lists and override sum and sub
        __add__ and __sub__/__rsub__ is very similar to the typical implementation of the merge function
    """

    def __add__(self, other):
        custom_list_answ = CustomNumericalList()
        current = 0
        while current < len(self) and current < len(other):
            custom_list_answ.append(self[current] + other[current])
            current += 1
        while current < len(self):
            custom_list_answ.append(self[current])
            current += 1
        while current < len(other):
            custom_list_answ.append(other[current])
            current += 1
        return custom_list_answ

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        custom_list_answ = CustomNumericalList()
        current = 0
        while current < len(self) and current < len(other):
            custom_list_answ.append(self[current] - other[current])
            current += 1
        while current < len(self):
            custom_list_answ.append(self[current])
            current += 1
        while current < len(other):
            custom_list_answ.append(-other[current])
            current += 1
        return custom_list_answ

    def __rsub__(self, other):
        """Just take the result of __sub__ with the sign '-'"""
        return CustomNumericalList(map(lambda item: -item, self.__sub__(other)))

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)


def main():
    pass


if __name__ == '__main__':
    main()
