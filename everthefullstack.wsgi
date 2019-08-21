# vim: syntax=python
import sys
# Na linha abaixo basta  informar o caminho completo para o arquivo bin/activate_this.py dentro da pasta do virtual env
activate_this = '/home/everthefullstack/ambientes_virtuais/python3.6/bin/activate_this.py'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
sys.path.append('/home/everthefullstack/apps_wsgi/everthefullstack')
from server import app as application