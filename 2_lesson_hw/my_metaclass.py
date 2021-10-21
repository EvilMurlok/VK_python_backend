class CustomAttrMetaclass(type):
    """
        This is a metaclass that prefixes with 'custom_'
        at the beginning of the names of all attributes
        and methods (except magic ones)
    """

    def __new__(mcs, cls_name, bases, attrs):
        if cls_name.startswith('None'):
            return None
        custom_attrs = {
            attr if attr.startswith('__') and attr.endswith('__') else 'custom_' + attr: value
            for attr, value in attrs.items()
        }
        custom_attrs['__setattr__'] = lambda self, name, value: object.__setattr__(self, 'custom_' + name, value)
        return super(CustomAttrMetaclass, mcs).__new__(mcs,
                                                       cls_name,
                                                       bases,
                                                       custom_attrs)


class CustomPointClass(metaclass=CustomAttrMetaclass):
    coordinate_system = 'Cartesian'
    dimension = 2

    def __init__(self, x_val=0, y_val=0):
        self.x = x_val
        self.y = y_val

    def set_new_point(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


def main():
    point = CustomPointClass(10, 19)
    print(point.custom_coordinate_system)
    try:
        print(point.coordinate_system)
    except AttributeError as err:
        print(err)

    print(point.custom_dimension)
    try:
        print(point.dimension)
    except AttributeError as err:
        print(err)

    print(point.custom_x)
    print(point.custom_y)

    point.custom_set_new_point(8, 88)
    try:
        point.set_new_point(666, 666)
    except AttributeError as err:
        print(err)

    print(point.custom_x)
    print(point.custom_y)
    try:
        print(point.x)
        print(point.y)
    except AttributeError as err:
        print(err)

    p2 = CustomPointClass(13, 13)


if __name__ == '__main__':
    main()
