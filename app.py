from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a segunda página
@app.route('/second')
def second():
    return render_template('segunda.html')

if __name__ == '__main__':
    app.run(debug=True)