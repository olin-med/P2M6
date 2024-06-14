# P2M6

## Descrição
O código desse repositório é capaz de identificar rostos em um vídeo utilizando o método Haar Cascade.

## Instruções de Execução
Pré requisitos:
Python3

Para executar clone o repositório:
```bash
git clone https://github.com/olin-med/P2M6.git
```
Em seguida entre no diretório do projeto e instale as dependências necessárias:
```bash
cd P2M6
pip install -r requirements.txt
```
Por fim rode o seguinte comando:
```bash
python/python3 main.py
```
## Perguntas Técnicas

### 2.1
O Haar Cascade é um método de detecção de objetos que utiliza representações de imagens chamadas imagens integrais, características Haar-Like que consistem de retângulos capazes de determinar diferenças de intensidade entre regiões vizinhas da imagem. Além desses dois elementos, é realizada uma cascata(cascade) de algorítiomos classificadores (Adaboost) para identificar e eslecionar características mais interessantes.

### 2.2
Viabilidade Técnica:
CNN/ 
Filtros de correlação cruzada/ 
HAAR Cascade/ 
NN Linear

A CNN juntamente com os filtros de correlação cruzada apresentam os melhores resultados em termos de detecção de faces. Métodos como Neural Networks e Haar Cascade são mais limitados, muitas vezes deixando de detectar rostos penas por estarem de perfil.

Facilidade de Implementação:
HAAR Cascade/ 
NN Linear/ 
CNN/ 
Filtros de correlação cruzada

O Haar Cascade e a NN são as duas soluções de mais fácil implementação, ao passo que as CNNs e os Filtros possuem uma complexidade matemática muito maior resultado em uma maior dificuldadde na implementação.

Versatilidade da Solução:
CNN/ 
Filtros de correlação cruzada/ 
NN Linear/ 
HAAR Cascade/ 

Flitros de correlação e CNNs, por possuirem mais graus de liberdade podem ser aplicadas a uma gama maior de problemas do que o Haar Cascade, e as NN muitas vezes não conseguem lidar adequadamente com problemas a partir de certo nível de complexidade.

### 2.3
Filtros de correlação cruzada/ 
CNN/ 
HAAR Cascade/ 
NN Linear

Seria muit difícil cumprir essa tarefa com uma NN linear. Para o Haar Cascade teria de ser gerado um novo classificador. Já ocorreru uma [tentativa](https://towardsdatascience.com/whats-the-difference-between-haar-feature-classifiers-and-convolutional-neural-networks-ce6828343aeb) documentada de classificar emoções tanto com o Haar Cascade quanto com o CNN e os resultados da CNN foram superiores. Por fim, filtros de correlação provavelmente seriam a abordagem mais adequada ao problema, uma vez que utilizam o cruzamento de filtros convoluvionais para determinar o que é igual e o que é diferente. 

### 2.4
As CNNs são capazes de levar em consideração estados anteriores na classificação devido ao backpropagation. Por esse motivo, as emoções detectadas nos frames anteriores seriam levadas em conta na classificação de novas emoções.

### 2.5
German Cano
