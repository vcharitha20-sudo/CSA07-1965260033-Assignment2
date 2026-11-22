"""Synchronous Bellman-Ford distance vector."""
INF=99
names='PQRST'
cost={('P','Q'):4,('P','R'):1,('Q','R'):2,('Q','S'):6,('R','S'):3,('S','T'):5}

def run(edges):
    link={}
    for (u,v),c in edges.items():link[u,v]=link[v,u]=c
    table={u:{v:(0 if u==v else link.get((u,v),INF)) for v in names} for u in names}
    hop={u:{v:(v if (u,v) in link else '-') for v in names} for u in names}
    rounds=0
    while True:
        rounds+=1; old={u:dict(table[u]) for u in names}; changed=False
        for u in names:
            for n in names:
                if link.get((u,n),INF)>=INF:continue
                for dest in names:
                    candidate=link[u,n]+old[n][dest]
                    if candidate<table[u][dest]:
                        table[u][dest]=candidate;hop[u][dest]=n;changed=True
        if not changed:break
    print(f'converged after {rounds} rounds')
    for u in names:print(u,' '.join(f'{table[u][v]:2d}' for v in names))
    print('forwarding table of P:')
    for v in names[1:]:print(f' to {v}: cost {table["P"][v]}, next hop {hop["P"][v]}')

print('ORIGINAL');run(cost)
print('R-S LINK FAILED');changed=dict(cost);changed[('R','S')]=INF;run(changed)
