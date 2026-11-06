"""Cut a ~75 s preview from the strongest stretch of a song.

Usage: python3 make_preview.py <in.mp3> <out.mp3>
Prints: duration, start, length (seconds) as JSON.
"""
import json
import subprocess
import sys

import numpy as np

SR = 11025
PREVIEW = 60.0


def main(src, dst):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    dur = len(x) / SR
    sec = int(dur)
    rms = np.sqrt(np.array([np.mean(x[i * SR:(i + 1) * SR] ** 2) for i in range(sec)]) + 1e-12)

    length = min(PREVIEW, max(30.0, dur * 0.5))
    L = int(length)
    lo = min(15, max(0, sec - L))           # skip the intro
    hi = max(lo, sec - L - 5)               # don't run into the outro
    best, start = -1.0, lo
    c = np.concatenate([[0], np.cumsum(rms)])
    for s in range(lo, hi + 1):
        m = (c[s + L] - c[s]) / L
        if m > best:
            best, start = m, s
    # back up to the quietest second just before the window, so it starts on a phrase
    look = range(max(lo, start - 6), start + 1)
    start = min(look, key=lambda s: rms[s])

    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(length), "-i", src,
         "-af", f"afade=t=in:d=1.5,afade=t=out:st={length - 4}:d=4,loudnorm=I=-14:TP=-1.5:LRA=11",
         "-ar", "44100", "-ac", "2", "-b:a", "128k", "-map_metadata", "-1", dst],
        check=True,
    )
    print(json.dumps({"duration": round(dur, 1), "start": start, "length": length}))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
