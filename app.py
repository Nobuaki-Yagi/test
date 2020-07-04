from flask import Flask, render_template, request
# WTFormsを使ってユーザからデータを収集する
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)


# sayhelloというテキストエリアを持ったformを用意する
class HelloForm(Form):
                                  # 適切かどうかどうかの判断をする
    sayhello = TextAreaField('', [validators.DataRequired()])


@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)


# POSTメソッドを使ってフォームのデータをサーバに送信する
@app.route('/hello', methods=['POST'])
def hello():
    # HelloFormをインスタンス化して使う
    form = HelloForm(request.form)
    # POSTメソッドかつ、検証されたものを
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
