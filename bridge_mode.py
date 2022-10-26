
from abc import abstractmethod, ABCMeta, ABC

'''
桥模式 设计模式，用在两个 并列关系的场景中 或者 某个事物和事物的属性，
重点是 在事物类中， 调用属性类的 方法
'''


class Shape(metaclass=ABCMeta):  # 形状类
    def __init__(self, color_obj):  # 重点 重点， 把颜色的对象传入，作为shape的一个属性，这样形状类可以调用颜色类的方法
        self.color = color_obj

    @abstractmethod
    def draw(self):  # 在形状类中  调用涂写颜色的功能， 在具体形状中实现
        pass


class Color(metaclass=ABCMeta):  # 颜色类， 颜色类作为 形状的一个属性
    @abstractmethod
    def paint(self, shape_obj):
        pass


class Rectangle(Shape):  # 具体形状的类
    name = "Rectangle Test"

    def draw(self):
        self.color.paint(self)


class Circular(Shape):
    name = "Circular Test"

    def draw(self):
        self.color.paint(self)


class Yellow(Color):
    def paint(self, shape_obj):
        # 具体实现，为shape_obj图上黄色
        print("{} is yellow".format(shape_obj.name))


class Green(Color):
    def paint(self, shape_obj):
        print("{} is Green".format(shape_obj.name))


if __name__ == "__main__":
    print("桥模式")
    rec_shape = Rectangle(Yellow())
    rec_shape.draw()

    rec_shape_green = Rectangle(Green())
    rec_shape_green.draw()
