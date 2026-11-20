"""Genera el sitio estático de los laboratorios de las secciones 4 y 5.
Uso: python3 fuente/site.py   (crea la carpeta ../sitio lista para subir a GitHub Pages)"""
import os,shutil,sys
D=os.path.dirname(os.path.abspath(__file__))
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(D),'sitio')
USER='jayutomas623'; REPO='redes-neuronales'
BASE=f'https://{USER}.github.io/{REPO}'
# (archivo fuente, ruta corta, sección, título, descripción, color, emoji)
LABS=[("4-1-piramide","c1","piramide","4.1","Sube la pirámide del dato","Transforma datos sueltos de La Paz en información, conocimiento y sabiduría.","#7C3AED","🔺"),
("4-2-tipos-de-datos","c1","tipos-de-datos","4.2","¿Número o cantidad? Clasifica los datos","Ordena el archivador y comprueba por qué un carnet no es una cantidad.","#0E7490","🗄️"),
("4-4-cinco-v","c1","cinco-v","4.4","Las 5V y el conteo repartido","Reconoce las 5V del Big Data y reparte un conteo entre varias computadoras.","#C2410C","🖥️"),
("5-2-limpieza","c1","limpieza","5.2","Lava los datos como la quinua","Encuentra duplicados, vacíos, imposibles y extremos en la tabla cruda.","#15803D","🫧"),
("5-3-transformacion","c1","transformacion","5.3","Convierte palabras en números","Codifica el transporte con one-hot y escala los tiempos entre 0 y 1.","#1D4ED8","🔢"),
("5-6-graficos","c1","graficos","5.6","El gráfico que miente","Mueve el eje, elige el gráfico correcto y arregla uno mal hecho.","#BE123C","📊"),
("11-4-etiquetas","c2","etiquetas","11.4","¿Quién le enseña a la red?","Etiqueta hojas de papa y mira qué aprende una neurona con etiquetas malas.","#A16207","🍃"),
("11-6-cuaderno","c2","cuaderno","11.6","Prepara un dataset real","Un cuaderno de Google Colab con 344 pingüinos de la Antártida.","#0F766E","🐧"),
("14-1-digitos","c2","digitos","14.1","Dibuja un número y mira qué piensa la red","Una red ya entrenada frente a tu letra, una llama y un cuadro negro.","#9333EA","✍️"),
("14-5-cuaderno","c2","cuaderno-digitos","14.5","Una red que lee números escritos a mano","Un cuaderno de Google Colab: usar, medir la confianza y decidir.","#7C3AED","📒"),
("17-1-tipos-de-redes","c2","tipos-de-redes","17.1","¿Qué red usarías?","Cinco familias de redes y ocho problemas reales para elegir.","#0369A1","🧩")]
head=open(D+'/head.html').read().strip(); css=open(D+'/common.css').read(); js=open(D+'/common.js').read()
def page(s,desc="Laboratorio interactivo del libro Redes Neuronales en Mortales"):
    s=s.replace('<!--HEAD-->',head).replace('/*COMMON*/',css).replace('/*COMMONJS*/',js)
    return f'<!doctype html>\n<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="{desc}"><meta name="theme-color" content="#F2F5FB"></head><body>{s}</body></html>\n'
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(f'{OUT}/c1'); os.makedirs(f'{OUT}/c2')
R=f'/{REPO}'
for k,(src,cd,slug,sec,title,desc,col,em) in enumerate(LABS):
    s=open(f'{D}/{src}.html').read()
    prev=LABS[k-1] if k>0 else None; nxt=LABS[k+1] if k<len(LABS)-1 else None
    st='class="btn" style="text-decoration:none;display:inline-flex;align-items:center"'
    nav='<nav class="row" style="justify-content:space-between;gap:10px" aria-label="Otros laboratorios">'
    nav+=(f'<a {st} href="{R}/{prev[1]}/{prev[2]}/">← {prev[3]}</a>' if prev else '<span></span>')
    nav+=f'<a {st} href="{R}/">Todos los laboratorios</a>'
    nav+=(f'<a {st} href="{R}/{nxt[1]}/{nxt[2]}/">{nxt[3]} →</a>' if nxt else '<span></span>')+'</nav>'
    s=s.replace('<!--NAV-->',nav)
    os.makedirs(f'{OUT}/{cd}/{slug}')
    open(f'{OUT}/{cd}/{slug}/index.html','w').write(page(s,f'Laboratorio {sec}: {desc}'))
card=lambda L:f'    <a class="lab" href="{R}/{L[1]}/{L[2]}/" style="--c:{L[6]}"><span class="em" aria-hidden="true">{L[7]}</span><span class="tag">Laboratorio {L[3]}</span><b>{L[4]}</b><span class="d">{L[5]}</span><span class="go">Entrar →</span></a>'
hub=open(D+'/hub.html').read()
grp=lambda p:"\n".join(card(L) for L in LABS if L[3].split('.')[0]==p)
H=page(hub.replace('<!--LABS4-->',grp('4')).replace('<!--LABS5-->',grp('5')).replace('<!--LABS11-->',grp('11')).replace('<!--LABS14-->',grp('14')).replace('<!--LABS17-->',grp('17')))
for f in ['index.html','c1/index.html','c2/index.html']: open(f'{OUT}/{f}','w').write(H)
nf=page(f'<title>Página no encontrada</title><!--HEAD--><style>/*COMMON*/</style><main class="wrap"><div data-chispa="sad" class="chispa"></div><h1>Esta página no existe</h1><p class="lede">Quizá la dirección se escribió con un error. Revisa la dirección impresa bajo el QR o entra a la lista de laboratorios.</p><a class="btn primary" style="text-decoration:none;width:max-content;display:inline-flex;align-items:center" href="/{REPO}/c1/">Ver los laboratorios</a></main><script>/*COMMONJS*/</script>')
open(f'{OUT}/404.html','w').write(nf)
open(f'{OUT}/.nojekyll','w').write('')
open(f'{OUT}/README.md','w').write("# Redes Neuronales en Mortales · Laboratorios de las secciones 4, 5, 11, 14 y 17.1\n\nLaboratorios interactivos enlazados desde los códigos QR del libro *Redes Neuronales en Mortales*.\n\nSitio: "+BASE+"/\n\n| Sección | Laboratorio | Dirección |\n|---|---|---|\n"+"\n".join(f"| {L[3]} | {L[4]} | {BASE}/{L[1]}/{L[2]}/ |" for L in LABS)+"\n\nPáginas HTML estáticas, sin servidor ni recolección de datos. El código fuente está en `fuente/` (ejecuta `python3 fuente/site.py`).\n\n**No cambies las direcciones `c1/...`, `c2/...` ni `cuadernos/...`: están impresas en el libro.**\n")
shutil.copytree(D,f'{OUT}/fuente',ignore=shutil.ignore_patterns('__pycache__'))
shutil.copytree(os.path.join(os.path.dirname(D),'cuadernos'),f'{OUT}/cuadernos')
print("ok",BASE,[L[1] for L in LABS])
