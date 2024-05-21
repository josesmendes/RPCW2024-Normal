import csv

def obter_doenca_e_descricao():
    with open("/home/jose-mendes/teste/ex2/Disease_Description.csv", mode='r', encoding='utf-8') as file:
        dicinario = {}
        reader = csv.DictReader(file)
        for row in reader:
             dicinario[row['Disease']] = row['Description']
    return dicinario

descricao = obter_doenca_e_descricao()




def obter_doenca_e_sintomas():
    with open("/home/jose-mendes/teste/ex2/Disease_Syntoms.csv", mode='r', encoding='utf-8') as file:
        dicinario = {}
        reader = csv.DictReader(file)
        counter = 0
        for row in reader:
            doenca = row['Disease']
            if doenca in dicinario.keys():
                lista = []
                for i in range(1, 18):
                    if row[f'Symptom_{i}']:
                        lista.append(row[f'Symptom_{i}'])
                lista1 = dicinario[doenca]
                for val in lista:
                    if val not in lista1:
                        lista1.append(val)
                dicinario[doenca] = lista1
            else:
                lista = []
                for i in range(1, 18):
                    if row[f'Symptom_{i}']:
                        lista.append(row[f'Symptom_{i}'])
                dicinario[doenca] = lista
        return dicinario

dic = obter_doenca_e_sintomas()

def cria_texto(dicionario):
    sintomas_global = []
    doenca = None
    file = open("teste.ttl", "w")
    texto = ""
    for key,val in dicionario.items():
        new_d = key.replace(" ","_")
        file.write(texto)
        doenca = new_d
        if doenca in descricao.keys():
            texto += f"""
:{doenca} a :Disease ;
                :description "{descricao[doenca]}";
                :hasSymptom"""         
        else:
            texto += f"""
:{doenca} a :Disease ;
                :hasSymptom"""         
        for sint in val[:-1]:
            sint = sint.replace(" ","")
            texto += f" :{sint.title()},"
            if(sint not in sintomas_global):
                sintomas_global.append(sint)
        sint = val[-1].title().replace(" ","")
        texto += f" :{sint}."
        if val[-1].title() not in sintomas_global:
            sintomas_global.append(val[-1].title())
    file.write(texto)
    for sintoma in sintomas_global:
        sintoma = sintoma.replace(" ","")
        file.write(f"\n:{sintoma} a :Symptom .")
    file.close

cria_texto(dic)

#def obter_doenca_e_descricao():
#    with open("/home/jose-mendes/teste/ex2/Disease_Description.csv", mode='r', encoding='utf-8') as file:
#        dicinario = {}
#        reader = csv.DictReader(file)
#        for row in reader:
#             dicinario[row['Disease']] = row['Description']
#    return dicinario


