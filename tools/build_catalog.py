"""Build the public catalog (site/data/catalog.json) from the private source catalog.

Only fields visitors need are copied. Private notes, source filenames, aliases and
editorial status never leave this script.

Usage: python3 build_catalog.py <private Catalog_Data.json> <site dir>
"""
import json
import os
import sys

SRC, SITE = sys.argv[1], sys.argv[2]
src = json.load(open(SRC))

# ---- John's decisions (2026-11-06) ----
EXCLUDE_BOOKS = {"insulin-resistance-reset"}          # leave the cookbook off for now
BOOK_OVERRIDES = {
    "after-the-cross": {"subtitle": "A Mission Through Acts"},
    "blessings-in-brokenness": {"title": "The Blessings in Brokenness"},
}
# Full-length works first, then booklets and studies.
FULL_KINDS = {"Book draft", "Devotional draft", "Unified manuscript"}

# Songs: finished recordings from the "We Will Overcome SB Album" folder, in this order.
SONGS = [
    # (site id, display title, catalog id or None)
    ("from-trouble-to-testimony", "From Trouble to Testimony", "from-trouble-to-testimony"),
    ("higher-ground", "Higher Ground", "higher-ground"),
    ("we-will-overcome", "We Will Overcome", "we-will-overcome"),
    ("still-i-rise", "Still I Rise", "still-i-rise"),
    ("living-by-faith", "Living by Faith", "living-by-faith"),
    ("a-beautiful-redemption", "A Beautiful Redemption", "a-beautiful-redemption"),
    ("more-than-conquerors", "More Than Conquerors", "more-than-conquerors"),
    ("let-the-redeemed-say-so", "Let the Redeemed Say So", "let-the-redeemed-say-so"),
    ("ive-been-redeemed", "I’ve Been Redeemed", "ive-been-redeemed"),
    ("i-am-a-soldier", "I Am a Soldier", "i-am-a-soldier"),
    ("ive-got-too-much-to-lose", "I’ve Got Too Much to Lose", "ive-got-too-much-to-lose"),
    ("closer-to-your-throne", "Closer to Your Throne", "closer-to-your-throne"),
    ("fallow-ground", "Fallow Ground", "fallow-ground"),
    ("picking-up-the-pieces", "Picking Up the Pieces", "picking-up-the-pieces"),
    ("back-home", "Back Home", "back-home"),
    ("porch-light-on", "Porch Light On", "porch-light-on"),
    ("angels-wings", "Angels Wings", "angels-wings"),
    ("i-hope-youre-there", "I Hope You’re There", "i-hope-youre-there"),
    ("psalm-23", "Psalm 23", "psalm-23"),
    ("when-he-steps-in", "When He Steps In", "when-he-steps-in"),
    ("all-things", "All Things", "all-things"),
    ("i-got-something", "I Got Something", "i-got-something"),
    ("sunrise", "Sunrise", "sunrise"),
    ("sounds-like-livin", "Sounds Like Livin’", "sounds-like-livin"),
    ("the-one-who-stayed", "The One Who Stayed", "the-one-who-stayed"),
    ("wrong-door-right-man", "Wrong Door, Right Man", "wrong-door-right-man"),
    ("keep-on-walking", "Keep On Walking", "keep-on-walking"),
    ("just-being-dad-to-you", "Just Being Dad to You", None),
    ("you-are-with-me", "You Are With Me", None),
    ("in-my-fathers-house-duet", "In My Father’s House (Duet)", None),
    ("in-my-fathers-house-modern", "In My Father’s House (Modern)", None),
    ("lean-on-the-lord", "Lean on the Lord", None),
    ("none-like-him", "None Like Him", None),
    ("still-holding-me", "Still Holding Me", None),
    ("when-all-i-have-is-you", "When All I Have Is You", None),
]
# Catalog descriptions that are placeholders, not descriptions. Show nothing instead.
PLACEHOLDER_DESCRIPTIONS = {"all-things", "i-got-something", "psalm-23", "when-he-steps-in",
                            "wrong-door-right-man", "the-one-who-stayed"}
