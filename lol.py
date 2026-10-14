import sys
import os
import re
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

# Zabezpecenie utf-8 vystupu na Windows konzole
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Cesty
BASE_DIR = r"C:\Users\Alex\Desktop\do client\kda-mod"
LOG_FILE = os.path.join(BASE_DIR, "lol.txt")
TARGET_BASE = os.path.join(BASE_DIR, "spacemap")  # Výsledok: C:\Users\Alex\Desktop\do client\kda-mod\spacemap\spacemap\...

REMOTE_BASE_URL = "https://unsmod.eu/"
MAX_WORKERS = 10  # Počet paralelných sťahovaní

def extract_missing_assets(log_path):
    """
    Nájde všetky linky / assety v lol.txt (čisté URL, pôvodné GET ... 404 záznamy,
    aj URL s query parametrami) a extrahuje relatívnu cestu a cieľovú unsmod URL.
    """
    if not os.path.exists(log_path):
        print(f"Súbor {log_path} nebol nájdený!")
        return []

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Hľadáme akékoľvek http/https linky v súbore
    url_pattern = re.compile(r'https?://[^\s"\'<>]+')
    matches = url_pattern.findall(content)

    assets = []
    seen_rel_paths = set()

    for url in matches:
        # Odstránime interpunkciu na konci (zátvorky, čiarky a pod.)
        clean_url = url.rstrip(').,;\'">')
        parsed = urllib.parse.urlparse(clean_url)
        clean_path = re.sub(r'/+', '/', parsed.path).lstrip('/')

        if 'spacemap/' in clean_path:
            idx = clean_path.find('spacemap/')
            rel_path = clean_path[idx:]
        elif any(clean_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.json', '.ogg', '.mp3', '.wav', '.svg']):
            rel_path = clean_path
        else:
            continue

        # Preskočíme prázdne cesty alebo adresáre
        if not rel_path or rel_path.endswith('/'):
            continue

        # Deduplikácia podľa relatívnej cesty súboru
        if rel_path in seen_rel_paths:
            continue
        seen_rel_paths.add(rel_path)

        unsmod_url = urllib.parse.urljoin(REMOTE_BASE_URL, rel_path)
        local_path = os.path.normpath(os.path.join(TARGET_BASE, rel_path))

        assets.append({
            "original_url": url,
            "download_url": unsmod_url,
            "rel_path": rel_path,
            "local_path": local_path
        })

    return assets

def download_asset(asset, session):
    download_url = asset["download_url"]
    local_path = asset["local_path"]

    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        return "EXIST", asset, None

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    try:
        r = session.get(download_url, timeout=15)
        if r.status_code == 200 and r.content:
            with open(local_path, "wb") as f:
                f.write(r.content)
            return "SUCCESS", asset, len(r.content)
        else:
            return "HTTP_ERROR", asset, r.status_code
    except Exception as e:
        return "EXCEPTION", asset, str(e)

def main():
    print(f"=== Hľadanie chýbajúcich assetov v {LOG_FILE} ===")
    assets = extract_missing_assets(LOG_FILE)
    print(f"Nájdených unikátnych spacemap assetov: {len(assets)}\n")

    if not assets:
        print("Neboli nájdené žiadne assety na stiahnutie.")
        return

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })

    downloaded = 0
    skipped = 0
    failed = 0

    print("=== Začínam sťahovanie ===")
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(download_asset, asset, session) for asset in assets]

        for future in as_completed(futures):
            status, asset, info = future.result()
            rel = asset["rel_path"]

            if status == "SUCCESS":
                downloaded += 1
                print(f"[OK 200] Stiahnuté: {rel} ({info} B)")
            elif status == "EXIST":
                skipped += 1
                print(f"[SKIP] Už existuje: {rel}")
            elif status == "HTTP_ERROR":
                failed += 1
                print(f"[CHYBA {info}] {asset['download_url']}")
            elif status == "EXCEPTION":
                failed += 1
                print(f"[ZLYHALO] {asset['download_url']} - {info}")

    print("\n=== ZHRNUTIE ===")
    print(f"Celkovo nájdených: {len(assets)}")
    print(f"Úspešne stiahnutých: {downloaded}")
    print(f"Už existovalo:       {skipped}")
    print(f"Neúspešných (404...): {failed}")
    print(f"Cieľový priečinok:   {TARGET_BASE}")

if __name__ == "__main__":
    main()
