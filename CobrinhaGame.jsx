import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { FaPlay, FaSnake } from 'react-icons/fa';

const CobrinhaGame = ({ balance, bet, onBetChange, onWin }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [score, setScore] = useState(0);
  const [multiplier, setMultiplier] = useState(1.0);
  const [result, setResult] = useState('Clique em INICIAR para jogar!');
  
  const canvasRef = useRef(null);
  const gameRef = useRef(null);
  
  const startGame = () => {
    if (bet > balance) return;
    
    setIsPlaying(true);
    setScore(0);
    setMultiplier(1.0);
    setResult('Use as setas para controlar a cobrinha!');
    
    // Initialize game
    initGame();
  };
  
  const initGame = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    // Game settings
    const gridSize = 20;
    const tileCount = canvas.width / gridSize;
    
    // Snake initial position
    let snake = [{x: 10, y: 10}];
    
    // Food position
    let food = generateFood(snake, tileCount);
    
    // Direction
    let dx = 0;
    let dy = 0;
    
    // Game loop
    function gameLoop() {
      if (!isPlaying) return;
      
      setTimeout(() => {
        clearCanvas();
        moveSnake();
        drawFood();
        drawSnake();
        checkCollision();
        
        if (isPlaying) {
          requestAnimationFrame(gameLoop);
        }
      }, 100);
    }
    
    // Clear canvas
    function clearCanvas() {
      ctx.fillStyle = '#1a1a2e';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    
    // Move snake
    function moveSnake() {
      const head = {x: snake[0].x + dx, y: snake[0].y + dy};
      snake.unshift(head);
      
      if (head.x === food.x && head.y === food.y) {
        // Snake ate food
        setScore(prev => prev + 10);
        setMultiplier(prev => prev + 0.1);
        
        // Check if it's a bomb (10% chance)
        if (Math.random() < 0.1) {
          // Bomb! Game over
          gameOver();
          return;
        }
        
        // Generate new food
        food = generateFood(snake, tileCount);
      } else {
        snake.pop();
      }
    }
    
    // Draw snake
    function drawSnake() {
      snake.forEach((segment, index) => {
        if (index === 0) {
          // Head
          ctx.fillStyle = '#ffd700';
        } else {
          // Body
          ctx.fillStyle = '#10b981';
        }
        ctx.fillRect(segment.x * gridSize, segment.y * gridSize, gridSize - 2, gridSize - 2);
      });
    }
    
    // Draw food
    function drawFood() {
      ctx.fillStyle = '#8b5cf6';
      ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize - 2, gridSize - 2);
    }
    
    // Generate food
    function generateFood(snake, tileCount) {
      let newFood;
      do {
        newFood = {
          x: Math.floor(Math.random() * tileCount),
          y: Math.floor(Math.random() * tileCount)
        };
      } while (snake.some(segment => segment.x === newFood.x && segment.y === newFood.y));
      return newFood;
    }
    
    // Check collision
    function checkCollision() {
      const head = snake[0];
      
      // Wall collision
      if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
        gameOver();
        return;
      }
      
      // Self collision
      for (let i = 1; i < snake.length; i++) {
        if (head.x === snake[i].x && head.y === snake[i].y) {
          gameOver();
          return;
        }
      }
    }
    
    // Game over
    function gameOver() {
      setIsPlaying(false);
      
      // Calculate winnings
      const winnings = Math.floor(bet * multiplier);
      onWin(winnings);
      
      if (winnings > bet) {
        setResult(`🎉 PARABÉNS! Você ganhou R$ ${winnings.toFixed(2).replace('.', ',')}!`);
      } else {
        setResult('😔 Game Over! Tente novamente!');
      }
    }
    
    // Keyboard controls
    const handleKeyDown = (e) => {
      if (!isPlaying) return;
      
      switch(e.key) {
        case 'ArrowUp':
          if (dy !== 1) { dx = 0; dy = -1; }
          break;
        case 'ArrowDown':
          if (dy !== -1) { dx = 0; dy = 1; }
          break;
        case 'ArrowLeft':
          if (dx !== 1) { dx = -1; dy = 0; }
          break;
        case 'ArrowRight':
          if (dx !== -1) { dx = 1; dy = 0; }
          break;
      }
    };
    
    document.addEventListener('keydown', handleKeyDown);
    
    // Start game loop
    gameLoop();
    
    // Cleanup
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  };
  
  useEffect(() => {
    if (isPlaying) {
      gameRef.current = initGame();
    }
    
    return () => {
      if (gameRef.current) {
        gameRef.current();
      }
    };
  }, [isPlaying]);
  
  return (
    <div className="game-content">
      <h2 className="game-title">
        <FaSnake /> COBRINHA - JOGO DE MULTIPLICADORES
      </h2>
      
      <BetControls bet={bet} onBetChange={onBetChange} />
      
      <div className="cobrinha-area">
        <canvas 
          ref={canvasRef}
          width={400} 
          height={400}
          className="cobrinha-canvas"
        />
        
        <div className="cobrinha-info">
          <div className="score">
            Pontuação: <span>{score}</span>
          </div>
          <div className="multiplier">
            Multiplicador: <span>{multiplier.toFixed(2)}x</span>
          </div>
        </div>
      </div>
      
      <motion.button
        className="spin-button"
        onClick={startGame}
        disabled={isPlaying}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        {isPlaying ? (
          <>
            <FaPlay /> JOGANDO...
          </>
        ) : (
          <>
            <FaPlay /> INICIAR COBRINHA!
          </>
        )}
      </motion.button>
      
      <div className={`result ${result.includes('Ganhou') ? 'win' : 'lose'}`}>
        {result}
      </div>
    </div>
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

export default CobrinhaGame;
