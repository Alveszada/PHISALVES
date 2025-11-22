# PHISHING
> Simulações de phishing para auditorias internas — uso ético e autorizado

**Resumão:**  
PHISALVES é um *proof-of-concept* em Python/Flask que demonstra um fluxo simples de simulação de phishing para fins de auditoria e conscientização de segurança. O projeto grava interações em arquivos locais para análise posterior (ex.: taxa de submissão, dados submetidos voluntariamente, acessos), e envia alguns metadados do cliente para coleta analítica.

## ⚠️ Aviso importante — uso autorizado apenas
Este repositório contém materiais destinados **apenas** a simulações de phishing em ambientes controlados com autorização explícita e documentada da organização-alvo. Não publique, execute ou utilize este código contra contas ou sistemas sem consentimento formal. Uso não autorizado pode configurar crime e/ou responsabilidade civil.

## O que contém (alto nível)
- `app.py` — aplicação Flask mínima que apresenta um formulário de “atualização de cadastro” e grava entradas em arquivos (`logins.txt`, `info.txt`).
- `templates/index.html` — página HTML utilizada como isca (layout simples).
- Arquivos de log locais usados apenas para demonstração/relatórios.

**É proibido o uso deste código para atividades não autorizadas, testes sem consentimento ou qualquer fim malicioso.**
