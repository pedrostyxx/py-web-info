# Aplicação Web de Informações Técnicas

![enter image description here](https://cdn.dribbble.com/users/241205/screenshots/3906737/media/69a961e84975a67590b706bd6cb62e45.jpg)

Uma aplicação web simples construída com Flask que fornece informações técnicas sobre o dispositivo do usuário, como User-Agent, endereço IP e resolução da tela.

## Instalação

Siga estas etapas para configurar o ambiente de desenvolvimento:

1. Clone o repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`.

## Exemplo de Uso

Você pode acessar a página inicial em um navegador da web e obter informações técnicas sobre o seu dispositivo, incluindo User-Agent, endereço IP e idioma do navegador.

Para acessar as informações diretamente por meio de uma solicitação HTTP, você pode usar `curl`:

```bash
curl http://localhost:5000/info
```

Isso retornará um JSON com as informações técnicas.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de pull para melhorias ou correções.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
