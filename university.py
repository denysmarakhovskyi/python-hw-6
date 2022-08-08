"""Модуль який обʼєднує в собі класи
які допомогають управляти університетом: курсами, студентами і вчителями.
Деякі з цих класів частково реалізовані.
Потрібно пройти по всіх класах, зрозуміти логуку і завершити реалізацію певних методів.
Деякі з цих класів частково реалізовані, але більшість класі потребує допрацювання.
Потрібно пройти по всіх класах, зрозуміти логіку і завершити реалізацію певних методів.
Для тестування можна використовувати інший файл main.py, в данному файлі тестування не робимо.
Потрібно реалізувати всі методи які позначені TODO.
Також потрібно додати до кожно класу метод  def __str__(self):
Для того щоб зрозуміти логіку метода читаємо Python Docstring
(строки по типу тієї яку ви зараз читаєте),
а також дивимося Python typing.
Також потрібно реалізувати до кожного класу метод  def __str__(self):
"""

from datetime import date, datetime
from abc import abstractclassmethod
from abc import ABC, abstractmethod


class Person:
    """Клас Person який означає просто людину і обʼєднує в собі базові атрибути."""
    """Клас Person який обʼєднує в собі базові атрибути кожній людині."""

    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self.first_name = first_name


@ @-24

, 15 + 27, 22 @ @


def get_age(self):
    """Метод який розрахову і повертає поточний вік людини в залежності від дати народження."""

    today = date.today()
    age = today.year - self.birth_date.year - (
            (today.month, today.day) <
            (self.birth_date.month, self.birth_date.day))
    age = (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    )
    return age


age = property(get_age)


def __str__(self):
    return f"Person {self.first_name} {self.last_name}, {self.age} years old."


class Course:
    """Клас курсу в університеті. Обʼєднує логіку яка стосується по курсу."""

    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.start_date = start_date


@ @-45

, 19 + 55, 17 @ @


def is_active(self) -> bool:
    """

def __str__(self):
    return f'{self.name} course. Start: {self.start_date}. Finish: {self.end_date}'
    return f"{self.name} course. Start: {self.start_date}. Finish: {self.end_date}"



class UniversityEmployee(Person):
class UniversityEmployee(Person, ABC):
    """Клас UniversityEmployee який відповідає за працівника університету.
    Наслідується від класу Person.
    Відрізняється від класу Person тим що додано новий атрибут salry
    який відповідає за зарплату працівника(за місяць).
    """

def __init__(self, first_name: str, last_name: str, birth_date: date,
             salary: int):
def __init__(self, first_name: str, last_name: str, birth_date: date, salary: int):
    super().__init__(first_name, last_name, birth_date)
    self.monthly_salary = salary

@@ -67,7 +75,7 @@ def get_yearly_salary(self):
    TODO розробити!
    """


@abstractclassmethod
@abstractmethod
def answer_question(self, course: Course, question: str) -> bool:
    """Метод який викликається коли студент задає питання по навчанню.
    Якщо працівник може відповісти на питання метод повертає True,
@@ -87,8 +95,14 @@ class Teacher(UniversityEmployee):
Можна додавати додаткові атрибути для внутрішньої логіки.
"""


def __init__(self, first_name: str, last_name: str, birth_date: date,
             salary: int, course: Course):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date: date,
            salary: int,
            course: Course,
    ):
        super().__init__(first_name, last_name, birth_date, salary)
        self.course = course


@ @-116

, 15 + 130, 21 @ @


def change_course(self, course: Course) -> bool:
    class Mentor(UniversityEmployee):
        """Клас Mentor який відповідає за ментора університету.
        Наслідується від класу UniversityEmployee.

        Ментор може менторити на декількох курсах одночасно.
        (атрибут courses)
        Курси на яких ментор працює можна замінити за допомогою метода change_courses.
        Можна додавати додаткові атрибути для внутрішньої логіки.
        """

        def __init__(self, first_name: str, last_name: str, birth_date: date,
                     salary: int, courses: list[Course]):
            def __init__(
                    self,
                    first_name: str,
                    last_name: str,
                    birth_date: date,
                    salary: int,
                    courses: list[Course],
            ):
                super().__init__(first_name, last_name, birth_date, salary)
                self.courses = courses


@ @-142

, 7 + 162, 7 @ @


def answer_question(self, course: Course, question: str) -> bool:
    Тобто, якщо
    ментор
    має
    2
    активних
    курси, то
    ментор
    буде
    відповідати
    на
    кожне
    друге
    запитання.
    Тобто, якщо
    ментор
    має
    3
    активних
    курси, то
    ментор
    буде
    відповідати
    на
    кожне
    третє
    запитання.

    Ментор
    як
    і
    вчитель
    ніколи
    не
    відповідає
    на
    питання
    по
    курсах
    на
    яких
    він
    не
    менторить(атрибут
    courses) і
    на
    курсах
    які
    вже
    не
    є
    активними.


@ @-156

, 23 + 176, 23 @ @


