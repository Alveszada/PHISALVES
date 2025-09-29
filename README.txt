# PHISALVES
> Simulações de phishing para auditorias internas — uso ético e autorizado

**Resumão:**  
PHISALVES é um *proof-of-concept* em Python/Flask que demonstra um fluxo simples de simulação de phishing para fins de auditoria e conscientização de segurança. O projeto grava interações em arquivos locais para análise posterior (ex.: taxa de submissão, dados submetidos voluntariamente, acessos), e envia alguns metadados do cliente para coleta analítica.

---

## ⚠️ Aviso importante — uso autorizado apenas
Este repositório contém materiais destinados **apenas** a simulações de phishing em ambientes controlados com autorização explícita e documentada da organização-alvo. Não publique, execute ou utilize este código contra contas ou sistemas sem consentimento formal. Uso não autorizado pode configurar crime e/ou responsabilidade civil.

Ao utilizar este repositório você deve ter:
- Autorização escrita da organização (escopo, período, responsáveis).
- Um responsável técnico e legal pelo teste.
- Plano de comunicação e mitigação (como contatar usuários afetados, rol de respostas).
- Conformidade com leis locais e políticas internas.

---

## O que contém (alto nível)
- `app.py` — aplicação Flask mínima que apresenta um formulário de “atualização de cadastro” e grava entradas em arquivos (`logins.txt`, `info.txt`).
- `templates/index.html` — página HTML utilizada como isca (layout simples).
- Arquivos de log locais usados apenas para demonstração/relatórios.

> Nota: o código fornecido é **educacional** e NÃO contém mecanismos avançados de persistência, anonimização ou proteção de dados. Veja a seção “Boas práticas” abaixo.

---

## Objetivo
- Fornecer um exemplo didático de como um teste de phishing pode ser modelado para fins de auditoria interna.
- Ajudar equipes de segurança a entender o fluxo de coleta de métricas (sem instruções para abuso).
- Servir de base para integração com processos formais de conscientização e geração de relatórios.

---

## Funcionalidades (descrição não-operacional)
- Página de “confirmação/atualização de cadastro” (formulário HTML).
- Registro de acessos (IP, timestamp, id de campanha).
- Coleta de metadados do navegador (userAgent, language, platform) via requisição POST para fins analíticos.
- Arquivos simples de log para posterior análise e elaboração de relatório de conscientização.

---

## Boas práticas e segurança (LEIA ANTES DE TESTAR)
1. **Autorização:** Não execute sem autorização documentada. Tenha escopo por escrito e aceite das áreas jurídicas/recursos humanos.  
2. **Proteção de dados:** Trate qualquer informação pessoal como sensível. Evite armazenar dados em texto puro; se necessário, criptografe e limite retenção.  
3. **Acesso aos logs:** Restrinja acesso aos arquivos de log a pessoas autorizadas. Utilize controles de acesso (chaves, permissões de sistema) e registre quem acessa os logs.  
4. **Anonimização & minimização:** Colete apenas o mínimo necessário para medir o objetivo do teste (ex.: taxa de clique/inscrição) e anonimizar dados quando possível.  
5. **Retenção:** Defina política de retenção (ex.: excluir logs após X dias) e procedimentos seguros de descarte.  
6. **Comunicação pós-teste:** Prepare comunicação para colaboradores impactados: relatório, lições aprendidas e treinamentos.  
7. **Ambiente de teste:** Execute em ambiente isolado (VPC/DMZ) e em servidores controlados pela sua equipe de segurança.  
8. **Conformidade legal:** Consulte jurídico e políticas locais sobre testes de engenharia social.

---

## Como documentar e evidenciar a autorização (modelo sugerido)
> Documento de autorização (exemplo mínimo)  
- Escopo: Domínios/usuários/intervalo de tempo envolvidos  
- Responsáveis: contato técnico e contato legal  
- Objetivo: avaliação de conscientização / auditoria interna  
- Assinaturas: representante da área + jurídico + segurança

(Adicione este documento como anexo ao repositório privado ou mantenha em repositório de políticas interno.)
---
⚠️ Este projeto está sob a licença MIT, porém com a seguinte condição adicional:
**É proibido o uso deste código para atividades não autorizadas, testes sem consentimento ou qualquer fim malicioso.**
