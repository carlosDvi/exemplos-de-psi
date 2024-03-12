from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/jogos/<J>')
def jogos(J):
   return render_template('jogos.html', J=J)







if __name__ == '__main__':
    app.run()