def copyright(func):
    def new_func():
        print("@ yeonwoo")
        func()

    return new_func


@copyright
def smile():
    print("😊")


@copyright
def angry():
    print("😒")


@copyright
def love():
    print("😘")


# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)

smile()
angry()
love()
