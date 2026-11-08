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

ABOUT_INTRO = """<p class="eyebrow">About</p>
      <h2 id="about-h">Minister. Musician. Writer.</h2>
      <p>Bro. John Kennon is a local minister who has spent more than thirty years writing the way he preaches: straight from Scripture, honest about the hard places, and certain that God rebuilds what life tears down.</p>"""
ABOUT_MINISTRY = """<p>At the Apostolic Church of Beaumont, he serves in the music ministry as a multi-instrumentalist and singer, teaches adult Sunday school, and is part of the livestream ministry. He also ministers in nursing homes, helps other local churches, and preaches when invited.</p>
      <p>His songs pull from gospel, country, and Southern rock, built on strong vocal harmony. His books carry the same message in a quieter voice, through testimony and the everyday moments where faith gets tested.</p>"""
ABOUT_FAMILY = """<p>At home, he is blessed with a beautiful wife, four lovely daughters, three sons, two amazing sons-in-law, two amazing daughters-in-law, and a five-year-old grandson.</p>"""
ABOUT_BODY = ABOUT_INTRO + "\n      " + ABOUT_MINISTRY + "\n      " + ABOUT_FAMILY + """
      <p>Higher Ground Ministries is the home for all of it.</p>
      <p class="sig">Bro. John Kennon</p>"""
ABOUT_HOME = ABOUT_INTRO + "\n      " + ABOUT_FAMILY + """
      <p><a class="more" href="about.html">More about Bro. John</a></p>"""

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
        <p class="eyebrow">The album &middot; John P. Kennon</p>
        <h2 id="music-h">We Will Overcome</h2>
        <p><em>We Will Overcome</em> is a gospel album with a Southern road under it: songs of victory through the blood of the Lamb, written for anyone fighting their way from trouble to testimony.</p>
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
        <p>Books, devotionals, and teaching studies by John P. Kennon: Scripture opened plainly, testimony told honestly, and the apostolic faith of the Book of Acts lived out in everyday life.</p>
      </div>
      <a class="more" href="books.html">All books</a>
    </div>
    <div class="books compact" data-books="teaser"></div>
  </div>
</section>
<section class="band alt study" aria-labelledby="study-h">
  <div class="wrap">
    <div class="study-grid">
      <a class="study-cover" href="studies/next-steps-1-what-must-i-do-to-be-saved.pdf" target="_blank" rel="noopener"><img src="img/studies/ns1-1-01.jpg" alt="Title slide: What Must I Do to Be Saved? Next Steps Lesson 1" width="960" height="540" loading="lazy"></a>
      <div class="study-text">
        <p class="eyebrow">Bible study &middot; Next Steps, Lesson 1</p>
        <h2 id="study-h">What Must I Do to Be Saved?</h2>
        <p>A doctrinal overview from the Book of Acts. This lesson starts with the human condition and the gospel of the death, burial, and resurrection of Jesus, then walks through grace and faith, repentance, baptism in the name of Jesus, and the gift of the Holy Ghost, the plan Peter preached on the Day of Pentecost.</p>
        <p>Open it on your own, or teach it to a small group or new believer. It is also available in Spanish.</p>
        <div class="study-actions">
          <a class="btn" href="studies/next-steps-1-what-must-i-do-to-be-saved.pdf" target="_blank" rel="noopener">Open the lesson</a>
          <a class="btn line" href="studies/next-steps-1-que-debo-hacer-para-ser-salvo.pdf" target="_blank" rel="noopener" lang="es">En espa&ntilde;ol</a>
        </div>
      </div>
    </div>
    <ul class="study-slides" aria-label="Slides from the lesson">
      <li><img src="img/studies/ns1-2-02.jpg" alt="Slide: goal of the lesson" width="960" height="540" loading="lazy"></li>
      <li><img src="img/studies/ns1-4-04.jpg" alt="Slide: the solution, the gospel" width="960" height="540" loading="lazy"></li>
      <li><img src="img/studies/ns1-12-12.jpg" alt="Slide: baptism" width="960" height="540" loading="lazy"></li>
      <li><img src="img/studies/ns1-15-15.jpg" alt="Slide: salvation past, present, future" width="960" height="540" loading="lazy"></li>
    </ul>
  </div>
