import os
import json
import urllib.request

# ⬇️ SEM vlož JSON ako string
json_string = '''{

    "1": {
        "1": {
            "name": "G-Enforcer",
            "icon": "genforcer",
            "desc": "genforcer_shop_desc"
        },
        "2": {
            "name": "G-Bastion",
            "icon": "gbastion",
            "desc": "gbastion_shop_desc"
        },
        "3": {
            "name": "V-Revenger",
            "icon": "vrevenger",
            "desc": "vrevenger_shop_desc"
        },
        "4": {
            "name": "V-Avenger",
            "icon": "vavenger",
            "desc": "vavenger_shop_desc"
        },
        "5": {
            "name": "Vengeance",
            "icon": "vengeance",
            "desc": "vengeance_shop_desc"
        },
        "6": {
            "name": "Phoenix",
            "icon": "phoenix",
            "desc": "phoenix_shop_desc"
        },
        "7": {
            "name": "Yamato",
            "icon": "yamato",
            "desc": "yamato_shop_desc"
        },
        "8": {
            "name": "Defcom",
            "icon": "defcom",
            "desc": "defcom_shop_desc"
        },
        "9": {
            "name": "Leonov",
            "icon": "leonov",
            "desc": "leonov_shop_desc"
        },
        "10": {
            "name": "Liberator",
            "icon": "liberator",
            "desc": "liberator_shop_desc"
        },
        "11": {
            "name": "Piranha",
            "icon": "piranha",
            "desc": "piranha_shop_desc"
        },
        "12": {
            "name": "Nostormo",
            "icon": "nostromo",
            "desc": "nostromo_shop_desc"
        },
        "13": {
            "name": "BigBoy",
            "icon": "bigboy",
            "desc": "bigboy_shop_desc"
        },
        "14": {
            "name": "Goliath",
            "icon": "goliath",
            "desc": "goliath_shop_desc"
        },
        "15": {
            "name": "V-Honor",
            "icon": "vhonor",
            "desc": "vhonor_shop_desc"
        },
        "16": {
            "name": "V-Experience",
            "icon": "vexp",
            "desc": "vexp_shop_desc"
        },
        "17": {
            "name": "G-Experience",
            "icon": "gexp",
            "desc": "gexp_shop_desc"
        },
        "18": {
            "name": "G-Honor",
            "icon": "ghon",
            "desc": "ghon_shop_desc"
        },
        "19": {
            "name": "G-Goal",
            "icon": "goal",
            "desc": "goal_shop_desc"
        },
        "20": {
            "name": "G-Kick",
            "icon": "kick",
            "desc": "kick_shop_desc"
        },
        "21": {
            "name": "G-Referee",
            "icon": "referee",
            "desc": "referee_shop_desc"
        },
        "22": {
            "name": "G-Independence",
            "icon": "american",
            "desc": "american_shop_desc"
        },
        "23": {
            "name": "G-Spectrum",
            "icon": "spectrum",
            "desc": "spectrum_shop_desc"
        },
        "24": {
            "name": "G-Solace",
            "icon": "solace",
            "desc": "solace_shop_desc"
        },
        "25": {
            "name": "G-Venom",
            "icon": "venom",
            "desc": "venom_shop_desc"
        },
        "26": {
            "name": "G-Diminisher",
            "icon": "diminisher",
            "desc": "diminisher_shop_desc"
        },
        "27": {
            "name": "G-Sentinel",
            "icon": "sentinel",
            "desc": "sentinel_shop_desc"
        },
        "28": {
            "name": "G-Turkey",
            "icon": "gturkey",
            "desc": "gturkey_shop_desc"
        },
        "29": {
            "name": "V-Lightning",
            "icon": "vlight",
            "desc": "vlight_shop_desc"
        },
        "30": {
            "name": "V-Pusat",
            "icon": "pusat",
            "desc": "pusat_shop_desc"
        },
        "31": {
            "name": "G-Surgeon",
            "icon": "surgeon",
            "desc": "surgeon_shop_desc"
        },
        "78": {
            "name": "G-Vanquisher",
            "icon": "vanquisher",
            "desc": "gvanquisher_shop_desc"
        },
        "79": {
            "name": "G-Sovereign",
            "icon": "sovereign",
            "desc": "gsovereign_shop_desc"
        },
        "80": {
            "name": "G-Peacemaker",
            "icon": "peacemaker",
            "desc": "gpeacemaker_shop_desc"
        },
        "81": {
            "name": "G-Saturn",
            "icon": "saturn",
            "desc": "saturn_shop_desc"
        },
        "82": {
            "name": "G-Germany",
            "icon": "ggerman",
            "desc": "ggerman_shop_desc"
        },
        "83": {
            "name": "G-Referee",
            "icon": "referee",
            "desc": "referee_shop_desc"
        },
        "91": {
            "name": "G-Bronze",
            "icon": "bronze",
            "desc": "bronzeshop_desc"
        },
        "92": {
            "name": "G-Silver",
            "icon": "silver",
            "desc": "silver_shop_desc"
        },
        "93": {
            "name": "G-Gold",
            "icon": "gold",
            "desc": "gold_shop_desc"
        },
        "94": {
            "name": "G-Space",
            "icon": "space",
            "desc": "gspace_shop_desc"
        },
        "95": {
            "name": "G-RGB",
            "icon": "rgbg",
            "desc": "rgbg_shop_desc"
        },
        "106": {
            "name": "N-Starhawk",
            "icon": "nenvoy",
            "desc": "nstarhawk_shop_desc"
        },
        "107": {
            "name": "G-Tech",
            "icon": "gtech",
            "desc": "gtech_shop_desc"
        },
        "109": {
            "name": "Tartarus",
            "icon": "lspacefire",
            "desc": "lspacefire_shop_desc"
        },
        "110": {
            "name": "V-Referee",
            "icon": "vreferee",
            "desc": "vreferee_shop_desc"
        },
        "111": {
            "name": "V-Kick",
            "icon": "vkick",
            "desc": "vkick_shop_desc"
        },
        "112": {
            "name": "V-Goal",
            "icon": "vgoal",
            "desc": "vgoal_shop_desc"
        },
        "115": {
            "name": "G-Nightmare",
            "icon": "gpumpkinplayer",
            "desc": "gpumpkinplayer_shop_desc"
        },
        "119": {
            "name": "G-Czech",
            "icon": "gzech",
            "desc": "gzech_shop_desc"
        },
        "120": {
            "name": "G-Poland",
            "icon": "gpoland",
            "desc": "gpoland_shop_desc"
        },
        "121": {
            "name": "G-England",
            "icon": "gengland",
            "desc": "gengland_shop_desc"
        },
        "122": {
            "name": "G-France",
            "icon": "gfrance",
            "desc": "gfrance_shop_desc"
        },
        "123": {
            "name": "G-Belgium",
            "icon": "gbelgium",
            "desc": "gbelgium_shop_desc"
        },
        "124": {
            "name": "V-Zeus",
            "icon": "vzeus",
            "desc": "vzeus_shop_desc"
        },
        "125": {
            "name": "V-Toxic",
            "icon": "vzeus",
            "desc": "vzeus_shop_desc"
        },
        "128": {
            "name": "G-Frosty",
            "icon": "gfrozen",
            "desc": "gfrozen_shop_desc"
        },
        "129": {
            "name": "V-Frosty",
            "icon": "vfrozen",
            "desc": "vfrozen_shop_desc"
        },
        "132": {"name": "G-Spectrum-Frosty", "icon": "spectrum_frost", "desc": "spectrum_shop_desc"},
        "133": {
            "name": "G-Ignite",
            "icon": "ignite",
            "desc": "ignitet_shop_desc"
          }
          ,
          "134": {
            "name": "G-Red",
            "icon": "redg",
            "desc": "redg_shop_desc"
          }
          ,
          "135": {
            "name": "G-Orange",
            "icon": "orangeg",
            "desc": "orangeg_shop_desc"
          }
          ,
          "136": {
            "name": "G-Blue",
            "icon": "blueg",
            "desc": "blueg_shop_desc"
          }
          ,
          "137": {
            "name": "G-SolaceFrosty",
            "icon": "solaceFrosty",
            "desc": "solaceFrosty_shop_desc"
          }
          ,
          "138": {
            "name": "G-DiminisherFrosty",
            "icon": "diminisherFrosty",
            "desc": "diminisherFrosty_shop_desc"
          },
          "139": {"name": "G-Love", "icon": "glove", "desc": "glove_shop_desc"},
          "146": {"name": "G-V0-RGB", "icon": "venomrgb", "desc": "venomrgb_shop_desc"},
          "148": { "name": "Venom-Frosty", "icon": "venomfrozen", "desc": "venomfrosty_shop_desc" },
          "149": { "name": "Sentinel-Frosty", "icon": "sentinelfrozen", "desc": "sentinelfrozen_shop_desc" },
          "151": { "name": "Sentinel-Gold", "icon": "sentinelgold", "desc": "sentinelgold_shop_desc" },
          "152": { "name": "Goliath-Gold", "icon": "ganniversary", "desc": "ganniversary_shop_desc" },
          "153": { "name": "Solace-Gold", "icon": "solacegold", "desc": "solacegold_shop_desc" },
          "154": { "name": "Diminisher-Gold", "icon": "dimigold", "desc": "dimigold_shop_desc" },
          "155": { "name": "Spectrum-Gold", "icon": "specgold", "desc": "specgold_shop_desc" },
          "156": { "name": "Venom-Gold", "icon": "venomgold", "desc": "venomgold_shop_desc" },
          "160": { "name": "Veng-Gold", "icon": "venggold", "desc": "vgold_shop_desc" },
          "163": { "name": "Phoenix Champion", "icon": "phoenixchamp", "desc": "phoenixchamp_shop_desc" },
          "164": { "name": "G-Sakura", "icon": "gsakura", "desc": "gsakura_shop_desc" },
          "173": { "name": "G-inferno", "icon": "ginferno", "desc": "ginferno_shop_desc" },
          "175": { "name": "G-Pirate", "icon": "gpirate", "desc": "ginfiltrator_shop_desc" }
    }

}'''




