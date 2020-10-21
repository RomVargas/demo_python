from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/demo")
def demo():
    nest_list = [1, 2, [3, 4, [5, 6], 7], 8]
    imprimir(nest_list)
    return "demo_Docker"

def imprimir(lista):
    response = []
    for elemento in lista:
        if isinstance(elemento, list):
            imprimir(elemento)
        else:
            print(elemento)


if __name__ == "__main__":
    app.run()