</section>
<section class="band" aria-labelledby="about-h">
  <div class="wrap about">
    <img class="portrait-img" src="img/john-kennon.jpg" alt="Bro. John Kennon" width="640" height="800">
    <div class="about-body">
      {ABOUT_HOME}
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
    <p class="lead">Books, devotionals, and teaching studies by John P. Kennon: Scripture opened plainly, testimony told honestly, and the apostolic faith of the Book of Acts lived out in everyday life.</p>
  </div>
  {RIDGES}
</header>
<main id="main">
<section class="band">
  <div class="wrap">
    <div class="intro-block">
      <p class="eyebrow">About the books</p>
      <div class="intro-text">
        <p>These books come from the same place as the songs: the pulpit, the prayer room, and the hard seasons in between. The full-length works range from <em>What Happened After the Cross?</em>, which follows the gospel from Calvary into the conversion accounts of Acts, to <em>Untimely</em>, an honest account of a family&rsquo;s journey through sudden loss, grief, and forgiveness. Alongside them are a 52-week devotional, <em>A Vision of the Harvest</em>, and journeys through Exodus, the story of Balaam, and Israel&rsquo;s kings.</p>
        <p>The booklets and studies were written for the congregation and the Sunday school class: teaching on prayer, baptism in Jesus&rsquo; name, the continuing work of the Holy Ghost, marriage, and learning to trust again. Each one opens the Scripture plainly, tells the truth about brokenness, and points to the same God who still restores, still fills, and still speaks.</p>
        <p class="note">These works are being prepared for publication. Read a sample from each one while the full editions are finished.</p>
      </div>
    </div>
    <section class="vase" aria-labelledby="vase-h">
      <div class="vase-text">
        <p class="eyebrow">From <em>Untimely</em> &middot; Chapter 11</p>
        <h2 id="vase-h">The Shattered Vase</h2>
        <blockquote>
          <p>Before the accident&hellip; I had a vision during prayer. A vase. Shattered.</p>
          <p>But in the vision, the Lord did something I didn&rsquo;t expect. He picked up every piece. He didn&rsquo;t discard the broken. And then I heard it in my spirit: &ldquo;I can make it better than it was before.&rdquo;</p>
          <p>At the time, I had no idea what it meant. I taught on this in our adult Sunday school, a lesson I will never forget: the blessing is in the brokenness. But on June 14, when Loren left this world&hellip; I knew. The vase was us.</p>
          <p>He doesn&rsquo;t always prevent the breaking. But He never wastes the pieces.</p>
        </blockquote>
        <p class="sig">Bro. John Kennon</p>
      </div>
      <ol class="vase-panels">
        <li><img src="img/vase/vase-1.jpg" alt="A family gathered happily around a painted vase" loading="lazy"><span>Our family. Our hearts. Our plans.</span></li>
        <li><img src="img/vase/vase-2.jpg" alt="The vase lies shattered on the floor as the family grieves" loading="lazy"><span>Shattered. But not thrown away.</span></li>
        <li><img src="img/vase/vase-3.jpg" alt="A hand of light reaches down and the vase glows through its cracks" loading="lazy"><span>He picked up every piece.</span></li>
        <li><img src="img/vase/vase-4.jpg" alt="The vase restored, the family smiling around it" loading="lazy"><span>&ldquo;I can make it better than it was before.&rdquo;</span></li>
      </ol>
    </section>
    <h2 class="group-title">Books</h2>
    <div class="books shelf" data-books="full"></div>
    <h2 class="group-title">Booklets &amp; studies</h2>
    <div class="books shelf" data-books="short"></div>
    <h2 class="group-title">From the family</h2>
    <div class="family-intro">
      <p class="eyebrow">Bro. John&rsquo;s daughter</p>
      <h2>Grace Stacks</h2>
      <p>Grace has written two works of her own: a letter to her younger self about loss, faith, and finding her way back to hope, and a hand-lettered devotional of Scripture, prayers, and notes of faith. We are proud to share them here.</p>
    </div>
    <div class="books shelf family-books" data-books="family"></div>
    </div>
  </div>
</section>
</main>""")

page("music.html", "We Will Overcome",
     "We Will Overcome, the album by John P. Kennon: original gospel, country and Southern rock songs. Listen to previews.", f"""
<header class="hero page-hero">
  <div class="wrap">
    <p class="sub">The album &middot; John P. Kennon</p>
    <h1>We Will <em>Overcome</em></h1>
    <p class="lead"><em>We Will Overcome</em> is a gospel album with a Southern road under it: songs of victory through the blood of the Lamb, written for anyone fighting their way from trouble to testimony.</p>
  </div>
  {RIDGES}
