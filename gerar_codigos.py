#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Códigos de Resgate para Casino
Gera códigos únicos e os salva em um arquivo .txt
"""

import random
import string
import os
from datetime import datetime

def gerar_codigo_resgate():
    """Gera um código de resgate único"""
    # Formato: CASINO + 8 caracteres aleatórios (letras e números)
    codigo = 'CASINO' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return codigo

def gerar_valor():
    """Gera um valor aleatório entre R$ 100 e R$ 1000"""
    return random.randint(100, 1000)

def salvar_codigos(quantidade=10):
    """Gera e salva códigos de resgate em um arquivo"""
    nome_arquivo = 'codigos_resgate.txt'
    
    # Cabeçalho do arquivo
    cabecalho = f"""🎰 CÓDIGOS DE RESGATE - FEUDAL BET 🎰
📅 Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
💰 Quantidade de códigos: {quantidade}
{'='*60}

"""
    
    # Gera códigos
    codigos = []
    for i in range(quantidade):
        codigo = gerar_codigo_resgate()
        valor = gerar_valor()
        codigos.append(f"{codigo} - R$ {valor:.2f} - DISPONÍVEL")
    
    # Salva no arquivo
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(cabecalho)
            for codigo in codigos:
                f.write(codigo + '\n')
        
        print(f"✅ {quantidade} códigos gerados e salvos em '{nome_arquivo}'")
        print(f"📁 Arquivo salvo em: {os.path.abspath(nome_arquivo)}")
        
        # Mostra alguns códigos gerados
        print("\n🔑 Códigos gerados:")
        for i, codigo in enumerate(codigos[:5], 1):
            print(f"  {i}. {codigo}")
        
        if len(codigos) > 5:
            print(f"  ... e mais {len(codigos) - 5} códigos")
            
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")

def main():
    print("🎰 GERADOR DE CÓDIGOS DE RESGATE 🎰")
    print("=" * 40)
    
    try:
        quantidade = input("Quantos códigos deseja gerar? (padrão: 10): ").strip()
        if not quantidade:
            quantidade = 10
        else:
            quantidade = int(quantidade)
            
        if quantidade <= 0:
            print("❌ Quantidade deve ser maior que 0!")
            return
            
        if quantidade > 100:
            print("⚠️  Quantidade muito alta! Limitando a 100 códigos.")
            quantidade = 100
            
    except ValueError:
        print("❌ Entrada inválida! Usando padrão de 10 códigos.")
        quantidade = 10
    
    print(f"\n🔄 Gerando {quantidade} códigos de resgate...")
    salvar_codigos(quantidade)
    
    print("\n🎉 Processo concluído!")
    print("💡 Use estes códigos no casino para adicionar dinheiro ao seu saldo!")

if __name__ == "__main__":
    main()

