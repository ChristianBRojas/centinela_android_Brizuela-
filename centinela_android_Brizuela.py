import os
import time
import sys

def limpiar_pantalla():
    os.system('clear')

def banner():
    print("=" * 45)
    print("      🛡️  ASISTENTE DE CIBERSEGURIDAD 🛡️      ")
    print("        Auditor de Amenazas para Android      ")
    print("=" * 45)

def escanear_sistema():
    limpiar_pantalla()
    banner()
    print("\n[+] Iniciando análisis de entorno local...")
    time.sleep(1)
    
    # Usamos el directorio actual ('.') para no necesitar permisos externos
    ruta_local = "."
    
    archivos_peligrosos = 0
    extensiones_riesgo = ['.apk', '.exe', '.sh', '.bat']
    
    print(f"🔍 Escaneando carpeta del proyecto: {os.path.abspath(ruta_local)}...")
    time.sleep(0.5)
    
    try:
        archivos = os.listdir(ruta_local)
        if not archivos:
            print("📂 La carpeta está limpia de archivos temporales.")
        for archivo in archivos:
            if any(archivo.endswith(ext) for ext in extensiones_riesgo):
                print(f"⚠️  ALERTA: Archivo ejecutable de riesgo detectado: {archivo}")
                archivos_peligrosos += 1
            else:
                print(f"📄 Archivo seguro analizado: {archivo}")
    except Exception as e:
        print(f"❌ Error inesperado al leer la carpeta: {e}")
            
    print("\n[+] Análisis finalizado.")
    if archivos_peligrosos > 0:
        print(f"🚨 RESULTADO: ¡Atención! Se encontraron {archivos_peligrosos} ejecutables en este directorio.")
    else:
        print("✅ RESULTADO: El entorno de ejecución local está completamente seguro.")
    
    input("\nPresiona Enter para continuar...")

def auditor_permisos():
    limpiar_pantalla()
    banner()
    print("\n🔍 AUDITORÍA DE PERMISOS ABUSIVOS")
    print("El malware usa ciertos permisos para espiarte o robarte dinero.")
    print("-" * 45)
    
    permisos = {
        "Accesibilidad": "¿Tienes apps de origen desconocido con este permiso activo? (El malware lo usa para controlar tu pantalla de forma remota).",
        "SMS": "¿Alguna app de juegos o herramientas te pide leer tus SMS? (Peligro: pueden robar tus claves bancarias).",
        "Administrador de Dispositivo": "¿Hay apps extrañas aquí? (Esto evita que las puedas desinstalar de forma normal).",
        "Aparecer encima": "¿Notas publicidad flotante en tu pantalla? Hay una app con este permiso que te inunda de anuncios."
    }
    
    for perm, descripcion in permisos.items():
        print(f"\n📌 Permiso: {perm}")
        print(descripcion)
        rpta = input("¿Sospechas de alguna app con este permiso en tu celu? (s/n): ").strip().lower()
        if rpta == 's':
            print("💡 RECOMENDACIÓN: Ve a Ajustes > Aplicaciones > Accesos especiales y desactívalo de inmediato.")
            time.sleep(2)
            
    input("\nAuditoría terminada. Presiona Enter para volver...")

def detector_phishing():
    limpiar_pantalla()
    banner()
    print("\n🎣 ANALIZADOR DE ENLACES (ANTI-PHISHING)")
    print("Pega aquí el enlace (URL) sospechoso que recibiste por SMS o WhatsApp:")
    url = input("👉 URL a analizar: ").strip().lower()
    
    if not url:
        return

    print("\n[+] Analizando estructura del enlace...")
    time.sleep(1.5)
    
    alertas = 0
    remplazos_falsos = ["banco", "netflix", "correos", "soporte", "seguridad", "actualizar", "regalo", "visa", "mastercard"]
    
    if "https" not in url:
        print("❌ ALERTA: El sitio no usa cifrado seguro (HTTP). Es altamente peligroso.")
        alertas += 1
        
    if "@" in url:
        print("❌ ALERTA: La URL contiene un carácter '@'. Es un truco clásico para camuflar páginas falsas.")
        alertas += 1
        
    for palabra in remplazos_falsos:
        if palabra in url and not (url.endswith(f"{palabra}.com") or url.endswith(f"{palabra}.cl") or url.endswith(f"{palabra}.org")):
            print(f"⚠️  SOSPECHA: El enlace menciona '{palabra}' pero el dominio web no parece ser el oficial.")
            alertas += 1
            
    if alertas >= 2:
        print("\n🚨 DICTAMEN: ¡ALTO RIESGO! Este enlace comparte el patrón de una campaña de Phishing. ¡No entres!")
    elif alertas == 1:
        print("\n⚠️  DICTAMEN: SOSPECHOSO. Procede con cuidado y verifica con los canales oficiales.")
    else:
        print("\n✅ DICTAMEN: No se detectaron anomalías evidentes de Phishing automático.")
        
    input("\nPresiona Enter para continuar...")

while True:
    limpiar_pantalla()
    banner()
    print("\n1. Escanear directorio local (Buscar archivos de riesgo)")
    print("2. Auditar permisos peligrosos del celular")
    print("3. Analizar enlace sospechoso (Anti-Phishing)")
    print("4. Salir del Asistente")
    
    opcion = input("\nSelecciona una opción (1-4): ").strip()
    
    if opcion == "1":
        escanear_sistema()
    elif opcion == "2":
        auditor_permisos()
    elif opcion == "3":
        detector_phishing()
    elif opcion == "4":
        print("\nCerrando sistemas de defensa. ¡Mantente seguro, mi general!")
        sys.exit()
