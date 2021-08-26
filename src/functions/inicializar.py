import  os #espara el manejo de archivos y rutas

class Inicializar():
    basedir = os.path.abspath(os.path.join(__file__,"../.."))
    DateFormat='%d/%m/%Y'
    HourFormat="%H%M%S"

    #jsonData
    Json =basedir + u'\pages'

    Environment = 'Dev'

    if Environment =='Dev':
        user = 'postgres',
        password = 'ADMIN',
        host = '127.0.0.1',
        port = '5432',
        database = 'test_db'

    #navegador
    NAVEGADOR =u'CHROME'

    #diretorio de evidencia
    Path_Evidencias = basedir +u'/data/capturas'

    #hoja de datos excel
    Excel = basedir+ u'/data/DataTest.xlsx'

    if Environment =='Dev':
        URL ='https://www.spotify.com/do/signup/'
    if Environment == 'Test':
        URL = 'https://en.wikipedia.org/wiki/PATH_(variable)'
