"""QR estáticos de respaldo (no caducan). Uso: python3 fuente/qr.py carpeta_salida"""
import segno,os,sys
BASE='https://jayutomas623.github.io/redes-neuronales'
SLUGS=[("4.1","c1/piramide"),("4.2","c1/tipos-de-datos"),("4.4","c1/cinco-v"),("5.2","c1/limpieza"),("5.3","c1/transformacion"),("5.6","c1/graficos"),("11.4","c2/etiquetas"),("11.6","c2/cuaderno"),("14.1","c2/digitos"),("14.5","c2/cuaderno-digitos"),("17.1","c2/tipos-de-redes")]
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
for sec,slug in SLUGS:
    u=f"{BASE}/{slug}/"; n=f"qr-{sec.replace('.','-')}-{slug.split('/')[1]}"
    q=segno.make(u,error='q')
    q.save(f"{OUT}/{n}.svg",scale=10,border=4,dark='#0A2540',xmldecl=False)
    q.save(f"{OUT}/{n}.png",scale=24,border=4,dark='#0A2540')
    print(n,u)
