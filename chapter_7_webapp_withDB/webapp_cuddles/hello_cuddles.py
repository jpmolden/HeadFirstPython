''' Chapter 5: Building Webapps

'''
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/requestcomplete', methods=['POST'])
def do_search() -> 'html':
    name = request.form['name']
    occupation = request.form['occupation']
    email = request.form['email']
    cuddle_num = request.form['cuddle_num']
    title = 'Thank You ' + request.form['name'] + '! '
    log_request(request, cuddle_num)
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


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('cuddle_request.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


def log_request(req: 'flask_request', res: str) -> None:
    with open('cuddle_request.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, sep='|', file=log)


if __name__ == '__main__':
    app.run(debug=True)
