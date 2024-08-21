# test git
import os
from dotenv import load_dotenv

load_dotenv()

DIR = os.getenv('DIR')

# https://www.youtube.com/watch?v=VJm_AjiTEEc

# PS I:\my_python> cd I:\my_python\my_programs\обучение\git_learning
# PS I:\my_python\my_programs\обучение\git_learning> git init
# Initialized empty Git repository in I:/my_python/my_programs/обучение/git_learning/.git/
# PS I:\my_python\my_programs\обучение\git_learning> git remote add origin https://github.com/RenatZahar/git_learning.git
# PS I:\my_python\my_programs\обучение\git_learning> 


# копия репо
# cd -> папка
# git clone <url>

# проверка статуса репо
# git status

# подготовка к коммиту файлов
# git add README.MD
# git add .

# старт коммита 
# git commit -m 'Added only README'

# просмотр истории
# git log 

# просмотр веток
# git branch

# создание новых веток 
# git branch <название ветки>

# возврат к версии или к ветке 
# git checkout <commit №/ имя ветки>

# связываем мастер ветку локального гита и удаленного
# git push --set-upstream origin master

# выгрузка на гит хаб
# git push