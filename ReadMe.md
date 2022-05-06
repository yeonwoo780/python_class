# Ch-02

### python Decorater

 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용

<br/>

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

<hr/>

# Ch-03

## Object Oriented Programming (OOP)

> 데이터(data)를 추상화시켜 상태(속성)와 행위(methods)를 가진 객체(object)로 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직(흐름)을 구성하는 프로그래밍 방법

> 프로그램을 실제 세상에 가깝게 모델링하는 기법

## class

> 어떤 문제를 해결하기 위한 데이터를 만들기 위해 OOP 원칙에 따라 집단(현실 세계)에 속하는 속성과 행위(methods)를 변수와 메서드로 정의한 것

> **"로봇 설계도"**

## instance (object)

> class에서 정의한 것(설계도)을 토대로 실제 메모리상에 할당된 것(실제 사물, object)으로 실제 프로그램에서 사용되는 데이터이다.

> 하나의 class로 만들어진 여러 instance(object)는 각각 **독립적**이다.

> **"실제 로봇"**

## OOP 원칙

### 캡슐화 : encapsulation

> 객체(object)의 **속성과 행위(methods)**를 하나로 묶고, 구현된 일부를 외부에 감추어 은닉한다.

### 추상화 : abstraction

> 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써 공통의 속성이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.

### 상속 : Inheritance

> 부모 class의 속성과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우 상속받은 자식 class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다. 또한 자식 class에서 추가적으로 속성이나 행위(methods)를 정의할 수 있게 한다.

### 다형성 : Polymorphism

> 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화할 수 있도록 한다.

- A 공장에서 만든 타이어를 YSS 자동차 회사에서 사용할 수 있고 YYR 자동차 회사에서도 사용할 수 있다.
- 또한, 이 타이어는 탱크의 타이어 개발에 재료로 사용될 수도 있다.



### __init__

- 강의에서 등장한 **__init__ 메서드는 생성자 함수라고 하며 인스턴스가 만들어질 때 인스턴스를 초기화합니다.** 

- __init__ 메서드는 특별한 기능이 있는 매직 메서드중 하나이며 함수 이름을 다른 이름으로 바꿀 수 없습니다.

- 매직 메서드는 나중에 깊게 설명해드립니다.

- 관련 문서 : https://docs.python.org/3/reference/datamodel.html?highlight=__init__#object.__init__

### attribute

- 인스턴스에는 데이터(속성값)와 메서드(속성메서드)로 이루어지는 클래스 attribute가 있습니다.

- 메서드는 함수인데, 그 첫 번째 파라미터는 호출된 인스턴스 자신(self)입니다.

- attribute는 점(.) 뒤에 나오는 모든 이름입니다. **인스턴스.attribute,** **인스턴스.attribute( )**



### namespace

- 개체를 구분할 수 있는 범위


