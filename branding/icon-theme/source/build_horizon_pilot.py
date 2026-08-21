#!/usr/bin/env python3
"""Generate the original OBLinux Horizon Layer icon-theme pilot."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "pilot" / "OBLinux-Horizon"
SCALABLE = THEME / "scalable"

PALETTE = {
    "navy": "#111820",
    "slate": "#1B2836",
    "ocean": "#176B87",
    "cyan": "#4CC9D8",
    "white": "#F2F5F7",
    "amber": "#E5A84B",
    "green": "#35B98A",
    "red": "#DF5B61",
}


def svg(body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  <defs><linearGradient id="o" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#2385A2"/><stop offset="1" stop-color="{PALETTE['ocean']}"/></linearGradient></defs>
  {body}
</svg>\n'''


def folder(glyph: str = "", accent: str = PALETTE["cyan"]) -> str:
    return svg(f'''<path d="M8 31q0-9 9-9h31l11 11h52q9 0 9 9v65q0 9-9 9H17q-9 0-9-9z" fill="url(#o)"/>
  <path d="M8 54h112v53q0 9-9 9H17q-9 0-9-9z" fill="{PALETTE['slate']}" opacity=".34"/>
  <path d="M13 78c25-14 45 15 68 0 15-10 27-6 39-1" fill="none" stroke="{accent}" stroke-width="5" stroke-linecap="round"/>
  {glyph}''')


def tile(glyph: str, accent: str = PALETTE["cyan"]) -> str:
    return svg(f'''<rect x="10" y="10" width="108" height="108" rx="27" fill="{PALETTE['slate']}"/>
  {glyph.replace("ACCENT", accent)}''')


GLYPHS = {
    "home": '<path d="m35 66 29-25 29 25v31H73V76H55v21H35z" fill="#F2F5F7"/><path d="m29 65 35-30 35 30" fill="none" stroke="ACCENT" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    "desktop": '<rect x="28" y="31" width="72" height="52" rx="6" fill="none" stroke="#F2F5F7" stroke-width="7"/><path d="M51 99h26M64 84v15" stroke="ACCENT" stroke-width="7" stroke-linecap="round"/>',
    "documents": '<path d="M39 26h37l17 17v59H39z" fill="#F2F5F7"/><path d="M76 26v18h17M50 61h32M50 74h32M50 87h22" fill="none" stroke="ACCENT" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
    "downloads": '<path d="M64 28v47M45 59l19 19 19-19" fill="none" stroke="#F2F5F7" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 94h60" stroke="ACCENT" stroke-width="7" stroke-linecap="round"/>',
    "music": '<path d="M51 91V43l39-9v46" fill="none" stroke="#F2F5F7" stroke-width="7" stroke-linejoin="round"/><circle cx="42" cy="93" r="12" fill="ACCENT"/><circle cx="81" cy="82" r="12" fill="ACCENT"/>',
    "pictures": '<rect x="27" y="30" width="74" height="68" rx="8" fill="none" stroke="#F2F5F7" stroke-width="7"/><circle cx="77" cy="51" r="8" fill="ACCENT"/><path d="m34 88 20-22 14 14 10-10 16 18" fill="none" stroke="#F2F5F7" stroke-width="6" stroke-linejoin="round"/>',
    "videos": '<rect x="27" y="34" width="74" height="60" rx="9" fill="none" stroke="#F2F5F7" stroke-width="7"/><path d="m56 51 25 13-25 14z" fill="ACCENT"/>',
    "trash": '<path d="M39 43h50l-4 61H43zM34 36h60M52 36l4-12h16l4 12" fill="none" stroke="#F2F5F7" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M57 57v29M72 57v29" stroke="ACCENT" stroke-width="5" stroke-linecap="round"/>',
    "drive": '<rect x="26" y="33" width="76" height="62" rx="10" fill="#F2F5F7"/><path d="M34 70h60" stroke="#1B2836" stroke-width="6"/><circle cx="84" cy="82" r="6" fill="ACCENT"/><circle cx="66" cy="82" r="6" fill="#35B98A"/>',
    "usb": '<path d="M64 25v59M64 25l-10 12M64 25l10 12M64 53h25M89 53v-9M64 68H42v-9" fill="none" stroke="#F2F5F7" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="42" cy="55" r="7" fill="ACCENT"/><rect x="83" y="35" width="12" height="12" rx="2" fill="ACCENT"/><circle cx="64" cy="96" r="12" fill="ACCENT"/>',
    "network": '<circle cx="64" cy="64" r="13" fill="ACCENT"/><circle cx="34" cy="38" r="9" fill="#F2F5F7"/><circle cx="94" cy="38" r="9" fill="#F2F5F7"/><circle cx="64" cy="101" r="9" fill="#F2F5F7"/><path d="m42 45 13 12M86 45 73 57M64 77v15" stroke="#F2F5F7" stroke-width="6" stroke-linecap="round"/>',
    "settings": '<circle cx="64" cy="64" r="31" fill="none" stroke="ACCENT" stroke-width="9" stroke-dasharray="16 7"/><circle cx="64" cy="64" r="13" fill="#F2F5F7"/>',
    "terminal": '<rect x="23" y="29" width="82" height="70" rx="10" fill="#111820" stroke="#F2F5F7" stroke-width="6"/><path d="m38 51 13 13-13 13M60 78h26" fill="none" stroke="ACCENT" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    "software": '<path d="M29 48h70v55H29z" fill="#F2F5F7"/><path d="M42 48c0-14 8-23 22-23s22 9 22 23" fill="none" stroke="#F2F5F7" stroke-width="7"/><circle cx="48" cy="72" r="9" fill="#DF5B61"/><circle cx="75" cy="72" r="9" fill="ACCENT"/><path d="m60 89 10-9 10 9-10 9z" fill="#35B98A"/>',
    "printer": '<path d="M38 46V25h52v21M38 88H27V49h74v39H90M40 73h48v31H40z" fill="none" stroke="#F2F5F7" stroke-width="7" stroke-linejoin="round"/><circle cx="88" cy="61" r="5" fill="ACCENT"/>',
    "bluetooth": '<path d="M58 25v78l29-25-29-25 25-21-25-7zM36 43l51 43M36 85l22-19" fill="none" stroke="#F2F5F7" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><circle cx="91" cy="64" r="6" fill="ACCENT"/>',
    "security": '<path d="M64 23 96 35v25c0 24-13 38-32 47-19-9-32-23-32-47V35z" fill="#F2F5F7"/><path d="m47 64 11 11 24-27" fill="none" stroke="ACCENT" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
    "power": '<path d="M64 24v39M44 38a36 36 0 1 0 40 0" fill="none" stroke="#F2F5F7" stroke-width="9" stroke-linecap="round"/><circle cx="64" cy="64" r="8" fill="ACCENT"/>',
    "accessibility": '<circle cx="64" cy="29" r="11" fill="ACCENT"/><path d="M35 48h58M64 49v30M64 62 43 91M64 62l21 29" fill="none" stroke="#F2F5F7" stroke-width="8" stroke-linecap="round"/>',
}


def write(rel: str, content: str) -> None:
    path = SCALABLE / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    folders = {
        "folder": "",
        "folder-documents": GLYPHS["documents"],
        "folder-download": GLYPHS["downloads"],
        "folder-music": GLYPHS["music"],
        "folder-pictures": GLYPHS["pictures"],
        "folder-videos": GLYPHS["videos"],
    }
    for name, glyph in folders.items():
        write(f"places/{name}.svg", folder(glyph))

    places = ["home", "desktop", "trash"]
    devices = ["drive", "usb", "network", "printer", "bluetooth"]
    categories = ["settings", "terminal", "software", "security", "power", "accessibility"]
    for name in places:
        write(f"places/user-{name}.svg", tile(GLYPHS[name]))
    for name in devices:
        write(f"devices/oblinux-{name}.svg", tile(GLYPHS[name]))
    for name in categories:
        accent = PALETTE["amber"] if name == "power" else PALETTE["cyan"]
        write(f"categories/oblinux-{name}.svg", tile(GLYPHS[name], accent))

    index = '''[Icon Theme]\nName=OBLinux Horizon Pilot\nComment=Horizon Layer design pilot; not for production use\nInherits=Papirus-Dark,Papirus,hicolor\nDirectories=scalable/places,scalable/devices,scalable/categories\n\n[scalable/places]\nSize=128\nMinSize=16\nMaxSize=256\nType=Scalable\nContext=Places\n\n[scalable/devices]\nSize=128\nMinSize=16\nMaxSize=256\nType=Scalable\nContext=Devices\n\n[scalable/categories]\nSize=128\nMinSize=16\nMaxSize=256\nType=Scalable\nContext=Categories\n'''
    THEME.mkdir(parents=True, exist_ok=True)
    (THEME / "index.theme").write_text(index, encoding="utf-8")
    print(f"Generated {sum(1 for _ in SCALABLE.rglob('*.svg'))} pilot icons in {THEME}")


if __name__ == "__main__":
    main()
