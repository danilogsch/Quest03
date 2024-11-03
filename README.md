# Quest03
Repositório contendo arquivos da terceira questão da Prova Prática do Processo de Seleção para Pesquisador I do SENAI.

# Conteúdo

- Script em Python que utiliza o algoritmo AES em modo ECB (Electronic Codebook) com uma chave de 128 bits para decodificar a mensagem através da biblioteca "pycryptodome".

- Script em Python utilizando o módulo "unittest" para garantir que a decodficação da mensagem funciona corretamente.

# Instalação (Testado no Ubuntu Jammy 22.04 com Python 3.10.12)

```
mkdir danilo
cd danilo
git clone https://github.com/danilogsch/Quest03.git

```

O Ubuntu Jammy já vem instalado com Python 3.10.12. Caso seu sistema operacional não possua o interpretador python, siga as instruções referentes ao seu sistema no [site oficial](https://wiki.python.org/moin/BeginnersGuide/Download).

Instale o gerenciador de pacotes "pip" e as dependências:

```
cd Quest03
sudo apt-get install pip
pip install -r requirements.txt
```