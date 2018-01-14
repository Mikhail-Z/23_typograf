from flask import Flask, render_template, request
import typograph as tp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        input_text = request.form['text']
        return tp.handle_text(input_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
