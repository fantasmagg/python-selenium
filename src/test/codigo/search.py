import re
import datetime

#re.findall

#text = "hola nose por que soy tan mierda se cuales son los pasos para mejorar mi vida y no lo estoy haciendo"

#palabra = re.findall('nose',text, re.IGNORECASE)


#for pl in palabra:
 #   print(pl)


#-----------------------------------------------------------------

#re.search

#text = "hola nose por que soy tan mierda se cuales son los pasos para mejorar mi vida y no lo estoy haciendo"

#palabra = re.search('n', text, re.IGNORECASE)#search nos dice desde donde empiesa  hasta donde termina

#if palabra:
 #   print("aqui esta")
  #  text = re.sub('nose','lo cambie por esto',text,re.IGNORECASE)

#else:
 #   print("no la encuentro")


#print(text)
#-----------------------------------------------------------------------------------
#text = "hola universo ,se que yo fui el culpable ,y sabemos que no deberiamos estar juntos "

#palabra = re.split(',',text)# split en este caso le pasamos las comas para que se pare las cosas
#mira el ejemplo
#print(palabra)

#for pl in palabra:
 #   print(pl)
  #  if pl =='se que yo fui el culpable ':
   #     break

#-----------------------------------------------------------------------------
#tema #PatronDeBusqueda = r"(?<=deberiamos )\w+"



#Scenario ={}

#text = "hola universo ,se que yo fui el culpable ,y sabemos que no deberiamos estar juntos "

#PatronDeBusqueda = r"(?<=deberiamos )\w+"  #eso es un patron de busqueda hay le desimos (r"(?<=deberiamos )\w")
#?<=deberiamos ) cose lo que esta despues de esa palabra y un espasio en este caso la palabra seria (estar)
#\w ) eso es que se encarga de cojerla

#palabra = re.findall(str(PatronDeBusqueda),text,re.IGNORECASE)

#print(palabra)

#Scenario['fff'] = str(palabra[0])

#print("hoaaaaaaaaaaaaaaaa " + Scenario['fff'])


#------------------------------------------------------------------------------

adressbase = u'https://pestasre.swagger.io/v2'
partHost ="\endpoint\FECHA\Scenario:Today"

def full_host (_partHost):
    _RegexPartHost = str (replace(_partHost))
    _endpoint = adressbase + _RegexPartHost
    print(_endpoint)



def replace(text):
    PatrodeBusqueda = r"(?<=Scenario:)\w+"
    variables = re.findall(str(PatrodeBusqueda),text,re.IGNORECASE)
    for variable in variables:
        if variable =='Today':
            dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
            texts = re.sub('(Scenario:)([^&.]+)', dateToday,text,re.IGNORECASE)
            continue
    return texts






endpoint = full_host(partHost)