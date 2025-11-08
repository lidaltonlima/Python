# Níveis de Seriedade

| Nível | Constante  | Descrição                                                    |
| ----- | ---------- | ------------------------------------------------------------ |
| 10    | `DEBUG`    | Detalhes de depuração, útil para desenvolvedores.            |
| 20    | `INFO`     | Mensagens informativas sobre o andamento normal do programa. |
| 30    | `WARNING`  | Algo inesperado, mas o programa ainda pode continuar.        |
| 40    | `ERROR`    | Um erro ocorreu e afetou a execução atual.                   |
| 50    | `CRITICAL` | Um erro grave que pode parar o programa.                     |

# Principais Métodos

| Método                          | Descrição                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| `logging.debug(msg)`            | Registra uma mensagem de depuração.                                                    |
| `logging.info(msg)`             | Registra uma mensagem informativa.                                                     |
| `logging.warning(msg)`          | Registra um aviso.                                                                     |
| `logging.error(msg)`            | Registra um erro.                                                                      |
| `logging.critical(msg)`         | Registra uma falha crítica.                                                            |
| `logging.exception(msg)`        | Similar a `error()`, mas inclui o traceback da exceção. (Usado dentro de um `except`.) |
| `logging.basicConfig(**kwargs)` | Configura o formato e o destino do log (arquivo, console, etc.).                       |

# Campos (placeholders) mais comuns

| Código          | Descrição                                               |
| --------------- | ------------------------------------------------------- |
| `%(asctime)s`   | Data e hora em que o log foi gerado.                    |
| `%(levelname)s` | Nível do log (`DEBUG`, `INFO`, `WARNING`, etc.).        |
| `%(message)s`   | A mensagem que você passou (ex: `logging.info("Olá")`). |
| `%(name)s`      | Nome do logger (útil quando se usa vários loggers).     |
| `%(filename)s`  | Nome do arquivo de onde veio o log.                     |
| `%(module)s`    | Nome do módulo (sem extensão).                          |
| `%(funcName)s`  | Nome da função que gerou o log.                         |
| `%(lineno)d`    | Número da linha onde o log foi chamado.                 |
| `%(pathname)s`  | Caminho completo do arquivo fonte.                      |
| `%(thread)d`    | ID da thread.                                           |
| `%(process)d`   | ID do processo.                                         |

# Loggers, Handlers e Formatters

A arquitetura do logging é dividida em 3 componentes principais:

1. Logger – Onde você escreve a mensagem (ex: logging.getLogger('meu_app'))
2. Handler – Define para onde a mensagem vai (arquivo, console, e-mail, etc.)
3. Formatter – Define como a mensagem será exibida (data, nível, texto, etc.)

# Logs rotativos automáticos

Se quiser ter vários arquivos de log (ex: um novo a cada dia, ou quando atinge certo tamanho), use `RotatingFileHandler`:

```Python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=100_000, backupCount=5)
```

Isso cria novos arquivos (`app.log.1`, `app.log.2`, …) automaticamente quando o arquivo atinge 100 KB.

# F-Strings

O logging não recomenda o uso de f-strings então deve ser usado o %.

| Código | Tipo de dado            | Descrição                                                           |
| ------ | ----------------------- | ------------------------------------------------------------------- |
| %s     | String                  | Insere uma string                                                   |
| %d     | Inteiro decimal         | Insere um número inteiro em base decimal                            |
| %i     | Inteiro                 | Similar ao `%d`, insere um número inteiro                           |
| %f     | Ponto flutuante         | Insere um número de ponto flutuante (float)                         |
| %.nf   | Ponto flutuante         | Insere um float com `n` casas decimais (ex: `%.2f` para 2 casas)    |
| %x     | Inteiro hexadecimal     | Insere um número inteiro em formato hexadecimal (letras minúsculas) |
| %X     | Inteiro hexadecimal     | Insere um número inteiro em formato hexadecimal (letras maiúsculas) |
| %o     | Inteiro octal           | Insere um número inteiro em formato octal                           |
| %e     | Notação científica      | Insere um float em notação científica (ex: 1.23e+04)                |
| %g     | Float ou notação cient. | Usa `%f` ou `%e`, dependendo do valor                               |
| %%     | Porcentagem literal     | Insere o caractere `%` literalmente                                 |
