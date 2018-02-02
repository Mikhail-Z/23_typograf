from flask import Flask, render_template, request
import typograph as tp
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import TextAreaField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'
csrf = CSRFProtect()
csrf.init_app(app)


class Text4ChangeForm(FlaskForm):
    input_text = TextAreaField()


@app.route('/', methods=['GET', 'POST'])
def form():
    form = Text4ChangeForm()
    if request.method == 'POST':
        input_text = request.form['input_text']
        print(input_text)
        return tp.handle_text(input_text)
    else:
        return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run()
