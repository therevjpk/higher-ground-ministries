# Higher Ground Ministries

Website for https://highergroundministries.church: books and music from John P. Kennon.

Plain static site hosted on Render (no build step). Domain registered at Wix, DNS pointed to Render.

## Layout
- `index.html`, `books.html`, `music.html`, `about.html`: the pages
- `data/catalog.json`: every book and song shown on the site. Edit this to change a title, description, or add a link.
- `img/books/`, `img/songs/`: covers (`<id>.jpg`)
- `audio/`: 60-second song previews (`<id>.mp3`)
- `samples/`: reading samples (`<id>.pdf`)
- `assets/`: shared CSS and JavaScript

A book's "Read a sample" button and a song's player only appear when the matching file exists.
`purchase_url` and `listen_url` are empty until real store or streaming links exist.

## Tools (not served)
- `tools/build_catalog.py`: builds `data/catalog.json` from the private source catalog (kept out of this repo)
- `tools/build_pages.py`: writes the four HTML pages from one shared template
- `tools/make_preview.py`: cuts a 60-second preview from a full recording
