# 💳 Sistema de Pagamento - FEUDAL BET

## 🎯 Visão Geral

O sistema de pagamento implementado permite aos usuários adicionar dinheiro ao seu saldo no casino através de códigos de resgate (redeem codes). O sistema está disponível em todas as três versões do casino:

1. **HTML/CSS/JavaScript** (`casino_web.html`)
2. **React** (`casino_react.jsx`)
3. **Python Tkinter** (`casino_brasileiro.py`)

## 🔑 Funcionalidades

### ✨ Geração de Códigos
- Gera códigos únicos no formato `CASINO + 8 caracteres`
- Valores aleatórios entre R$ 100,00 e R$ 1.000,00
- Salva automaticamente em arquivo `.txt`
- Interface intuitiva com abas

### 💰 Resgate de Códigos
- Validação de códigos de resgate
- Adição automática ao saldo
- Marcação de códigos como utilizados
- Feedback visual e mensagens de confirmação

## 🚀 Como Usar

### 1. **HTML/CSS/JavaScript**
```bash
# Abra o arquivo no navegador
casino_web.html
```
- Clique no botão **"+ ADICIONAR DINHEIRO"** no painel de saldo
- Use as abas para alternar entre resgatar e gerar códigos
- Os códigos são salvos automaticamente em `codigos_resgate.txt`

### 2. **React**
```bash
# Instale as dependências
npm install

# Execute o projeto
npm start
```
- Clique no botão **"+ ADICIONAR DINHEIRO"** no painel de saldo
- Interface moderna com animações Framer Motion
- Sistema de abas responsivo

### 3. **Python Tkinter**
```bash
# Execute o casino
python casino_brasileiro.py
```
- Clique no botão **"+ ADICIONAR DINHEIRO"** no painel de saldo
- Janela modal com sistema de abas
- Salva códigos em arquivo local

### 4. **Gerador Independente**
```bash
# Execute o gerador de códigos
python gerar_codigos.py
```
- Gera códigos em lote
- Salva em arquivo com cabeçalho formatado
- Interface de linha de comando

## 📁 Estrutura dos Arquivos

### Arquivo de Códigos (`codigos_resgate.txt`)
```
🎰 CÓDIGOS DE RESGATE - FEUDAL BET 🎰
📅 Gerado em: 15/12/2024 14:30:25
💰 Quantidade de códigos: 10
============================================================

CASINO1A2B3C4D - R$ 450.00 - DISPONÍVEL
CASINO5E6F7G8H - R$ 750.00 - DISPONÍVEL
CASINO9I0J1K2L - R$ 320.00 - DISPONÍVEL
...
```

## 🎨 Características do Design

### Interface Moderna
- **Glassmorphism**: Efeitos de vidro translúcido
- **Gradientes**: Cores vibrantes e atrativas
- **Animações**: Transições suaves e responsivas
- **Responsividade**: Adaptável a diferentes tamanhos de tela

### Paleta de Cores
- **Dourado**: `#ffd700` - Elementos principais
- **Verde**: `#10b981` - Botões de ação positiva
- **Roxo**: `#8b5cf6` - Botões de geração
- **Azul escuro**: `#1a1a2e` - Fundo principal

## 🔧 Implementação Técnica

### HTML/CSS/JavaScript
- **Modal**: Overlay com backdrop blur
- **Sistema de Abas**: Alternância dinâmica de conteúdo
- **LocalStorage**: Persistência de códigos gerados
- **Download**: Geração automática de arquivos

### React
- **Componentes**: Estrutura modular e reutilizável
- **Estado**: Gerenciamento com hooks useState
- **Animações**: Framer Motion para transições
- **Props**: Comunicação entre componentes

### Python Tkinter
- **Janelas Modais**: Toplevel com foco
- **Sistema de Abas**: Radio buttons para navegação
- **Arquivos**: I/O para salvar códigos
- **Validação**: Verificação de formato de códigos

## 📱 Responsividade

### Breakpoints
- **Desktop**: > 768px - Layout completo
- **Tablet**: 480px - 768px - Layout adaptado
- **Mobile**: < 480px - Layout otimizado

### Adaptações
- Botões redimensionados
- Texto ajustado
- Espaçamento otimizado
- Navegação touch-friendly

## 🚨 Tratamento de Erros

### Validações
- Códigos vazios
- Formato inválido
- Códigos já utilizados
- Erros de arquivo

### Feedback
- Mensagens de sucesso
- Alertas de erro
- Confirmações visuais
- Logs de operação

## 🔮 Funcionalidades Futuras

### Planejadas
- **Sistema de Usuários**: Contas individuais
- **Histórico**: Log de transações
- **Backup**: Sincronização em nuvem
- **API**: Integração com sistemas externos

### Melhorias
- **Criptografia**: Códigos seguros
- **Validação**: Verificação online
- **Notificações**: Alertas em tempo real
- **Relatórios**: Estatísticas de uso

## 📞 Suporte

### Problemas Comuns
1. **Código não funciona**: Verifique o formato (CASINO + 8 caracteres)
2. **Arquivo não salva**: Verifique permissões de escrita
3. **Interface não carrega**: Verifique dependências e navegador

### Soluções
- Limpe o cache do navegador
- Verifique a versão do Python (3.6+)
- Instale as dependências do React
- Verifique permissões de arquivo

## 📄 Licença

Este projeto é de código aberto e pode ser usado, modificado e distribuído livremente.

---

**🎰 FEUDAL BET - Sistema de Pagamento Completo! 🎰**

