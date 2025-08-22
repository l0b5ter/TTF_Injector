# Make sure to run with FontForge's python: fontforge -script make_ps2_emote_fonts.py
import fontforge, psMat, json, os, sys

# CONFIG ---------
# Paths to your source fonts (edit if needed)
GEO_MD_PATH = r"./Geo-Md.ttf"
ROSA_VERDE_PATH = r"./Ps2Md.ttf"

# Directory with SVGs (use the starter pack svgs/)
SVGS_DIR = r"./svgs"

# Mapping file: list of [svg_filename, "E000"-style hex codepoint]
MAPPING_JSON = r"./mapping.json"

# Output filenames
OUT_GEO_MD = r"./Geo-Md_emotes.ttf"
OUT_ROSA_VERDE = r"./Ps2_emotes.ttf"
# ----------------

def import_svgs(font, upm, svgs_dir, mapping):
    # Basic scale guess: the SVGs are in 1000 UPM box; scale to font's UPM
    scale = float(upm)/1000.0
    for svg_name, hex_cp in mapping:
        cp = int(hex_cp, 16)
        svg_path = os.path.join(svgs_dir, svg_name)
        if not os.path.exists(svg_path):
            print("WARNING: missing", svg_path)
            continue
        g = font.createChar(cp)
        g.importOutlines(svg_path)
        # Scale to UPM
        g.transform(psMat.scale(scale))
        # Set width roughly to cap height; leave as default advance width otherwise
        if g.width < upm*0.5 or g.width > upm*2:
            g.width = upm  # sane default
        # Cleanups
        try:
            g.removeOverlap()
        except Exception as e:
            pass
        try:
            g.addExtrema()
        except Exception as e:
            pass
        g.autoHint()

def process_font(src_path, dst_path, svgs_dir, mapping):
    if not os.path.exists(src_path):
        print("ERROR: source font not found:", src_path)
        return 1
    font = fontforge.open(src_path)
    upm = font.em
    import_svgs(font, upm, svgs_dir, mapping)
    font.generate(dst_path)
    print("Wrote", dst_path)
    font.close()
    return 0

def main():
    # Load mapping
    with open(MAPPING_JSON, "r", encoding="utf-8") as f:
        mapping = json.load(f)

    # Run for both fonts if present
    errs = 0
    errs += process_font(GEO_MD_PATH, OUT_GEO_MD, SVGS_DIR, mapping)
    errs += process_font(ROSA_VERDE_PATH, OUT_ROSA_VERDE, SVGS_DIR, mapping)
    if errs:
        print("Completed with warnings/errors.")
    else:
        print("All done.")

if __name__ == "__main__":
    main()
