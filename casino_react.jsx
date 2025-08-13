import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FaCoins, FaGamepad, FaSyncAlt, FaPlay, FaRocket, FaDice, FaFish, FaCircleNotch, FaPlus, FaCreditCard, FaCheck, FaMagic, FaTimes } from 'react-icons/fa';
import './casino_react.css';

// Componente principal do Casino
const CasinoBrasileiro = () => {
  const [balance, setBalance] = useState(1000);
  const [currentGame, setCurrentGame] = useState('slot');
  const [bets, setBets] = useState({
    slot: 10,
    rocket: 10,
    roulette: 10,
    dice: 10,
    fishing: 10,
    plinko: 10,
    tigrinho: 10
  });
  const [showPaymentModal, setShowPaymentModal] = useState(false);
  const [redeemCodes, setRedeemCodes] = useState([]);
  const [activeTab, setActiveTab] = useState('redeem');

  const updateBet = (game, amount) => {
    const newBet = bets[game] + amount;
    if (newBet >= 1 && newBet <= 10000 && newBet <= balance) {
      setBets(prev => ({ ...prev, [game]: newBet }));
    }
  };

  const reloadBalance = () => {
    setBalance(1000);
    alert('Saldo recarregado para R$ 1.000,00!');
  };

  const generateRedeemCode = () => {
    const code = 'CASINO' + Math.random().toString(36).substr(2, 8).toUpperCase();
    const amount = Math.floor(Math.random() * 900) + 100; // R$ 100 to R$ 1000
    
    const newCode = { code, amount, used: false };
    setRedeemCodes(prev => [...prev, newCode]);
    
    // Save to file (simulated)
    saveRedeemCodesToFile([...redeemCodes, newCode]);
    
    return { code, amount };
  };

  const saveRedeemCodesToFile = (codes) => {
    // In a real application, this would save to a server
    // For now, we'll simulate it by creating a downloadable file
    const content = codes.map(c => `${c.code} - R$ ${c.amount.toFixed(2)} - ${c.used ? 'USADO' : 'DISPONÍVEL'}`).join('\n');
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'codigos_resgate.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  const redeemCode = (code) => {
    const codeData = redeemCodes.find(c => c.code === code && !c.used);
    
    if (codeData) {
      // Mark as used
      setRedeemCodes(prev => prev.map(c => 
        c.code === code ? { ...c, used: true } : c
      ));
      
      // Add money to balance
      setBalance(prev => prev + codeData.amount);
      
      // Save updated codes to file
      const updatedCodes = redeemCodes.map(c => 
        c.code === code ? { ...c, used: true } : c
      );
      saveRedeemCodesToFile(updatedCodes);
      
      alert(`🎉 Código resgatado com sucesso! Adicionado R$ ${codeData.amount.toFixed(2).replace('.', ',')} ao seu saldo!`);
      return true;
    }
    return false;
  };

  return (
    <div className="casino-container">
      {/* Header com animação */}
      <motion.div 
        className="casino-header"
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        <h1 className="casino-title">
          <span className="title-icon">🎰</span>
                      FEUDAL BET - CASINO PREMIUM
          <span className="title-icon">🎰</span>
        </h1>
        <p className="casino-subtitle">
          Os melhores jogos das plataformas brasileiras com design ultra-moderno!
        </p>
        
        {/* Carrossel de Propagandas */}
        <AdCarousel />
      </motion.div>

      {/* Barra de informações */}
      <motion.div 
        className="info-bar"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.2, ease: "easeOut" }}
      >
        <div className="info-item">
          <h3><FaCoins /> SALDO</h3>
          <div className="balance-amount">R$ {balance.toFixed(2).replace('.', ',')}</div>
          <motion.button 
            className="add-money-btn"
            onClick={() => setShowPaymentModal(true)}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <FaPlus /> ADICIONAR DINHEIRO
          </motion.button>
        </div>
        
        <div className="info-item">
          <h3><FaGamepad /> JOGO ATUAL</h3>
          <select 
            value={currentGame} 
            onChange={(e) => setCurrentGame(e.target.value)}
            className="game-selector"
          >
            <option value="slot">Caça-Níquel</option>
            <option value="rocket">Rocket</option>
            <option value="roulette">Roleta</option>
            <option value="dice">Dados</option>
            <option value="fishing">Pesca</option>
            <option value="plinko">Plinko</option>
            <option value="tigrinho">Tigrinho</option>
            <option value="cobrinha">Cobrinha</option>
          </select>
        </div>
        
        <div className="info-item">
          <button onClick={reloadBalance} className="reload-button">
            <FaSyncAlt /> RECARREGAR
          </button>
        </div>
      </motion.div>

      {/* Área do jogo */}
      <motion.div 
        className="game-area"
        key={currentGame}
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
      >
        <AnimatePresence mode="wait">
          {currentGame === 'slot' && (
            <SlotMachine 
              key="slot"
              balance={balance}
              bet={bets.slot}
              onBetChange={(amount) => updateBet('slot', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'rocket' && (
            <RocketGame 
              key="rocket"
              balance={balance}
              bet={bets.rocket}
              onBetChange={(amount) => updateBet('rocket', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'roulette' && (
            <RouletteGame 
              key="roulette"
              balance={balance}
              bet={bets.roulette}
              onBetChange={(amount) => updateBet('roulette', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'dice' && (
            <DiceGame 
              key="dice"
              balance={balance}
              bet={bets.dice}
              onBetChange={(amount) => updateBet('dice', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'fishing' && (
            <FishingGame 
              key="fishing"
              balance={balance}
              bet={bets.fishing}
              onBetChange={(amount) => updateBet('fishing', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'plinko' && (
            <PlinkoGame 
              key="plinko"
              balance={balance}
              bet={bets.plinko}
              onBetChange={(amount) => updateBet('plinko', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
          
          {currentGame === 'tigrinho' && (
            <TigrinhoGame 
              key="tigrinho"
              balance={balance}
              bet={bets.tigrinho}
              onBetChange={(amount) => updateBet('tigrinho', amount)}
              onWin={(winnings) => setBalance(prev => prev + winnings)}
            />
          )}
        </AnimatePresence>
      </motion.div>

      {/* Payment Modal */}
      <PaymentModal
        isOpen={showPaymentModal}
        onClose={() => setShowPaymentModal(false)}
        activeTab={activeTab}
        onTabChange={setActiveTab}
        onGenerateCode={generateRedeemCode}
        onRedeemCode={redeemCode}
        redeemCodes={redeemCodes}
      />
    </div>
  );
};

// Componente do Caça-Níquel
const SlotMachine = ({ balance, bet, onBetChange, onWin }) => {
  const [reels, setReels] = useState(['🎰', '🎰', '🎰']);
  const [isSpinning, setIsSpinning] = useState(false);
  const [result, setResult] = useState('Aguardando giro...');

  const spin = () => {
    if (isSpinning || bet > balance) return;
    
    setIsSpinning(true);
    setResult('Girando...');
    
    // Animação dos rolos
    let spins = 0;
    const spinInterval = setInterval(() => {
      const symbols = ['🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '🎰', '⭐'];
      setReels([
        symbols[Math.floor(Math.random() * symbols.length)],
        symbols[Math.floor(Math.random() * symbols.length)],
        symbols[Math.floor(Math.random() * symbols.length)]
      ]);
      
      spins++;
      if (spins >= 10) {
        clearInterval(spinInterval);
        finishSpin();
      }
    }, 100);
  };

  const finishSpin = () => {
    const symbols = ['🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '🎰', '⭐'];
    const finalReels = [
      symbols[Math.floor(Math.random() * symbols.length)],
      symbols[Math.floor(Math.random() * symbols.length)],
      symbols[Math.floor(Math.random() * symbols.length)]
    ];
    
    setReels(finalReels);
    
    // Verifica vitória
    const winnings = checkWin(finalReels);
    if (winnings > 0) {
      onWin(winnings);
      setResult(`🎉 PARABÉNS! Você ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
    } else {
      setResult('😔 Que pena! Tente novamente!');
    }
    
    setIsSpinning(false);
  };

  const checkWin = (reels) => {
    if (reels[0] === reels[1] && reels[1] === reels[2]) {
      const symbol = reels[0];
      if (symbol === '💎') return bet * 10;
      if (['🎰', '7️⃣', '⭐'].includes(symbol)) return bet * 5;
      return bet * 3;
    } else if (reels[0] === reels[1] || reels[1] === reels[2] || reels[0] === reels[2]) {
      return bet * 1.5;
    }
    return 0;
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🎰 CAÇA-NÍQUEL TRADICIONAL</h2>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <div className="slot-machine">
        <div className="reels">
          {reels.map((symbol, index) => (
            <motion.div
              key={index}
              className="reel"
              animate={{ 
                rotateY: isSpinning ? 360 : 0,
                scale: isSpinning ? 1.1 : 1
              }}
              transition={{ duration: 0.1, repeat: isSpinning ? Infinity : 0 }}
            >
              {symbol}
            </motion.div>
          ))}
        </div>
        
        <motion.button
          className="spin-button"
          onClick={spin}
          disabled={isSpinning}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <FaPlay /> {isSpinning ? 'GIRANDO...' : 'GIRAR!'}
        </motion.button>
      </div>
      
      <div className={`result ${result.includes('PARABÉNS') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente do Rocket
const RocketGame = ({ balance, bet, onBetChange, onWin }) => {
  const [multiplier, setMultiplier] = useState(1.0);
  const [isRunning, setIsRunning] = useState(false);
  const [result, setResult] = useState('Clique em APOSTAR para iniciar!');

  const startRocket = () => {
    if (bet > balance || isRunning) return;
    
    setIsRunning(true);
    setMultiplier(1.0);
    setResult('Crescendo...');
    
    const rocketInterval = setInterval(() => {
      if (Math.random() < 0.1) {
        clearInterval(rocketInterval);
        explode();
        return;
      }
      
      setMultiplier(prev => {
        const newMultiplier = prev + 0.1;
        if (newMultiplier >= 10.0) {
          clearInterval(rocketInterval);
          win(newMultiplier);
          return newMultiplier;
        }
        return newMultiplier;
      });
    }, 100);
  };

  const explode = () => {
    setResult('💥 BOOM! Foguete explodiu! Perdeu a aposta!');
    setIsRunning(false);
  };

  const win = (finalMultiplier) => {
    const winnings = bet * finalMultiplier;
    onWin(winnings);
    setResult(`🎉 PARABÉNS! Foguete chegou a ${finalMultiplier.toFixed(1)}x! Ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
    setIsRunning(false);
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🚀 ROCKET - JOGO DE MULTIPLICADOR</h2>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <div className="rocket-area">
        <motion.div
          className="rocket"
          animate={{ 
            y: isRunning ? [-10, 10, -10] : 0,
            rotate: isRunning ? [0, 5, -5, 0] : 0
          }}
          transition={{ duration: 2, repeat: isRunning ? Infinity : 0 }}
        >
          🚀
        </motion.div>
        
        <div className="multiplier">
          Multiplicador: {multiplier.toFixed(2)}x
        </div>
        
        <motion.button
          className="spin-button"
          onClick={startRocket}
          disabled={isRunning}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          <FaRocket /> {isRunning ? 'CRESCENDO...' : 'APOSTAR!'}
        </motion.button>
      </div>
      
      <div className={`result ${result.includes('PARABÉNS') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente da Roleta
const RouletteGame = ({ balance, bet, onBetChange, onWin }) => {
  const [result, setResult] = useState('Clique em GIRAR para jogar!');

  const spinRoulette = () => {
    if (bet > balance) return;
    
    const result = Math.floor(Math.random() * 37);
    let winnings = 0;
    
    if (result === 0) {
      winnings = bet * 35;
    } else if (result % 2 === 0) {
      winnings = bet * 2;
    } else {
      winnings = bet * 2;
    }
    
    onWin(winnings);
    setResult(`🎲 Resultado: ${result}! Ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🎲 ROLETA EUROPEIA</h2>
      
      <div className="roulette-grid">
        {Array.from({ length: 37 }, (_, i) => (
          <motion.button
            key={i}
            className={`roulette-number ${i === 0 ? 'zero' : i % 2 === 0 ? 'even' : 'odd'}`}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
          >
            {i}
          </motion.button>
        ))}
      </div>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <motion.button
        className="spin-button"
        onClick={spinRoulette}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        <FaCircleNotch /> GIRAR ROLETA!
      </motion.button>
      
      <div className={`result ${result.includes('Ganhou') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente dos Dados
const DiceGame = ({ balance, bet, onBetChange, onWin }) => {
  const [dice, setDice] = useState([1, 1]);
  const [result, setResult] = useState('Clique em ROLAR para jogar!');

  const rollDice = () => {
    if (bet > balance) return;
    
    const dice1 = Math.floor(Math.random() * 6) + 1;
    const dice2 = Math.floor(Math.random() * 6) + 1;
    const total = dice1 + dice2;
    
    setDice([dice1, dice2]);
    
    let winnings = 0;
    if (total === 7 || total === 11) {
      winnings = bet * 2;
      onWin(winnings);
      setResult(`🎉 PARABÉNS! Soma ${total}! Ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
    } else {
      setResult(`😔 Soma ${total}. Tente novamente!`);
    }
  };

  const diceSymbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'];

  return (
    <div className="game-content">
      <h2 className="game-title">🎲 JOGO DE DADOS</h2>
      
      <div className="dice-area">
        <div className="dice">
          {dice.map((value, index) => (
            <motion.div
              key={index}
              className="die"
              animate={{ rotate: [0, 360] }}
              transition={{ duration: 0.5 }}
            >
              {diceSymbols[value - 1]}
            </motion.div>
          ))}
        </div>
        <div className="dice-sum">Soma: {dice[0] + dice[1]}</div>
      </div>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <motion.button
        className="spin-button"
        onClick={rollDice}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        <FaDice /> ROLAR DADOS!
      </motion.button>
      
      <div className={`result ${result.includes('PARABÉNS') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente da Pesca
const FishingGame = ({ balance, bet, onBetChange, onWin }) => {
  const [fishCaught, setFishCaught] = useState(new Set());
  const [result, setResult] = useState('Clique nos peixes para pescar!');

  const fishTypes = ['🐟', '🐠', '🦈', '🐡', '🦑', '🦐', '🦞', '🦀'];
  const fishValues = {
    '🐟': 1.5, '🐠': 2.0, '🦈': 3.0, '🐡': 2.5,
    '🦑': 1.8, '🦐': 1.2, '🦞': 4.0, '🦀': 1.0
  };

  const catchFish = (fish, index) => {
    if (bet > balance || fishCaught.has(index)) return;
    
    const multiplier = fishValues[fish];
    const winnings = bet * multiplier;
    
    onWin(winnings);
    setFishCaught(prev => new Set([...prev, index]));
    setResult(`🎣 Pescou ${fish}! Multiplicador ${multiplier}x! Ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🎣 JOGO DE PESCA</h2>
      
      <div className="fishing-area">
        <div className="fish-container">
          {fishTypes.map((fish, index) => (
            <motion.button
              key={index}
              className={`fish ${fishCaught.has(index) ? 'caught' : ''}`}
              onClick={() => catchFish(fish, index)}
              disabled={fishCaught.has(index)}
              whileHover={{ scale: 1.1, y: -5 }}
              whileTap={{ scale: 0.9 }}
            >
              {fishCaught.has(index) ? '🌊' : fish}
            </motion.button>
          ))}
        </div>
      </div>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <div className={`result ${result.includes('Ganhou') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente do Plinko
const PlinkoGame = ({ balance, bet, onBetChange, onWin }) => {
  const [isDropping, setIsDropping] = useState(false);
  const [result, setResult] = useState('Clique em SOLTAR BOLA para jogar!');

  const multipliers = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 0.5, 0.2];
  const weights = [0.3, 0.25, 0.2, 0.15, 0.05, 0.02, 0.25, 0.3];

  const dropBall = () => {
    if (bet > balance || isDropping) return;
    
    setIsDropping(true);
    setResult('Bola caindo...');
    
    // Simulate ball drop
    setTimeout(() => {
      const random = Math.random();
      let cumulativeWeight = 0;
      let selectedMultiplier = 0.2;
      
      for (let i = 0; i < weights.length; i++) {
        cumulativeWeight += weights[i];
        if (random <= cumulativeWeight) {
          selectedMultiplier = multipliers[i];
          break;
        }
      }
      
      const winnings = bet * selectedMultiplier;
      onWin(winnings);
      
      if (winnings > 0) {
        setResult(`🎉 PARABÉNS! Bola caiu no ${selectedMultiplier}x! Ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
      } else {
        setResult(`😔 Bola caiu no ${selectedMultiplier}x. Tente novamente!`);
      }
      
      setIsDropping(false);
    }, 2000);
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🔴 PLINKO - JOGO DE QUEDAS</h2>
      
      <div className="plinko-area">
        <div className="plinko-board">
          <div className="plinko-drop-zone">
            <motion.div 
              className="plinko-ball"
              animate={isDropping ? { y: 300 } : { y: 0 }}
              transition={{ duration: isDropping ? 2 : 0.5 }}
            >
              🔴
            </motion.div>
          </div>
          <div className="plinko-pins"></div>
          <div className="plinko-buckets">
            {multipliers.map((mult, index) => (
              <div key={index} className="bucket" data-multiplier={mult}>
                {mult}x
              </div>
            ))}
          </div>
        </div>
      </div>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <motion.button
        className="spin-button"
        onClick={dropBall}
        disabled={isDropping}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        {isDropping ? '🔴 CAINDO...' : '🔴 SOLTAR BOLA!'}
      </motion.button>
      
      <div className={`result ${result.includes('Ganhou') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Componente do Tigrinho
const TigrinhoGame = ({ balance, bet, onBetChange, onWin }) => {
  const [reels, setReels] = useState(['🐯', '🐯', '🐯']);
  const [isSpinning, setIsSpinning] = useState(false);
  const [result, setResult] = useState('Clique em GIRAR para jogar!');
  const [specialSymbol, setSpecialSymbol] = useState('🎰');

  const symbols = ['🐯', '🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '⭐', '🎰'];

  const spinReels = () => {
    if (bet > balance || isSpinning) return;
    
    setIsSpinning(true);
    setResult('Girando...');
    
    // Animate reels
    let spins = 0;
    const spinInterval = setInterval(() => {
      setReels([
        symbols[Math.floor(Math.random() * symbols.length)],
        symbols[Math.floor(Math.random() * symbols.length)],
        symbols[Math.floor(Math.random() * symbols.length)]
      ]);
      
      spins++;
      if (spins >= 12) {
        clearInterval(spinInterval);
        finishSpin();
      }
    }, 100);
  };

  const finishSpin = () => {
    const finalReels = [
      symbols[Math.floor(Math.random() * symbols.length)],
      symbols[Math.floor(Math.random() * symbols.length)],
      symbols[Math.floor(Math.random() * symbols.length)]
    ];
    
    setReels(finalReels);
    
    // Check for special symbol
    const hasSpecial = Math.random() < 0.1;
    if (hasSpecial) {
      setSpecialSymbol('🎰');
    }
    
    // Check win
    const winnings = checkWin(finalReels, hasSpecial);
    if (winnings > 0) {
      onWin(winnings);
      setResult(`🎉 PARABÉNS! Você ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
    } else {
      setResult('😔 Que pena! Tente novamente!');
    }
    
    setIsSpinning(false);
  };

  const checkWin = (reels, specialSymbol) => {
    // Check for three tigers (highest payout)
    if (reels[0] === '🐯' && reels[1] === '🐯' && reels[2] === '🐯') {
      return bet * 20;
    }
    
    // Check for three diamonds
    if (reels[0] === '💎' && reels[1] === '💎' && reels[2] === '💎') {
      return bet * 15;
    }
    
    // Check for three sevens
    if (reels[0] === '7️⃣' && reels[1] === '7️⃣' && reels[2] === '7️⃣') {
      return bet * 10;
    }
    
    // Check for three of any kind
    if (reels[0] === reels[1] && reels[1] === reels[2]) {
      return bet * 5;
    }
    
    // Check for two tigers
    if ((reels[0] === '🐯' && reels[1] === '🐯') || 
        (reels[1] === '🐯' && reels[2] === '🐯') || 
        (reels[0] === '🐯' && reels[2] === '🐯')) {
      return bet * 3;
    }
    
    // Check for two of any kind
    if (reels[0] === reels[1] || reels[1] === reels[2] || reels[0] === reels[2]) {
      return bet * 1.5;
    }
    
    // Special symbol bonus
    if (specialSymbol) {
      return bet * 2;
    }
    
    return 0;
  };

  return (
    <div className="game-content">
      <h2 className="game-title">🐯 TIGRINHO - SLOT BRASILEIRO</h2>
      
      <div className="tigrinho-area">
        <div className="tigrinho-reels">
          {reels.map((symbol, index) => (
            <motion.div
              key={index}
              className="tigrinho-reel"
              animate={isSpinning ? { rotateY: 360 } : {}}
              transition={{ duration: 0.1, repeat: isSpinning ? Infinity : 0 }}
            >
              {symbol}
            </motion.div>
          ))}
        </div>
        
        <div className="tigrinho-special">
          <div className="special-symbol">{specialSymbol}</div>
          <div className="special-text">Símbolo Especial</div>
        </div>
      </div>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <motion.button
        className="spin-button"
        onClick={spinReels}
        disabled={isSpinning}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        {isSpinning ? '🐯 GIRANDO...' : '🐯 GIRAR TIGRINHO!'}
      </motion.button>
      
      <div className={`result ${result.includes('Ganhou') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
  );
};

// Payment Modal Component
const PaymentModal = ({ isOpen, onClose, activeTab, onTabChange, onGenerateCode, onRedeemCode, redeemCodes }) => {
  const [redeemCodeInput, setRedeemCodeInput] = useState('');
  const [generatedCode, setGeneratedCode] = useState(null);

  const handleGenerateCode = () => {
    const result = onGenerateCode();
    setGeneratedCode(result);
  };

  const handleRedeemCode = () => {
    if (onRedeemCode(redeemCodeInput)) {
      setRedeemCodeInput('');
      onClose();
    }
  };

  if (!isOpen) return null;

  return (
    <motion.div
      className="payment-modal"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <motion.div
        className="payment-content"
        initial={{ scale: 0.9, y: 20 }}
        animate={{ scale: 1, y: 0 }}
        transition={{ type: "spring", damping: 25, stiffness: 300 }}
      >
        <div className="payment-header">
          <h2><FaCreditCard /> SISTEMA DE PAGAMENTO</h2>
          <button className="close-btn" onClick={onClose}>
            <FaTimes />
          </button>
        </div>
        
        <div className="payment-tabs">
          <button 
            className={`tab-btn ${activeTab === 'redeem' ? 'active' : ''}`}
            onClick={() => onTabChange('redeem')}
          >
            💳 Resgatar Código
          </button>
          <button 
            className={`tab-btn ${activeTab === 'generate' ? 'active' : ''}`}
            onClick={() => onTabChange('generate')}
          >
            🔑 Gerar Códigos
          </button>
        </div>
        
        {activeTab === 'redeem' && (
          <motion.div
            className="tab-content"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.3 }}
          >
            <div className="input-group">
              <label htmlFor="redeemCodeInput">Código de Resgate:</label>
              <input
                type="text"
                id="redeemCodeInput"
                value={redeemCodeInput}
                onChange={(e) => setRedeemCodeInput(e.target.value)}
                placeholder="Digite o código aqui..."
                maxLength={16}
              />
            </div>
            <motion.button
              className="redeem-btn"
              onClick={handleRedeemCode}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              <FaCheck /> RESGATAR CÓDIGO
            </motion.button>
          </motion.div>
        )}
        
        {activeTab === 'generate' && (
          <motion.div
            className="tab-content"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.3 }}
          >
            <div className="generate-info">
              <p>Gere códigos de resgate para adicionar dinheiro ao seu saldo.</p>
              <p>Os códigos são salvos automaticamente em um arquivo .txt</p>
            </div>
            <motion.button
              className="generate-btn"
              onClick={handleGenerateCode}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              <FaMagic /> GERAR NOVO CÓDIGO
            </motion.button>
            
            {generatedCode && (
              <motion.div
                className="code-result"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
              >
                <h3>🎉 Código Gerado com Sucesso!</h3>
                <div className="generated-code">
                  <strong>Código:</strong> {generatedCode.code}
                </div>
                <div className="generated-amount">
                  <strong>Valor:</strong> R$ {generatedCode.amount.toFixed(2).replace('.', ',')}
                </div>
                <p className="code-note">O código foi salvo no arquivo "codigos_resgate.txt"</p>
              </motion.div>
            )}
          </motion.div>
        )}
      </motion.div>
    </motion.div>
  );
};

// Componente do Carrossel de Propagandas
const AdCarousel = () => {
  const [currentSlide, setCurrentSlide] = useState(0);
  
  const ads = [
    {
      image: "https://via.placeholder.com/800x200/ffd700/1a1a2e?text=PROPAGANDA+1",
      title: "🎰 PROMOÇÃO ESPECIAL!",
      description: "Ganhe até 100x seu dinheiro no Rocket!"
    },
    {
      image: "https://via.placeholder.com/800x200/10b981/1a1a2e?text=PROPAGANDA+2",
      title: "🐯 TIGRINHO PREMIUM!",
      description: "Jackpot progressivo com milhões em prêmios!"
    },
            {
          image: "snake.png",
          title: "🎲 NOVO JOGO: COBRINHA!",
          description: "Colete multiplicadores e evite as bombas!"
        }
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % ads.length);
    }, 5000);

    return () => clearInterval(interval);
  }, [ads.length]);

  const goToSlide = (index) => {
    setCurrentSlide(index);
  };

  const changeSlide = (direction) => {
    setCurrentSlide((prev) => (prev + direction + ads.length) % ads.length);
  };

  return (
    <motion.div 
      className="ad-carousel"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 0.4, ease: "easeOut" }}
    >
      <div className="carousel-container">
        {ads.map((ad, index) => (
          <motion.div
            key={index}
            className={`carousel-slide ${index === currentSlide ? 'active' : ''}`}
            initial={{ opacity: 0 }}
            animate={{ opacity: index === currentSlide ? 1 : 0 }}
            transition={{ duration: 0.5 }}
          >
            <img src={ad.image} alt={`Propaganda ${index + 1}`} className="ad-image" />
            <div className="ad-overlay">
              <h3>{ad.title}</h3>
              <p>{ad.description}</p>
            </div>
          </motion.div>
        ))}
      </div>
      
      {/* Controles do Carrossel */}
      <motion.button 
        className="carousel-btn prev"
        onClick={() => changeSlide(-1)}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        ❮
      </motion.button>
      
      <motion.button 
        className="carousel-btn next"
        onClick={() => changeSlide(1)}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        ❯
      </motion.button>
      
      {/* Indicadores */}
      <div className="carousel-indicators">
        {ads.map((_, index) => (
          <motion.span
            key={index}
            className={`indicator ${index === currentSlide ? 'active' : ''}`}
            onClick={() => goToSlide(index)}
            whileHover={{ scale: 1.2 }}
            whileTap={{ scale: 0.9 }}
          />
        ))}
      </div>
    </motion.div>
  );
};

// Componente de Controles de Aposta
const BetControls = ({ bet, onBetChange }) => (
  <div className="bet-controls">
    <div className="bet-amount">R$ {bet.toFixed(2).replace('.', ',')}</div>
    <div className="bet-buttons">
      <motion.button
        className="bet-btn negative"
        onClick={() => onBetChange(-10)}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        -10
      </motion.button>
      <motion.button
        className="bet-btn negative"
        onClick={() => onBetChange(-1)}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        -1
      </motion.button>
      <motion.button
        className="bet-btn positive"
        onClick={() => onBetChange(1)}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        +1
      </motion.button>
      <motion.button
        className="bet-btn positive"
        onClick={() => onBetChange(10)}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        +10
      </motion.button>
    </div>
  </div>
);

export default CasinoBrasileiro;
