import langdetect

# Função que verifica se existe palavras de uma determinada classe
def existe_dessa_classe(classe, palavras):
  for palavra in palavras:
    if palavra[1] == classe[0]:
      return True
  return False

# Função para impressão das palavras na tela pt-BR
def imprimir_pt(palavras_classificadas):
  classes = [('ADJ', 'Adjetivos'), ('ADV', 'Advérbios'), ('ADV-KS', 'Advérbios Conectivos Subordinativos'),
             ('ADV-KS-REL', 'Advérbios Conectivos Relativos'), ('ART', 'Artigos'), ('KC', 'Conjuções Coordenativas'),
             ('KS', 'Conjuções Subordinativas'), ('IN', 'Interjeições'), ('NUM', 'Numerais'), ('PDEN', 'Palavras Denotativas'),
             ('PCP', 'Particípios'), ('PROADJ', 'Pronomes Adjetivos'), ('PRO-KS', 'Pronomes Conectivos Subordinados'),
             ('PRO-KS-REL', 'Pronomes Conectivos Subordinados Relativos'), ('PROPESS', 'Pronomes Pessoais'), ('PROSUB', 'Pronome Substantivo'),
             ('CUR', 'Simbolos de moedas'), ('N', 'Substantivos'), ('NPROP', 'Substantivos Próprios'), ('V', 'Verbos'),
             ('VAUX', 'Verbos Auxiliares')]
  saida=[]
  for classe in classes:        
    if existe_dessa_classe(classe, palavras_classificadas):
     
              
      if(classe[1]=="Substantivos" or classe[1]=="Substantivos Próprios"):
        for palavra in palavras_classificadas:
          if palavra[1] == classe[0]:
            saida.append("("+str(palavra[0])+")")
          elif(palavra[0]=="," or palavra[0]=="e" or palavra[0]=="."):
            saida.append("∧")
          elif(palavra[0]=="todos" or palavra[0]=="todo"):
            saida.append("∀")
          elif(palavra[0]=="são" or palavra[0]== "é"):
            saida.append("∈")
          elif(palavra[0]=="não"):
            saida.append("¬")
          elif(palavra[0]=="possuem" or palavra[0]=="possui"):
            saida.append("→")
          elif(palavra[0]=="vivem" or palavra[0]=="habitam"):
            saida.append("⊆")
          elif(palavra[0]=="ou"):
            saida.append("∨")
          elif(palavra[0]=="alguns"):
            saida.append("∃")
          elif(palavra[0]=="eles"):
            saida.append("eles")
          elif(palavra[0]== "no" or palavra[0]== "na" or palavra[0]== "o" or palavra[0]== "a" or palavra[0]== "nos" or palavra[0]== "nas"
               or palavra[0]== "os" or palavra[0]== "as" or palavra[0]== "(" or palavra[0]== ")"or palavra[0]=="que" or palavra[0]=="em"):
            flag=0               
          else:
            saida.append("("+str(palavra[0])+")")
            
  tamanho=len(saida)
  
  if(saida[tamanho-1]== "∧"):
    saida[tamanho-1]="."
  
  cont_eles=0
  cont_alguns=0
  contexto=""  
  for i in range(tamanho):
    
    if(saida[i]=="¬"):
      
      if(saida[i+1]=="→"):
        
        aux=saida[i+1]
        saida[i+1]=saida[i]
        saida[i]=aux
        
      elif(saida[i+1]=="∈"):
        
        saida[i]="∉"
        saida[i+1]=""
        
    
              
    if("(" in saida[i]):
      if("(" in saida[i+1]):
        
        val_Anterior=str(saida[i])
        val_Anterior=val_Anterior.replace(")"," ")
        
        val_Prox=str(saida[i+1])
        val_Prox=val_Prox.replace("(","")
        saida[i]=val_Anterior+val_Prox
        saida[i+1]=""
        
    if(saida[i]=="eles"):
      if("(" in saida[i+1]):
        saida[i]=""
      else:
        for k in range(tamanho):
          if(saida[k]=="⊆" and cont_eles==0):
            contexto=saida[k-1]
            cont_eles+=1
            saida[i]=contexto
            
    if(saida[i]=="∃"):
      for k in range(tamanho):
          if(saida[k]=="⊆" and cont_alguns==0):
            contexto=saida[k-1]
            cont_alguns+=1
      saida[i]= str(saida[i])+" "+contexto
       
    
  for i in range(tamanho):
    if("selvagens"in saida[i]):
      print(saida[i],end=" ")
      print(".")
      break
    print(saida[i],end=" ")

       




# Função que checa a lingua e imprime a classificação correta
def imprimir(palavras_classificadas, lingua):
  if lingua == 'pt':
    imprimir_pt(palavras_classificadas)
  

# Função que detecta o idoma do texto
def get_idioma(frase):
    return langdetect.detect(frase)