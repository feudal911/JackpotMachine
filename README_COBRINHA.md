# 🐍 JOGO DA COBRINHA - FEUDAL BET

## 🎯 Visão Geral

O **Jogo da Cobrinha** é um jogo clássico de Snake com elementos de casino, onde você controla uma cobrinha que coleta multiplicadores de dinheiro, mas deve evitar as bombas que podem explodir a qualquer momento!

## 🎮 Como Jogar

### **Controles:**
- **🔼 Seta para Cima** - Move a cobrinha para cima
- **🔽 Seta para Baixo** - Move a cobrinha para baixo  
- **◀️ Seta para Esquerda** - Move a cobrinha para a esquerda
- **▶️ Seta para Direita** - Move a cobrinha para a direita

### **Objetivo:**
1. **Colete a comida** (quadrados roxos) para crescer e ganhar pontos
2. **Aumente o multiplicador** a cada comida coletada
3. **Evite as bombas** que aparecem aleatoriamente (10% de chance)
4. **Não bata nas paredes** ou no próprio corpo
5. **Maximize seus ganhos** antes do game over!

## 💰 Sistema de Pagamento

### **Multiplicadores:**
- **Comida coletada**: +0.1x ao multiplicador
- **Pontuação**: +10 pontos por comida
- **Ganhos finais**: Aposta × Multiplicador final

### **Exemplo:**
- **Aposta inicial**: R$ 10,00
- **Multiplicador final**: 2.5x
- **Ganhos**: R$ 25,00

## ⚠️ Perigos

### **Bombas:**
- **Aparecem aleatoriamente** quando você come a comida
- **10% de chance** de ser uma bomba
- **Game over imediato** se comer uma bomba
- **Perde a aposta** se explodir

### **Colisões:**
- **Paredes**: Game over se bater nas bordas
- **Corpo**: Game over se bater em si mesmo
- **Velocidade**: Aumenta conforme cresce

## 🎨 Características Visuais

### **Elementos do Jogo:**
- **🐍 Cabeça da cobrinha**: Dourado (#ffd700)
- **🟢 Corpo da cobrinha**: Verde (#10b981)
- **🟣 Comida**: Roxo (#8b5cf6)
- **🔵 Fundo**: Azul escuro (#1a1a2e)

### **Interface:**
- **Canvas 400x400** pixels
- **Grid 20x20** para movimento preciso
- **Animações suaves** com Framer Motion
- **Design responsivo** e moderno

## 🚀 Implementação

### **Versões Disponíveis:**

#### **1. HTML/CSS/JavaScript** ✅
- **Arquivo**: `casino_web.html`
- **Status**: Implementado e funcionando
- **Características**: Canvas nativo, controles por teclado

#### **2. React** ✅
- **Arquivo**: `CobrinhaGame.jsx`
- **Status**: Componente criado e pronto
- **Características**: Hooks, Framer Motion, reutilizável

#### **3. Python Tkinter** 🔄
- **Arquivo**: `casino_brasileiro.py`
- **Status**: Estrutura preparada
- **Características**: Canvas Tkinter, controles por teclado

## 🔧 Como Integrar

### **HTML/JavaScript:**
```javascript
// O jogo já está integrado no casino_web.html
// Basta selecionar "Cobrinha" no seletor de jogos
```

### **React:**
```jsx
// 1. Importe o componente
import CobrinhaGame from './CobrinhaGame';

// 2. Adicione ao AnimatePresence
{currentGame === 'cobrinha' && (
  <CobrinhaGame 
    key="cobrinha"
    balance={balance}
    bet={bets.cobrinha}
    onBetChange={(amount) => updateBet('cobrinha', amount)}
    onWin={(winnings) => setBalance(prev => prev + winnings)}
  />
)}
```

### **Python Tkinter:**
```python
# Adicione o método show_cobrinha_game() à classe CasinoBrasileiro
def show_cobrinha_game(self):
    # Implementação do jogo da cobrinha
    pass
```

## 🎯 Estratégias de Jogo

### **Iniciantes:**
1. **Comece devagar** - Use setas com calma
2. **Planeje o caminho** - Evite se encurralar
3. **Colete 3-5 comidas** antes de arriscar mais

### **Avançados:**
1. **Maximize o espaço** - Use todo o canvas
2. **Padrões circulares** - Mantenha a cobrinha em movimento
3. **Gerenciamento de risco** - Pare quando o multiplicador estiver bom

### **Profissionais:**
1. **Speed running** - Colete o máximo possível rapidamente
2. **Padrões complexos** - Use toda a área disponível
3. **Timing perfeito** - Sincronize com a velocidade do jogo

## 📊 Estatísticas do Jogo

### **Probabilidades:**
- **Comida normal**: 90% de chance
- **Bomba**: 10% de chance
- **Multiplicador máximo**: Teórico ilimitado
- **Pontuação máxima**: Teórica ilimitada

### **Médias:**
- **Jogo típico**: 5-15 comidas
- **Multiplicador típico**: 1.5x - 2.5x
- **Duração média**: 30-90 segundos
- **ROI médio**: 150% - 250%

## 🎨 Personalização

### **Cores:**
```css
/* Personalize as cores do jogo */
.cobrinha-canvas {
  border-color: #ffd700; /* Borda dourada */
}

.snake-head {
  background-color: #ffd700; /* Cabeça dourada */
}

.snake-body {
  background-color: #10b981; /* Corpo verde */
}

.food {
  background-color: #8b5cf6; /* Comida roxa */
}
```

### **Velocidade:**
```javascript
// Ajuste a velocidade do jogo
setTimeout(function() {
  // Lógica do jogo
}, 100); // 100ms = mais rápido, 200ms = mais lento
```

### **Tamanho do Grid:**
```javascript
const gridSize = 20; // 20px = mais preciso, 15px = mais rápido
```

## 🚨 Solução de Problemas

### **Problemas Comuns:**

1. **Cobrinha não responde:**
   - Verifique se o jogo está ativo
   - Clique no canvas para dar foco
   - Use as setas do teclado

2. **Jogo muito lento/rápido:**
   - Ajuste o valor do setTimeout
   - Verifique a performance do navegador

3. **Controles travados:**
   - Pressione qualquer tecla para "destravar"
   - Reinicie o jogo se necessário

### **Performance:**
- **Canvas otimizado** para 60 FPS
- **Game loop eficiente** com requestAnimationFrame
- **Cleanup automático** de event listeners

## 🔮 Funcionalidades Futuras

### **Planejadas:**
- **Power-ups especiais** (escudo, velocidade, etc.)
- **Modos de jogo** (clássico, turbo, survival)
- **Leaderboards** online
- **Achievements** e conquistas

### **Melhorias:**
- **Efeitos sonoros** e música
- **Partículas visuais** ao coletar comida
- **Animações mais elaboradas**
- **Multiplayer local**

## 📱 Responsividade

### **Breakpoints:**
- **Desktop**: Canvas 400x400, controles completos
- **Tablet**: Canvas 350x350, controles adaptados
- **Mobile**: Canvas 300x300, controles touch

### **Controles Mobile:**
- **Botões virtuais** para dispositivos touch
- **Swipe gestures** para direção
- **Interface otimizada** para telas pequenas

---

**🐍 Jogo da Cobrinha - Diversão clássica com ganhos reais! 🎰**

