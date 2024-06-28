
# API Rede Feminina

  

Esta API foi desenvolvida para apoiar o combate ao câncer de mama, oferecendo funcionalidades essenciais para gerenciamento de dados e autenticação de usuários. A aplicação foi construída utilizando Flask em Python 3.12 e emprega Firebase para autenticação. A arquitetura de software segue o padrão modular baseado no Clean Architecture, dividida em core e módulos.


## Versões Necessárias

  

 [![Python][python_img]][python_ln] 
Versão: 3.12.0

## Sumário

- [Funcionalidades](#funcionalidades) 
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Nomenclatura](#nomenclatura)
- [Padrão para classes de interface](#padrão-para-classes-de-interface)
- [Padrão para classes de implementação de interface](#padrão-para-classes-de-implementação-de-interface)
- [Padrão para classes de entidade em Python](#padrão-para-classes-de-entidade-em-python)
- [Princípio da inversão de dependências (DIP)](#princípio-da-inversão-de-dependências-dip) 
- [Uso de Adapters](#uso-de-adapters) 
- [Convenção de Commits](#convenção-de-commits) 
- [Convenção de nomenclatura para branches](#convenção-de-nomenclatura-para-branches) 
- [Licença](#licença)


### Funcionalidades

- **Auto cadastro do paciente**: O paciente consegue realizar seu próprio cadastro no sistema, para acessa-lo.

- **Agendar consultas**: O paciente consegue agendar consultas através de um calendário intuitivo, que mostra quais os dias e horários disponíveis.



### Como Executar o Projeto

-   Verifique se sua versão do Python é >= 3.12.0.

- Clone o repositório:
`git clone https://github.com/zanelladev/rede_feminina_api.git` 

-   Instale as dependências do arquivo requirements.txt.
    
-   Configure as variáveis de ambiente necessárias.
    
-   Utilize o runner do VSCode para execução.
    
### Nomenclatura

-   **Diretórios e Arquivos**:
    
    -   **Snake Case**:
        -   Use o estilo snake_case para nomes de arquivos.
        -   Todas as letras devem ser minúsculas.
        -   Palavras separadas por sublinhado.
-   **Classes**: PascalCase

-   **Variáveis**, **Funções** e **Métodos**: camelCase

-   **Interfaces**: Começam com um `I`, por exemplo: `IAuthRepository`

-   **Implementação**: Nome da interface sem `I`, por exemplo: `AuthRepository`
    

### Descrição Concisa

-   Mantenha o nome do arquivo descritivo e conciso, refletindo seu conteúdo ou funcionalidade.


### Padrão para classes de interface
  
**Boa prática:**
```py
class IAuthRepository(ABC):
	# implementação da classe
```

**Má prática:**
```py
class AuthRepositoryInterface(ABC):
    # implementação da classe
```

### Padrão para classes de implementação de interface
  
**Boa prática:**
```py
class AuthRepository(IAuthRepository): 
	# implementação da classe
```

**Má prática:**
```py
class AuthRepositoryImplements(IAuthRepository):
    # implementação da classe
```

### Padrão para classes de entidade em Python

**Boa prática:**
```py
class UserEntity:
    # Definição da entidade User`
```

**Má prática:**
```py
class User:
    # Definição da entidade User`
```

### Princípio da inversão de dependências (DIP)

  

É um dos cinco princípios SOLID da programação orientada a objetos. Ele estabelece que:

- Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

- Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

  

*Em termos mais simples, o DIP sugere que os módulos de alto nível devem depender de abstrações, não de implementações concretas. Isso permite que você escreva código que seja mais flexível e fácil de manter, pois os módulos de alto nível não estão vinculados a detalhes de implementação específicos dos módulos de baixo nível*.

  

 **Para aplicar o DIP em um projeto, você precisa seguir algumas práticas**:

- **Definir abstrações claras**: Identifique as interfaces ou classes abstratas que descrevem os comportamentos que os módulos de alto nível precisam. Essas abstrações devem ser independentes de qualquer implementação concreta.

- **Injetar dependências**: Em vez de instanciar objetos diretamente dentro de outros objetos, injete as dependências por meio de construtores, métodos ou propriedades. Isso permite que as implementações concretas sejam substituídas por outras implementações compatíveis sem alterar o código dos módulos de alto nível.

- **Seguir o Princípio da Inversão de Controle (IoC)**: No DIP, o controle é invertido para que as implementações concretas dependam das abstrações. Isso é frequentemente alcançado por meio de um contêiner de injeção de dependência que gerencia a criação e resolução de dependências.

- **Testar unidades isoladas**: Ao usar abstrações e injetar dependências, você pode escrever testes de unidade mais facilmente, substituindo as implementações reais por mocks ou stubs durante os testes.

  

*Ao seguir essas práticas, você pode criar um código mais flexível, modular e fácil de manter, alinhado com os princípios do DIP*.

  

```py
class AuthRepository(IAuthRepository):
    def __init__(self, firebaseAuthy):
        self.auth = firebaseAuth
```

### Uso de Adapters

Os adapters são responsáveis por receber um Map e retornar uma Entity, ou, o inverso. Além disso, também existem adapters que recebem uma Entity e retornam outra Entity.



### Convenção de Commits

Para os commits, será utilizado o padrão do [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0), seguindo as seguintes convenções:

-   `feat`: para novas funcionalidades.
-   `fix`: para correções de bugs.
-   `test`: para adição ou modificação de testes.
-   `refactor`: para refatorações de código que não corrigem bugs nem adicionam novas funcionalidades.
-   `chore`: para tarefas de manutenção, como ajustes na estrutura de arquivos, configurações etc.
-   `docs`: para alterações na documentação.
-   `perf`: para melhorias de performance.
-   `style`: para alterações que não afetam o significado do código (espaços em branco, formatação, ponto e vírgula ausente etc.).
-   `build`: para alterações que afetam o sistema de build ou dependências externas.
-   `revert`: para reversões a um commit anterior.

### Convenção de nomenclatura para branches

Utilize o mesmo padrão de nomenclatura do Conventional Commits:
- `feat/new-feature-name`


### Licença

This project is distributed under the BSD 3-Clause license. See the [LICENSE](https://github.com/zanelladev/rede_feminina_api/blob/main/LICENSE) file for details.

<!-- Links úteis: -->



[python_img]: https://img.shields.io/badge/python-3120A0?style=for-the-badge&logo=python&logoColor=ffdd54&message=3.4.0

[python_ln]: https://www.python.org/downloads/release/python-3120/ "https://www.python.org/downloads/release/python-3120/"