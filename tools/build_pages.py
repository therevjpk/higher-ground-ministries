"""Write the site's HTML pages with a shared head, nav and footer."""
import sys

SITE = sys.argv[1]
DOMAIN = "https://highergroundministries.church"
FONTS = ("https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;800;900"
         "&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400"
         "&family=IBM+Plex+Mono:wght@400;500&display=swap")
RIDGES = """<svg class="ridges" viewBox="0 0 1440 260" preserveAspectRatio="none" aria-hidden="true">
    <circle cx="1040" cy="190" r="70"/>
    <path d="M0 170 L180 120 L360 150 L560 80 L760 140 L980 95 L1180 150 L1440 110 L1440 260 L0 260Z"/>
    <path d="M0 210 L220 160 L420 200 L640 140 L860 195 L1080 150 L1300 200 L1440 175 L1440 260 L0 260Z"/>
    <path d="M0 245 L300 205 L600 240 L900 210 L1200 240 L1440 220 L1440 260 L0 260Z"/>
  </svg>"""
NAV = [("index.html", "Home"), ("books.html", "Books"), ("music.html", "Music"),
       ("about.html", "About"), ("index.html#contact", "Contact")]


def page(file, title, description, body):
    links = "\n".join(
        f'      <li><a href="{h}"{" aria-current=\"page\"" if h == file else ""}>{n}</a></li>' for h, n in NAV)
    canonical = DOMAIN + "/" + ("" if file == "index.html" else file)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="nav" aria-label="Main">
  <div class="wrap">
    <a class="mark" href="index.html">Higher <span>Ground</span></a>
    <ul>
{links}
    </ul>
  </div>
</nav>
{body}
<footer>
  <div class="wrap">
    <span>&copy; 2026 Higher Ground Ministries</span>
    <span>highergroundministries.church</span>
    <span>Bro. John Kennon &middot; John P. Kennon</span>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""
    open(f"{SITE}/{file}", "w").write(html)


CONTACT = """<section class="band contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap">
    <div>
      <h2 id="contact-h">Get in touch</h2>
      <p>Prayer requests, booking for preaching or music, questions about the books, or just a word of encouragement. Bro. John reads every message.</p>
      <p>Check the box to hear first about book releases and new songs.</p>
    </div>
    <div>
      <p class="thanks" id="thanks" hidden>Thank you. Your message is on its way, and Bro. John will get back to you.</p>
      <form id="contact-form" action="https://formsubmit.co/stackskennon@gmail.com" method="POST">
        <input type="hidden" name="_subject" value="New message from highergroundministries.church">
        <input type="hidden" name="_next" value="https://highergroundministries.church/?sent=1#contact">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="row2">
          <div class="fld"><label for="cf-name">Name</label><input id="cf-name" name="name" type="text" autocomplete="name" required></div>
          <div class="fld"><label for="cf-email">Email</label><input id="cf-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="fld"><label for="cf-topic">Topic</label>
          <select id="cf-topic" name="topic">
            <option>General</option><option>Prayer request</option><option>Booking: preaching or music</option><option>Books</option><option>Music</option>
          </select></div>
        <div class="fld"><label for="cf-msg">Message</label><textarea id="cf-msg" name="message" required></textarea></div>
        <label class="chk"><input id="cf-updates" type="checkbox" name="updates" value="Yes, send release updates"> Send me book and music release updates</label>
        <button class="btn" type="submit">Send message</button>
      </form>
    </div>
  </div>
</section>"""

ABOUT_BODY = """<p class="eyebrow">About</p>
      <h2 id="about-h">Preacher. Writer. Songwriter.</h2>
      <p>Bro. John Kennon is a United Pentecostal minister who writes the way he preaches: straight from Scripture, honest about the hard places, and certain that God rebuilds what life tears down.</p>
      <p>His songs pull from gospel, country, and Southern rock, built on strong vocal harmony. His books carry the same message in a quieter voice, through testimony and the everyday moments where faith gets tested.</p>
      <p>Higher Ground Ministries is the home for all of it.</p>
      <p class="sig">Bro. John Kennon</p>"""

