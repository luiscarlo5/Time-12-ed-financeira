# dados obtidos por previsao por regressao Linear Ordinanria com
# precos de alimentos em varejo de sao paulo dee janeiro de 2019
# ate dezembro de 2023
def previsor(ultimo_mes):
  infla_julho = 0.006632080
  infla_agosto = 0.006588386
  infla_setembro = 0.00654526
  aux_infla = [infla_julho, infla_agosto, infla_setembro]
  meses_new3 = []
  aux = ultimo_mes
  for infla in aux_infla:
    aux = (aux) + (aux * infla)

    meses_new3.append(aux)

  
  return meses_new3