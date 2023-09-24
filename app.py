import os
from datetime import datetime

from flask import Flask, render_template, request, url_for, flash
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


def num_sum(num):
    num = int(num)
    if num > 22:
        return num_sum(sum(map(int, list(str(num)))))
    return num


@app.route("/", methods=['POST', 'GET'])
def index():
    list_value = []

    if request.method == 'POST':
        name = request.form['user-name']
        day = request.form['user-day']
        month = request.form['user-month']
        year = request.form['user-year']

        if not day.isdigit():
            flash("Поле День должно содержать только цифры")
        else:
            if int(day) > 31:
                flash("Дней не может быть больше 31")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if not month.isdigit():
            flash("Поле Месяц должно содержать только цифры")
        else:
            if int(month) > 12:
                flash("Месяцев не может быть больше 12")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if not year.isdigit():
            flash("Поле Год должно содержать только цифры")
        else:
            if 1900 > int(year) or int(year) > datetime.now().year:
                flash(
                    f"Год должен быть в диапазоне от 1900 до {datetime.now().year}")
                context = {
                    'title': 'Матрица личностей',
                }
                return render_template('index.html', context=context)

        if day.isdigit() and month.isdigit() and year.isdigit():
            birthday = f'{day}.{month}.{year}'

            f1 = num_sum(day)  # 13
            f2 = num_sum(month)  # 1
            f3 = num_sum(year)  # 17
            f4 = num_sum(f1 + f2 + f3)  # 4

            f5 = num_sum(f1 + f2 + f3 + f4)  # 8 center

            f6 = num_sum(f5 + f1)  # 21
            f7 = num_sum(f6 + f1)  # 7

            f8 = num_sum(f5 + f2)  # 9
            f9 = num_sum(f8 + f2)  # 10

            f10 = num_sum(f5 + f3)  # 7
            f11 = num_sum(f10 + f3)  # 6

            f12 = num_sum(f5 + f4)  # 12
            f13 = num_sum(f12 + f3)  # 16

            f14 = num_sum(f10 + f12)  # 19
            f15 = num_sum(f10 + f14)  # 8
            f16 = num_sum(f12 + f14)  # 4

            f17 = num_sum(f1 + f2)  # 14
            f18 = num_sum(f2 + f3)  # 18
            f19 = num_sum(f3 + f4)  # 21
            f20 = num_sum(f1 + f4)  # 17

            f21 = num_sum(f17 + f5)  # 22
            f22 = num_sum(f21 + f17)  # 9

            f23 = num_sum(f5 + f18)  # 8
            f24 = num_sum(f23 + f18)  # 8

            f25 = num_sum(f5 + f19)  # 11
            f26 = num_sum(f25 + f19)  # 5

            f27 = num_sum(f5 + f20)  # 7
            f28 = num_sum(f27 + f20)  # 6

            # circle-line
            # 5 age
            f29 = num_sum(f1 + f17)  # 9
            f30 = num_sum(f1 + f29)  # 22
            f31 = num_sum(f29 + f17)  # 5
            f32 = num_sum(f29 + f31)  # 14
            f33 = num_sum(f31 + f17)  # 19
            f34 = num_sum(f30 + f1)  # 8
            f35 = num_sum(f29 + f30)  # 4

            # 15 age
            f36 = num_sum()  # 15
            f37 = num_sum()  # 16
            f38 = num_sum()  # 11
            f39 = num_sum()  # 7
            f40 = num_sum()  # 8
            f41 = num_sum()  # 4
            f42 = num_sum()  # 17

            # 25 age
            f43 = num_sum()  # 19
            f44 = num_sum()  # 10
            f45 = num_sum()  # 10
            f46 = num_sum()  # 11
            f47 = num_sum()  # 20
            f48 = num_sum()  # 21
            f49 = num_sum()  # 12

            # 35 age
            f50 = num_sum()  # 8
            f51 = num_sum()  # 8
            f52 = num_sum()  # 8
            f53 = num_sum()  # 16
            f54 = num_sum()  # 7
            f55 = num_sum()  # 6
            f56 = num_sum()  # 15

            # 45 age
            f57 = num_sum()  # 11
            f58 = num_sum()  # 10
            f59 = num_sum()  # 9
            f60 = num_sum()  # 21
            f61 = num_sum()  # 5
            f62 = num_sum()  # 16
            f63 = num_sum()  # 8

            # 55 age
            f64 = num_sum()  # 7
            f65 = num_sum()  # 10
            f66 = num_sum()  # 4
            f67 = num_sum()  # 17
            f68 = num_sum()  # 11
            f69 = num_sum()  # 15
            f70 = num_sum()  # 18

            # 65 age
            f71 = num_sum()  # 21
            f72 = num_sum()  # 7
            f73 = num_sum()  # 11
            f74 = num_sum()  # 10
            f75 = num_sum()  # 11
            f76 = num_sum()  # 10
            f77 = num_sum()  # 5

            # 75 age
            f78 = num_sum()  # 3
            f79 = num_sum()  # 16
            f80 = num_sum()  # 11
            f81 = num_sum()  # 19
            f82 = num_sum()  # 20
            f83 = num_sum()  # 10
            f84 = num_sum()  # 5

            context = {
                'title': 'Калькулятор',
                'birthday': birthday,
                'name': name,
                'month': month,
                'day': day,
                'year': year
            }

            return render_template('index.html', context=context)

    context = {
        'title': 'Калькулятор'
    }

    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run()
