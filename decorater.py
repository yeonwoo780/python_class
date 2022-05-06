def copyright(func):  # 호출할 함수를 매개변수로 받음
    def new_func():  # 호출할 함수를 감싸는 함수
        print("@ yeonwoo")  # 출력
        func()  # 매개변수로 받은 함수 호출

    return new_func  # nec_func 함수 반환


@copyright  # 데코레이터
def smile():
    print("😊")


@copyright  # 데코레이터
def angry():
    print("😒")


@copyright  # 데코레이터
def love():
    print("😘")


# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()  # 함수 호출
angry()  # 함수 호출
love()  # 함수 호출
