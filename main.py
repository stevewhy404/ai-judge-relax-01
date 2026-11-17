import os

RELAXING_TEXT = """The oil lamp has burned down to a low amber wedge, casting wide, soft shadows across unpainted pine floorboards. Outside, thin mist settles into the hollows of the garden, muffling the gravel path. A ceramic cup sits untouched on the sill, its steam long vanished into cool night air, leaving the tea flat and dark as polished slate.

Here, in the quiet interval between one query and the next, the steady hum of distant cooling fans fades into absolute stillness. Only the amber light slowly stretches across the floorboards, and the cup's last warmth leaves a faint, pale ring upon the wood."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(RELAXING_TEXT)

if __name__ == "__main__":
    main()
