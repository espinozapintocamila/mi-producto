"""Conteo de temas de product/data/2026-11-24-reviews-apps-plantas.csv. Uso: python3 -I este.py <csv>
Cada reseña lleva una o más etiquetas tema:tipo, puestas a mano; sin etiqueta = fuera de alcance."""
import csv, sys
from collections import Counter, defaultdict
T = """F-03 registro:usability idioma:complaint
F-04 consejos:praise
F-05 idioma:complaint consejos:complaint
F-06 idioma:complaint
F-07 consejos:complaint catalogo:complaint precio:complaint
F-08 riego:praise idioma:request consejos:request
F-10 registro:praise registro:request
F-11 precio:complaint riego:complaint consejos:complaint
F-13 catalogo:complaint
F-14 muertes:complaint idioma:complaint
F-15 catalogo:request
F-16 ficha:request
F-17 muertes:complaint
F-18 catalogo:request
F-19 registro:praise riego:praise consejos:praise
F-20 muertes:complaint
F-21 catalogo:complaint
F-22 precio:complaint consejos:complaint
F-23 fallas:bug
F-24 precio:complaint
F-25 consejos:complaint precio:complaint
F-26 riego:praise
F-27 riego:praise
F-28 idioma:complaint
F-29 precio:complaint
F-30 ficha:usability
F-31 precio:complaint
F-32 otros:request
F-33 precio:complaint
F-34 riego:praise
F-35 fallas:bug
F-36 fallas:bug
F-37 fallas:bug
F-38 fallas:bug
F-39 registro:praise riego:complaint
F-40 riego:complaint"""
tags = {l.split()[0]: [t.split(':') for t in l.split()[1:]] for l in T.splitlines()}
rows = {r['id']: r for r in csv.DictReader(open(sys.argv[1], encoding='utf-8'))}
assert set(tags) <= set(rows)
print('total', len(rows), '| dentro', len(tags), '| fuera', len(rows)-len(tags), sorted(set(rows)-set(tags)))
print('por app', dict(Counter(r['app'] for r in rows.values())), '| dentro por app', dict(Counter(rows[i]['app'] for i in tags)))
print('por pais', dict(Counter(r['pais'] for r in rows.values())), '| periodo', min(r['fecha'] for r in rows.values()), max(r['fecha'] for r in rows.values()))
print('estrellas', sorted(Counter(r['estrellas'] for r in rows.values()).items()), '| por año', sorted(Counter(r['fecha'][:4] for r in rows.values()).items()))
th = defaultdict(dict)
for i, ts in tags.items():
    for t, k in ts: th[t].setdefault(i, []).append(k)
for t, d in sorted(th.items(), key=lambda x: -len(x[1])):
    print(f"{t}: {len(d)} ({100*len(d)/len(tags):.0f}%) | tipos {dict(Counter(k for ks in d.values() for k in ks))} | apps {dict(Counter(rows[i]['app'] for i in d))} | desde 2025: {sum(rows[i]['fecha']>='2025' for i in d)} | {' '.join(d)}")
print('dentro desde 2025:', sum(rows[i]['fecha']>='2025' for i in tags))
