# Twiks


>## 📱 O twiks é um aplicativo de análise de dados usando a API do Twitter!

### Aplicação foi desenvolvida para praticar meus conhecimentos usando python, banco de dados e análise de dados.

-A ideia é usar o Tweepy (API do Twitter) como objeto de estudo de ciência de dados e também banco de dados

>## 🛠 Tecnologias

- Python
  - Tweepy
  - Pandas
  - Numpy
  - Matplotlib
  - Programação Orientada a Objetos
- Banco de dados NoSQL
  - Firestore
- Versionamento de códigos
  - Git
  - Github

># ⚙️ Como funciona?
>## 📁 Armazenamento de dados

### Firestore

![image](https://user-images.githubusercontent.com/84272231/205072064-b7ce7b3b-85a3-455b-b0a4-d9f913dfdfe4.png)

O Twiks usa o firestore, um banco de dados NoSQL online para armazenar os dados, onde é dividido em coleções e documentos, como na print abaixo.

![image](https://user-images.githubusercontent.com/84272231/205071712-eb99e546-fc20-4370-be00-781827a804b8.png)

#### Integração no sistema

Foi criada uma classe somente para fazer o CRUD do banco de dados, onde é instanciada em outros lugares

![image](https://user-images.githubusercontent.com/84272231/205072426-ca5aa514-19ac-41f7-aa04-39489006a42b.png)

>## 📜 Algoritmos e Script

### Python

A principal linguagem de programação usada é o Python, por causa da biblioteca tweepy, que deixa de maneira mais rápida as informações que a API provê, apartir das informações que são trazidas em arquivos .JSON, uso bibliotecas de ciência de dados e estatística como o Pandas, Numpy e Matplotlib, tudo usando com base no paradigma de programação orientad a objetos.

#### Integração no Sistema

##### Tweepy
![image](https://user-images.githubusercontent.com/84272231/205073563-bc695377-a2b8-4666-8c88-99ee5c18baea.png)

##### Numpy, Pandas e Matplotlib
![image](https://user-images.githubusercontent.com/84272231/205073694-557cfc37-346f-4786-9b34-548d7b7548ce.png)

>## 📈 Resultados finais

#### Gráficos
##### Hora mais comum de criação de tweet
![image](https://user-images.githubusercontent.com/84272231/205073915-f99df44d-9549-4c7c-aa9e-cc74d18a6ebe.png)

##### Gráfico de Setor por post de usuário curtido
![image](https://user-images.githubusercontent.com/84272231/205074196-ff6b0ed8-9ca5-402b-888d-9773b1f4fa4a.png)

##### Salvamento de dados
###### Salvado apenas meus tweets
![image](https://user-images.githubusercontent.com/84272231/205074305-a8452dec-8b09-4880-9510-ab6e18fb6467.png)


## 🔮 Próximos passos
O aplicativo ainda está sendo desenvolvido, a ideia é colocar mais funções como um bot que responde no twitter assim que chamado, e mais algumas análises de graficos.
