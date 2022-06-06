# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def user_data(first_name, last_name, year_birth, city_residence, email, phone):
    return print(
        f'Получается Ваше  - Имя: {first_name} Фамилия: {last_name} Год рождения: {year_birth} Город проживания: {city_residence} Email: {email} Телефон: {phone}')


user_data(first_name=input('Введите Ваше Имя: '),
          last_name=input('А теперь Фамилию: '),
          year_birth=input('Год рождения: '),
          city_residence=input('Город проживания: '),
          email=input('Ваш электроный адрес - Email: '),
          phone=input('И наконец Ваш телефон: ')
          )
