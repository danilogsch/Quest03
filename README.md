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
sudo chmod +x crackme.py 
sudo chmod +x unit_testing.py 
```

O script responsável por realizar a decodificação da mensagem e imprimir a mesma em terminal de execução do software, pode ser rodado com o comando:

```
python3 crackme.py
#Se você tem Python2 instalado, o comando seria:
python crackme.py
```
Você deve ver a menssagem "Sistemas Embarcados" no terminal.

## Descrição dos Testes Unitários

Abaixo estão os cenários de teste desenvolvidos para garantir o correto funcionamento da função de descriptografia AES.

### 1. `test_decrypt_aes_ecb_valid`
   - **Descrição**: Testa a descriptografia com a chave correta e um texto cifrado válido.
   - **Resultado Esperado**: A mensagem descriptografada deve corresponder ao texto esperado ("Sistemas Embarcados").
   - **Objetivo**: Verifica se a função de descriptografia funciona conforme o esperado com entradas válidas.

### 2. `test_decrypt_aes_ecb_with_incorrect_key`
   - **Descrição**: Testa a descriptografia utilizando uma chave incorreta.
   - **Resultado Esperado**: A função deve lançar uma `ValueError`, indicando que a descriptografia falhou devido à chave incorreta.
   - **Objetivo**: Assegura que a função lida com chaves incorretas levantando uma exceção apropriada.

### 3. `test_empty_ciphertext`
   - **Descrição**: Testa a descriptografia com um texto cifrado vazio.
   - **Resultado Esperado**: A função deve retornar uma string vazia sem erros.
   - **Objetivo**: Confirma que a função trata corretamente a entrada de texto cifrado vazio sem lançar exceções.

### 4. `test_invalid_ciphertext_length`
   - **Descrição**: Testa a descriptografia com um texto cifrado cujo comprimento não é múltiplo do tamanho do bloco AES (16 bytes).
   - **Resultado Esperado**: A função deve lançar uma `ValueError` devido ao comprimento inválido do texto cifrado.
   - **Objetivo**: Garante que a função valida o comprimento do texto cifrado e lida com isso corretamente se estiver incorreto.

### 5. `test_key_with_invalid_characters`
   - **Descrição**: Testa a descriptografia com uma chave que inclui caracteres especiais ou bytes inválidos.
   - **Resultado Esperado**: A função deve lançar uma `ValueError` devido à chave incorreta.
   - **Objetivo**: Confirma que a função lida com caracteres inválidos na chave ao levantar uma exceção.

### 6. `test_ciphertext_with_padding`
   - **Descrição**: Testa a descriptografia em um texto cifrado com padding. Aqui, o padding deve resultar em saída que não seja UTF-8, especialmente quando a chave ou texto cifrado estão corrompidos.
   - **Resultado Esperado**: A função deve lançar uma `ValueError` devido aos caracteres não UTF-8 após a descriptografia.
   - **Objetivo**: Verifica o tratamento do padding em textos cifrados e o tratamento adequado de erro para texto corrompido ou descriptografado incorretamente.

### 7. `test_invalid_key_length`
   - **Descrição**: Testa a descriptografia com uma chave de comprimento incorreto (diferente de 16 bytes para AES-128).
   - **Resultado Esperado**: A função deve lançar uma `ValueError` devido ao comprimento inválido da chave.
   - **Objetivo**: Assegura que a função valida o comprimento da chave e levanta uma exceção se a chave não tiver o comprimento necessário.

### 8. `test_invalid_ciphertext_format`
   - **Descrição**: Testa a descriptografia com um texto cifrado que não está no formato hexadecimal.
   - **Resultado Esperado**: A função deve lançar uma `binascii.Error` devido aos dados hexadecimais inválidos.
   - **Objetivo**: Confirma que a função verifica e levanta o erro correto se o texto cifrado estiver em formato inadequado.

## Como Executar os Testes

```
python3 unit_testing.py 
#Similarmente ao scrpt anterior, em Python2 seria:
python unit_testing.py 
```

Deve aparecer no terminal:

```
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

Os 8 pontos da primeira linha significam que os 8 testes passaram.

