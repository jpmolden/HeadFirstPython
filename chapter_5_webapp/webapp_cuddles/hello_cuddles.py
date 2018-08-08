''' Chapter 5: Building Webapps

'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/requestcomplete', methods=['POST'])
def do_search() -> 'html':
    name = request.form['name']
    occupation = request.form['occupation']
    email = request.form['email']
    cuddle_num = request.form['cuddle_num']
    title = 'Thank You ' + request.form['name'] + '! '
    return render_template('results.html',
                           j_title = title,
                           j_name = name,
                           j_email = email,
                           j_cuddle_num = cuddle_num,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           j_title='Official Bri Cuddle Request!')

if __name__ == '__main__':
    app.run(debug=True)