data = json.loads(json_string)

# Lokálny adresár kde majú byť shop obrázky
shop_img_path = r"C:\Users\Alex\Desktop\kda-mod\kda-mod\spacemap\spacemap\image\shopImg\1"
# URL zdroj
shop_img_url = "https://ariaom.com/spacemap/image/shopImg/1/"

# Prejdi všetky "ikony"
for section in data.values():
    for ship in section.values():
        icon = ship.get("icon", "").strip()
        if not icon:
            continue

        downloaded = False

        # Skús najprv .webp, potom .png
        for ext in [".webp", ".png"]:
            image_filename = f"{icon}{ext}"
            image_dest = os.path.join(shop_img_path, image_filename)
            image_url = shop_img_url + image_filename

            if not os.path.exists(image_dest):
                try:
                    urllib.request.urlretrieve(image_url, image_dest)
                    print(f"[OK] Stiahnuté: {image_filename}")
                    downloaded = True
                    break
                except Exception as e:
                    print(f"[WARN] {image_filename} sa nepodarilo: {e}")
            else:
                print(f"[SKIP] Už existuje: {image_filename}")
                downloaded = True
                break

        # DETAIL GIF
        detail_filename = f"{icon}_detail.gif"
        detail_dest = os.path.join(shop_img_path, detail_filename)
        detail_url = shop_img_url + detail_filename

        if not os.path.exists(detail_dest):
            try:
                urllib.request.urlretrieve(detail_url, detail_dest)
                print(f"[OK] Stiahnuté: {detail_filename}")
            except Exception as e:
                print(f"[WARN] {detail_filename} sa nepodarilo: {e}")
        else:
            print(f"[SKIP] Už existuje: {detail_filename}")