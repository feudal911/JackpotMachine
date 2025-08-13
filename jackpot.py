import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading
from PIL import Image, ImageTk
import os

class ModernSlotMachine:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎰 CAÇA-NÍQUEL PREMIUM 🎰")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Configurações do jogo
        self.money = 1000.0
        self.bet = 10.0
        self.is_spinning = False
        self.symbols = ['🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '🎰', '⭐', '🍀', '🔥']
        self.current_reels = ['🎰', '🎰', '🎰']
        self.win_lines = []
        
        # Cores e estilos
        self.colors = {
            'bg': '#1a1a2e',
            'card_bg': '#16213e',
            'accent': '#0f3460',
            'gold': '#ffd700',
            'silver': '#c0c0c0',
            'text': '#ffffff',
            'success': '#4ade80',
            'danger': '#f87171'
        }
        
        self.setup_ui()
        self.update_display()
        
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Título principal
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(
            title_frame, 
            text="🎰 CAÇA-NÍQUEL PREMIUM 🎰", 
            font=('Arial Black', 24, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Tente sua sorte e ganhe grandes prêmios!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        subtitle.pack(pady=(5, 0))
        
        # Frame das informações do jogador
        info_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        info_frame.pack(fill='x', pady=(0, 20))
        
        # Saldo
        balance_frame = tk.Frame(info_frame, bg=self.colors['card_bg'])
        balance_frame.pack(side='left', padx=20, pady=15)
        
        tk.Label(
            balance_frame,
            text="💰 SALDO:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.balance_label = tk.Label(
            balance_frame,
            text="R$ 0.00",
            font=('Arial', 18, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['card_bg']
        )
        self.balance_label.pack()
        
        # Aposta
        bet_frame = tk.Frame(info_frame, bg=self.colors['card_bg'])
        bet_frame.pack(side='left', padx=40, pady=15)
        
        tk.Label(
            bet_frame,
            text="🎯 APOSTA:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.bet_label = tk.Label(
            bet_frame,
            text="R$ 0.00",
            font=('Arial', 18, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.bet_label.pack()
        
        # Controles de aposta
        bet_controls = tk.Frame(info_frame, bg=self.colors['card_bg'])
        bet_controls.pack(side='right', padx=20, pady=15)
        
        tk.Label(
            bet_controls,
            text="Ajustar Aposta:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        ).pack()
        
        bet_buttons_frame = tk.Frame(bet_controls, bg=self.colors['card_bg'])
        bet_buttons_frame.pack(pady=(5, 0))
        
        tk.Button(
            bet_buttons_frame,
            text="-10",
            command=lambda: self.change_bet(-10),
            font=('Arial', 10, 'bold'),
            bg=self.colors['danger'],
            fg='white',
            width=5,
            relief='raised',
            bd=2
        ).pack(side='left', padx=2)
        
        tk.Button(
            bet_buttons_frame,
            text="-1",
            command=lambda: self.change_bet(-1),
            font=('Arial', 10, 'bold'),
            bg=self.colors['danger'],
            fg='white',
            width=5,
            relief='raised',
            bd=2
        ).pack(side='left', padx=2)
        
        tk.Button(
            bet_buttons_frame,
            text="+1",
            command=lambda: self.change_bet(1),
            font=('Arial', 10, 'bold'),
            bg=self.colors['success'],
            fg='white',
            width=5,
            relief='raised',
            bd=2
        ).pack(side='left', padx=2)
        
        tk.Button(
            bet_buttons_frame,
            text="+10",
            command=lambda: self.change_bet(10),
            font=('Arial', 10, 'bold'),
            bg=self.colors['success'],
            fg='white',
            width=5,
            relief='raised',
            bd=2
        ).pack(side='left', padx=2)
        
        # Frame dos rolos
        reels_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief='raised', bd=3)
        reels_frame.pack(fill='x', pady=(0, 20))
        
        # Título dos rolos
        tk.Label(
            reels_frame,
            text="🎰 ROLOS DA SORTE 🎰",
            font=('Arial Black', 16, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(15, 10))
        
        # Container dos rolos
        reels_container = tk.Frame(reels_frame, bg=self.colors['card_bg'])
        reels_container.pack(pady=(0, 20))
        
        # Rolo 1
        reel1_frame = tk.Frame(reels_container, bg=self.colors['accent'], relief='sunken', bd=3)
        reel1_frame.pack(side='left', padx=10)
        
        self.reel1_label = tk.Label(
            reel1_frame,
            text="🎰",
            font=('Arial', 48),
            bg=self.colors['accent'],
            fg='white',
            width=3,
            height=2
        )
        self.reel1_label.pack(padx=20, pady=20)
        
        # Rolo 2
        reel2_frame = tk.Frame(reels_container, bg=self.colors['accent'], relief='sunken', bd=3)
        reel2_frame.pack(side='left', padx=10)
        
        self.reel2_label = tk.Label(
            reel2_frame,
            text="🎰",
            font=('Arial', 48),
            bg=self.colors['accent'],
            fg='white',
            width=3,
            height=2
        )
        self.reel2_label.pack(padx=20, pady=20)
        
        # Rolo 3
        reel3_frame = tk.Frame(reels_container, bg=self.colors['accent'], relief='sunken', bd=3)
        reel3_frame.pack(side='left', padx=10)
        
        self.reel3_label = tk.Label(
            reel3_frame,
            text="🎰",
            font=('Arial', 48),
            bg=self.colors['accent'],
            fg='white',
            width=3,
            height=2
        )
        self.reel3_label.pack(padx=20, pady=20)
        
        # Botão de girar
        spin_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        spin_frame.pack(pady=(0, 20))
        
        self.spin_button = tk.Button(
            spin_frame,
            text="🎰 GIRAR! 🎰",
            command=self.spin,
            font=('Arial Black', 18, 'bold'),
            bg=self.colors['gold'],
            fg='black',
            width=20,
            height=2,
            relief='raised',
            bd=4,
            cursor='hand2'
        )
        self.spin_button.pack()
        
        # Frame de resultados
        results_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        results_frame.pack(fill='x')
        
        # Título dos resultados
        tk.Label(
            results_frame,
            text="📊 RESULTADOS",
            font=('Arial Black', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(15, 10))
        
        # Resultado atual
        self.result_label = tk.Label(
            results_frame,
            text="Aguardando giro...",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.result_label.pack(pady=(0, 10))
        
        # Linhas de vitória
        self.win_lines_label = tk.Label(
            results_frame,
            text="",
            font=('Arial', 10),
            fg=self.colors['success'],
            bg=self.colors['card_bg']
        )
        self.win_lines_label.pack(pady=(0, 15))
        
        # Frame das regras
        rules_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief='raised', bd=2)
        rules_frame.pack(fill='x', pady=(20, 0))
        
        tk.Label(
            rules_frame,
            text="📖 REGRAS DO JOGO",
            font=('Arial Black', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(10, 5))
        
        rules_text = """
        💎💎💎 = JACKPOT (10x) | 🎰🎰🎰 = 5x | 7️⃣7️⃣7️⃣ = 5x | ⭐⭐⭐ = 5x
        🍀🍀🍀 = 4x | 🔥🔥🔥 = 4x | 🍎🍎🍎 = 3x | 🍊🍊🍊 = 3x | 🍇🍇🍇 = 3x | 🍒🍒🍒 = 3x
        Dois símbolos iguais = 1.5x | Aposta mínima: R$ 1,00 | Aposta máxima: R$ 10.000,00
        """
        
        rules_label = tk.Label(
            rules_frame,
            text=rules_text,
            font=('Arial', 9),
            fg=self.colors['text'],
            bg=self.colors['card_bg'],
            justify='left'
        )
        rules_label.pack(pady=(0, 10))
        
    def change_bet(self, amount):
        if not self.is_spinning:
            new_bet = self.bet + amount
            if 1 <= new_bet <= 10000 and new_bet <= self.money:
                self.bet = new_bet
                self.update_display()
                
    def update_display(self):
        self.balance_label.config(text=f"R$ {self.money:.2f}")
        self.bet_label.config(text=f"R$ {self.bet:.2f}")
        
    def spin(self):
        if self.is_spinning:
            return
            
        if self.bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente para esta aposta!")
            return
            
        self.is_spinning = True
        self.spin_button.config(state='disabled', text="🎰 GIRRANDO... 🎰")
        self.money -= self.bet
        self.update_display()
        
        # Inicia a animação em thread separada
        spin_thread = threading.Thread(target=self.animate_spin)
        spin_thread.daemon = True
        spin_thread.start()
        
    def animate_spin(self):
        # Animação de giro
        for _ in range(10):
            if not self.is_spinning:
                break
                
            # Gera símbolos aleatórios para animação
            temp_reels = [random.choice(self.symbols) for _ in range(3)]
            
            # Atualiza a interface na thread principal
            self.root.after(0, self.update_reels, temp_reels)
            time.sleep(0.1)
            
        # Resultado final
        final_reels = [random.choice(self.symbols) for _ in range(3)]
        self.root.after(0, self.finish_spin, final_reels)
        
    def update_reels(self, reels):
        self.reel1_label.config(text=reels[0])
        self.reel2_label.config(text=reels[1])
        self.reel3_label.config(text=reels[2])
        
    def finish_spin(self, final_reels):
        self.current_reels = final_reels
        self.update_reels(final_reels)
        
        # Verifica resultado
        winnings = self.check_win(final_reels)
        
        if winnings > 0:
            self.money += winnings
            self.result_label.config(
                text=f"🎉 PARABÉNS! Você ganhou R$ {winnings:.2f}!",
                fg=self.colors['success']
            )
        else:
            self.result_label.config(
                text="😔 Que pena! Tente novamente!",
                fg=self.colors['danger']
            )
            
        self.update_display()
        self.is_spinning = False
        self.spin_button.config(state='normal', text="🎰 GIRAR! 🎰")
        
    def check_win(self, reels):
        # Verifica combinações vencedoras
        if reels[0] == reels[1] == reels[2]:
            symbol = reels[0]
            if symbol == '💎':
                return self.bet * 10  # Jackpot
            elif symbol in ['🎰', '7️⃣', '⭐']:
                return self.bet * 5
            elif symbol in ['🍀', '🔥']:
                return self.bet * 4
            else:
                return self.bet * 3
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            return self.bet * 1.5
        return 0
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Verifica se o PIL está instalado
    try:
        from PIL import Image, ImageTk
    except ImportError:
        print("Instalando dependências necessárias...")
        os.system("pip install pillow")
        from PIL import Image, ImageTk
        
    print("🎰 Iniciando Caça-Níquel Premium...")
    slot = ModernSlotMachine()
    slot.run()