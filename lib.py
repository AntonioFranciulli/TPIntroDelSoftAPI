import json

# Library of auxiliary functions used throught the API.

def aux_eliminar_voluntario(lista_voluntarios, cuil):
  '''
    Recibe una lista en formato str
    Elimina el cuil dado
    Devuelve lista en formato str
  '''
  # lista_voluntarios: list = json.loads(lista) # '[]' => []
  for i in range(len(lista_voluntarios)):
    if lista_voluntarios[i] == cuil:
      print(f'Se elimino {cuil}')
      lista_voluntarios.pop(i)
      break
  
  return json.dumps(lista_voluntarios) # [] => '[]'