SONG_CREDITS = {
    "the-one-who-stayed": "Written and recorded by John P. Kennon · Also released by The Loners",
}


def asset(rel_dir, id_, exts):
    for ext in exts:
        rel = f"{rel_dir}/{id_}.{ext}"
        if os.path.exists(os.path.join(SITE, rel)):
            return rel
    return None


books = []
for b in src["books"]:
    if b["stage"] != "Manuscript available" or b["id"] in EXCLUDE_BOOKS:
        continue
    o = BOOK_OVERRIDES.get(b["id"], {})
    books.append({
        "id": b["id"],
        "title": o.get("title", b["title"]),
        "subtitle": o.get("subtitle", ""),
        "kind": b["kind"],
        "group": "full" if b["kind"] in FULL_KINDS else "short",
        "description": b["description"],
        "cover": asset("img/books", b["id"], ["jpg", "png"]),
        "sample": asset("samples", b["id"], ["pdf"]),
        "purchase_url": "",
    })
# Back-cover copy and subtitles written from each manuscript (tools/book_copy.json)
COPY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "book_copy.json")))
for b in books:
    b.update(COPY.get(b["id"], {}))
books.sort(key=lambda x: 0 if x["group"] == "full" else 1)

# Books by family members, shown in their own section.
FAMILY_BOOKS = [{
    "id": "letter-to-the-girl",
    "title": "A Letter to the Girl I Used to Be",
    "subtitle": "",
    "author": "Grace Stacks",
    "kind": "Book draft",
    "group": "family",
    "description": ("Grace Stacks writes to her younger self: the girl who felt things deeply, doubted her worth "
                    "and her faith, and carried more than she could explain. It is for anyone learning who they "
                    "are while carrying a story heavier than they expected, and a reminder that what shaped you "
                    "never disqualified you from being loved or heard."),
    "purchase_url": "",
}]
FAMILY_BOOKS.append({
    "id": "graces-devotional",
    "title": "Grace’s Devotional",
    "subtitle": "Scripture, prayers, and notes of faith",
    "author": "Grace Stacks",
    "kind": "Devotional journal",
    "group": "family",
    "description": "Some of the truest words about faith are written in pencil. Grace’s Devotional is Grace Stacks’ own notebook of walking with Jesus through everyday life, kept page by page with hand-lettered headings, colored-pencil hearts, drawings, and the Scriptures that carried her.\n\nInside are forty-nine short entries on the things young believers really face: friendship and gossip, social media, overthinking, comparing yourself, regrets, worry, and waiting on God. Each pairs a verse with her own reflection or prayer, like the reminder that “God isn’t delaying you. God is preparing you.” Read slowly. Keep your Bible nearby. Leave room to pray.",
    "purchase_url": "",
})
for fb in FAMILY_BOOKS:
    fb["cover"] = asset("img/books", fb["id"], ["jpg", "png"])
    fb["sample"] = asset("samples", fb["id"], ["pdf"])
    books.append(fb)

by_id = {s["id"]: s for s in src["songs"]}
songs = []
for i, (sid, title, cid) in enumerate(SONGS):
    c = by_id.get(cid) if cid else None
    desc = "" if (not c or sid in PLACEHOLDER_DESCRIPTIONS) else c["description"]
    songs.append({
        "id": sid,
        "title": title,
        "description": desc,
        "credit": SONG_CREDITS.get(sid, ""),
        "cover": asset("img/songs", sid, ["jpg", "png"]),
        "preview": asset("audio", sid, ["mp3"]),
        "featured": i == 0,
        "listen_url": "",
        "purchase_url": "",
    })

os.makedirs(os.path.join(SITE, "data"), exist_ok=True)
json.dump({"author": "John P. Kennon", "books": books, "songs": songs},
          open(os.path.join(SITE, "data/catalog.json"), "w"), ensure_ascii=False, indent=1)
print(f"books: {len(books)} ({sum(1 for b in books if b['cover'])} covers, "
      f"{sum(1 for b in books if b['sample'])} samples) | songs: {len(songs)} "
      f"({sum(1 for s in songs if s['cover'])} covers, {sum(1 for s in songs if s['preview'])} previews)")
