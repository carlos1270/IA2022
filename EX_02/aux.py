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
  for classe in classes:
    if existe_dessa_classe(classe, palavras_classificadas):
      print(f"***{classe[1]}***")
      for palavra in palavras_classificadas:
        if palavra[1] == classe[0]:
          print(f"\t{palavra[0]}")

# Função para impressão das palavras na tela en
def imprimir_en(palavras_classificadas):
  classes = [('CC', 'Conjuções de Coordenação'), ('CD', 'Digitos Cardeais'), ('DT','Determinantes'), ('EX', 'Existênciais'), 
             ('FW', 'Palavras estrangeiras'), ('IN', 'Preposições/Conjuções'), ('JJ', 'Adjetivos'), ('JJR', 'Adjetivos Relacionais'), 
             ('JJS', 'Adjetivos Superlativos'), ('LS', 'Marcadores de lista'), ('MD', 'Modais'), ('NN', 'Substantivos singulares'), 
             ('NNS', 'Substantivos singulares'), ('NNP', 'Substantivos proprios'), ('NNPS', 'Substantivos plurais'),
             ('PDT', 'Predeterminadores'), ('WRB', 'Advérbios Interrogativos'), ('WP$','Adjetivos Possessivos'), ('WP', 'Pronomes Interrogativos'),
             ('WDT', 'Determinantes de WP'), ('VBZ', 'Verbos'), ('VBP', 'Verbos'), ('VBN', 'Verbos'), ('VBG', 'Verbos'), ('VBD', 'Verbos'),
             ('VB', 'Verbos'), ('UH', 'Interjeições'), ('TO', 'To go'), ('RP', 'Particulas'), ('RBS', 'Advérbios'), ('RB', 'Advérbios'), 
             ('RBR', 'Advérbios'), ('PRP', 'Pronomes Pessoais'), ('PRP$', 'Pronomes Profissionais')]
  for classe in classes:
    if existe_dessa_classe(classe, palavras_classificadas):
      print(f"***{classe[1]}***")
      for palavra in palavras_classificadas:
        if palavra[1] == classe[0]:
          print(f"\t{palavra[0]}")

# Função que checa a lingua e imprime a classificação correta
def imprimir(palavras_classificadas, lingua):
  if lingua == 'pt':
    imprimir_pt(palavras_classificadas)
  imprimir_en(palavras_classificadas)

# Função que detecta o idoma do texto
def get_idioma(frase):
    return langdetect.detect(frase)