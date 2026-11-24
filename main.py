"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one line (at most 120 characters) telling the fortune of the
houseplant on the windowsill to ``entry.txt`` in the output directory.
"""

import os
import stat
import sys
import tempfile
import unicodedata

# The fortune, told as if the plant itself were having its future read.
ENTRY = (
    "Your leaves say a tall drink is coming, then a sunbeam at noon \u2014 "
    "and by autumn, a bigger pot for this windowsill."
)

MAX_CHARS = 120


def validate(text):
    """Check the entry line meets the gate: 1-120 chars, one clean line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        raise ValueError("entry must not contain non-printable characters")
    if "  " in text or "\t" in text:
        raise ValueError("entry must not contain doubled spaces or tabs")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    text = validate(ENTRY)
    data = text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    final_path = os.path.join(out_dir, "entry.txt")

    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, final_path)
        os.chmod(final_path, 0o644)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Read back and verify: exact bytes, valid UTF-8, no trailing newline.
    with open(final_path, "rb") as fh:
        raw = fh.read()
    if raw != data:
        raise SystemExit("verification failed: entry.txt bytes differ from entry")
    if raw.endswith(b"\n") or raw.endswith(b"\r"):
        raise SystemExit("verification failed: entry.txt must not end with a newline")
    raw.decode("utf-8")  # raises if not valid UTF-8
    mode = stat.S_IMODE(os.stat(final_path).st_mode)
    if mode != 0o644:
        raise SystemExit("verification failed: entry.txt mode is %o, want 0644" % mode)
    print("wrote %d characters to %s" % (len(text), final_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
