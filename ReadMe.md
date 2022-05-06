### python Decorater

 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용

<br>

```python
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

smile()  # 함수 호출
angry()  # 함수 호출
love()  # 함수 호출
```

### 객체 지향 프로그래밍 == Object Oriented Programming == OOP

- 프로그램을 실제 세상에 가깝게 모델링하는 기법

- 데이터를 추상화시켜 속성과 행위를 가진 객체로 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법

### 클래스 (class)

- 특별한 데이터와 메서드의 집합

- ***설계도***라고 할 수 있다.

### 객체 (object)

- class에 선언된 모양 그대로 생성된 실체

### 인스턴스 (instance)

- 객체가 소프트웨어에 실체화될 때 즉, **메모리에 할당되어 사용될 때 해당 객체를 인스턴스라고 한다.**

- 객체는 인스턴스의 상위 개념이지만, 일반적으로 인스턴스와 같은 의미로 사용된다.

- 하나의 클래스로 만들어진 여러 인스턴스들은 각각 독립적이다.
