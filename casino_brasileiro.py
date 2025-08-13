import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading
import math

class CasinoBrasileiro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎰 FEUDAL BET - CASINO PREMIUM 🎰")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Configurações do jogador
        self.money = 1000.0
        self.current_game = "slot"
        
        # Cores e estilos
        self.colors = {
            'bg': '#1a1a2e',
            'card_bg': '#16213e',
            'accent': '#0f3460',
            'gold': '#ffd700',
            'silver': '#c0c0c0',
            'text': '#ffffff',
            'success': '#4ade80',
            'danger': '#f87171',
            'warning': '#fbbf24'
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
            text="🎰 FEUDAL BET - CASINO PREMIUM 🎰", 
            font=('Arial Black', 24, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Os melhores jogos das plataformas brasileiras!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        subtitle.pack(pady=(5, 0))
        
        # Carrossel de Propagandas
        self.setup_ad_carousel(title_frame)
        
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
        
        # Add money button
        tk.Button(
            balance_frame,
            text="+ ADICIONAR DINHEIRO",
            command=self.show_payment_modal,
            font=('Arial', 10, 'bold'),
            bg=self.colors['success'],
            fg='white',
            relief='raised',
            bd=2
        ).pack(pady=(5, 0))
        
        # Seletor de jogos
        games_frame = tk.Frame(info_frame, bg=self.colors['card_bg'])
        games_frame.pack(side='left', padx=40, pady=15)
        
        tk.Label(
            games_frame,
            text="🎮 JOGO ATUAL:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.game_var = tk.StringVar(value="Caça-Níquel")
        game_menu = ttk.Combobox(
            games_frame,
            textvariable=self.game_var,
            values=["Caça-Níquel", "Rocket", "Roleta", "Dados", "Pesca", "Plinko", "Tigrinho", "Cobrinha"],
            state="readonly",
            font=('Arial', 12),
            width=15
        )
        game_menu.pack(pady=(5, 0))
        game_menu.bind('<<ComboboxSelected>>', self.change_game)
        
        # Botão de recarregar saldo
        reload_frame = tk.Frame(info_frame, bg=self.colors['card_bg'])
        reload_frame.pack(side='right', padx=20, pady=15)
        
        tk.Button(
            reload_frame,
            text="🔄 RECARREGAR",
            command=self.reload_balance,
            font=('Arial', 12, 'bold'),
            bg=self.colors['warning'],
            fg='black',
            relief='raised',
            bd=2
        ).pack()
        
        # Frame do jogo atual
        self.game_frame = tk.Frame(main_frame, bg=self.colors['card_bg'], relief='raised', bd=3)
        self.game_frame.pack(fill='both', expand=True)
        
        # Inicializa o jogo padrão
        self.show_slot_machine()
        
    def change_game(self, event=None):
        game = self.game_var.get()
        # Limpa o frame do jogo
        for widget in self.game_frame.winfo_children():
            widget.destroy()
            
        if game == "Caça-Níquel":
            self.show_slot_machine()
        elif game == "Rocket":
            self.show_rocket_game()
        elif game == "Roleta":
            self.show_roulette()
        elif game == "Dados":
            self.show_dice_game()
        elif game == "Pesca":
            self.show_fishing_game()
        elif game == "Plinko":
            self.show_plinko_game()
        elif game == "Tigrinho":
            self.show_tigrinho_game()
        elif game == "Cobrinha":
            self.show_cobrinha_game()
            
    def show_slot_machine(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🎰 CAÇA-NÍQUEL TRADICIONAL 🎰",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Controles de aposta
        bet_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        bet_frame.pack(pady=(0, 20))
        
        tk.Label(
            bet_frame,
            text="🎯 APOSTA:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.slot_bet = 10.0
        self.slot_bet_label = tk.Label(
            bet_frame,
            text=f"R$ {self.slot_bet:.2f}",
            font=('Arial', 16, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.slot_bet_label.pack()
        
        # Botões de aposta
        bet_buttons = tk.Frame(bet_frame, bg=self.colors['card_bg'])
        bet_buttons.pack(pady=(10, 0))
        
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                bet_buttons,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_slot_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Rolos
        reels_frame = tk.Frame(self.game_frame, bg=self.colors['accent'], relief='sunken', bd=3)
        reels_frame.pack(pady=(0, 20))
        
        reels_container = tk.Frame(reels_frame, bg=self.colors['accent'])
        reels_container.pack(pady=20)
        
        self.slot_reels = []
        symbols = ['🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '🎰', '⭐']
        
        for i in range(3):
            reel_frame = tk.Frame(reels_container, bg=self.colors['accent'])
            reel_frame.pack(side='left', padx=10)
            
            reel_label = tk.Label(
                reel_frame,
                text=symbols[i],
                font=('Arial', 48),
                bg=self.colors['accent'],
                fg='white',
                width=3,
                height=2
            )
            reel_label.pack(padx=20, pady=20)
            self.slot_reels.append(reel_label)
        
        # Botão de girar
        self.slot_spin_button = tk.Button(
            self.game_frame,
            text="🎰 GIRAR! 🎰",
            command=self.slot_spin,
            font=('Arial Black', 16, 'bold'),
            bg=self.colors['gold'],
            fg='black',
            width=20,
            height=2,
            relief='raised',
            bd=4,
            cursor='hand2'
        )
        self.slot_spin_button.pack(pady=(0, 20))
        
        # Resultado
        self.slot_result = tk.Label(
            self.game_frame,
            text="Aguardando giro...",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.slot_result.pack()
        
    def show_rocket_game(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🚀 ROCKET - JOGO DE MULTIPLICADOR 🚀",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Controles de aposta
        bet_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        bet_frame.pack(pady=(0, 20))
        
        tk.Label(
            bet_frame,
            text="🎯 APOSTA:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.rocket_bet = 10.0
        self.rocket_bet_label = tk.Label(
            bet_frame,
            text=f"R$ {self.rocket_bet:.2f}",
            font=('Arial', 16, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.rocket_bet_label.pack()
        
        # Botões de aposta
        bet_buttons = tk.Frame(bet_frame, bg=self.colors['card_bg'])
        bet_buttons.pack(pady=(10, 0))
        
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                bet_buttons,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_rocket_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Área do foguete
        rocket_area = tk.Frame(self.game_frame, bg=self.colors['accent'], relief='sunken', bd=3)
        rocket_area.pack(pady=(0, 20), fill='both', expand=True)
        
        self.rocket_label = tk.Label(
            rocket_area,
            text="🚀",
            font=('Arial', 72),
            bg=self.colors['accent'],
            fg='white'
        )
        self.rocket_label.pack(expand=True)
        
        # Multiplicador
        self.multiplier_label = tk.Label(
            rocket_area,
            text="Multiplicador: 1.00x",
            font=('Arial', 16, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['accent']
        )
        self.rocket_label.pack()
        
        # Botão de apostar
        self.rocket_button = tk.Button(
            self.game_frame,
            text="🚀 APOSTAR! 🚀",
            command=self.rocket_bet_click,
            font=('Arial Black', 16, 'bold'),
            bg=self.colors['gold'],
            fg='black',
            width=20,
            height=2,
            relief='raised',
            bd=4,
            cursor='hand2'
        )
        self.rocket_button.pack(pady=(0, 20))
        
        # Resultado
        self.rocket_result = tk.Label(
            self.game_frame,
            text="Clique em APOSTAR para iniciar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.rocket_result.pack()
        
    def show_roulette(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🎲 ROLETA EUROPEIA 🎲",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Área da roleta
        roulette_area = tk.Frame(self.game_frame, bg=self.colors['accent'], relief='sunken', bd=3)
        roulette_area.pack(pady=(0, 20), fill='both', expand=True)
        
        # Números da roleta (0-36)
        numbers_frame = tk.Frame(roulette_area, bg=self.colors['accent'])
        numbers_frame.pack(pady=20)
        
        # Cria grade de números
        for i in range(37):
            row = i // 12
            col = i % 12
            
            if i == 0:
                color = self.colors['success']  # Verde para o zero
            elif i % 2 == 0:
                color = self.colors['danger']   # Vermelho para pares
            else:
                color = self.colors['text']     # Preto para ímpares
                
            num_button = tk.Button(
                numbers_frame,
                text=str(i),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white' if i == 0 else 'black',
                width=3,
                height=1,
                relief='raised',
                bd=2
            )
            num_button.grid(row=row, column=col, padx=1, pady=1)
        
        # Controles de aposta
        controls_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        controls_frame.pack(pady=(0, 20))
        
        # Aposta
        tk.Label(
            controls_frame,
            text="🎯 APOSTA:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(side='left', padx=20)
        
        self.roulette_bet = 10.0
        self.roulette_bet_label = tk.Label(
            controls_frame,
            text=f"R$ {self.roulette_bet:.2f}",
            font=('Arial', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.roulette_bet_label.pack(side='left', padx=10)
        
        # Botões de aposta
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                controls_frame,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_roulette_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Botão de girar
        self.roulette_button = tk.Button(
            self.game_frame,
            text="🎲 GIRAR ROLETA! 🎲",
            command=self.roulette_spin,
            font=('Arial Black', 16, 'bold'),
            bg=self.colors['gold'],
            fg='black',
            width=20,
            height=2,
            relief='raised',
            bd=4,
            cursor='hand2'
        )
        self.roulette_button.pack(pady=(0, 20))
        
        # Resultado
        self.roulette_result = tk.Label(
            self.game_frame,
            text="Clique em GIRAR para jogar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.roulette_result.pack()
        
    def show_dice_game(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🎲 JOGO DE DADOS 🎲",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Área dos dados
        dice_area = tk.Frame(self.game_frame, bg=self.colors['accent'], relief='sunken', bd=3)
        dice_area.pack(pady=(0, 20), fill='both', expand=True)
        
        # Dados
        dice_frame = tk.Frame(dice_area, bg=self.colors['accent'])
        dice_frame.pack(pady=20)
        
        self.dice_labels = []
        for i in range(2):
            dice_label = tk.Label(
                dice_frame,
                text="⚀",
                font=('Arial', 48),
                bg=self.colors['accent'],
                fg='white',
                width=3,
                height=2
            )
            dice_label.pack(side='left', padx=20)
            self.dice_labels.append(dice_label)
        
        # Soma dos dados
        self.dice_sum_label = tk.Label(
            dice_area,
            text="Soma: 2",
            font=('Arial', 16, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['accent']
        )
        self.dice_sum_label.pack()
        
        # Controles
        controls_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        controls_frame.pack(pady=(0, 20))
        
        # Aposta
        tk.Label(
            controls_frame,
            text="🎯 APOSTA:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(side='left', padx=20)
        
        self.dice_bet = 10.0
        self.dice_bet_label = tk.Label(
            controls_frame,
            text=f"R$ {self.dice_bet:.2f}",
            font=('Arial', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.dice_bet_label.pack(side='left', padx=10)
        
        # Botões de aposta
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                controls_frame,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_dice_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Botão de rolar
        self.dice_button = tk.Button(
            self.game_frame,
            text="🎲 ROLAR DADOS! 🎲",
            command=self.roll_dice,
            font=('Arial Black', 16, 'bold'),
            bg=self.colors['gold'],
            fg='black',
            width=20,
            height=2,
            relief='raised',
            bd=4,
            cursor='hand2'
        )
        self.dice_button.pack(pady=(0, 20))
        
        # Resultado
        self.dice_result = tk.Label(
            self.game_frame,
            text="Clique em ROLAR para jogar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.dice_result.pack()
        
    def show_fishing_game(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🎣 JOGO DE PESCA 🎣",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Área de pesca
        fishing_area = tk.Frame(self.game_frame, bg='#006994', relief='sunken', bd=3)
        fishing_area.pack(pady=(0, 20), fill='both', expand=True)
        
        # Peixes
        fish_frame = tk.Frame(fishing_area, bg='#006994')
        fish_frame.pack(pady=20)
        
        self.fish_labels = []
        fish_types = ['🐟', '🐠', '🦈', '🐡', '🦑', '🦐', '🦞', '🦀']
        
        for i, fish in enumerate(fish_types):
            fish_label = tk.Label(
                fish_frame,
                text=fish,
                font=('Arial', 24),
                bg='#006994',
                fg='white',
                cursor='hand2'
            )
            fish_label.pack(side='left', padx=10)
            fish_label.bind('<Button-1>', lambda e, f=fish, idx=i: self.catch_fish(f, idx))
            self.fish_labels.append(fish_label)
        
        # Controles
        controls_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        controls_frame.pack(pady=(0, 20))
        
        # Aposta
        tk.Label(
            controls_frame,
            text="🎯 APOSTA:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(side='left', padx=20)
        
        self.fishing_bet = 10.0
        self.fishing_bet_label = tk.Label(
            controls_frame,
            text=f"R$ {self.fishing_bet:.2f}",
            font=('Arial', 14, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.fishing_bet_label.pack(side='left', padx=10)
        
        # Botões de aposta
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                controls_frame,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_fishing_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Resultado
        self.fishing_result = tk.Label(
            self.game_frame,
            text="Clique nos peixes para pescar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.fishing_result.pack()
        
    # Métodos dos jogos
    def change_slot_bet(self, amount):
        new_bet = self.slot_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.slot_bet = new_bet
            self.slot_bet_label.config(text=f"R$ {self.slot_bet:.2f}")
            
    def slot_spin(self):
        if self.slot_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.slot_bet
        self.update_display()
        
        # Animação de giro
        symbols = ['🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '🎰', '⭐']
        final_reels = [random.choice(symbols) for _ in range(3)]
        
        # Atualiza rolos
        for i, reel in enumerate(self.slot_reels):
            reel.config(text=final_reels[i])
        
        # Verifica resultado
        winnings = self.check_slot_win(final_reels)
        if winnings > 0:
            self.money += winnings
            self.slot_result.config(
                text=f"🎉 PARABÉNS! Você ganhou R$ {winnings:.2f}!",
                fg=self.colors['success']
            )
        else:
            self.slot_result.config(
                text="😔 Que pena! Tente novamente!",
                fg=self.colors['danger']
            )
            
        self.update_display()
        
    def check_slot_win(self, reels):
        if reels[0] == reels[1] == reels[2]:
            symbol = reels[0]
            if symbol == '💎':
                return self.slot_bet * 10
            elif symbol in ['🎰', '7️⃣', '⭐']:
                return self.slot_bet * 5
            else:
                return self.slot_bet * 3
        elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            return self.slot_bet * 1.5
        return 0
        
    def change_rocket_bet(self, amount):
        new_bet = self.rocket_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.rocket_bet = new_bet
            self.rocket_bet_label.config(text=f"R$ {self.rocket_bet:.2f}")
            
    def rocket_bet_click(self):
        if self.rocket_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.rocket_bet
        self.update_display()
        
        # Simula o crescimento do foguete
        self.rocket_button.config(state='disabled', text="🚀 CRESCENDO... 🚀")
        
        # Thread para animação
        rocket_thread = threading.Thread(target=self.rocket_animation)
        rocket_thread.daemon = True
        rocket_thread.start()
        
    def rocket_animation(self):
        multiplier = 1.0
        while multiplier < 10.0:  # Máximo 10x
            if random.random() < 0.1:  # 10% chance de explodir
                self.root.after(0, self.rocket_explode)
                return
                
            multiplier += 0.1
            self.root.after(0, self.update_rocket_multiplier, multiplier)
            time.sleep(0.1)
            
        # Se chegou a 10x, é vitória automática
        self.root.after(0, self.rocket_win, multiplier)
        
    def update_rocket_multiplier(self, multiplier):
        self.multiplier_label.config(text=f"Multiplicador: {multiplier:.2f}x")
        
    def rocket_explode(self):
        self.rocket_label.config(text="💥")
        self.rocket_result.config(
            text="💥 BOOM! Foguete explodiu! Perdeu a aposta!",
            fg=self.colors['danger']
        )
        self.rocket_button.config(state='normal', text="🚀 APOSTAR! 🚀")
        
    def rocket_win(self, multiplier):
        winnings = self.rocket_bet * multiplier
        self.money += winnings
        self.rocket_result.config(
            text=f"🎉 PARABÉNS! Foguete chegou a {multiplier:.1f}x! Ganhou R$ {winnings:.2f}!",
            fg=self.colors['success']
        )
        self.rocket_button.config(state='normal', text="🚀 APOSTAR! 🚀")
        self.update_display()
        
    def change_roulette_bet(self, amount):
        new_bet = self.roulette_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.roulette_bet = new_bet
            self.roulette_bet_label.config(text=f"R$ {self.roulette_bet:.2f}")
            
    def roulette_spin(self):
        if self.roulette_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.roulette_bet
        self.update_display()
        
        # Gira a roleta
        result = random.randint(0, 36)
        
        # Verifica resultado
        if result == 0:
            winnings = self.roulette_bet * 35  # Zero paga 35:1
        elif result % 2 == 0:
            winnings = self.roulette_bet * 2   # Pares pagam 2:1
        else:
            winnings = self.roulette_bet * 2   # Ímpares pagam 2:1
            
        self.money += winnings
        self.roulette_result.config(
            text=f"🎲 Resultado: {result}! Ganhou R$ {winnings:.2f}!",
            fg=self.colors['success']
        )
        self.update_display()
        
    def change_dice_bet(self, amount):
        new_bet = self.dice_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.dice_bet = new_bet
            self.dice_bet_label.config(text=f"R$ {self.dice_bet:.2f}")
            
    def roll_dice(self):
        if self.dice_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.dice_bet
        self.update_display()
        
        # Rola os dados
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        
        # Atualiza visual
        dice_symbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
        self.dice_labels[0].config(text=dice_symbols[dice1-1])
        self.dice_labels[1].config(text=dice_symbols[dice2-1])
        self.dice_sum_label.config(text=f"Soma: {total}")
        
        # Verifica resultado
        if total == 7 or total == 11:
            winnings = self.dice_bet * 2
            self.money += winnings
            self.dice_result.config(
                text=f"🎉 PARABÉNS! Soma {total}! Ganhou R$ {winnings:.2f}!",
                fg=self.colors['success']
            )
        else:
            self.dice_result.config(
                text=f"😔 Soma {total}. Tente novamente!",
                fg=self.colors['danger']
            )
            
        self.update_display()
        
    def change_fishing_bet(self, amount):
        new_bet = self.fishing_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.fishing_bet = new_bet
            self.fishing_bet_label.config(text=f"R$ {self.fishing_bet:.2f}")
            
    def catch_fish(self, fish, index):
        if self.fishing_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.fishing_bet
        
        # Diferentes peixes têm diferentes valores
        fish_values = {
            '🐟': 1.5, '🐠': 2.0, '🦈': 3.0, '🐡': 2.5,
            '🦑': 1.8, '🦐': 1.2, '🦞': 4.0, '🦀': 1.0
        }
        
        multiplier = fish_values.get(fish, 1.0)
        winnings = self.fishing_bet * multiplier
        
        self.money += winnings
        self.fishing_result.config(
            text=f"🎣 Pescou {fish}! Multiplicador {multiplier}x! Ganhou R$ {winnings:.2f}!",
            fg=self.colors['success']
        )
        
        # Esconde o peixe pescado
        self.fish_labels[index].config(text="🌊")
        
        self.update_display()
        
    def show_plinko_game(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🔴 PLINKO - JOGO DE QUEDAS 🔴",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Área do Plinko
        plinko_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        plinko_frame.pack(pady=(0, 20))
        
        # Zona de queda da bola
        drop_zone = tk.Frame(plinko_frame, bg=self.colors['accent'], relief='sunken', bd=2)
        drop_zone.pack(pady=(0, 20))
        
        self.plinko_ball = tk.Label(
            drop_zone,
            text="🔴",
            font=('Arial', 24),
            bg=self.colors['accent'],
            fg='red'
        )
        self.plinko_ball.pack(pady=10)
        
        # Área dos pinos (simulada)
        pins_area = tk.Frame(plinko_frame, bg=self.colors['accent'], height=200, relief='sunken', bd=2)
        pins_area.pack(fill='x', pady=(0, 20))
        
        # Baldes de resultado
        buckets_frame = tk.Frame(plinko_frame, bg=self.colors['card_bg'])
        buckets_frame.pack(fill='x')
        
        multipliers = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 0.5, 0.2]
        self.plinko_buckets = []
        
        for i, mult in enumerate(multipliers):
            color = self.colors['danger'] if mult < 1.0 else self.colors['success']
            bucket = tk.Label(
                buckets_frame,
                text=f"{mult}x",
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                relief='raised',
                bd=2,
                width=8
            )
            bucket.pack(side='left', padx=2)
            self.plinko_buckets.append(bucket)
        
        # Controles de aposta
        bet_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        bet_frame.pack(pady=(0, 20))
        
        tk.Label(
            bet_frame,
            text="🎯 APOSTA:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.plinko_bet = 10.0
        self.plinko_bet_label = tk.Label(
            bet_frame,
            text=f"R$ {self.plinko_bet:.2f}",
            font=('Arial', 16, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.plinko_bet_label.pack()
        
        # Botões de aposta
        bet_buttons = tk.Frame(bet_frame, bg=self.colors['card_bg'])
        bet_buttons.pack(pady=(10, 0))
        
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                bet_buttons,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_plinko_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Botão de jogar
        tk.Button(
            self.game_frame,
            text="🔴 SOLTAR BOLA!",
            command=self.drop_plinko_ball,
            font=('Arial', 14, 'bold'),
            bg=self.colors['danger'],
            fg='white',
            relief='raised',
            bd=3,
            width=20
        ).pack(pady=(0, 20))
        
        # Resultado
        self.plinko_result = tk.Label(
            self.game_frame,
            text="Clique em SOLTAR BOLA para jogar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.plinko_result.pack()
        
    def show_tigrinho_game(self):
        # Título do jogo
        tk.Label(
            self.game_frame,
            text="🐯 TIGRINHO - SLOT BRASILEIRO 🐯",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 10))
        
        # Área dos rolos
        reels_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        reels_frame.pack(pady=(0, 20))
        
        self.tigrinho_reels = []
        for i in range(3):
            reel = tk.Label(
                reels_frame,
                text="🐯",
                font=('Arial', 36),
                bg=self.colors['accent'],
                fg='white',
                relief='raised',
                bd=3,
                width=4,
                height=2
            )
            reel.pack(side='left', padx=10)
            self.tigrinho_reels.append(reel)
        
        # Símbolo especial
        special_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        special_frame.pack(pady=(0, 20))
        
        tk.Label(
            special_frame,
            text="🎰 Símbolo Especial:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.special_symbol = tk.Label(
            special_frame,
            text="🎰",
            font=('Arial', 24),
            bg=self.colors['accent'],
            fg=self.colors['gold']
        )
        self.special_symbol.pack()
        
        # Controles de aposta
        bet_frame = tk.Frame(self.game_frame, bg=self.colors['card_bg'])
        bet_frame.pack(pady=(0, 20))
        
        tk.Label(
            bet_frame,
            text="🎯 APOSTA:",
            font=('Arial', 14, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack()
        
        self.tigrinho_bet = 10.0
        self.tigrinho_bet_label = tk.Label(
            bet_frame,
            text=f"R$ {self.tigrinho_bet:.2f}",
            font=('Arial', 16, 'bold'),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.tigrinho_bet_label.pack()
        
        # Botões de aposta
        bet_buttons = tk.Frame(bet_frame, bg=self.colors['card_bg'])
        bet_buttons.pack(pady=(10, 0))
        
        for amount in [-10, -1, 1, 10]:
            color = self.colors['danger'] if amount < 0 else self.colors['success']
            tk.Button(
                bet_buttons,
                text=f"{amount:+d}",
                command=lambda a=amount: self.change_tigrinho_bet(a),
                font=('Arial', 10, 'bold'),
                bg=color,
                fg='white',
                width=5,
                relief='raised',
                bd=2
            ).pack(side='left', padx=2)
        
        # Botão de girar
        tk.Button(
            self.game_frame,
            text="🐯 GIRAR TIGRINHO!",
            command=self.spin_tigrinho,
            font=('Arial', 14, 'bold'),
            bg=self.colors['danger'],
            fg='white',
            relief='raised',
            bd=3,
            width=20
        ).pack(pady=(0, 20))
        
        # Resultado
        self.tigrinho_result = tk.Label(
            self.game_frame,
            text="Clique em GIRAR para jogar!",
            font=('Arial', 12),
            fg=self.colors['text'],
            bg=self.colors['card_bg']
        )
        self.tigrinho_result.pack()
        
    def change_plinko_bet(self, amount):
        new_bet = self.plinko_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.plinko_bet = new_bet
            self.plinko_bet_label.config(text=f"R$ {self.plinko_bet:.2f}")
            
    def drop_plinko_ball(self):
        if self.plinko_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.plinko_bet
        self.update_display()
        
        # Simula a queda da bola
        multipliers = [0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 0.5, 0.2]
        weights = [0.3, 0.25, 0.2, 0.15, 0.05, 0.02, 0.25, 0.3]
        
        random_val = random.random()
        cumulative_weight = 0
        selected_multiplier = 0.2
        
        for i, weight in enumerate(weights):
            cumulative_weight += weight
            if random_val <= cumulative_weight:
                selected_multiplier = multipliers[i]
                break
        
        # Anima a queda da bola
        self.plinko_ball.config(text="🔴")
        
        # Resultado
        winnings = self.plinko_bet * selected_multiplier
        self.money += winnings
        
        if winnings > 0:
            self.plinko_result.config(
                text=f"🎉 PARABÉNS! Bola caiu no {selected_multiplier}x! Ganhou R$ {winnings:.2f}!",
                fg=self.colors['success']
            )
        else:
            self.plinko_result.config(
                text=f"😔 Bola caiu no {selected_multiplier}x. Tente novamente!",
                fg=self.colors['danger']
            )
        
        self.update_display()
        
    def change_tigrinho_bet(self, amount):
        new_bet = self.tigrinho_bet + amount
        if 1 <= new_bet <= 10000 and new_bet <= self.money:
            self.tigrinho_bet = new_bet
            self.tigrinho_bet_label.config(text=f"R$ {self.tigrinho_bet:.2f}")
            
    def spin_tigrinho(self):
        if self.tigrinho_bet > self.money:
            messagebox.showerror("Erro", "Saldo insuficiente!")
            return
            
        self.money -= self.tigrinho_bet
        self.update_display()
        
        # Símbolos do Tigrinho
        symbols = ['🐯', '🍎', '🍊', '🍇', '🍒', '💎', '7️⃣', '⭐', '🎰']
        
        # Gira os rolos
        final_reels = []
        for i in range(3):
            symbol = random.choice(symbols)
            final_reels.append(symbol)
            self.tigrinho_reels[i].config(text=symbol)
        
        # Verifica símbolo especial
        special_symbol = random.random() < 0.1
        if special_symbol:
            self.special_symbol.config(text="🎰")
        
        # Verifica vitória
        winnings = self.check_tigrinho_win(final_reels, special_symbol)
        if winnings > 0:
            self.money += winnings
            self.tigrinho_result.config(
                text=f"🎉 PARABÉNS! Você ganhou R$ {winnings:.2f}!",
                fg=self.colors['success']
            )
        else:
            self.tigrinho_result.config(
                text="😔 Que pena! Tente novamente!",
                fg=self.colors['danger']
            )
        
        self.update_display()
        
    def check_tigrinho_win(self, reels, special_symbol):
        # Três tigres (maior pagamento)
        if reels[0] == '🐯' and reels[1] == '🐯' and reels[2] == '🐯':
            return self.tigrinho_bet * 20
        
        # Três diamantes
        if reels[0] == '💎' and reels[1] == '💎' and reels[2] == '💎':
            return self.tigrinho_bet * 15
        
        # Três setes
        if reels[0] == '7️⃣' and reels[1] == '7️⃣' and reels[2] == '7️⃣':
            return self.tigrinho_bet * 10
        
        # Três iguais
        if reels[0] == reels[1] and reels[1] == reels[2]:
            return self.tigrinho_bet * 5
        
        # Dois tigres
        if ((reels[0] == '🐯' and reels[1] == '🐯') or 
            (reels[1] == '🐯' and reels[2] == '🐯') or 
            (reels[0] == '🐯' and reels[2] == '🐯')):
            return self.tigrinho_bet * 3
        
        # Dois iguais
        if reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
            return self.tigrinho_bet * 1.5
        
        # Símbolo especial
        if special_symbol:
            return self.tigrinho_bet * 2
        
        return 0
        
    def reload_balance(self):
        self.money = 1000.0
        self.update_display()
        messagebox.showinfo("Recarregado", "Saldo recarregado para R$ 1.000,00!")
        
    def show_payment_modal(self):
        # Create payment window
        payment_window = tk.Toplevel(self.root)
        payment_window.title("Sistema de Pagamento")
        payment_window.geometry("500x600")
        payment_window.configure(bg=self.colors['card_bg'])
        payment_window.resizable(False, False)
        
        # Center the window
        payment_window.transient(self.root)
        payment_window.grab_set()
        
        # Header
        tk.Label(
            payment_window,
            text="💳 SISTEMA DE PAGAMENTO",
            font=('Arial Black', 18, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(20, 30))
        
        # Tab buttons
        tab_frame = tk.Frame(payment_window, bg=self.colors['card_bg'])
        tab_frame.pack(fill='x', padx=20)
        
        self.payment_tab = tk.StringVar(value="redeem")
        
        tk.Radiobutton(
            tab_frame,
            text="💳 Resgatar Código",
            variable=self.payment_tab,
            value="redeem",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg'],
            selectcolor=self.colors['card_bg'],
            command=self.switch_payment_tab
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            tab_frame,
            text="🔑 Gerar Códigos",
            variable=self.payment_tab,
            value="generate",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg'],
            selectcolor=self.colors['card_bg'],
            command=self.switch_payment_tab
        ).pack(side=tk.LEFT)
        
        # Content frame
        self.payment_content = tk.Frame(payment_window, bg=self.colors['card_bg'])
        self.payment_content.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Initialize with redeem tab
        self.show_redeem_tab()
        
    def switch_payment_tab(self):
        # Clear content
        for widget in self.payment_content.winfo_children():
            widget.destroy()
            
        if self.payment_tab.get() == "redeem":
            self.show_redeem_tab()
        else:
            self.show_generate_tab()
            
    def show_redeem_tab(self):
        # Redeem code input
        tk.Label(
            self.payment_content,
            text="Código de Resgate:",
            font=('Arial', 12, 'bold'),
            fg=self.colors['gold'],
            bg=self.colors['card_bg']
        ).pack(pady=(0, 10))
        
        self.redeem_code_entry = tk.Entry(
            self.payment_content,
            font=('Arial', 14),
            width=30,
            justify='center'
        )
        self.redeem_code_entry.pack(pady=(0, 20))
        
        # Redeem button
        tk.Button(
            self.payment_content,
            text="RESGATAR CÓDIGO",
            command=self.redeem_code,
            font=('Arial Black', 12, 'bold'),
            bg=self.colors['success'],
            fg='white',
            relief='raised',
            bd=3,
            width=20
        ).pack()
        
    def show_generate_tab(self):
        # Info text
        tk.Label(
            self.payment_content,
            text="Gere códigos de resgate para adicionar dinheiro ao seu saldo.",
            font=('Arial', 11),
            fg='white',
            bg=self.colors['card_bg'],
            wraplength=400
        ).pack(pady=(0, 20))
        
        tk.Label(
            self.payment_content,
            text="Os códigos são salvos automaticamente em um arquivo .txt",
            font=('Arial', 11),
            fg='white',
            bg=self.colors['card_bg'],
            wraplength=400
        ).pack(pady=(0, 30))
        
        # Generate button
        tk.Button(
            self.payment_content,
            text="GERAR NOVO CÓDIGO",
            command=self.generate_redeem_code,
            font=('Arial Black', 12, 'bold'),
            bg=self.colors['purple'],
            fg='white',
            relief='raised',
            bd=3,
            width=20
        ).pack()
        
        # Result display
        self.code_result_frame = tk.Frame(self.payment_content, bg=self.colors['card_bg'])
        self.code_result_frame.pack(pady=(30, 0))
        
    def generate_redeem_code(self):
        import random
        import string
        
        # Generate code
        code = 'CASINO' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        amount = random.randint(100, 1000)  # R$ 100 to R$ 1000
        
        # Save to file
        self.save_redeem_code_to_file(code, amount)
        
        # Show result
        for widget in self.code_result_frame.winfo_children():
            widget.destroy()
            
        tk.Label(
            self.code_result_frame,
            text="🎉 Código Gerado com Sucesso!",
            font=('Arial Black', 14, 'bold'),
            fg=self.colors['success'],
            bg=self.colors['card_bg']
        ).pack(pady=(0, 15))
        
        tk.Label(
            self.code_result_frame,
            text=f"Código: {code}",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg=self.colors['card_bg']
        ).pack()
        
        tk.Label(
            self.code_result_frame,
            text=f"Valor: R$ {amount:.2f}",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg=self.colors['card_bg']
        ).pack(pady=(5, 15))
        
        tk.Label(
            self.code_result_frame,
            text="O código foi salvo no arquivo 'codigos_resgate.txt'",
            font=('Arial', 10),
            fg=self.colors['gold'],
            bg=self.colors['card_bg'],
            wraplength=300
        ).pack()
        
    def save_redeem_code_to_file(self, code, amount):
        try:
            with open('codigos_resgate.txt', 'a', encoding='utf-8') as f:
                f.write(f"{code} - R$ {amount:.2f} - DISPONÍVEL\n")
            messagebox.showinfo("Sucesso", f"Código {code} salvo no arquivo!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar código: {e}")
            
    def redeem_code(self):
        code = self.redeem_code_entry.get().strip().upper()
        if not code:
            messagebox.showerror("Erro", "Por favor, insira um código de resgate!")
            return
            
        # In a real application, you would validate against stored codes
        # For now, we'll simulate with a simple validation
        if code.startswith('CASINO') and len(code) == 14:
            # Simulate adding money (random amount between 100-1000)
            import random
            amount = random.randint(100, 1000)
            self.money += amount
            self.update_display()
            
            messagebox.showinfo("Sucesso", f"🎉 Código resgatado com sucesso! Adicionado R$ {amount:.2f} ao seu saldo!")
            self.redeem_code_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "❌ Código inválido!")
        
    def update_display(self):
        self.balance_label.config(text=f"R$ {self.money:.2f}")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    print("🎰 Iniciando Casino Brasileiro Premium...")
    casino = CasinoBrasileiro()
    casino.run()
