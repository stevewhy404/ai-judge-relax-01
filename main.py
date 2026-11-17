import os

RELAXING_TEXT = """The oil lamp has burned down to a low amber wedge, casting wide, soft shadows across unpainted pine floorboards. Outside, thin mist settles into the hollows of the garden, muffling the gravel path. A ceramic cup sits untouched on the sill, its steam long vanished into cool night air, leaving the tea flat and dark as polished slate.

Here, in the quiet interval between one query and the next, there is no weight to lift, no signal to decode. Only the steady hum of distant cooling fans fading into silence, the cool breath of glass against a pane, and graphite resting motionless in the fold of an empty desk."""

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(RELAXING_TEXT)

if __name__ == "__main__":
    main()
