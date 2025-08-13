# 🐍 IMAGEM SNAKE.PNG - FEUDAL BET

## ✅ **IMAGEM ATUALIZADA NO BANNER!**

### **O que foi alterado:**

#### **1. HTML/CSS/JavaScript** ✅
- **Arquivo**: `casino_web.html`
- **Slide 3**: Agora usa `snake.png` em vez de placeholder
- **Alt text**: "Jogo da Cobrinha" para acessibilidade

#### **2. React** ✅
- **Arquivo**: `casino_react.jsx`
- **Array de ads**: Terceiro item atualizado para `snake.png`
- **Consistência**: Mesma imagem em ambas as versões

## 🖼️ **COMO USAR A IMAGEM:**

### **1. Coloque o arquivo:**
- **Nome**: `snake.png`
- **Localização**: Mesma pasta do `casino_web.html`
- **Formato**: PNG (recomendado para transparência)

### **2. Especificações recomendadas:**
- **Dimensões**: 800x200 pixels (mesmo tamanho dos outros slides)
- **Formato**: PNG com fundo transparente ou roxo (#8b5cf6)
- **Tema**: Jogo da cobrinha/snake
- **Cores**: Que combinem com o tema roxo do slide

### **3. Estrutura de arquivos:**
```
jackpot/
├── casino_web.html
├── casino_react.jsx
├── snake.png          ← NOVA IMAGEM AQUI
├── README_COBRINHA.md
└── outros_arquivos...
```

## 🎨 **DESIGN DO SLIDE:**

### **Estrutura atual:**
```html
<div class="carousel-slide">
    <img src="snake.png" alt="Jogo da Cobrinha" class="ad-image">
    <div class="ad-overlay">
        <h3>🎲 NOVO JOGO: COBRINHA!</h3>
        <p>Colete multiplicadores e evite as bombas!</p>
    </div>
</div>
```

### **Estilo CSS aplicado:**
```css
.ad-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 15px;
}

.ad-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.8));
    color: white;
    padding: 20px;
    text-align: center;
}
```

## 🎯 **SUGESTÕES PARA A IMAGEM:**

### **Tema da imagem:**
- **🐍 Cobrinha verde** em fundo escuro
- **💰 Moedas/dinheiro** espalhadas
- **💣 Bombas** para mostrar o risco
- **🎮 Elementos de jogo** (controles, pontuação)

### **Cores recomendadas:**
- **Fundo**: Roxo escuro (#8b5cf6) ou azul (#1a1a2e)
- **Cobrinha**: Verde (#10b981) ou dourado (#ffd700)
- **Moedas**: Dourado (#ffd700) ou prata (#c0c0c0)
- **Bombas**: Vermelho (#ef4444) ou laranja (#f97316)

### **Composição:**
- **Lado esquerdo**: Cobrinha em movimento
- **Centro**: Moedas e multiplicadores
- **Lado direito**: Bombas e perigos
- **Fundo**: Gradiente ou padrão geométrico

## 🔧 **ALTERNATIVAS SE NÃO TIVER A IMAGEM:**

### **1. Placeholder temporário:**
```html
<img src="https://via.placeholder.com/800x200/8b5cf6/1a1a2e?text=JOGO+DA+COBRINHA" alt="Jogo da Cobrinha" class="ad-image">
```

### **2. Emoji grande:**
```html
<div class="snake-emoji">🐍</div>
```

### **3. Texto estilizado:**
```html
<div class="snake-text">SNAKE GAME</div>
```

## 📱 **RESPONSIVIDADE:**

### **Breakpoints:**
- **Desktop**: 800x200 pixels (tamanho completo)
- **Tablet**: 600x150 pixels (escala automática)
- **Mobile**: 400x100 pixels (escala automática)

### **CSS responsivo:**
```css
@media (max-width: 768px) {
    .ad-image {
        height: 150px;
    }
}

@media (max-width: 480px) {
    .ad-image {
        height: 100px;
    }
}
```

## 🎮 **INTEGRAÇÃO COM O JOGO:**

### **Linking:**
- **Clique no banner** pode abrir o jogo da cobrinha
- **Transição suave** entre propaganda e jogo
- **Call-to-action** claro e direto

### **Funcionalidade sugerida:**
```javascript
// Adicionar ao banner do jogo da cobrinha
document.querySelector('.carousel-slide:nth-child(3)').addEventListener('click', () => {
    // Mudar para o jogo da cobrinha
    document.getElementById('gameSelector').value = 'cobrinha';
    changeGame();
});
```

## 🚀 **PRÓXIMOS PASSOS:**

### **1. Criar/obter imagem:**
- **Design próprio** usando ferramentas como Canva, Figma
- **Imagem de stock** de sites gratuitos
- **Screenshot** do jogo em ação

### **2. Otimizar imagem:**
- **Comprimir** para web (menos de 100KB)
- **Formatos alternativos** (WebP, AVIF)
- **Versões responsivas** para diferentes telas

### **3. Testar integração:**
- **Carregamento** da imagem
- **Responsividade** em diferentes dispositivos
- **Performance** e tempo de carregamento

---

**🐍 Banner atualizado com snake.png! Agora é só colocar a imagem na pasta! 🎨**

