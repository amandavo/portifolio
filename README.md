# PORTIFOLIO | AMANDA VIEIRA

## :pencil: Sobre
O projeto tem como objetivo criar um portifolio em site para a matéria de Design Digital.

## :gear: Tecnologias Utilizadas
[Figma](http://www.figma.com), [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML), [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript), [Python](https://www.python.org/), [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Visual Studio Code](https://code.visualstudio.com/)

## :dart: Backlog
  
 #### Requisitos Funcionais  
| CÓDIGO | DESCRIÇÃO |
|:------:|:---------:|
| RF 01 | Protótipo navegavel |
| RF 02 | Wireframe para Desktop e Mobile |
| RF 03 | Uso de HTML 5 e CSS 3 |
| RF 04 | Arquivo README |
| RF 05 | Sistema completo |
| RF 06 | Responsividade |
| RF 07 | Implantação local |
| RF 08 | Uso de fonte externa |
| RF 09 | Hospedagem pelo Heroku |
 
#### Requisitos Não Funcionais  
| CÓDIGO | DESCRIÇÃO | 
|:------:|:---------:|
| RNF 01 | Banco de dados em MySQL|
| RNF 02 | Frontend em Javascript |
| RNF 03 | Interface simples e intuitiva |
| RNF 04 | Backend em Python 3+ e microframework Flask |

## :file_folder: Configuração das pastas
* `doc`: Pasta com Protótipos
* `src`: Pasta com Códigos.
outros: Pasta com Documentação relacionada ao Projeto

## :mag_right: Como rodar
    
Tecnologias necessárias: Python 3.10 e Workbench
    
- crie uma pasta, entre nela e clone o reposiório
~~~   
git clone https://github.com/amandavo/portifolio.git
~~~
    
- entre na pasta source do projeto 
~~~   
cd portifolio\src
~~~
    
- instale o ambiente que ele será processado 
~~~   
py -m venv venv
~~~
    
- ative o ambiente 
~~~   
venv\Scripts\activate
~~~

- baixe as bibliotecas necessarias 
~~~   
pip install -r requirements.txt
~~~

- entre na pasta api
~~~   
cd api
~~~

- inicie o site 
~~~   
flask run
~~~

- caso nao aceite, utilize 
~~~   
python3 app.py
~~~
    
- acesse o site utilizando 
~~~   
http://127.0.0.1:5000
~~~