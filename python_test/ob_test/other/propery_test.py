import time


class Parent:
    name = ""
    scot = 0

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value
    # property 属性使用
    name_demo = property(get_name, set_name)

# "-----风格线---"

    @property
    def get_scot(self):
        return self.scot

    @get_scot.setter
    def get_scot(self, value):
        self.scot = value


if __name__ == "__main__":
    p = Parent()
    p.name = 10
    print(p.get_name())
    print(p.name)
    p.set_name("xiao")
    print(p.name)

    # property 属性使用
    print("-----风格线---")
    print(p.name_demo)
    p.name_demo = "demo"
    print(p.name_demo)

    # 高级用法
    print(p.get_scot)
    p.get_scot = 10
    print(p.get_scot)
