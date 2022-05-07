class SelfTest:

    # 클래스 변수
    name = "yeonwoo"

    def __init__(self, x):
        self.x = x

    # 클래스 매서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self : {self}")
        print("class 안의 self 주소 : ", id(self))
        print("func2")


test_obj = SelfTest(17)
test_obj.func2()
SelfTest.func1()

print("인스턴스의 주소: ", id(test_obj))

test_obj.func1()
print(test_obj.func1())
