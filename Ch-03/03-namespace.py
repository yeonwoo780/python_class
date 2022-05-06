class Robot:

    population = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots workings")

    # 클래스 매서드
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} Robot")


print(Robot.population)
siri = Robot("siri", 123154133)
jarvis = Robot("jarvis", 1231424534)
bixby = Robot("bixby", 12324234245)

print(Robot.__dict__)

print(siri.__dict__)

print(jarvis.__dict__)

print(siri.name)
print(bixby.name)

print(siri.population)

siri.how_many()

Robot.say_hi()
