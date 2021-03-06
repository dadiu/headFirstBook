from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route(
    '/search',
    methods=['POST']
)
def do_something()->'html':

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))

    return render_template(
        'results.html',
        the_title="搜索结果：",
        the_phrase=phrase,
        the_letters=letters,
        the_results=results
    )


@app.route('/')
@app.route('/entry')
def entry_page()->'html':
    return render_template(
        'entry.html',
        the_title="输入文字"
    )


if __name__ == '__main__':
    app.run(debug=True)
