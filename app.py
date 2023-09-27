import os
from datetime import datetime, date

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

    if request.method == 'POST':
        name = request.form['user-name']
        day = request.form['user-day']
        month = request.form['user-month']
        year = request.form['user-year']

        today = date.today()
        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))

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
            f13 = num_sum(f12 + f4)  # 16

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
            f36 = num_sum(f2 + f17)  # 15
            f37 = num_sum(f2 + f36)  # 16
            f38 = num_sum(f17 + f36)  # 11
            f39 = num_sum(f17 + f38)  # 7
            f40 = num_sum(f36 + f38)  # 8
            f41 = num_sum(f36 + f37)  # 4
            f42 = num_sum(f2 + f37)  # 17

            # 25 age
            f43 = num_sum(f2 + f18)  # 19
            f44 = num_sum(f43 + f18)  # 10
            f45 = num_sum(f44 + f18)  # 10
            f46 = num_sum(f43 + f44)  # 11
            f47 = num_sum(f43 + f2)  # 20
            f48 = num_sum(f2 + f47)  # 21
            f49 = num_sum(f43 + f47)  # 12

            # 35 age
            f50 = num_sum(f18 + f3)  # 8
            f51 = num_sum(f50 + f18)  # 8
            f52 = num_sum(f18 + f51)  # 8
            f53 = num_sum(f50 + f51)  # 16
            f54 = num_sum(f50 + f3)  # 7
            f55 = num_sum(f54 + f3)  # 6
            f56 = num_sum(f50 + f54)  # 15

            # 45 age
            f57 = num_sum(f3 + f19)  # 11
            f58 = num_sum(f3 + f57)  # 10
            f59 = num_sum(f3 + f58)  # 9
            f60 = num_sum(f57 + f58)  # 21
            f61 = num_sum(f57 + f19)  # 5
            f62 = num_sum(f57 + f61)  # 16
            f63 = num_sum(f19 + f61)  # 8

            # 55 age
            f64 = num_sum(f19 + f4)  # 7
            f65 = num_sum(f19 + f64)  # 10
            f66 = num_sum(f19 + f65)  # 4
            f67 = num_sum(f64 + f65)  # 17
            f68 = num_sum(f4 + f64)  # 11
            f69 = num_sum(f4 + f68)  # 15
            f70 = num_sum(f64 + f68)  # 18

            # 65 age
            f71 = num_sum(f4 + f20)  # 21
            f72 = num_sum(f4 + f71)  # 7
            f73 = num_sum(f4 + f72)  # 11
            f74 = num_sum(f71 + f72)  # 10
            f75 = num_sum(f20 + f71)  # 11
            f76 = num_sum(f20 + f75)  # 10
            f77 = num_sum(f71 + f75)  # 5

            # 75 age
            f78 = num_sum(f1 + f20)  # 3
            f79 = num_sum(f1 + f78)  # 16
            f80 = num_sum(f1 + f79)  # 11
            f81 = num_sum(f78 + f79)  # 19
            f82 = num_sum(f78 + f20)  # 20
            f83 = num_sum(f82 + f20)  # 10
            f84 = num_sum(f78 + f82)  # 5

            context = {
                'title': 'Калькулятор',
                'birthday': birthday,
                'name': name,
                'age': age,
                'f1': f1,
                'f2': f2,
                'f3': f3,
                'f4': f4,
                'f5': f5,
                'f6': f6,
                'f7': f7,
                'f8': f8,
                'f9': f9,
                'f10': f10,
                'f11': f11,
                'f12': f12,
                'f13': f13,
                'f14': f14,
                'f15': f15,
                'f16': f16,
                'f17': f17,
                'f18': f18,
                'f19': f19,
                'f20': f20,
                'f21': f21,
                'f22': f22,
                'f23': f23,
                'f24': f24,
                'f25': f25,
                'f26': f26,
                'f27': f27,
                'f28': f28,
                'f29': f29,
                'f30': f30,
                'f31': f31,
                'f32': f32,
                'f33': f33,
                'f34': f34,
                'f35': f35,
                'f36': f36,
                'f37': f37,
                'f38': f38,
                'f39': f39,
                'f40': f40,
                'f41': f41,
                'f42': f42,
                'f43': f43,
                'f44': f44,
                'f45': f45,
                'f46': f46,
                'f47': f47,
                'f48': f48,
                'f49': f49,
                'f50': f50,
                'f51': f51,
                'f52': f52,
                'f53': f53,
                'f54': f54,
                'f55': f55,
                'f56': f56,
                'f57': f57,
                'f58': f58,
                'f59': f59,
                'f60': f60,
                'f61': f61,
                'f62': f62,
                'f63': f63,
                'f64': f64,
                'f65': f65,
                'f66': f66,
                'f67': f67,
                'f68': f68,
                'f69': f69,
                'f70': f70,
                'f71': f71,
                'f72': f72,
                'f73': f73,
                'f74': f74,
                'f75': f75,
                'f76': f76,
                'f77': f77,
                'f78': f78,
                'f79': f79,
                'f80': f80,
                'f81': f81,
                'f82': f82,
                'f83': f83,
                'f84': f84
            }

            return render_template('index.html', context=context)

    context = {
        'title': 'Калькулятор'
    }

    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run()
