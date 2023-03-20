# Python-Analyst-Project
Модуль users должен содержать классы Human, Student(Human), Teacher(Human).
Класс Human должен содержать следующую информацию: имя, фамилию, возраст, пол, национальность, а также способы задания этой информации.
h1 = Human(name="John", familyname="Wick", age=35, gender="male", nationality="USA")
Список методов:

set_name()
set_family()
set_age()
set_gender()
set_nationality()
get_info() # возвращает словарь с личной информацией об объекте
Класс Student - это детский класс класса Human. Он должен содержать следующую информацию о каждом студенте: имя, фамилия, возраст, пол, национальность, название школы или университета, список предметов и соответствующие методы для установки этой информации.
Список методов в дополнение к списку методов из родительского класса Human:

set_school()
add_subject() # добавить предмет в список предметов
Класс Teacher - это детский класс класса Human. Он должен содержать следующую информацию о каждом преподавателе: имя, фамилия, возраст, пол, национальность, название школы или университета, предмет преподавания и соответствующие методы для установки этой информации.
Список методов в дополнение к списку методов из родительского класса Human:

set_school()
add_subject() # добавить предмет преподаваемый учителем
При непосредственном запуске модуля users напрямую должен отображаться список классов, а также списки методов соответствующих классов, приведенных в модуле.


Модуль organizations должен содержать класс School.
Класс School должен содержать следующую информацию: название или номер школы, адрес школы, номер телефона школы, электронный адрес учебного заведения, количество учеников, количество учителей, а также способы задания этой информации.

s1 = School(name="NIS", address="Astana, Kazakhstan", phone="999999", num_stud=1000, num_teachers=50)
Список методов:

set_name()
set_address()
set_phone()
set_email()
set_num_stud()
set_num_teachers()
add_student()
add_teacher()
get_info() # возвращает словарь с информацией про школу без личной информации студентов / преподавателей
get_report() # создает отчет (файл "csv") с информацией о школе и о каждом ученике, а также о преподавателе в этой школе. 


При непосредственном запуске модуля organizations напрямую должен отображаться список классов, а также списки методов соответствующих классов, приведенных в модуле.
