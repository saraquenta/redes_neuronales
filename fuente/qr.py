"""QR estáticos de respaldo (no caducan). Uso: python3 fuente/qr.py carpeta_salida"""
import segno,os,sys
BASE='https://saraquenta.github.io/redes_neuronales'
SLUGS=[("14.1","c2/digitos"),("14.5","c2/cuaderno-digitos"),("17.1","c2/tipos-de-redes")]
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
for sec,slug in SLUGS:
    u=f"{BASE}/{slug}/"; n=f"qr-{sec.replace('.','-')}-{slug.split('/')[1]}"
    q=segno.make(u,error='q')
    q.save(f"{OUT}/{n}.svg",scale=10,border=4,dark='#0A2540',xmldecl=False)
    q.save(f"{OUT}/{n}.png",scale=24,border=4,dark='#0A2540')
    print(n,u)