</header>
<main id="main">
<section class="band">
  <div class="wrap">
    <div class="intro-block album">
      <div class="album-art">
        <img src="img/album-we-will-overcome.jpg" alt="We Will Overcome album cover" width="1200" height="1200">
      </div>
      <div class="intro-text">
        <p class="eyebrow">About the album</p>
        <p><em>We Will Overcome</em> is a collection of songs born out of thirty years of living, losing, and holding on. Rooted in Scripture and carried by gospel, country, and Southern rock with strong vocal harmony, it moves from bold declarations of victory through the blood of the Lamb (<em>We Will Overcome</em>, <em>More Than Conquerors</em>, <em>I Am a Soldier</em>) to quiet prayers for God to break up the hard ground of the heart (<em>Fallow Ground</em>, <em>Closer to Your Throne</em>).</p>
        <p>It walks the prodigal road home in <em>Back Home</em> and <em>Porch Light On</em>, sits with grief and the hope of heaven in <em>Angels Wings</em> and <em>I Hope You&rsquo;re There</em>, and celebrates the simple gift of love and life in <em>Sunrise</em> and <em>Sounds Like Livin&rsquo;</em>. Through it all runs one message: whatever you&rsquo;ve been through, you can still rise. Through Jesus, we will overcome.</p>
        <p class="note">Each song has a one-minute preview.</p>
      </div>
    </div>
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
    <img class="portrait-img" src="img/john-kennon.jpg" alt="Bro. John Kennon" width="640" height="800">
    <div class="about-body">
      {ABOUT_BODY}
      <p><a class="btn line" href="index.html#contact">Get in touch</a></p>
    </div>
  </div>
  <div class="wrap">
    <div class="gallery">
      <figure><img src="img/john-preaching.jpg" alt="Bro. John Kennon preaching" width="640" height="800" loading="lazy"><figcaption>Preaching the Word</figcaption></figure>
      <figure><img src="img/john-drums.jpg" alt="Bro. John Kennon playing drums" width="480" height="600" loading="lazy"><figcaption>On the drums</figcaption></figure>
      <figure><img src="img/john-and-wife.jpg" alt="Bro. John Kennon and his wife, Bonny" width="640" height="800" loading="lazy"><figcaption>With Bonny</figcaption></figure>
      <figure><img src="img/family.jpg" alt="Bro. John Kennon with his wife and family" width="640" height="800" loading="lazy"><figcaption>With family</figcaption></figure>
      <figure class="wide"><img src="img/family-all.jpg" alt="Bro. John Kennon with almost the whole family" width="1500" height="1000" loading="lazy"><figcaption>Almost the whole family</figcaption></figure>
    </div>
  </div>
  <div class="wrap scrapbook">
    <h2 class="group-title">A little more about us</h2>
    <p class="scrap-lead">Coffee, dad jokes, date nights, and a whole lot of sarcasm. Tap any page to see it full size.</p>
    <div class="scrap-pages">
      <figure><a href="img/scrapbook/us.jpg" target="_blank" rel="noopener"><img src="img/scrapbook/us.jpg" alt="Sketchbook collage of Bro. John and Bonny Kennon: My person. My purpose. My greatest blessing. Not perfect. Just forgiven. Determined to finish well." width="1024" height="1536" loading="lazy"></a><figcaption>The two of us</figcaption></figure>
      <figure><a href="img/scrapbook/john.jpg" target="_blank" rel="noopener"><img src="img/scrapbook/john.jpg" alt="Sketchbook collage about Bro. John Kennon: faith, family man, hard worker, dry sense of humor. I lead at work, but my greatest calling is at home." width="1024" height="1536" loading="lazy"></a><figcaption>About John</figcaption></figure>
      <figure><a href="img/scrapbook/her.jpg" target="_blank" rel="noopener"><img src="img/scrapbook/her.jpg" alt="Sketchbook collage about Bonny Kennon: faith, family, purpose, creativity. Sunshine mixed with a little hurricane. Not perfect, just forgiven." width="1150" height="1370" loading="lazy"></a><figcaption>About Bonny</figcaption></figure>
    </div>
  </div>
</section>
</main>""")
print("pages written")
