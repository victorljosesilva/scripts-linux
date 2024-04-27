# Automação de Tarefas em Ambiente Linux Ubuntu Server

Este repositório contém uma coleção de scripts Python que automatizam tarefas comuns em um ambiente Linux Ubuntu Server. As tarefas incluem backup, gerenciamento de permissões de arquivos, monitoramento de recursos do sistema e outras relevantes para administração de sistemas.

## Tarefas Automatizadas

1. **Backup de Diretórios Específicos**: Script para realizar backup de diretórios específicos.
2. **Limpeza de Arquivos Temporários**: Script para limpar arquivos temporários de um diretório.
3. **Monitoramento de Recursos do Sistema**: Script para monitorar o uso da CPU, memória e disco.
4. **Verificação de Integridade de Arquivos**: Script para calcular o hash MD5 de um arquivo.
5. **Gerenciamento de Permissões de Arquivos**: Script para alterar as permissões de arquivos em um diretório.
6. **Monitoramento de Logs**: Script para monitorar um arquivo de log em busca de padrões específicos.
7. **Atualização de Pacotes do Sistema**: Script para atualizar os pacotes do sistema.

## Uso

Cada script possui instruções de uso no próprio arquivo. Certifique-se de ter as permissões adequadas para executar os scripts.

Para agendar a execução periódica dos scripts, você pode usar tarefas cron. Exemplos de como agendar as tarefas estão disponíveis na seção "Integração com Cron Jobs" nos comentários dos scripts.

## Requisitos

- Python 3.x
- Bibliotecas Python relevantes (se especificado nos scripts)
- Acesso de superusuário (root) para certas operações, como alteração de permissões de arquivos