page("index.html", "Higher Ground Ministries",
     "Books and original gospel music from Bro. John Kennon and Higher Ground Ministries.", f"""
<header class="hero" id="top">
  <div class="wrap">
    <p class="sub">Higher Ground Ministries &middot; Bro. John Kennon</p>
    <h1>Books &amp; songs <em>for the climb</em></h1>
    <p class="verse">&ldquo;When my heart is overwhelmed: lead me to the rock that is higher than I.&rdquo;<cite>PSALM 61:2 &middot; KJV</cite></p>
    <div class="cta">
      <a class="btn" href="books.html">See the books</a>
      <a class="btn ghost" href="music.html">Hear the album</a>
    </div>
  </div>
  {RIDGES}
</header>
<main id="main">
<section class="band dedication" aria-labelledby="dedication-h">
  <div class="wrap">
    <div class="dedication-body">
      <p class="eyebrow">A word before you begin</p>
      <h2 id="dedication-h">Thirty years in the making</h2>
      <p>What you&rsquo;ll find here is more than thirty years of writing and composing, gathered in one place for the first time. These songs, sermons, studies, and books were written through every season of life and ministry, on the mountaintops and in the valleys. Much of it was never meant for anyone but God and me.</p>
      <p>I share it now with one prayer: that something here meets you right where you are, and points you to the Rock that is higher than I.</p>
      <p>This work is dedicated first to the Lord Jesus Christ, who gave every song and every word worth keeping. And to my family, who lived these pages with me.</p>
      <p class="sig">Bro. John Kennon</p>
    </div>
  </div>
</section>
<section class="band alt" aria-labelledby="music-h">
  <div class="wrap">
    <div class="head-row">
      <div class="head">
        <p class="eyebrow">The album &middot; John Kennon</p>
        <h2 id="music-h">We Will Overcome</h2>
        <p>Gospel with a Southern road under it: Scripture-rooted lyrics, three-part harmony, and a band that knows when to lift.</p>
      </div>
      <a class="more" href="music.html">Hear the album</a>
    </div>
    <div data-songs="featured"></div>
    <ul class="songs compact" data-songs="teaser"></ul>
  </div>
</section>
<section class="band" aria-labelledby="books-h">
  <div class="wrap">
    <div class="head-row">
      <div class="head">
        <p class="eyebrow">Books &middot; John P. Kennon</p>
        <h2 id="books-h">Written from the valley floor</h2>
        <p>Scripture, testimony, and the kind of family-table stories that teach you something on the way home.</p>
      </div>
      <a class="more" href="books.html">All books</a>
    </div>
    <div class="books compact" data-books="teaser"></div>
  </div>
</section>
<section class="band" aria-labelledby="about-h">
  <div class="wrap about">
    <div class="portrait">Photo of<br>Bro. John Kennon</div>
    <div class="about-body">
      {ABOUT_BODY}
    </div>
  </div>
</section>
{CONTACT}
</main>""")

page("books.html", "Books by John P. Kennon",
     "Books, booklets and teaching studies by John P. Kennon, with reading samples.", f"""
<header class="hero page-hero">
  <div class="wrap">
    <p class="sub">Books &middot; John P. Kennon</p>
    <h1>Written from <em>the valley floor</em></h1>
    <p class="lead">These works are being prepared for publication. Read a sample from each one while the full editions are finished.</p>
  </div>
  {RIDGES}
</header>
<main id="main">
<section class="band">
  <div class="wrap">
    <h2 class="group-title">Books</h2>
    <div class="books" data-books="full"></div>
    <h2 class="group-title">Booklets &amp; studies</h2>
    <div class="books" data-books="short"></div>
    <h2 class="group-title">From the family</h2>
    <div class="family">
      <div class="books" data-books="family"></div>
      <div class="family-intro">
        <p class="eyebrow">Bro. John&rsquo;s daughter</p>
        <h2>Grace Stacks</h2>
        <p>Grace wrote her own book: a letter to her younger self about loss, faith, and finding her way back to hope. We are proud to share it here.</p>
      </div>
    </div>
  </div>
</section>
</main>""")

page("music.html", "We Will Overcome",
     "We Will Overcome, the album by John Kennon: original gospel, country and Southern rock songs. Listen to previews.", f"""
<header class="hero page-hero">
  <div class="wrap">
    <p class="sub">The album &middot; John Kennon</p>
    <h1>We Will <em>Overcome</em></h1>
    <p class="lead">Gospel with a Southern road under it: Scripture-rooted lyrics, three-part harmony, and a band that knows when to lift. Each song has a one-minute preview.</p>
  </div>
  {RIDGES}
</header>
<main id="main">
<section class="band">
  <div class="wrap">
    <div data-songs="featured"></div>
    <h2 class="group-title">We Will Overcome &middot; Full track list</h2>
    <ul class="songs" data-songs="list"></ul>
  </div>
</section>
</main>""")

page("about.html", "About Bro. John Kennon",
     "About Bro. John Kennon, minister, writer and songwriter, and Higher Ground Ministries.", f"""
<main id="main">
<section class="band" aria-labelledby="about-h">
  <div class="wrap about">
    <div class="portrait">Photo of<br>Bro. John Kennon</div>
    <div class="about-body">
      {ABOUT_BODY}
      <p><a class="btn line" href="index.html#contact">Get in touch</a></p>
    </div>
  </div>
</section>
</main>""")
print("pages written")
