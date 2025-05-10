import json
from pathlib import Path

src_path  = Path("/Users/liamachenbach/Documents/VSprojects/Isaac-GR00T-mimic/red_cup_pour/meta/episodes_stats.jsonl")        # <-- your input file
dest_path = Path("/Users/liamachenbach/Documents/VSprojects/Isaac-GR00T-mimic/red_cup_pour/meta/episodes_stats_no_sec0.jsonl")  # <-- output without secondary_0

with src_path.open() as f_in, dest_path.open("w") as f_out:
    for line in f_in:
        if not line.strip():           # skip empty lines
            continue
        obj = json.loads(line)

        # Safely drop the nested key if it exists
        obj.get("stats", {}).pop("observation.images.secondary_0", None)

        # If it might also appear outside "stats", drop those too:
        obj.pop("observation.images.secondary_0", None)

        # Write the cleaned record back out
        json.dump(obj, f_out, separators=(",", ":"))
        f_out.write("\n")

print(f"Done. Clean file written to {dest_path}")