def answer_question(self, course: Course, question: str) -> bool:
    mentor.answer_question(some_course,
                           'Чи можу я здати пізніше?') -> True  # теж саме питання, але вже знайшли час відповісти
    mentor.answer_question(some_course, 'Яка оцінка?') -> False  # не вистачило часу відповісти на це питання
    mentor.answer_question(expired_course, 'Чи можу я здати пізніше?') -> False
    mentor.answer_question(expired_course, 'Чи можу я здати пізніше?') -> False
    # питання на яке відповідали, і є час відповісти, але питання стосується курсу який вже закінчився
    mentor.answer_question(some_course, 'Що було на уроці?') -> True
    mentor.answer_question(some_course, 'Що було на уроці?') -> True
    # так як на минуле питання ми не відповідали, на наступне питання є можливість відповісти
    mentor.answer_question(some_course, 'Що було на уроці?') -> True
    mentor.answer_question(some_course, 'Що було на уроці?') -> True
    # не дивлячись на те що ми дуже зайняті, але маємо змогу відповісти на питання, на яке вже відповідали.
    mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> False
    mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> False
    # знову зайняті, False
    mentor.answer_question(some_other_course, 'Як мені виконати ДЗ?') -> True
    mentor.answer_question(some_other_course, 'Як мені виконати ДЗ?') -> True
    # те саме питання по іншому курсу, знайшли час відповісти в цей раз
    mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> True
    mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> True
    # те саме питання по першому курсу, можемо відповідати на це питання поза чергою
    TODO
    розробити!

    @ @-188

    , 13 + 208, 12 @ @

    def change_courses(self, courses: list[Course]) -> bool:
        """



class Student(Person):
    """
        Клас
        Student
        який
        відповідає
        за
        студента
        університету.

    Наслідується
    від
    класу
    Person.
    Можна
    додавати
    додаткові
    атрибути
    для
    внутрішньої
    логіки.
    """


    def add_mark(self, mark: int):
        """
    Метод
    який
    використовується
    вчителем
    коли
    той
    ставить
    оцінку
    стунденту.
    Оцінка
    не
    залежить
    від
    предмету.Потрібно
    зберігати
    всі
    оцінки
    які
    коли
    небудь
    були
    додані.


@ @-203

, 13 + 222, 13 @ @


def add_mark(self, mark: int):
    Для
    зберігання
    оцінок
    можна
    використовувати
    довільну
    структуру
    данних.
    TODO
    розробити!
    """


def get_all_marks(self) -> list[int]:
    """
    Метод
    який
    використовується
    вчителем
    коли
    той
    ставить
    оцінку
    стунденту.
    Оцінка
    не
    залежить
    від
    предмету.Потрібно
    зберігати
    всі
    оцінки
    які
    коли
    неьудь
    були
    додані.
    TODO
    розробити!
    """


def get_avarage_mark(self) -> float:
    """
    Метод
    який
    повертає
    середню
    оцінку
    студенту
    по
    всіх
    наданих
    студенту
    оцінках.
    Наприклад, студент
    має
    наступні
    оцінки[2, 10, 3]


@ @-220

, 14 + 239, 14 @ @


def get_avarage_mark(self) -> float:
    def get_average_by_last_n_marks(self, n: int) -> float:
        """Метод який повертає середню оцінку за певною кількістю останніх оцінок.
        Наприклад, студент має наступні оцінки: [2, 10, 3, 6, 8, 7],
        Наприклад, студент має наступні оцінки: [2, 10, 3, 6, 8, 7],
        якшо викликати функцію з аргументом n=2 то результат повинен бути 6,
        тому що 2 останні оцінки: 2 і 10 - (2+10)/2=6
        Якщо число n<=0 - повертаємо 0.
        Перевірку n на число робити не потрібно, програма може повертати стандартну помилку виконання.
        TODO розробити!
        """

    def get_average_from_date(self, from_date: datetime) -> float:
        """Метод який повертає середню оцінку за певний період (від певної дати).
        Для того щоб реалізувати цей метод потрібно хберігати інформацію про те коли певна оцінка була додана.
@@ -237,10 +256,42 @@ def get_average_from_date(self, from_date: datetime) -> float:
            (3, datetime(2022, 7, 26)),
            (6, datetime(2022, 7, 25)),
            (8, datetime(2022, 7, 24)),
            (7, datetime(2022, 7, 23))],
        якшо викликати функцію з аргументом from_date=datetime(2022, 7, 27) то результат повинен бути 6,
            (7, datetime(2022, 7, 23))],
        якшо викликати функцію з аргументом from_date=datetime(2022, 7, 27) то результат повинен бути 6,
        тому що в заданий період входять тільки 2 останні оцінки: 2 і 10 - (2+10)/2=6
        TODO розробити!
        """


class University:
    """Клас University який зберігає студентів, працівників, та курси
    та обʼєднує в собі базові методи потрібні для роботи університету.
    """

    def __init__(
            self,
            name: str,
            courses: list[Course],
            employees: list[UniversityEmployee],
            students: list[Student],
    ):
        self.name = name
        self.courses = courses
        self.employees = employees
        self.students = students

    def get_average_salary(self) -> float:
        """Метод який розраховує і повертає середню місячну зарплату працівників університету.
        TODO розробити!
        """

    def get_average_mark(self) -> float:
        """Метод який розраховує і повертає середню оцінку всіх студентів університету.
        Для цього потрібно враховувати середню оцінку кожно студента.
        TODO розробити!
        """

    def get_active_courses(self) -> list[Course]:
        """Метод повертає всі активні (в данний момент) курси (Course.is_active()).
        TODO розробити!
        """