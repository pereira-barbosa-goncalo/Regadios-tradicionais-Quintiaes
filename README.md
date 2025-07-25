# Regadios Tradicionais de Quintiães

## Descrição Geral
Este repositório contém um script Python (`pocas.py`) que implementa um sistema de consulta e exportação de turnos para as poças, automatizando a gestão dos tempos atribuídos a cada consorte ao longo do calendário anual. É uma ferramenta orientada a comunidades rurais ou entidades gestoras que necessitam de planificar de forma rigorosa a utilização partilhada de recursos hídricos. Agora também é possível adquirir um executável (`pocas_app.exe`) de modo a remover a necessidade de leitura de python

### Funcionalidades
- Listar consortes e respetivos turnos, com cálculo preciso das datas e horas de início/fim.
- Consultar qual consorte está ativo num determinado dia/hora.
- Exportar os turnos para ficheiros CSV, para posterior análise ou integração noutros sistemas.

Todo o cálculo é baseado em ciclos predefinidos de tempos atribuídos a cada consorte, iniciando-se em datas específicas do ano (definidas conforme a tradição ou regras locais). O código está estruturado para suportar facilmente outras poças ou alterações nos tempos de consórcio.

## Estrutura do Cálculo para as Poças já Implementadas

### Poça Javid
- **Início do ciclo**: Terça-feira mais próxima de 29 de junho às 21:10.
- **Unidades de tempo**: Minutos.
- **Ciclo composto por**: 12 turnos de duração variável.

### Poça Ínsuas
- **Início do ciclo**: Primeiro domingo de julho - 1 dia (sábado) às 21:00.
- **Unidades de tempo**: Horas.
- **Ciclo composto por**: Múltiplos turnos com durações entre 12 e 36 horas.
  - Terras de Fate - David Fernandes - 36 horas
  - Rigueira - António Pereira - 36 horas
  - Pomar - Carlos Xavier - 12 horas
  - Rigueira - Rosa Machado - 12 horas
  - Rigueira - Joaquim Lumbrem - 12 horas
  - Rigueira - Nídia - 12 horas
  - Rigueira - Domingos Coutinho - 12 horas
  - Compra - Rosa Machado - 12 horas
  - Rigueira - Cândido - 12 horas
  - Rigueira - Domingos Coutinho - 12 horas
  - Sepeira - Silvério - 24 horas
  - Ínssuas de baixo - 24 horas
  - Rigueira - Ana do "Rua" - 24 horas

O sistema suporta a repetição infinita dos ciclos até ao fim do ano (31 de dezembro).

## Funcionalidades Principais
- O utilizador escolhe a poça.
- Consultar Consortes.
- Listar a um específico consorte (escolhido pelo utilizador) os tempos que este toma posse e devolve em todos os ciclos. Com a possibilidade de exportar para CSV.
- Consulta do consorte que tem a posse quando é escolhido o dia e a hora.

## Requisitos
- Python 3.8+
- Bibliotecas:
  - `datetime` (padrão)
  - `csv` (padrão)
  - `unicodedata` (padrão)

## Notas Importantes
- O caminho para exportação de CSV deve ser introduzido manualmente e deve existir no sistema de ficheiros.
- As datas de início dos ciclos são calculadas dinamicamente com base no ano atual.

## Conclusão
Este sistema elimina a necessidade de cálculos manuais dos turnos de consortes e oferece uma solução confiável e repetível para comunidades que partilham poças ou outros recursos comuns. A sua simplicidade torna-o ideal para implementação local, sem necessidade de infraestrutura complexa.

## Referências

- **Autor**: Gonçalo Pereira

- **Fontes dos dados de consortes**:
  - **Javid**:
    - Escritura de partilha de água do ano de 1991.
  - **Ínsuas**:
    - Alfredo Silva
    - Maria Machado
    - Rosa Machado

## Citação
Na publicação deste software, é favor citar de acordo com o documento [CITATION](citação) presente neste repositório ou de acordo com os seguintes exemplos:
### formato APA
Pereira, G. (2025). Sistema de Consulta dos regadios tradicionais de Quintiães (Version 1.0.3) [Computer software]. https://github.com/pereira-barbosa-goncalo/Regadios-tradicionais-Quintiaes
### formato BibTeX
```bibtex
@software{Pereira_Sistema_de_Consulta_2025,
author = {Pereira, Gonçalo},
month = aug,
title = {{Sistema de Consulta dos regadios tradicionais de Quintiães}},
url = {https://github.com/pereira-barbosa-goncalo/Regadios-tradicionais-Quintiaes},
version = {1.0.3},
year = {2025}
}
