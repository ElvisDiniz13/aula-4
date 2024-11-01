clear limpa o shell do docker

cat desafios.txt = visualiza o arquivo

touch arq.txt = cria arquivo

rm arq.txt = remove o arquivo

mkdir fast-produtos = cria pasta

pyton -m venv ./venv = cria um ambiente virtual

. venv/bin/activate = ativa o ambiente virtual

deactivate = desabilita o venv

pip install Django = instala o django

pip freeze = mostra o que está instalado

pip freeze > requirements.txt = cria arquivo listando as versões instaladas

/bin/bash = deixa o shell "do jeito que conheço". Exemplo:





Dúvida respondida sobre o venv:

"Elvis Leite Diniz

Indaiatuba - SP

Eu não entendi muito bem o conceito de venv. O docker já não é um ambiente virtualizado? Pode me exp...

ver mais

Boa noite, Elvis!



O venv é uma ferramenta do Python que cria ambientes virtuais. Isso significa que ele cria um diretório isolado onde você pode instalar pacotes específicos para um projeto sem interferir na instalação global do Python ou em outros projetos.



Já o Docker é uma solução mais abrangente que virtualiza aplicações e ambientes, incluindo todo o sistema operacional e suas dependências.



Os dois podem ser usados juntos! Você pode utilizar o venv para isolar os pacotes que sua aplicação precisa, enquanto o Docker gerencia todo o ambiente.



O professor mencionou o uso do venv para mostrar que é uma boa prática no gerenciamento de pacotes.



Espero que isso ajude!"



django-admin start project setup . = criar projeto django



python manage.py runserver 0.0.0.0:8000 (127.0.0.1) se for windows



python manage.py startapp produto= cria um app (módulo do projeto)

docker hub = site com imagens prontas do Docker