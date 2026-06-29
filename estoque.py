import heapq
import random

estoque = {}
heap_vendas = []

def adicionar_produto(codigo, nome, quantidade):
    if codigo not in estoque:
        estoque[codigo] = {"nome": nome, "quantidade": quantidade, "vendas": 0}
    else:
        estoque[codigo]["quantidade"] += quantidade

def vender_produto(codigo, quantidade):
    if codigo in estoque and estoque[codigo]["quantidade"] >= quantidade:
        estoque[codigo]["quantidade"] -= quantidade
        estoque[codigo]["vendas"] += quantidade
        heapq.heappush(heap_vendas, (-estoque[codigo]["vendas"], codigo))
    else:
        print(f"Venda não realizada: estoque insuficiente ou produto inexistente. Código: {codigo}")

def buscar_produto(codigo):
    return estoque.get(codigo, "Produto não encontrado.")

def top_vendidos(n=5):
    vistos=set()
    resultado=[]
    temp_heap=heap_vendas[:]
    heapq.heapify(temp_heap)
    while temp_heap and len(resultado)<n:
        vendas_neg,codigo=heapq.heappop(temp_heap)
        if codigo not in vistos:
            vistos.add(codigo)
            p=estoque[codigo]
            resultado.append((codigo,p["nome"],-vendas_neg))
    return resultado

nomes=["Arroz","Feijão","Macarrão","Óleo","Açúcar"]
for i in range(1000):
    adicionar_produto(f"P{i:04d}", random.choice(nomes)+f" {i}", random.randint(10,100))

for _ in range(5000):
    vender_produto(f"P{random.randint(0,999):04d}", random.randint(1,5))

print("Top 5 produtos mais vendidos:")
for c,n,v in top_vendidos():
    print(f"{c} - {n}: {v} vendas")
