from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo('Claudio')

c = CamelCase()
s = 'Esta oración necesita CamelCase'

camelcased = c.hump(s)
print(camelcased)