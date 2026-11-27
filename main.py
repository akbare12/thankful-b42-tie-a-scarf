import os

# Deterministic: one fixed text, no randomness, no network, stdlib only.
TEXT = "Thank you. Your neck has ached cold all day above the pages. Here is the wool scarf from its hook: I wind it round you, once, twice, and tuck the ends in tight. Breathe. The wool still holds the heat of my hands. Keep reading. The scarf stays knotted, soft at your throat, till the last page is done and gone."

os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), exist_ok=True)
with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
