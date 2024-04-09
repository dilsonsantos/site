
# Project Site
## Flask
___
Flask é uma estrutura leve de aplicativo da web WSGI . Ele foi projetado para tornar o 
início rápido e fácil, com a capacidade de escalar para aplicações complexas. Começou 
como um simples wrapper em torno de Werkzeug e Jinja e se tornou uma das estruturas de 
aplicativos Web Python mais populares.

O Flask oferece sugestões, mas não impõe nenhuma dependência ou layout do projeto. Cabe 
ao desenvolvedor escolher as ferramentas e bibliotecas que deseja utilizar. Existem muitas 
extensões fornecidas pela comunidade que facilitam a adição de novas funcionalidades.

## Criando um projeto Flask
### Criar a pasta do projeto:
___
```
$ mkdir myproject
$ cd myproject
```
### Criando e ativando ambiente virtual:
```
$ activate.bat
(.env) $ deactivate
```
### Instalando o Flask
Instale e atualize do PyPI usando um instalador como pip:
```  
(.env) $ pip install -U Flask
```
## Dica:
___
> Você sempre deve ter um meio simples de recriar um 
> ambiente (por exemplo, se você tiver um arquivo de 
> requisitos requirements.txt, você pode invocar pip 
> install -r requirements.txt usando o pip do ambiente 
> para instalar todos os pacotes necessários para o 
> ambiente). Se por algum motivo você precisar mover 
> o ambiente para um novo local, deverá recriá-lo no 
> local desejado e excluir o do local antigo. Se você 
> mover um ambiente porque moveu um diretório pai dele, 
> deverá recriar o ambiente em seu novo local. Caso 
> contrário, o software instalado no ambiente pode não 
> funcionar conforme o esperado.
## Um exemplo simples
___
```Python  
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```
```Bash  
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
___

