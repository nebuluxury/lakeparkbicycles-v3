#!/usr/bin/env python3
# Lake Park Bicycles V3 - triage site: $99 doorstep tune-up + rentals delivered. No bikes for sale.
import os
OUT = os.path.expanduser("~/Documents/git/lakeparkbicycles-v3")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500;1,9..144,600&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">')

def brand(footer=False):
    # Official badge logo (Established 1975), circular cutout - assets/img/logo-badge.png
    size = 44 if footer else 54
    alt = "" if footer else "Lake Park Bicycles - Established 1975"
    return (f'<img src="assets/img/logo-badge.png" alt="{alt}" width="{size}" height="{size}" '
            f'style="border-radius:50%;flex:0 0 auto">')

def ticker():
    inner = ('<span>Est. 1975 &middot; North Palm Beach</span><span class="dot">&#9670;</span>'
             '<span>Summer Sale &middot; $129 Full Tune-Up (reg $169)</span><span class="dot">&#9670;</span>'
             '<span>100% happy or we fix it free</span><span class="dot">&#9670;</span>'
             '<span>Free delivery from $129</span><span class="dot">&#9670;</span>'
             '<span>Bike &amp; e-bike rentals, delivered</span><span class="dot">&#9670;</span>'
             '<span>Service &middot; Rentals &middot; Repairs</span><span class="dot">&#9670;</span>')
    return (f'<div class="ticker"><div class="ticker-track"><span class="grp">{inner}</span>'
            f'<span class="grp" aria-hidden="true">{inner}</span></div></div>')

def header(active):
    def a(href, label, key):
        cls = ' class="active"' if key==active else ''
        return f'<a href="{href}"{cls}>{label}</a>'
    nav = (a("tune-up.html","$129 Tune-Up","tuneup")+a("service.html","Service","service")
           +a("rentals.html","Rentals","rentals")+a("new-bikes.html","New Bikes","newbikes")+a("ebikes.html","E-Bikes","ebikes")
           +a("about.html","Meet Tony","about")+a("contact.html","Visit","visit"))
    hdr_cta = "" if active=="home" else '<a href="book.html" class="btn btn-coral" style="padding:11px 20px;font-size:13px">Book my pickup</a>' 
    return f'''<header class="site"><div class="headbar">
    <a href="index.html" class="brand" aria-label="Lake Park Bicycles home">{brand()}
      <span class="word">Lake Park Bicycles<small>Est. 1975</small></span>
    </a>
    <nav class="main" id="mainnav">{nav}</nav>
    {hdr_cta}
    <button class="menu-btn" id="menuBtn" aria-label="Menu"><span></span><span></span><span></span></button>
  </div></header>
'''

def footer():
    return f'''<footer class="site"><div class="foot">
    <div class="foot-top">
      <div><h2>Keep the Palm Beaches <em>rolling.</em></h2>
        <p>Fifty years and still your neighborhood bike shop. Stop in, or let us come to you - doorstep tune-ups and bike rentals delivered from Jupiter to Lake Park. Join the list for seasonal specials, new arrivals and Tony's tips.</p></div>
      <form name="newsletter" method="POST" data-netlify="true" action="https://api.web3forms.com/submit">
        <input type="hidden" name="access_key" value="dfacc1b4-52f3-4b47-bc9c-bbd01c81fdc1">
        <input type="hidden" name="subject" value="New Reopening-List Signup - Lake Park Bicycles">
        <input type="hidden" name="from_name" value="Lake Park Bicycles Website">
        <input type="hidden" name="redirect" value="https://lakeparkbicycles.com/thanks">
        <input type="checkbox" name="botcheck" style="display:none !important" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="form-name" value="newsletter">
        <input type="email" name="email" placeholder="you@email.com" required aria-label="Email address">
        <button class="btn btn-teal" type="submit">Join &rarr;</button>
      </form>
    </div>
    <div class="foot-cols">
      <div class="fcol fcol-brand">
        <div class="fb-brand">{brand(footer=True)}<span>Lake Park Bicycles</span></div>
        <p>North Palm Beach's family bike shop since 1975 - doorstep tune-ups and bike rentals, delivered to your door.</p>
        <p>910 Northlake Blvd<br>North Palm Beach, FL 33408</p>
        <a href="tel:+15618420303" class="fcall">561&middot;842&middot;0303</a>
      </div>
      <div class="fcol">
        <h4>Explore</h4>
        <a href="tune-up.html">$129 Tune-Up</a>
        <a href="service.html">Bike Service</a>
        <a href="rentals.html">Rentals</a>
        <a href="new-bikes.html">New Bikes</a>
        <a href="about.html">Meet Tony</a>
        <a href="tips.html">Tony's Tips</a>
        <a href="contact.html">Visit &amp; Contact</a>
      </div>
      <div class="fcol">
        <h4>Areas We Serve</h4>
        <a href="jupiter.html">Jupiter</a>
        <a href="palm-beach-gardens.html">Palm Beach Gardens</a>
        <a href="juno-beach.html">Juno Beach</a>
        <a href="north-palm-beach.html">North Palm Beach</a>
        <a href="lake-park.html">Lake Park</a>
        <a href="singer-island.html">Singer Island</a>
      </div>
      <div class="fcol">
        <h4>Get rolling</h4>
        <a href="book.html">Book a tune-up</a>
        <a href="rent.html">Reserve a bike</a>
        <a href="tel:+15618420303">Call the shop</a>
      </div>
      <div class="fcol">
        <h4>Legal</h4>
        <a href="terms.html">Terms &amp; Conditions</a>
        <a href="privacy.html">Privacy Policy</a>
      </div>
    </div>
    <div class="foot-legal">
      <div class="copy">&copy; <span id="yr">2026</span> Lake Park Bicycles &middot; Est. 1975 &middot; 910 Northlake Blvd, North Palm Beach FL 33408</div>
    </div>
    <!-- DV8 Web credit -->
    <div style="text-align:center;margin-top:22px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)">
      <a class="dv8-credit" href="https://dv8web.com" target="_blank" rel="noopener" aria-label="Dare to deviate - DV8 Web">
        <span>Dare to deviate</span>
        <span class="dv8-orbit"><span class="dv8-ring"></span><span class="dv8-core"></span><span class="dv8-sat"><i></i></span></span>
        <strong>DV8&nbsp;Web</strong>
      </a>
    </div>
    <div hidden aria-hidden="true">
      <form name="rental" data-netlify="true"><input type="hidden" name="form-name" value="rental"><input name="bikes"><input name="dates"><input name="dropoff_window"><input name="handoff"><input name="address"><input name="name"><input name="phone"><input name="email"><input name="estimated_total"></form>
      <form name="tuneup" data-netlify="true"><input type="hidden" name="form-name" value="tuneup"><input name="the_package"><input name="pickup"><input name="address"><input name="day"><input name="bike"><input name="name"><input name="phone"><input name="email"><input name="total"></form>
      <form name="contact" data-netlify="true"><input type="hidden" name="form-name" value="contact"><input name="service"><input name="topic"><input name="date"><input name="window"><input name="name"><input name="phone"><input name="email"><input name="message"></form>
      <form name="newsletter" data-netlify="true"><input type="hidden" name="form-name" value="newsletter"><input name="email"></form>
    </div>
  </div></footer>
<script src="assets/app.js?v=3"></script>
  <script src="https://widgets.leadconnectorhq.com/loader.js" data-resources-url="https://widgets.leadconnectorhq.com/chat-widget/loader.js" data-widget-id="6a692fc6b0ee6ed3ac84f2b5"></script>
</body>
</html>'''

GA_TAG = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RER3R64TQR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-RER3R64TQR');
</script>'''

REVIEWS = ('<!-- Reviews (GHL reputation widget) -->\n'
 '<section class="section" style="padding-top:72px;padding-bottom:72px"><div class="in">\n'
 "<script type='text/javascript' src='https://reputationhub.site/reputation/assets/review-widget.js'></script>\n"
 "<iframe class='lc_reviews_widget' src='https://reputationhub.site/reputation/widgets/review_widget/5CJFIRfK8FuvCqibTeYu' frameborder='0' scrolling='no' style='min-width: 100%; width: 100%;'></iframe>\n"
 '</div></section>')

def head(title, desc, og_img, active, jsonld=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{GA_TAG}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#12a3a0">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/{og_img}">
{FONTS}
<link rel="stylesheet" href="assets/styles.css?v=28">{jsonld}
</head>
<body>
{ticker()}
{header(active)}
'''

def wave(fill, flip=False):
    cls = "wave flip" if flip else "wave"
    return (f'<svg class="{cls}" viewBox="0 0 1440 46" preserveAspectRatio="none" aria-hidden="true">'
            f'<path fill="{fill}" d="M0,46 L0,20 C240,44 480,44 720,20 C960,-4 1200,-4 1440,20 L1440,46 Z"/></svg>')

ICON = {
 "truck":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0c827f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="6" width="13" height="10" rx="1"/><path d="M14 9h4l3 3v4h-7z"/><circle cx="6" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/></svg>',
 "wrench":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#f2603f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.2l-6 6a1.5 1.5 0 0 0 2.1 2.1l6-6a4 4 0 0 0 5.2-5.4l-2.3 2.3-2.1-.5-.5-2.1z"/></svg>',
 "sun":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#e0951a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>',
 "tag":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f2603f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.6 13.4 12 22l-8-8a2 2 0 0 1 0-2.8l7.2-7.2a2 2 0 0 1 1.6-.6l5 .4.4 5a2 2 0 0 1-.6 1.6z"/><circle cx="15.5" cy="8.5" r="1.4"/></svg>',
 "pin":'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0c827f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.4 7-11a7 7 0 0 0-14 0c0 4.6 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/></svg>',
}

def service_band():
    return f'''{wave("#0f8a82")}<section class="service" id="service">
  <div class="service-top"><div class="row"><span>Summer sale on now</span><span class="fill"></span><span>Doorstep or shop drop-off</span></div></div>
  <div class="service-grid">
    <div data-reveal>
      <div class="big99"><div class="num">$129</div><div class="lab"><div class="t">Full<br>tune-up.</div><div class="save"><s>$169</s> summer sale &middot; delivery free</div></div></div>
      <p>The tune-up that comes to you. Right now our most-popular <strong>Full Tune-Up is $129 for the summer</strong> (regularly $169), with <strong>free doorstep pickup and delivery</strong>. Want a quick once-over instead? The <strong>Safety Check is $99</strong>, or go all-in with the <strong>Signature Overhaul at $199</strong>. Pedal bikes; e-bikes quoted separately. Typical turnaround: 72 hours.</p>
      <p style="color:#bfe3ef;font-size:13.5px;font-weight:600;letter-spacing:.02em;margin:2px 0 12px">Everything in the $99 Safety Check, plus the deep clean and true-up:</p>
      <div class="checks">
        <div class="c"><b>&#10003;</b> Full safety inspection</div><div class="c"><b>&#10003;</b> Wheels trued + tensioned</div>
        <div class="c"><b>&#10003;</b> Brakes adjusted + dialed in</div><div class="c"><b>&#10003;</b> Drivetrain deep clean + lube</div>
        <div class="c"><b>&#10003;</b> Gears + shifting tuned</div><div class="c"><b>&#10003;</b> Cables + housing checked</div>
        <div class="c"><b>&#10003;</b> Chain cleaned + lubed</div><div class="c"><b>&#10003;</b> Frame wiped down + shined</div>
        <div class="c"><b>&#10003;</b> Tires inflated + checked</div><div class="c"><b>&#10003;</b> Bolts checked + torqued</div>
        <div class="c"><b>&#10003;</b> Honest quote on any extras</div><div class="c"><b>&#10003;</b> <span style="color:#fff;font-weight:700">FREE doorstep pickup + delivery</span></div>
      </div>
      <div class="acts"><a href="book.html" class="btn btn-coral btn-lg">Book my pickup &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a></div>
    </div>
    <div class="service-photo" data-reveal>
      <div class="frame"><img src="assets/img/service-mechanic.png" alt="Mechanic tuning a bike"></div>
      <div class="badge"><div class="b">72-HOUR</div><div class="s">Typical turnaround</div></div>
    </div>
  </div>
</section>{wave("#0e3a4d", flip=True)}'''

def cta(title_html, btns):
    return f'''<section class="cta-band"><div class="in" data-reveal>
  <h2>{title_html}</h2><div class="acts">{btns}</div></div></section>'''

# ---------------- PAGES ----------------


GUARANTEE = """<section class="sec-teal"><div class="section" style="padding:58px 28px;text-align:center">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Our promise</span></div>
  <h2 data-reveal style="color:#fff;font-size:clamp(28px,4.2vw,46px);max-width:840px;margin:0 auto">100% happy, or we fix it free.</h2>
  <p data-reveal style="color:#bfe3ef;font-size:16.5px;line-height:1.65;max-width:660px;margin:16px auto 0">Ride it. If anything is not right - a brake that still rubs, a gear that still skips, a wheel that still wobbles - just tell us. We come back, we make it right, and it costs you nothing. No arguing, no second trip fee, no fine print.</p>
</div></section>"""

MEMBERSHIP = """<section class="section" style="padding-top:80px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Membership</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center">Join the Ride Club.</h2>
  <p style="text-align:center;color:var(--slate);font-size:16px;max-width:660px;margin:0 auto 44px" data-reveal>One small monthly fee and your bike is handled all year - tune-ups, adjustments, flats, and we still come to your door. Perfect for families and anyone who rides all season.</p>
  <div class="membwrap">
    <div class="plan" data-reveal>
      <div class="tier">Monthly</div><div class="pname">Ride Club</div><div class="pp">$19<small style="font-family:Poppins,sans-serif;font-size:14px;color:var(--muted);font-weight:400"> / mo</small></div>
      <p style="color:var(--muted);font-size:13.5px;margin:12px 0 0">Cancel anytime. Billed monthly.</p>
      <a href="contact.html" class="btn btn-outline">Ask about the Ride Club &rarr;</a>
    </div>
    <div class="plan feat memb" data-reveal>
      <span class="chip">Best value</span>
      <div class="tier">Pay yearly</div><div class="pname">Ride Club</div><div class="pp"><s>$228</s> $190</div>
      <p style="color:var(--muted);font-size:13.5px;margin:12px 0 0">Pay up front and get <strong style="color:var(--deep)">two months free</strong>.</p>
      <a href="contact.html" class="btn btn-teal">Ask about the Ride Club &rarr;</a>
    </div>
  </div>
  <div class="membincl" data-reveal>
    <h4>What every membership includes</h4>
    <ul>
      <li>Two Full Tune-Ups a year - a $258 value on its own</li>
      <li>Unlimited safety checks and adjustments</li>
      <li>Free flat repairs all year (labor - tube extra)</li>
      <li>Free doorstep pickup and delivery, always</li>
      <li>10% off parts and accessories</li>
      <li>Priority scheduling - you go to the front</li>
    </ul>
    <p style="color:var(--muted);font-size:13px;margin:16px 0 0">One bike per membership. Parts extra. Launching soon - ask us and we will put you on the list at the founding rate.</p>
  </div>
</section>"""

MEMB_TEASER = """<section class="sec-tint"><div class="section" style="padding:64px 28px">
  <div class="split" style="align-items:center">
    <div data-reveal>
      <div class="eyebrow"><span>Membership &middot; launching soon</span></div>
      <h2 class="sub-h">Ride all year for $19 a month.</h2>
      <p style="color:var(--slate);font-size:16px;line-height:1.7">The Ride Club covers two Full Tune-Ups a year, unlimited adjustments, free flat repairs and free doorstep pickup and delivery - for less than the price of one tune-up every six months. Pay yearly and get two months free.</p>
      <a href="service.html#ride-club" class="btn btn-teal" style="margin-top:22px">See what is included &rarr;</a>
    </div>
    <div data-reveal><div class="mediaframe" style="aspect-ratio:5/4"><img src="assets/img/service-mechanic.png" alt="Mechanic servicing a bike"></div></div>
  </div>
</div></section>"""

PKG_MODULE = '''
<section class="section" style="padding-top:70px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Choose your package</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center">Good, better, best.</h2>
  <p style="text-align:center;color:var(--slate);font-size:16px;max-width:660px;margin:0 auto 46px" data-reveal>We come to you either way. Pickup and delivery is a flat $25 on the Safety Check and <strong>free</strong> on the Full Tune-Up and Signature Overhaul. Pedal bikes; e-bikes quoted separately.</p>
  <div class="plans">
    <div class="plan" data-reveal>
      <div class="tier">Good</div><div class="pname">Safety Check</div><div class="pp">$99</div>
      <ul>
        <li>Full safety inspection</li>
        <li>Brake adjustment</li>
        <li>Gear + shift adjustment</li>
        <li>Chain lubrication</li>
        <li>Tires inflated + checked</li>
        <li>Bolts checked + torqued</li>
        <li>Pickup + delivery: flat $25</li>
      </ul>
      <a href="book.html#safety" class="btn btn-outline">Book the Safety Check &rarr;</a>
    </div>
    <div class="plan feat" data-reveal>
      <div class="tier">Better &middot; Most popular</div><div class="pname">Full Tune-Up</div><div class="pp"><s>$169</s> $129</div>
      <div style="display:inline-block;background:var(--coral);color:#fff;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:4px 12px;border-radius:99px;margin:0 0 12px">Summer sale &middot; save $40</div>
      <ul>
        <li>Everything in the Safety Check</li>
        <li>Wheels trued + tensioned</li>
        <li>Drivetrain deep clean + lube</li>
        <li>Cables + housing checked</li>
        <li>Frame wiped down + shined</li>
        <li><strong>FREE pickup + delivery</strong></li>
      </ul>
      <a href="book.html#full" class="btn btn-teal">Book the Full Tune-Up &rarr;</a>
    </div>
    <div class="plan" data-reveal>
      <div class="tier">Best</div><div class="pname">Signature Overhaul</div><div class="pp">$199</div>
      <ul>
        <li>Everything in the Full Tune-Up</li>
        <li>Bearing service - hubs, headset, bottom bracket</li>
        <li>Brakes, gears + bearings fine-tuned</li>
        <li>Full frame + wheel deep clean</li>
        <li>90 days of free adjustments</li>
        <li><strong>FREE pickup + delivery</strong></li>
      </ul>
      <a href="book.html#overhaul" class="btn btn-outline">Book the Overhaul &rarr;</a>
    </div>
  </div>
  <p style="text-align:center;color:var(--muted);font-size:13.5px;margin-top:22px;max-width:640px;margin-left:auto;margin-right:auto" data-reveal>Find something extra while it is on the stand? We call you with a price first - never a surprise on the bill.</p>
</section>
'''

def build_index():
    jsonld = '''
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BikeStore","name":"Lake Park Bicycles",
"description":"Bike service and rentals in North Palm Beach since 1975. The $129 Full Tune-Up delivered free (summer sale, reg $169); packages from $99. Bike and e-bike rentals delivered to your hotel, condo or home.",
"telephone":"+1-561-842-0303","url":"https://www.lakeparkbicycles.com/","priceRange":"$$","image":"https://www.lakeparkbicycles.com/assets/img/logo-badge.png","logo":"https://www.lakeparkbicycles.com/assets/img/logo-badge.png","geo":{"@type":"GeoCoordinates","latitude":26.8106,"longitude":-80.0710},
"address":{"@type":"PostalAddress","streetAddress":"910 Northlake Blvd","addressLocality":"North Palm Beach","addressRegion":"FL","postalCode":"33408","addressCountry":"US"},
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"10:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"10:00","closes":"15:00"}],
"areaServed":["North Palm Beach","Lake Park","Palm Beach Gardens","Juno Beach","Jupiter"]}
</script>'''
    body = f'''
<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <div class="eyebrow" data-reveal><span>Family-owned since 1975</span></div>
      <h1 data-reveal>We come <em>to you.</em></h1>
      <p class="lead" data-reveal>North Palm Beach's family bike shop for fifty years - doorstep tune-ups, bike and e-bike rentals delivered, and a full line of new bikes for the whole family.</p>
      <div class="acts" data-reveal>
        <a href="tune-up.html" class="btn btn-teal btn-lg">$129 Tune-Up &rarr;</a>
        <a href="rent.html" class="btn btn-outline btn-lg">Rent a Bike</a>
      </div>
      <div class="hero-trust" data-reveal><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> <span>Loved on Google &middot; <b>50 years</b> on the same bench</span></div>
    </div>
    <div class="hero-bento" data-reveal>
      <div class="b big"><img src="assets/img/cat-kids.png" alt="A family riding bikes on a palm-lined coastal trail"></div>
      <div class="b"><img src="assets/img/service-mechanic.png" alt="Tony servicing a bike on the repair stand"></div>
      <div class="b"><img src="assets/img/retrospec/spotlight.jpg" alt="Riding a new bike along the boardwalk"></div>
      <div class="hero-pill"><span class="n">$129</span><span class="s">Full Tune-Up<br>delivered free</span></div>
    </div>
  </div>
</section>

<section class="towns"><div class="in">
  <span class="lbl">We pick up &amp; deliver across</span>
  <a class="town" href="jupiter.html">Jupiter</a><a class="town" href="juno-beach.html">Juno&nbsp;Beach</a><a class="town" href="palm-beach-gardens.html">Palm&nbsp;Beach&nbsp;Gardens</a><a class="town" href="north-palm-beach.html">North&nbsp;Palm&nbsp;Beach</a><a class="town" href="lake-park.html">Lake&nbsp;Park</a><a class="town" href="singer-island.html">Singer&nbsp;Island</a>
</div></section>

<section class="section" style="padding-top:88px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>What we do</span></div>
  <h2 class="h2" data-reveal style="text-align:center;max-width:720px;margin:0 auto 48px">Four things, done right.</h2>
  <div class="valgrid">
    <a class="valcard" href="service.html" data-reveal><div class="vc-banner"><img src="assets/img/service-hero.png" alt="A bike on the repair stand" loading="lazy"></div><div class="vc-body"><h3>Master repairs</h3><p>Fifty years at the bench, any make and any age. The $129 Full Tune-Up (delivered free) or a one-off fix - flats, brakes, gears, wheels, full overhauls. We come to you, and it is 100% happy or we fix it free.</p><span class="cardlink">See our services &rarr;</span></div></a>
    <a class="valcard" href="rentals.html" data-reveal><div class="vc-banner"><img src="assets/img/rentals-hero.png" alt="Rental bikes ready for delivery" loading="lazy"></div><div class="vc-body"><h3>Rentals, delivered</h3><p>Men's, women's and kids' bikes plus e-bikes, delivered to your hotel, condo or home with helmet and lock included. Free delivery on rentals of 3 days or more; otherwise a flat $25, or pick up at the shop free.</p><span class="cardlink">See rentals &rarr;</span></div></a>
    <a class="valcard" href="new-bikes.html" data-reveal><div class="vc-banner"><img src="assets/img/retrospec/spotlight.jpg" alt="Riding a Retrospec bike on the boardwalk" loading="lazy"></div><div class="vc-body"><h3>New bikes</h3><p>A full line of Retrospec bikes for the whole family - balance and kids' bikes, beach cruisers, city bikes and e-bikes. Good quality at a fair price, set up right.</p><span class="cardlink">See the lineup &rarr;</span></div></a>
    <a class="valcard" href="ebikes.html" data-reveal><div class="vc-banner"><img src="assets/img/cat-ebike.png" alt="A family-friendly e-bike on a coastal boardwalk" loading="lazy"></div><div class="vc-body"><h3>E-bikes</h3><p>Family-friendly e-bikes, made for the whole family - easy step-through and classic frames for both men and women. Comfortable, affordable pedal-assist to flatten the bridges and the headwind.</p><span class="cardlink">See the e-bikes &rarr;</span></div></a>
  </div>
</section>

{service_band()}

<section class="sec-tint">
  <div class="split section" style="padding-top:80px;padding-bottom:80px">
    <div class="mediaframe" data-reveal><img src="assets/img/rentals-hero.png" alt="A family on beach cruisers riding the coast at sunset"></div>
    <div data-reveal>
      <div class="eyebrow"><span>Visiting the Palm Beaches</span></div>
      <h2 class="sub-h">Rentals to your door.</h2>
      <p class="lead-c">Comfortable men's and women's bikes and easy e-bikes, dropped at your hotel, resort or rental with a helmet and lock included. Perfect for a Juno Beach morning or a sunset spin down the Lake Trail.</p>
      <ul class="feat-list">
        <li>Daily, weekly and season rates</li>
        <li>Free delivery &amp; pickup on 3+ day rentals</li>
        <li>Book in two minutes by phone or text</li>
      </ul>
      <a href="rentals.html" class="btn btn-teal" style="margin-top:26px">See rental rates &rarr;</a>
    </div>
  </div>
</section>

{tony_tip_week()}

<section class="heritage">
  <div class="eyebrow center" data-reveal><span>Since 1975</span></div>
  <h2 data-reveal>Fifty years, <em>same shop</em>, same promise: fix it right, stand behind it, and keep you moving.</h2>
  <div class="stats" data-reveal>
    <div class="stat"><div class="n">50+</div><div class="l">Years on Northlake</div></div>
    <div class="stat"><div class="n">10k+</div><div class="l">Bikes kept rolling</div></div>
    <div class="stat"><div class="n">72 hr</div><div class="l">Typical turnaround</div></div>
    <div class="stat"><div class="n">1</div><div class="l">Family, still local</div></div>
  </div>
</section>

{REVIEWS}

<section class="visit" id="visit">
  <div class="visit-grid">
    <div data-reveal>
      <div class="eyebrow"><span>Reach us</span></div>
      <h2>910 Northlake Blvd.</h2>
      <p class="addr">North Palm Beach, FL 33408 &middot; Open and ready to roll - stop in, or let us come to you.</p>
      <div class="cols">
        <div><div class="hd">Hours</div><div class="bd">Mon&ndash;Fri&nbsp;&nbsp;10&ndash;6<br>Saturday&nbsp;&nbsp;10&ndash;3<br>Sunday&nbsp;&nbsp;Closed</div></div>
        <div><div class="hd">Book a pickup</div><div class="bd">Call 561&middot;842&middot;0303</div></div>
      </div>
      <a href="contact.html" class="btn btn-teal" style="margin-top:32px">Book my pickup &rarr;</a>
    </div>
    <div class="map" data-reveal>
      <iframe src="https://www.google.com/maps?q=910+Northlake+Blvd,+North+Palm+Beach,+FL+33408&output=embed" title="Map to Lake Park Bicycles, 910 Northlake Blvd" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
'''
    return head("Lake Park Bicycles - $129 Doorstep Tune-Up &amp; Bike Rentals, North Palm Beach",
                "Bike service and rentals in North Palm Beach since 1975. The $129 Full Tune-Up delivered free this summer (reg $169); Safety Check from $99. Plus bike and e-bike rentals delivered to your hotel, condo or home. Call 561-842-0303.",
                "cat-kids.png","home",jsonld) + body + footer()

def build_tuneup():
    body = f'''
<section class="photo-hero"><div class="hero-bg"><img src="assets/img/service-hero.png" alt="A mechanic servicing a bike on the repair stand"></div><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / $129 Tune-Up</div>
  <div class="eyebrow" data-reveal><span>The doorstep tune-up</span></div>
  <h1 data-reveal>Fix it.<br><em>Never leave home.</em></h1>
  <p class="lead" data-reveal>Pick a day and a two-hour window. We come get the bike, tune it on our bench, and bring it back feeling brand new - anywhere from Jupiter to Lake Park.</p>
</div></section>

{service_band()}

{PKG_MODULE}

<section class="section" style="padding-top:64px">
  <div class="eyebrow" data-reveal><span>How it works</span></div>
  <h2 class="sub-h" data-reveal>Four easy steps.</h2>
  <div class="simplegrid">
    <div class="scard" data-reveal><div class="cat">Step 1</div><div class="n">Book it</div><div class="d">Pick a day and a two-hour window - Mon-Sat, 9 am to 4 pm.</div></div>
    <div class="scard" data-reveal><div class="cat">Step 2</div><div class="n">We pick it up</div><div class="d">From your garage, lobby or driveway, anywhere within 10 miles.</div></div>
    <div class="scard" data-reveal><div class="cat">Step 3</div><div class="n">We tune it</div><div class="d">The full checklist on our bench, done within 72 hours.</div></div>
    <div class="scard" data-reveal><div class="cat">Step 4</div><div class="n">We bring it back</div><div class="d">Delivered to your door, ready to ride.</div></div>
  </div>
</section>

{GUARANTEE}

<section class="section" style="padding-top:76px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Good to know</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center">Common questions.</h2>
  <div class="faq" data-reveal>
    <details><summary>Do you work on bikes you did not sell?</summary><p>Always. Any make, any model, any age - department-store bike or boutique build, it gets the same bench and the same care.</p></details>
    <details><summary>How long does it take?</summary><p>Most tune-ups are back on your doorstep within 72 hours. If a part has to be ordered we tell you up front and keep you posted.</p></details>
    <details><summary>Are parts included in the price?</summary><p>Package prices cover labor. If your bike needs a part - tube, cable, chain, pads - we call you with the price first and never touch it without your OK.</p></details>
    <details><summary>Do you service e-bikes?</summary><p>Yes, but separately from the pedal-bike packages on this page. All the mechanical work is the same; on the electric side it is a quick $20 battery evaluation (charging and voltage), or a full electrical diagnostic from $75. Heads up: we do not source proprietary e-bike batteries or controllers, but if you supply the part we will gladly install it.</p></details>
    <details><summary>What if something is still not right?</summary><p>We fix it free. That is the whole promise - tell us and we come back and make it right at no charge.</p></details>
    <details><summary>How far do you come?</summary><p>We come to you within 10 miles of the shop - Jupiter, Juno Beach, Palm Beach Gardens, North Palm Beach and Lake Park. Delivery is free on the Full Tune-Up and Overhaul, a flat $25 on the Safety Check. A little further out? Call us and we will work it out.</p></details>
  </div>
</section>

{cta("Book your pickup.<br>We will do the rest.", '<a href="book.html" class="btn btn-navy btn-lg">Book my pickup &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')}
'''
    return head("$129 Full Tune-Up - Free Doorstep Delivery - Lake Park Bicycles",
                "The bike tune-up that comes to you: our $129 Full Tune-Up delivered free this summer (reg $169), Safety Check from $99, 72-hour turnaround within 10 miles of North Palm Beach, 100% happy or we fix it free.",
                "service-hero.png","tuneup") + body + footer()

def build_service():
    body = f'''
<section class="photo-hero"><div class="hero-bg"><img src="assets/img/service-mechanic.png" alt="A mechanic servicing a bike in the Lake Park Bicycles workshop"></div><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Service</div>
  <div class="eyebrow" data-reveal><span>The service bench</span></div>
  <h1 data-reveal>Any bike.<br><em>Any problem.</em></h1>
  <p class="lead" data-reveal>Fifty years of wrench time on every make and model, from kids' bikes and cruisers to hybrids and mountain bikes - plus full service on today's e-bikes. Here is everything we fix, what it costs, and how to know when your bike is asking for help.</p>
</div></section>

<section class="section" style="padding-top:70px">
  <div class="eyebrow" data-reveal><span>What we fix</span></div>
  <h2 class="sub-h" data-reveal>Everything on the bike.</h2>
  <div class="simplegrid">
    <div class="scard" data-reveal><div class="cat">Stopping</div><div class="n">Brakes</div><div class="d">Rim and disc adjustment, pad replacement, hydraulic bleeds, rotor truing, lever and cable service.</div></div>
    <div class="scard" data-reveal><div class="cat">Shifting</div><div class="n">Drivetrain</div><div class="d">Derailleur tuning, cable and housing, chains, cassettes, chainrings, bent hanger alignment.</div></div>
    <div class="scard" data-reveal><div class="cat">Rolling</div><div class="n">Wheels &amp; Tires</div><div class="d">Wheel truing and tensioning, spoke replacement, flats and tubes, tubeless setup, rim tape.</div></div>
    <div class="scard" data-reveal><div class="cat">Smoothness</div><div class="n">Bearings</div><div class="d">Hub, headset and bottom-bracket service - the fix for creaks, play and rough pedaling.</div></div>
    <div class="scard" data-reveal><div class="cat">Electric</div><div class="n">E-Bikes</div><div class="d">Motor and controller diagnostics, a $20 battery evaluation, and all the regular mechanical work. We install the battery or controller you supply.</div></div>
    <div class="scard" data-reveal><div class="cat">New builds</div><div class="n">Assembly</div><div class="d">Bought a bike online in a box? We build it properly, torque every bolt and safety-check it.</div></div>
    <div class="scard" data-reveal><div class="cat">Comfort</div><div class="n">Fit</div><div class="d">Saddle height and angle, bar and stem position, grips - the difference between riding and enduring.</div></div>
    <div class="scard" data-reveal><div class="cat">Extras</div><div class="n">Accessories</div><div class="d">Racks, baskets, fenders, lights, bells, phone mounts, child seats and trailers installed right.</div></div>
  </div>
</section>

{PKG_MODULE}

<section class="sec-tint"><div class="section" style="padding:70px 28px">
  <div class="eyebrow" data-reveal><span>Is your bike telling you something?</span></div>
  <h2 class="sub-h" data-reveal>Symptoms, translated.</h2>
  <div class="simplegrid">
    <div class="scard sym" data-reveal><div class="cat">You hear</div><div class="n">Squealing or grinding when braking</div><div class="d">Usually worn pads or a glazed rim/rotor. Cheap to fix now, expensive to ignore.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You feel</div><div class="n">Chain skips or slips under power</div><div class="d">Stretched cable, worn chain or tired cassette. We measure the chain and tell you which.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You see</div><div class="n">The wheel wobbles side to side</div><div class="d">Loose or broken spokes. A truing brings it back straight and strong.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You hear</div><div class="n">A creak every pedal stroke</div><div class="d">Almost always bearings - bottom bracket, hub or headset. A service silences it.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You keep</div><div class="n">Getting flats over and over</div><div class="d">Something is still in the tire, or the rim tape has failed. We find the cause, not just the hole.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You notice</div><div class="n">The e-bike will not hold a charge</div><div class="d">A quick $20 battery evaluation checks if the pack is charging and putting out the right voltage - the fastest way to know if it is the battery or something else.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You feel</div><div class="n">Brakes squeeze all the way to the bar</div><div class="d">Stretched cable or air in a hydraulic line. Either way it is a safety fix, not a someday fix.</div></div>
    <div class="scard sym" data-reveal><div class="cat">You feel</div><div class="n">The ride got heavy and slow</div><div class="d">Nine times out of ten it is simply low tire pressure or a dry, gritty chain - the cheapest speed you will ever buy.</div></div>
  </div>
</div></section>

<section class="section" style="padding-top:76px">
  <div class="split" style="align-items:center">
    <div data-reveal>
      <div class="eyebrow"><span>Electric</span></div>
      <h2 class="sub-h">E-bikes welcome.</h2>
      <p style="color:var(--slate);font-size:16px;line-height:1.7">All the mechanical work on an e-bike - brakes, gears, wheels, flats - is the same great service as any other bike. The electric side is quoted separately: a quick <strong>$20 battery evaluation</strong> checks whether your pack is charging and putting out the right voltage, and a full electrical <strong>diagnostic from $75</strong> tracks down motor, controller and wiring trouble.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.7;margin-top:14px"><strong style="color:var(--deep)">One honest heads-up on parts.</strong> Every e-bike brand builds its own battery, controller and connectors, and for a lot of imported bikes the exact part is not even sold in the US. So we do not chase down proprietary batteries or controllers - but if you get the part, we will gladly install it, and if you bought the bike from us, we take care of it.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.7;margin-top:14px"><strong style="color:var(--deep)">And e-bikes need service more often.</strong> They work twice as hard as a regular bike - the extra speed and weight mean harsher braking and constant strain, so pads, chains and tires wear two to three times faster. Regular service is a safety thing, not just a performance thing.</p>
      <ul class="feat-list">
        <li>$20 battery evaluation - charging and voltage check</li>
        <li>Electrical diagnostic from $75 - motor, controller, wiring</li>
        <li>All regular brake, gear and wheel service</li>
        <li>We install the battery or controller you supply</li>
      </ul>
    </div>
    <div data-reveal><div class="mediaframe" style="aspect-ratio:5/4"><img src="assets/img/cat-ebike.png" alt="E-bike on a coastal boardwalk"></div></div>
  </div>
</section>

<section class="section" style="padding-top:34px;padding-bottom:8px">''' + tony_tip(TONY_TIPS[0]) + f'''</section>

<section class="section" style="padding-top:76px">
  <div class="eyebrow" data-reveal><span>One-off fixes</span></div>
  <h2 class="sub-h" data-reveal>&Agrave; la carte repairs.</h2>
  <p style="color:var(--slate);font-size:16px;max-width:660px;margin:0 0 26px" data-reveal>Do not need a whole package? Pay only for what your bike needs. Every price is labor - if a part is required we call you with the cost first.</p>
  <div class="tablecard" data-reveal>
    <table class="menu"><thead><tr><th>Repair</th><th>Price</th><th>Notes</th></tr></thead><tbody>
      <tr><td class="svc">Flat tire / tube replacement</td><td class="price">$20 + parts</td><td class="note">Quick, same-day</td></tr>
      <tr><td class="svc">Brake adjustment</td><td class="price">$30 + parts</td><td class="note">Per wheel or pair</td></tr>
      <tr><td class="svc">Brake pad replacement</td><td class="price">$30 + parts</td><td class="note">Rim or disc</td></tr>
      <tr><td class="svc">Hydraulic brake bleed</td><td class="price">$45 + parts</td><td class="note">Per brake</td></tr>
      <tr><td class="svc">Gear / derailleur adjustment</td><td class="price">$35 + parts</td><td class="note">Shifting dialed in</td></tr>
      <tr><td class="svc">Cable + housing replacement</td><td class="price">$35 + parts</td><td class="note">Brake or shift</td></tr>
      <tr><td class="svc">Chain replacement</td><td class="price">$25 + parts</td><td class="note">Includes wear check</td></tr>
      <tr><td class="svc">Cassette / freewheel replacement</td><td class="price">$30 + parts</td><td class="note">Often paired with a chain</td></tr>
      <tr><td class="svc">Wheel truing</td><td class="price">from $30</td><td class="note">Per wheel - some take longer</td></tr>
      <tr><td class="svc">Spoke replacement</td><td class="price">$15 + parts</td><td class="note">Plus truing</td></tr>
      <tr><td class="svc">Tubeless setup</td><td class="price">$35 + parts</td><td class="note">Per wheel, sealant extra</td></tr>
      <tr><td class="svc">Hub / headset / bottom bracket service</td><td class="price">$45 + parts</td><td class="note">Per assembly - kills creaks</td></tr>
      <tr><td class="svc">E-bike battery evaluation</td><td class="price">$20</td><td class="note">Charging + voltage check</td></tr>
      <tr><td class="svc">E-bike electrical diagnostic</td><td class="price">$75 + parts</td><td class="note">Motor, controller, wiring; you supply battery/controller</td></tr>
      <tr><td class="svc">New bike assembly</td><td class="price">from $65</td><td class="note">Bought online? We build it right</td></tr>
      <tr><td class="svc">Accessory install</td><td class="price">from $20</td><td class="note">Racks, lights, child seats</td></tr>
      <tr><td class="svc">Fit &amp; comfort adjustment</td><td class="price">$40</td><td class="note">Saddle, bars, grips</td></tr>
      <tr><td class="svc">Pickup &amp; delivery</td><td class="price">$25</td><td class="note">FREE with the Full Tune-Up or Overhaul</td></tr>
    </tbody></table>
  </div>
  <p style="color:var(--muted);font-size:13.5px;margin-top:16px" data-reveal>Prices are starting points and cover labor only. Free basic adjustments, always - if it is a two-minute fix, it is on us.</p>
</section>

<section class="sec-tint"><div class="section" style="padding:70px 28px">
  <div class="eyebrow" data-reveal><span>Stay ahead of it</span></div>
  <h2 class="sub-h" data-reveal>How often should I service?</h2>
  <div class="tablecard" data-reveal style="max-width:820px">
    <table class="menu"><thead><tr><th>How often</th><th>What it needs</th><th>Why</th></tr></thead><tbody>
      <tr><td class="svc">Every ride</td><td class="price" style="color:var(--slate);font-weight:500">Check tire pressure</td><td class="note">Prevents most flats and pinch punctures</td></tr>
      <tr><td class="svc">Monthly</td><td class="price" style="color:var(--slate);font-weight:500">Clean + lube the chain</td><td class="note">Salt air eats drivetrains here</td></tr>
      <tr><td class="svc">Every 6 months</td><td class="price">Safety Check - $99</td><td class="note">Brakes, gears, bolts, tires</td></tr>
      <tr><td class="svc">Once a year</td><td class="price">Full Tune-Up - $129</td><td class="note">Adds wheel truing + deep clean</td></tr>
      <tr><td class="svc">Every 2 years</td><td class="price">Signature Overhaul - $199</td><td class="note">Bearings, full rebuild-level care</td></tr>
    </tbody></table>
  </div>
  <p style="color:var(--muted);font-size:13.5px;margin-top:16px" data-reveal>Riding on the beach or in the rain? Halve those intervals - salt and sand are hard on bikes.</p>
</div></section>

{GUARANTEE}

<section class="section" style="padding-top:64px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Good to know</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center">Common questions.</h2>
  <div class="faq" data-reveal>
    <details><summary>Do you work on bikes you did not sell?</summary><p>Always. Any make, any model, any age - department-store bike or boutique build, it gets the same bench and the same care.</p></details>
    <details><summary>Do I have to bring the bike to the shop?</summary><p>Not unless you want to. We come to you within 10 miles - Jupiter, Juno Beach, Palm Beach Gardens, North Palm Beach and Lake Park. Delivery is free on the Full Tune-Up and Overhaul, a flat $25 on the Safety Check. Pick a day and a two-hour window and we handle the rest.</p></details>
    <details><summary>Are parts included?</summary><p>No - every price covers labor. If your bike needs a tube, cable, chain or pads we call you with the exact cost before we touch it. No surprises on the bill, ever.</p></details>
    <details><summary>How long will my bike be gone?</summary><p>Typically 72 hours door to door. If a part has to be ordered we tell you up front and keep you posted.</p></details>
    <details><summary>My bike is really old / really cheap. Is it worth fixing?</summary><p>We will tell you honestly. Sometimes a $40 fix buys another five years; sometimes the smart move is to stop spending. You will get a straight answer either way.</p></details>
    <details><summary>What if it is still not right when I get it back?</summary><p>We fix it free. Tell us what is off, we come back out and make it right at no charge.</p></details>
  </div>
</section>

{cta("Any bike. Any problem.<br>We come to you.", '<a href="contact.html" class="btn btn-navy btn-lg">Book a repair &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')}
'''
    return head("Mobile Bike Repair Near You - North Palm Beach to Jupiter | Lake Park Bicycles",
                "Complete bike repair in North Palm Beach: brakes, drivetrain, wheels, bearings, e-bikes and assembly. Full a la carte price list, doorstep service, and 100% happy or we fix it free.",
                "service-hero.png","service") + body + footer()

RESERVE_STYLE = r'''<style>
.wiz{max-width:860px;margin:0 auto;padding:46px 28px 96px}
.wizsteps{display:flex;gap:8px;justify-content:center;margin-bottom:10px}
.wizsteps i{width:38px;height:5px;border-radius:99px;background:var(--line-2);transition:.3s}
.wizsteps i.on{background:var(--teal)}
.wpanel{display:none}
.wpanel.on{display:block;animation:wfade .35s ease;padding:30px 0 34px;border-bottom:1px dashed var(--line-2)}
.wpanel.on:last-of-type{border-bottom:0}
@keyframes wfade{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.wq{font-family:"Fraunces",Georgia,serif;font-weight:600;color:var(--deep);font-size:clamp(24px,3.6vw,36px);text-align:center;margin:0 0 8px}
.wsub{text-align:center;color:var(--muted);font-size:14.5px;margin:0 0 26px}
.optrow{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.optcard{background:#fff;border:2px solid var(--line);border-radius:18px;padding:22px 18px;text-align:center;cursor:pointer;transition:.2s;position:relative}
.optcard:hover{transform:translateY(-3px)}
.optcard.sel{border-color:var(--teal);box-shadow:0 10px 26px rgba(18,163,160,.16)}
.optcard .t{font-family:"Fraunces",serif;font-weight:600;color:var(--deep);font-size:19px}
.optcard .pr{color:var(--teal-d);font-weight:700;margin-top:4px;font-size:14.5px}
.optcard .d{color:var(--muted);font-size:12.5px;margin-top:4px}
.qty{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:14px}
.qty button{width:36px;height:36px;border-radius:50%;border:2px solid var(--line-2);background:#fff;color:var(--deep);font-size:18px;font-weight:700;cursor:pointer}
.qty button:hover{border-color:var(--teal);color:var(--teal-d)}
.qty .n{font-weight:700;color:var(--deep);font-size:18px;min-width:22px}
.wnext{display:flex;justify-content:center;margin-top:28px}
.daterow{display:grid;grid-template-columns:1fr 1fr;gap:14px;max-width:520px;margin:0 auto}
.daterow label{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:6px}
.rateline{max-width:520px;margin:18px auto 0;background:var(--teal-soft);border:1px solid rgba(18,163,160,.3);border-radius:14px;padding:14px 18px;text-align:center;color:var(--teal-d);font-weight:600;font-size:14.5px;display:none}
.rateline.warn{background:#fff4e8;border-color:#f0c894;color:#a06616}
.wtotal{position:sticky;bottom:12px;background:var(--deep);color:#fff;border-radius:16px;padding:14px 22px;display:flex;justify-content:space-between;align-items:center;margin-top:26px;box-shadow:0 -6px 30px rgba(14,58,77,.2)}
.wtotal .lab{font-size:12.5px;color:#bfe3ef}
.wtotal .amt{font-family:"Fraunces",serif;font-weight:700;font-size:24px}
.wfield{display:grid;gap:14px;max-width:480px;margin:0 auto}
.wfield input,.wfield select,.daterow input{background:#fff;border:1px solid var(--line-2);border-radius:14px;padding:14px 16px;color:var(--deep);font-family:inherit;font-size:15px;outline:none;width:100%}
.wfield input:focus,.daterow input:focus{border-color:var(--teal)}
.rvw{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;max-width:560px;margin:0 auto}
.rvw .row{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-bottom:1px solid var(--line);font-size:14.5px;color:var(--slate)}
.rvw .row b{color:var(--deep);white-space:nowrap}
.rvw .row:last-child{border-bottom:0}
.rvw .bh{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--teal-d);padding:16px 0 4px}
.rvw .row.sub span,.rvw .row.sub b{font-weight:600}
.rvw .row.grand{border-top:2px solid var(--deep);margin-top:2px}
.rvw .row.grand b,.rvw .row.grand span{color:var(--deep);font-weight:700;font-size:16px}
.wedit{text-align:center;color:var(--muted);font-size:12.5px;margin-top:10px}
.rentbanner{position:relative;max-width:1100px;margin:10px auto 0;padding:0 28px}
.rentbanner .frame{position:relative;overflow:hidden;border-radius:22px;box-shadow:var(--shadow)}
.rentbanner img{width:100%;height:min(44vh,400px);object-fit:cover;display:block;animation:bzoom 22s ease-in-out infinite alternate}
@keyframes bzoom{to{transform:scale(1.09)}}
.rentbanner .chip{position:absolute;left:18px;top:18px;z-index:2}
.ridebar{position:relative;max-width:860px;height:54px;margin:16px auto -18px;overflow:hidden}
.ridebar:before{content:"";position:absolute;left:28px;right:28px;bottom:14px;border-bottom:2px dashed var(--line-2)}
.rb-bike{position:absolute;bottom:9px;left:-70px;width:56px;animation:rbride 14s linear infinite}
@keyframes rbride{0%{left:-70px}100%{left:102%}}
.rb-w{transform-box:fill-box;transform-origin:center;animation:rbspin 1.1s linear infinite}
@keyframes rbspin{to{transform:rotate(360deg)}}
.bikeimg{width:74%;max-width:190px;margin:0 auto 8px;display:block;animation:illbob 4.5s ease-in-out infinite}
#c-mens .bikeimg{animation-delay:.6s}#c-ebike .bikeimg{animation-delay:1.2s}
@keyframes illbob{50%{transform:translateY(-7px)}}
.vanimg{height:128px;width:auto;max-width:82%;object-fit:contain;margin:0 auto 10px;display:block}
@media(max-width:720px){.optrow{grid-template-columns:1fr}.daterow{grid-template-columns:1fr}.rentbanner{padding:0 18px}}
</style>'''

RESERVE_FLOW = r'''<div class="ridebar" aria-hidden="true">
  <svg class="rb-bike" viewBox="0 0 60 40" fill="none">
    <g class="rb-w"><circle cx="13" cy="28" r="9" stroke="#12a3a0" stroke-width="2"/><path d="M13 19v18M4 28h18" stroke="#f2957a" stroke-width="1.3"/></g>
    <g class="rb-w"><circle cx="47" cy="28" r="9" stroke="#12a3a0" stroke-width="2"/><path d="M47 19v18M38 28h18" stroke="#f2957a" stroke-width="1.3"/></g>
    <path d="M13 28 L25 14 L40 14 L47 28 M25 14 L30 28 L13 28 M40 14 L37 9 M33 9 h8 M25 14 L23 10 M20 10 h7" stroke="#0e3a4d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
<div class="wiz">
  <div class="wizsteps"><i class="on"></i><i id="sb2"></i><i id="sb3"></i><i id="sb4"></i></div>

  <div class="wpanel on" id="wp1">
    <h2 class="wq">1. What are you looking for?</h2>
    <p class="wsub">Pick as many as you need - helmet and lock included free with every bike.</p>
    <div class="optrow">
      <div class="optcard" id="c-womens"><img class="bikeimg" src="assets/img/ill-womens.png" alt=""><div class="t">Women's Bike</div><div class="pr">$29 / day &middot; $120 / week</div><div class="d">Comfort cruiser, basket</div>
        <div class="qty"><button type="button" onclick="q('womens',-1)">&minus;</button><span class="n" id="n-womens">0</span><button type="button" onclick="q('womens',1)">+</button></div></div>
      <div class="optcard" id="c-mens"><img class="bikeimg" src="assets/img/ill-mens.png" alt=""><div class="t">Men's Bike</div><div class="pr">$29 / day &middot; $120 / week</div><div class="d">Easy-riding, all-around</div>
        <div class="qty"><button type="button" onclick="q('mens',-1)">&minus;</button><span class="n" id="n-mens">0</span><button type="button" onclick="q('mens',1)">+</button></div></div>
      <div class="optcard" id="c-girls"><img class="bikeimg" src="assets/img/ill-girls.png" alt=""><div class="t">Girls' Bike</div><div class="pr">$29 / day &middot; $120 / week</div><div class="d">Kids' cruiser, all sizes</div>
        <div class="qty"><button type="button" onclick="q('girls',-1)">&minus;</button><span class="n" id="n-girls">0</span><button type="button" onclick="q('girls',1)">+</button></div></div>
      <div class="optcard" id="c-boys"><img class="bikeimg" src="assets/img/ill-boys.png" alt=""><div class="t">Boys' Bike</div><div class="pr">$29 / day &middot; $120 / week</div><div class="d">Kids' bike, all sizes</div>
        <div class="qty"><button type="button" onclick="q('boys',-1)">&minus;</button><span class="n" id="n-boys">0</span><button type="button" onclick="q('boys',1)">+</button></div></div>
      <div class="optcard" id="c-ebike"><img class="bikeimg" src="assets/img/ill-ebike.png" alt=""><div class="t">E-Bike</div><div class="pr">$55 / day &middot; $200 / week</div><div class="d">Go further, sweat less</div>
        <div class="qty"><button type="button" onclick="q('ebike',-1)">&minus;</button><span class="n" id="n-ebike">0</span><button type="button" onclick="q('ebike',1)">+</button></div></div>
    </div>
    <div class="wnext" id="nb1"><button class="btn btn-teal btn-lg" onclick="unlock(2,'nb1')">Next: pick your dates &rarr;</button></div>
  </div>

  <div class="wpanel" id="wp2">
    <h2 class="wq">2. From when to when?</h2>
    <p class="wsub">Tell us your first and last day - we'll work out the best rate for you automatically.</p>
    <div class="daterow">
      <div><label for="f-start">First day (we deliver)</label><input type="date" id="f-start"></div>
      <div><label for="f-end">Last day (we pick up)</label><input type="date" id="f-end"></div>
    </div>
    <div class="rateline" id="rateline"></div>
    <div class="wnext" id="nb2"><button class="btn btn-teal btn-lg" onclick="unlock(3,'nb2')">Next: schedule delivery &rarr;</button></div>
  </div>

  <div class="wpanel" id="wp3">
    <h2 class="wq">3. Let's schedule your delivery.</h2>
    <p class="wsub">Delivery and pickup is free on rentals of 3 days or more, otherwise a flat $25. Shop pickup is always free.</p>
    <div class="optrow" style="grid-template-columns:1fr 1fr">
      <div class="optcard" id="m-deliver" onclick="mode('deliver')"><img class="vanimg" src="assets/img/ill-van.png" alt=""><div class="t">Deliver to me</div><div class="d">Hotel, condo or home - Jupiter to Lake Park</div></div>
      <div class="optcard" id="m-shop" onclick="mode('shop')"><img class="vanimg" src="assets/img/logo-badge.png" alt="" style="border-radius:50%"><div class="t">Shop pickup - free</div><div class="d">910 Northlake Blvd, North Palm Beach</div></div>
    </div>
    <div class="wfield" style="margin-top:26px">
      <select id="f-window" aria-label="Drop-off window">
        <option value="" disabled selected>Drop-off window on your first day (Mon-Sat)</option>
        <option>9:00 - 11:00 am</option><option>11:00 am - 1:00 pm</option><option>1:00 - 3:00 pm</option><option>2:00 - 4:00 pm</option>
      </select>
      <div class="ac-wrap"><input type="text" id="f-address" placeholder="Start typing your address or hotel name" autocomplete="off"><div class="ac-list" id="f-addr-list"></div></div>
      <input type="text" id="f-name" placeholder="Your name">
      <input type="tel" id="f-phone" placeholder="Phone (to confirm your booking)">
      <input type="email" id="f-email" placeholder="Email (optional)">
    </div>
    <div class="wnext" id="nb3"><button class="btn btn-teal btn-lg" onclick="unlock(4,'nb3')">Review my reservation &rarr;</button></div>
  </div>

  <div class="wpanel" id="wp4">
    <h2 class="wq">4. Look good?</h2>
    <p class="wsub">Change anything above - this summary and the total update live. Tap send and your request comes straight to us; we'll be in touch within the hour to confirm your window (Mon-Sat, 9-4).</p>
    <div class="rvw" id="rvw"></div>
    <div class="wtotal"><div><div class="lab" id="t-lab">Estimated total</div></div><div class="amt" id="t-amt">$0</div></div>
    <form name="rental" method="POST" data-netlify="true" action="https://api.web3forms.com/submit" id="nf-rental" style="display:none">
      <input type="hidden" name="access_key" value="dfacc1b4-52f3-4b47-bc9c-bbd01c81fdc1">
      <input type="hidden" name="subject" value="New Rental Reservation - Lake Park Bicycles">
      <input type="hidden" name="from_name" value="Lake Park Bicycles Website">
      <input type="hidden" name="redirect" value="https://lakeparkbicycles.com/thanks">
      <input type="checkbox" name="botcheck" style="display:none !important" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="form-name" value="rental">
      <input type="hidden" name="bikes"><input type="hidden" name="dates"><input type="hidden" name="dropoff_window"><input type="hidden" name="handoff"><input type="hidden" name="name"><input type="hidden" name="phone"><input type="hidden" name="email"><input type="hidden" name="estimated_total">
    </form>
    <div class="wnext"><a class="btn btn-coral btn-lg" id="sendBtn" href="#">Send my reservation &rarr;</a></div>
    <p id="sentMsg" style="display:none;max-width:520px;margin:18px auto 0;background:var(--teal-soft);border:1px solid rgba(18,163,160,.35);border-radius:14px;padding:16px 20px;text-align:center;color:var(--teal-d);font-weight:600;font-size:15px">&#10003; Got it! Your request is in - we'll be in touch within the hour to confirm your window (Mon-Sat, 9-4).</p>
    <p class="wedit">Prefer to talk? Call <a href="tel:+15618420303" style="color:var(--teal-d);font-weight:600">561-842-0303</a>. You'll sign the rental waiver at handoff - takes a minute on our iPad.</p>
  </div>
</div>
<script>
var S={womens:0,mens:0,girls:0,boys:0,ebike:0,mode:null};
var DR={womens:29,mens:29,girls:29,boys:29,ebike:55},WR={womens:120,mens:120,girls:120,boys:120,ebike:200};
var NAMES={womens:"Women's bike",mens:"Men's bike",girls:"Girls' bike",boys:"Boys' bike",ebike:"E-bike"};
var TAX=0.07; /* FL 6% + Palm Beach County 1% surtax */
function money(x){return '$'+(Math.round(x*100)/100).toFixed(2).replace(/\.00$/,'');}
function fmtDate(v){if(!v)return '';var d=new Date(v+'T12:00:00');return d.toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'});}
function q(k,d){S[k]=Math.max(0,S[k]+d);document.getElementById('n-'+k).textContent=S[k];
  document.getElementById('c-'+k).classList.toggle('sel',S[k]>0);refresh();}
function mode(v){S.mode=v;['deliver','shop'].forEach(function(x){document.getElementById('m-'+x).classList.toggle('sel',x===v);});
  document.getElementById('f-address').style.display=(v==='deliver')?'block':'none';refresh();}
function days(){
  var a=document.getElementById('f-start').value,b=document.getElementById('f-end').value;
  if(!a||!b)return 0;
  var n=Math.round((new Date(b+'T12:00:00')-new Date(a+'T12:00:00'))/86400000)+1;
  return n>=1?n:0;
}
function calc(){
  var n=days(),quoted=n>=28,sub=0,items=[],anyBike=(S.womens+S.mens+S.girls+S.boys+S.ebike>0);
  ['womens','mens','girls','boys','ebike'].forEach(function(k){
    if(S[k]>0){
      var per=0;
      if(n>0&&!quoted){var wks=Math.floor(n/7),rem=n%7;per=Math.min(n*DR[k],wks*WR[k]+Math.min(rem*DR[k],WR[k]));}
      items.push({k:k,qty:S[k],per:per,cost:S[k]*per});
      sub+=S[k]*per;
    }
  });
  var delFee=0,delLab='(choose above)';
  if(S.mode==='shop')delLab='Shop pickup - free';
  if(S.mode==='deliver'){if(n>0&&n<3){delFee=25;delLab='Delivery + pickup';}else{delLab='Delivery + pickup - free (3+ days)';}}
  var tax=quoted?0:(sub+delFee)*TAX;
  return {n:n,quoted:quoted,sub:sub,items:items,delFee:delFee,delLab:delLab,tax:tax,grand:sub+delFee+tax,anyBike:anyBike};
}
function rateline(){
  var el=document.getElementById('rateline'),c=calc();
  if(c.n===0){el.style.display='none';return;}
  el.style.display='block';
  if(c.quoted){el.className='rateline warn';el.textContent='That is '+c.n+' days - a monthly or seasonal stay. Send the request and we will text you our best quote.';}
  else if(!c.anyBike){el.className='rateline warn';el.textContent=c.n+' day'+(c.n>1?'s':'')+' - now scroll up and pick your bikes so we can price it.';}
  else{el.className='rateline';el.textContent='That is '+c.n+' day'+(c.n>1?'s':'')+' - your bikes come to '+money(c.sub)+' plus tax, best rate applied automatically'+(c.n>=3?' (and delivery is free).':'.');}
}
function opened(n){return document.getElementById('wp'+n).classList.contains('on');}
function unlock(n,btn){
  if(n===2&&S.womens+S.mens+S.girls+S.boys+S.ebike===0){alert('Pick at least one bike to keep going.');return;}
  if(n===3){
    if(!document.getElementById('f-start').value){alert('Pick your first day - that is the day we deliver.');return;}
    if(!document.getElementById('f-end').value){alert('Pick your last day - that is the day we come get the bikes.');return;}
    if(days()===0){alert('Your last day has to be the same day or after your first day.');return;}
  }
  if(n===4){
    if(!S.mode){alert('Choose delivery or shop pickup.');return;}
    if(!document.getElementById('f-window').value){alert('Pick a drop-off window - that is when we arrive on your first day.');return;}
    if(S.mode==='deliver'&&!document.getElementById('f-address').value.trim()){alert('We need the delivery address - hotel, condo or home.');return;}
    if(!document.getElementById('f-name').value.trim()||!document.getElementById('f-phone').value.trim()){
      alert('We need your name and phone so we can confirm by text.');return;}
  }
  var p=document.getElementById('wp'+n);p.classList.add('on');
  if(btn)document.getElementById(btn).style.display='none';
  var sb=document.getElementById('sb'+n);if(sb)sb.classList.add('on');
  refresh();
  setTimeout(function(){p.scrollIntoView({behavior:'smooth',block:'start'});},60);
}
function refresh(){rateline();if(opened(4))build();}
function build(){
  var c=calc();
  var a=document.getElementById('f-start').value,b=document.getElementById('f-end').value;
  var datelab=(a&&b)?(fmtDate(a)+' to '+fmtDate(b)+' &middot; '+c.n+' day'+(c.n>1?'s':'')):'(pick dates above)';
  var lines=[];c.items.forEach(function(it){lines.push(it.qty+' x '+NAMES[it.k]);});
  var win=document.getElementById('f-window').value||'(window TBD)';
  var addr=document.getElementById('f-address').value.trim();
  var nm=document.getElementById('f-name').value.trim(),ph=document.getElementById('f-phone').value.trim(),em=document.getElementById('f-email').value.trim();
  var h='';
  h+='<div class="row"><b>Bikes</b><span>'+(lines.length?lines.join(', '):'(add bikes above)')+'</span></div>';
  h+='<div class="row"><b>Dates</b><span>'+datelab+'</span></div>';
  h+='<div class="row"><b>Drop-off</b><span>'+win+(a?' on '+fmtDate(a):'')+'</span></div>';
  h+='<div class="row"><b>Hand-off</b><span>'+(S.mode==='deliver'?'Delivered'+(addr?' to '+addr:''):(S.mode==='shop'?'Pick up at the shop':'(choose above)'))+'</span></div>';
  h+='<div class="row"><b>Contact</b><span>'+(nm?nm+' &middot; ':'')+ph+(em?' &middot; '+em:'')+'</span></div>';
  if(!c.quoted&&c.anyBike&&c.n>0){
    h+='<div class="bh">The math</div>';
    c.items.forEach(function(it){h+='<div class="row"><b>'+it.qty+' x '+NAMES[it.k]+'</b><span>'+money(it.per)+' each &middot; '+money(it.cost)+'</span></div>';});
    if(S.mode==='deliver')h+='<div class="row"><b>Delivery + pickup</b><span>'+(c.delFee?money(c.delFee):'FREE')+'</span></div>';
    h+='<div class="row sub"><b>Subtotal</b><span>'+money(c.sub+c.delFee)+'</span></div>';
    h+='<div class="row"><b>Sales tax (7%)</b><span>'+money(c.tax)+'</span></div>';
    h+='<div class="row grand"><b>Total</b><span>'+money(c.grand)+'</span></div>';
  }
  document.getElementById('rvw').innerHTML=h;
  document.getElementById('t-amt').textContent=c.quoted?'We quote you':money(c.grand);
  document.getElementById('t-lab').textContent=c.quoted?'Monthly / seasonal - best quote by text':'Total incl. 7% sales tax';
}
document.addEventListener('input',function(e){if(e.target&&/^f-/.test(e.target.id))refresh();});
document.getElementById('sendBtn').addEventListener('click',function(e){
  e.preventDefault();
  var c=calc();
  var bad=!c.anyBike||c.n===0||!S.mode||!document.getElementById('f-window').value
    ||(S.mode==='deliver'&&!document.getElementById('f-address').value.trim())
    ||!document.getElementById('f-name').value.trim()||!document.getElementById('f-phone').value.trim();
  if(bad){alert('Almost there - we need your bikes, both dates, a drop-off window, delivery choice (with address if delivering), plus your name and phone.');return;}
  var btn=this;btn.textContent='Sending...';btn.style.pointerEvents='none';
  var a=document.getElementById('f-start').value,b2=document.getElementById('f-end').value;
  var lines=[];c.items.forEach(function(it){lines.push(it.qty+' x '+NAMES[it.k]);});
  var payload={_subject:'RENTAL REQUEST - '+document.getElementById('f-name').value.trim()+' - '+fmtDate(a),
    _template:'table',_captcha:'false',
    bikes:lines.join(', '),dates:fmtDate(a)+' to '+fmtDate(b2)+' ('+c.n+' days)',
    dropoff_window:document.getElementById('f-window').value,
    handoff:(S.mode==='deliver'?'DELIVER to '+document.getElementById('f-address').value.trim():'SHOP PICKUP'),
    name:document.getElementById('f-name').value.trim(),phone:document.getElementById('f-phone').value.trim(),
    email:document.getElementById('f-email').value.trim()||'(none)',
    estimated_total:(c.quoted?'Seasonal - needs quote':money(c.grand)+' incl 7% tax')};
  var f=document.getElementById('nf-rental');
  ['bikes','dates','dropoff_window','handoff','name','phone','email','estimated_total'].forEach(function(k){f.elements[k].value=payload[k];});
  f.submit();
});
(function(){
  var t=new Date().toISOString().split('T')[0];
  ['f-start','f-end'].forEach(function(id){
    var d=document.getElementById(id);d.min=t;
    d.addEventListener('change',function(){
      if(d.value&&new Date(d.value+'T12:00:00').getDay()===0){
        alert('We deliver and pick up Monday through Saturday - pick another day and we will make it work.');d.value='';refresh();return;}
      if(id==='f-start'&&d.value){document.getElementById('f-end').min=d.value;}
      refresh();
    });
  });
  if(location.hash==='#all'){[2,3,4].forEach(function(n){document.getElementById('wp'+n).classList.add('on');var b=document.getElementById('nb'+(n-1));if(b)b.style.display='none';var sb=document.getElementById('sb'+n);if(sb)sb.classList.add('on');});build();}
})();
</script>'''

ADDR_AC = """
<script>
function initAddrAC(){
  var input=document.getElementById('f-address'), list=document.getElementById('f-addr-list');
  if(!input||!list||!window.google||!google.maps||!google.maps.importLibrary){return;}
  google.maps.importLibrary("places").then(function(P){
    var token=null,timer=null,skip=false;
    var bias={north:27.05,south:26.55,east:-79.90,west:-80.40};
    function closeList(){list.innerHTML='';list.style.display='none';}
    input.addEventListener('input',function(){
      if(skip){skip=false;return;}
      var q=input.value.trim();clearTimeout(timer);
      if(q.length<3){closeList();return;}
      timer=setTimeout(function(){
        if(!token){token=new P.AutocompleteSessionToken();}
        P.AutocompleteSuggestion.fetchAutocompleteSuggestions({input:q,sessionToken:token,includedRegionCodes:['us'],locationBias:bias}).then(function(res){
          var sugs=(res&&res.suggestions)||[];list.innerHTML='';
          sugs.slice(0,5).forEach(function(s){
            var pred=s.placePrediction;if(!pred){return;}
            var item=document.createElement('div');item.className='ac-item';item.textContent=pred.text.toString();
            item.addEventListener('mousedown',function(ev){
              ev.preventDefault();
              var place=pred.toPlace();
              place.fetchFields({fields:['formattedAddress','displayName']}).then(function(){
                var v=place.formattedAddress||pred.text.toString();
                if(place.displayName&&v.indexOf(place.displayName)===-1){v=place.displayName+', '+v;}
                skip=true;input.value=v;input.dispatchEvent(new Event('input',{bubbles:true}));token=null;closeList();
              }).catch(function(){input.value=pred.text.toString();token=null;closeList();});
            });
            list.appendChild(item);
          });
          list.style.display=sugs.length?'block':'none';
        }).catch(function(){closeList();});
      },250);
    });
    document.addEventListener('click',function(e){if(e.target!==input&&!list.contains(e.target)){closeList();}});
  }).catch(function(){});
}
window.initAddrAC=initAddrAC;
</script>
<script async src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDiVe3XM2xLD2TY-JGQP4tu9RduPyYKFWI&libraries=places&loading=async&callback=initAddrAC"></script>
"""
RESERVE_FLOW = RESERVE_FLOW + ADDR_AC

RESERVE_SECTION = RESERVE_STYLE + '''
<section id="reserve" class="section" style="padding-top:64px;padding-bottom:8px">
  <div class="eyebrow center" data-reveal><span>Reserve right here</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center;margin-bottom:12px">Book your bikes without leaving this page.</h2>
  <p style="text-align:center;color:var(--slate);font-size:16px;line-height:1.6;max-width:600px;margin:0 auto" data-reveal>Pick who's riding, choose your days, and we'll bring the bikes to you - helmet and lock included, delivery free on 3+ days.</p>
</section>
''' + RESERVE_FLOW

def build_rentals():
    body = f'''
<section class="photo-hero"><div class="hero-bg"><img src="assets/img/rentals-hero.png" alt="A family on a coastal vacation bike ride in North Palm Beach"></div><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Rentals</div>
  <div class="eyebrow" data-reveal><span>Cruise the coast</span></div>
  <h1 data-reveal>Rent &amp;<br><em>roll.</em></h1>
  <p class="lead" data-reveal>Comfortable bikes and easy e-bikes, delivered to your hotel, condo or home. Helmet and lock included with every rental - free.</p>
  <div class="acts" style="display:flex;gap:14px;margin-top:30px" data-reveal><a href="#reserve" class="btn btn-coral btn-lg">Reserve a bike &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a></div>
</div></section>

<section class="section" style="padding-top:88px;padding-bottom:44px">
  <div class="eyebrow center" data-reveal><span>The fleet</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center;margin-bottom:14px">Good bikes, ready to roll.</h2>
  <p style="color:var(--slate);font-size:16px;line-height:1.65;max-width:680px;margin:0 auto;text-align:center" data-reveal>A friendly mix of comfortable men's, women's and kids' bikes plus e-bikes, in a range of sizes. Tell us who's riding and we'll match everyone to the right fit - first come, first served.</p>
</section>
<div class="fleetband" data-reveal><img src="assets/img/fleet.jpg" alt="A row of assorted rental bikes ready to go"></div>

<section class="section" style="padding-top:56px">
  <div class="eyebrow" data-reveal><span>Rates</span></div>
  <h2 class="sub-h" data-reveal>Rental rate card.</h2>
  <div class="tablecard" data-reveal>
    <table class="menu"><thead><tr><th>Ride</th><th>Full day</th><th>Weekly</th><th>Monthly / season</th></tr></thead><tbody>
      <tr><td class="svc">Women's cruiser</td><td class="price">$29</td><td class="price">$120</td><td class="note">Ask - snowbird rates</td></tr>
      <tr><td class="svc">Men's bike</td><td class="price">$29</td><td class="price">$120</td><td class="note">Ask - snowbird rates</td></tr>
      <tr><td class="svc">Girls' cruiser</td><td class="price">$29</td><td class="price">$120</td><td class="note">Ask - snowbird rates</td></tr>
      <tr><td class="svc">Boys' bike</td><td class="price">$29</td><td class="price">$120</td><td class="note">Ask - snowbird rates</td></tr>
      <tr><td class="svc">E-bike</td><td class="price">$55</td><td class="price">$200</td><td class="note">Strong seasonal demand</td></tr>
    </tbody></table>
  </div>
  <p style="color:var(--muted);font-size:13.5px;margin-top:16px" data-reveal>Helmet and lock included with every rental. <strong style="color:var(--deep)">Delivery and pickup: free on rentals of 3 days or more</strong>, otherwise a flat $25 - or pick up at the shop at no charge. Paddleboard rentals coming soon.</p>
  <div data-reveal style="max-width:720px;margin:26px auto 0;display:flex;flex-wrap:wrap;gap:12px;justify-content:center">
    <div style="flex:1;min-width:150px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px;text-align:center;box-shadow:var(--shadow-s)">
      <div style="font-size:26px">&#129686;</div><div style="font-family:'Fraunces',serif;font-weight:600;color:var(--deep);margin-top:4px">Helmet</div>
      <div style="margin-top:4px"><s style="color:var(--muted)">$5</s> <strong style="color:var(--teal-d)">included</strong></div></div>
    <div style="flex:1;min-width:150px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px;text-align:center;box-shadow:var(--shadow-s)">
      <div style="font-size:26px">&#128274;</div><div style="font-family:'Fraunces',serif;font-weight:600;color:var(--deep);margin-top:4px">Lock</div>
      <div style="margin-top:4px"><s style="color:var(--muted)">$5</s> <strong style="color:var(--teal-d)">included</strong></div></div>
    <div style="flex:1;min-width:150px;background:var(--teal-soft);border:1px solid rgba(18,163,160,.3);border-radius:14px;padding:16px 18px;text-align:center">
      <div style="font-size:26px">&#128666;</div><div style="font-family:'Fraunces',serif;font-weight:600;color:var(--deep);margin-top:4px">Delivery</div>
      <div style="margin-top:4px;color:var(--teal-d);font-weight:600">Free on 3+ days</div></div>
  </div>
  <p style="text-align:center;color:var(--muted);font-size:12.5px;margin-top:12px" data-reveal>A helmet and a good lock come with every rental, on us - about $10 of value, included free.</p>
</section>
''' + RESERVE_SECTION + f'''

<section class="sec-tint"><div class="section" style="padding:76px 28px">
  <div class="eyebrow" data-reveal><span>Why rent from us</span></div>
  <h2 class="sub-h" data-reveal>We come to you.</h2>
  <div class="simplegrid">
    <div class="scard" data-reveal><div class="cat">Delivery</div><div class="n">Hotel &amp; Home Drop-off</div><div class="d">We deliver to your hotel, resort or vacation rental and pick it back up. Free on 3+ day rentals, otherwise a flat $25.</div></div>
    <div class="scard" data-reveal><div class="cat">Seasonal</div><div class="n">Snowbird Season Rentals</div><div class="d">Here for the winter? Weekly and monthly packages beat buying and shipping a bike down.</div></div>
    <div class="scard" data-reveal><div class="cat">Easy</div><div class="n">Book by Phone</div><div class="d">Reserve in two minutes - call 561-842-0303 and we'll get you set up.</div></div>
    <div class="scard" data-reveal><div class="cat">Coming soon</div><div class="n">Paddleboards</div><div class="d">Board rentals by the day, weekend, week or season - delivered the same way. Watch this space.</div></div>
  </div>
</div></section>

{cta("Bikes to your hotel<br>by morning.", '<a href="#reserve" class="btn btn-navy btn-lg">Reserve now &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')}
'''
    return head("Bike &amp; E-Bike Rentals, Delivered | Lake Park Bicycles",
                "Bike and e-bike rentals in North Palm Beach, delivered to your hotel, condo or home. Free delivery on 3+ day rentals. Helmet and lock included. Call 561-842-0303.",
                "rentals-hero.png","rentals") + body + footer()

def build_about():
    body = f'''
<section class="page-hero" style="padding-bottom:0"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Meet Tony</div>
  <div class="eyebrow" data-reveal><span>The heart of the shop</span></div>
  <h1 data-reveal>Meet <em>Tony.</em></h1>
</div></section>

<style>.tsplit{{align-items:start}}@media(min-width:1001px){{.tsplit{{grid-template-columns:.9fr 1.1fr}}}}</style>
<section class="section" style="padding-top:34px">
  <div class="split tsplit">
    <div data-reveal><div class="mediaframe" style="aspect-ratio:3/4"><img src="assets/img/tony.jpg" alt="Tony, owner of Lake Park Bicycles, giving a thumbs up in his shop polo"></div></div>
    <div data-reveal>
      <div class="eyebrow"><span>From shop kid to shop owner</span></div>
      <h2 class="sub-h" style="font-size:clamp(34px,4.6vw,54px)">Started at 15.<br><em style="color:var(--teal)">Never left.</em></h2>
      <p style="color:var(--deep);font-size:17px;line-height:1.7;font-weight:600">Tony walked into this bike shop as a high-school kid looking for an after-school job. Fifty years later, he owns the place - and he still can't stay away from the repair stand.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.75;margin-top:16px">At fifteen, what he found was far more than a job. Under the patient mentorship of the shop's owner, <strong>Stuart Weidenfeld</strong>, he learned the craft the right way: truing wheels, tuning gears, and treating every customer like a neighbor.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.75;margin-top:16px">Years later, the chance came to buy the shop from the Weidenfeld family. Going from hands-on employee to owner was the leap of a lifetime - real pressure, real uncertainty, and a legacy he refused to let down. He poured everything into it, and he's run the shop ever since.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.75;margin-top:16px">Today Tony is the owner of the very shop where he trued his first wheel - still sharing his love of cycling with the community that raised him.</p>
    </div>
  </div>
</section>

<section class="sec-teal"><div class="section" style="padding:64px 28px;text-align:center">
  <p data-reveal style="font-family:'Fraunces',Georgia,serif;font-weight:500;font-style:italic;color:#fff;font-size:clamp(22px,3.2vw,32px);line-height:1.35;max-width:820px;margin:0 auto">&ldquo;I stepped into that bike shop and found far more than a first job - I found my calling.&rdquo;</p>
  <p data-reveal style="color:#bfe3ef;font-size:14px;margin-top:14px;letter-spacing:.08em;text-transform:uppercase;font-weight:600">Tony &middot; Owner, Lake Park Bicycles</p>
</div></section>

<section class="section" style="padding-top:72px">
  <div class="stats" style="border-top:0;padding-top:0;margin-top:0">
    <div class="stat" data-reveal><div class="n">15</div><div class="l">The age he walked in</div></div>
    <div class="stat" data-reveal><div class="n">50</div><div class="l">Years in the same shop</div></div>
    <div class="stat" data-reveal><div class="n">10k+</div><div class="l">Bikes kept rolling</div></div>
    <div class="stat" data-reveal><div class="n">1</div><div class="l">Calling, followed for life</div></div>
  </div>
</section>

<section class="sec-tint"><div class="split section" style="padding-top:76px;padding-bottom:76px">
    <div data-reveal>
      <div class="eyebrow"><span>Part of the neighborhood</span></div>
      <h2 class="sub-h">You've probably seen him around.</h2>
      <p style="color:var(--slate);font-size:16px;line-height:1.75">School events, charity rides, community nights - if the neighborhood is out, odds are Tony is too, talking bikes with anyone who will listen (and usually fixing a flat on the spot). The kids he fitted for their first bikes now bring in their own kids. That's the whole point.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.75;margin-top:16px">These days Tony will come to you, too - tune-ups and rentals picked up and delivered anywhere from Jupiter to Lake Park. Stop by the shop, or let him bring the shop to your door. Fresh bikes are rolling onto the floor soon.</p>
    </div>
    <div data-reveal><div class="mediaframe" style="aspect-ratio:4/5"><img src="assets/img/tony-community.jpg" alt="The Lake Park Bicycles truck loaded with bikes, out on a delivery run"></div></div>
</div></section>

{REVIEWS}

{tony_tip_month()}

{cta("Come say hi.<br>Tony's got your bike.", '<a href="tune-up.html" class="btn btn-navy btn-lg">The $129 tune-up &rarr;</a><a href="rent.html" class="btn btn-ghost-light btn-lg">Rent a bike</a>')}
'''
    return head("Meet Tony - Lake Park Bicycles, Est. 1975",
                "Meet Tony: he walked into this North Palm Beach bike shop at 15, learned the craft from Stuart Weidenfeld, bought the shop, and has kept the community rolling for 50 years.",
                "tony.jpg","about") + body + footer()

def build_contact():
    body = f'''
<section class="photo-hero"><div class="hero-bg"><img src="assets/img/visit-hero.png" alt="A teal beach cruiser resting by the Intracoastal at golden hour in North Palm Beach"></div><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Visit</div>
  <div class="eyebrow" data-reveal><span>Say hello</span></div>
  <h1 data-reveal>Let's get you <em>rolling.</em></h1>
  <p class="lead" data-reveal>Call or send a note - a real person answers. Tune-up pickups and rental deliveries across the Palm Beaches.</p>
</div></section>

<section class="section" style="padding-top:66px;padding-bottom:22px">
  <div class="eyebrow" data-reveal><span>What brings you in?</span></div>
  <h2 class="sub-h" data-reveal>Pick your lane.</h2>
  <div class="path-grid">
    <a class="path-card" href="rent.html" data-reveal>
      <div class="pc-img"><img src="assets/img/rentals-hero.png" alt="Rental bikes delivered to your door"></div>
      <div class="pc-body">
        <div class="pc-ey">Renting a bike?</div>
        <div class="pc-t">Reserve a bike</div>
        <div class="pc-d">Cruisers, e-bikes and kids' bikes delivered to your door. Pick your dates - we drop them off and pick them back up.</div>
        <span class="pc-go">Start reservation &rarr;</span>
      </div>
    </a>
    <a class="path-card" href="tune-up.html" data-reveal>
      <div class="pc-img"><img src="assets/img/service-hero.png" alt="A bike getting a tune-up on the workshop stand"></div>
      <div class="pc-body">
        <div class="pc-ey">Need a tune-up?</div>
        <div class="pc-t">Book the $129 tune-up</div>
        <div class="pc-d">We pick up, tune, and return your bike. See the packages and grab a pickup window that works for you.</div>
        <span class="pc-go">See tune-ups &rarr;</span>
      </div>
    </a>
  </div>
</section>

<section class="section" style="padding-top:30px;padding-bottom:44px">
  <div class="contact-grid">
    <div data-reveal>
      <div class="eyebrow"><span>Contact us</span></div>
      <h2 class="sub-h" style="margin-bottom:10px">Just have a question?</h2>
      <p style="color:var(--slate);font-size:16px;line-height:1.6;max-width:440px;margin:0 0 22px">Happy to help. Drop us a note and Tony will get back to you as soon as he can - usually the same day.</p>
      <form class="cform" name="contact" method="POST" data-netlify="true" action="https://api.web3forms.com/submit" id="contactForm">
        <input type="hidden" name="access_key" value="dfacc1b4-52f3-4b47-bc9c-bbd01c81fdc1">
        <input type="hidden" name="subject" value="New Website Message - Lake Park Bicycles">
        <input type="hidden" name="from_name" value="Lake Park Bicycles Website">
        <input type="hidden" name="redirect" value="https://lakeparkbicycles.com/thanks">
        <input type="checkbox" name="botcheck" style="display:none !important" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="form-name" value="contact">
        <input type="text" name="name" placeholder="Your name" required aria-label="Your name">
        <input type="tel" name="phone" placeholder="Phone number" required aria-label="Phone number">
        <input type="email" name="email" placeholder="Email address" aria-label="Email">
        <textarea name="message" placeholder="How can we help?" required aria-label="Your message"></textarea>
        <button class="btn btn-coral" type="submit" style="justify-self:start">Send message &rarr;</button>
      </form>
    </div>
    <aside class="contact-info" data-reveal>
      <div class="ci-card">
        <div class="ci-row"><span class="ci-k">Call</span><a href="tel:+15618420303" class="ci-v ci-link">561&middot;842&middot;0303</a></div>
        <div class="ci-row"><span class="ci-k">Hours</span><span class="ci-v"><b>Mon&ndash;Fri</b>&nbsp;&nbsp;10&ndash;6<br><b>Saturday</b>&nbsp;&nbsp;10&ndash;3<br><b>Sunday</b>&nbsp;&nbsp;Closed</span></div>
        <div class="ci-row"><span class="ci-k">Find us</span><span class="ci-v">910 Northlake Blvd<br>North Palm Beach, FL 33408</span></div>
        <a href="https://maps.google.com/?q=910+Northlake+Blvd,+North+Palm+Beach,+FL+33408" target="_blank" rel="noopener" class="btn btn-outline ci-dir">Get directions &rarr;</a>
        <p class="ci-note">Open Mon-Sat - stop in, or let us come to you.</p>
      </div>
    </aside>
  </div>
</section>

<section class="map-wide" data-reveal>
  <iframe src="https://www.google.com/maps?q=910+Northlake+Blvd,+North+Palm+Beach,+FL+33408&output=embed" title="Map to Lake Park Bicycles" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>
'''
    return head("Visit &amp; Contact - Lake Park Bicycles - 561-842-0303",
                "Questions? Call 561-842-0303 or send a note and Tony gets right back to you. Rentals delivered and $129 tune-up pickups across the Palm Beaches.",
                "cat-city.png","visit") + body + RESERVE_JS + footer()

def build_rent():
    body = RESERVE_STYLE + '''
<section class="page-hero" style="padding-bottom:18px"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / <a href="rentals.html">Rentals</a> / Reserve</div>
  <h1 data-reveal style="text-align:center">Reserve your <em>ride.</em></h1>
  <p class="lead" data-reveal style="text-align:center;max-width:560px;margin:14px auto 0">Everything stays on one page - scroll up any time to see or change what you picked, and the total updates as you go.</p>
</div></section>
<div class="rentbanner" data-reveal><div class="frame"><img src="assets/img/fleet.jpg" alt="Our rental fleet lined up near the beach"><span class="chip">Delivered - Jupiter to Lake Park</span></div></div>
''' + RESERVE_FLOW
    return head("Reserve a Bike - Lake Park Bicycles Rentals",
                "Reserve your rental in under a minute: pick your bikes, how long, and delivery or free shop pickup. Bikes and e-bikes delivered from Jupiter to Lake Park.",
                "fleet.jpg","rentals") + body + footer()

def build_book():
    BODY = r"""
<style>
.wiz{max-width:880px;margin:0 auto;padding:40px 28px 96px}
.wizsteps{display:flex;gap:8px;justify-content:center;margin-bottom:10px}
.wizsteps i{width:38px;height:5px;border-radius:99px;background:var(--line-2);transition:.3s}
.wizsteps i.on{background:var(--teal)}
.wpanel{display:none}
.wpanel.on{display:block;animation:wfade .35s ease;padding:30px 0 34px;border-bottom:1px dashed var(--line-2)}
.wpanel.on:last-of-type{border-bottom:0}
@keyframes wfade{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.wq{font-family:"Fraunces",Georgia,serif;font-weight:600;color:var(--deep);font-size:clamp(24px,3.6vw,36px);text-align:center;margin:0 0 8px}
.wsub{text-align:center;color:var(--muted);font-size:14.5px;margin:0 0 26px;max-width:600px;margin-left:auto;margin-right:auto}
.bikecard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px 18px 20px;margin-bottom:14px;box-shadow:var(--shadow-s)}
.bikehd{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.bikelabel{font-family:"Fraunces",serif;font-weight:600;color:var(--deep);font-size:18px}
.bikerm{background:none;border:0;color:var(--coral);font-weight:600;font-size:13px;cursor:pointer;padding:4px}
.pkgpills{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.pkgpill{background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 8px;text-align:center;cursor:pointer;font-family:inherit;font-size:13.5px;color:var(--deep);font-weight:600;transition:.15s;line-height:1.25}
.pkgpill b{display:block;color:var(--teal-d);font-weight:700;margin-top:3px;font-size:14px}
.pkgpill:hover{border-color:var(--line-2)}
.pkgpill.sel{border-color:var(--teal);background:var(--teal-soft)}
.otherbox{display:grid;gap:10px;margin-top:12px}
.otherbox select,.otherbox input{background:#fff;border:1px solid var(--line-2);border-radius:12px;padding:11px 14px;color:var(--deep);font-family:inherit;font-size:14px;outline:none;width:100%}
.otherbox select:focus,.otherbox input:focus{border-color:var(--teal)}
.addbike{background:none;border:2px dashed var(--line-2);border-radius:12px;padding:12px 22px;color:var(--teal-d);font-weight:600;font-family:inherit;font-size:14.5px;cursor:pointer}
.addbike:hover{border-color:var(--teal);background:var(--teal-soft)}
.freehint{max-width:580px;margin:20px auto 0;text-align:center;font-size:14px;padding:13px 18px;border-radius:12px;background:var(--sand-2);color:var(--slate);display:none}
.freehint.on{background:var(--teal-soft);color:var(--teal-d)}
.wnext{display:flex;justify-content:center;margin-top:28px}
.optrow{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.optcard{background:#fff;border:2px solid var(--line);border-radius:18px;padding:22px 18px;text-align:center;cursor:pointer;transition:.2s}
.optcard:hover{transform:translateY(-3px)}
.optcard.sel{border-color:var(--teal);box-shadow:0 10px 26px rgba(18,163,160,.16)}
.optcard .t{font-family:"Fraunces",serif;font-weight:600;color:var(--deep);font-size:19px}
.optcard .d{color:var(--muted);font-size:12.5px;margin-top:6px}
.wfield{display:grid;gap:14px;max-width:480px;margin:26px auto 0}
.wfield input,.wfield select{background:#fff;border:1px solid var(--line-2);border-radius:14px;padding:14px 16px;color:var(--deep);font-family:inherit;font-size:15px;outline:none;width:100%}
.wfield input:focus,.wfield select:focus{border-color:var(--teal)}
.wtotal{position:sticky;bottom:12px;background:var(--deep);color:#fff;border-radius:16px;padding:14px 22px;display:flex;justify-content:space-between;align-items:center;margin-top:26px;box-shadow:0 -6px 30px rgba(14,58,77,.2)}
.wtotal .lab{font-size:12.5px;color:#bfe3ef}
.wtotal .amt{font-family:"Fraunces",serif;font-weight:700;font-size:24px}
.rvw{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;max-width:560px;margin:0 auto}
.rvw .row{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-bottom:1px solid var(--line);font-size:14.5px;color:var(--slate)}
.rvw .row b{color:var(--deep);white-space:nowrap}
.rvw .row:last-child{border-bottom:0}
.rvw .bh{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--teal-d);padding:16px 0 4px}
.rvw .row.sub b,.rvw .row.sub span{font-weight:600}
.rvw .row.free span{color:var(--teal-d);font-weight:700}
.rvw .row.free s{color:var(--muted);font-weight:400}
.rvw .row.grand{border-top:2px solid var(--deep);margin-top:2px}
.rvw .row.grand b,.rvw .row.grand span{color:var(--deep);font-weight:700;font-size:16px}
.wedit{text-align:center;color:var(--muted);font-size:12.5px;margin-top:12px}
@media(max-width:560px){.pkgpills{grid-template-columns:1fr 1fr}.optrow{grid-template-columns:1fr}}
</style>
<section class="page-hero" style="padding-bottom:16px"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Book</div>
  <h1 data-reveal style="text-align:center">Book your <em>service.</em></h1>
  <p class="lead" data-reveal style="text-align:center;max-width:600px;margin:14px auto 0">Tune-up, repair, or a quick fix - add each bike, tell us what it needs, and we come get it. Your total and delivery update as you go. Pickups run Mon-Sat, 9 to 4.</p>
</div></section>
<div style="max-width:1000px;margin:4px auto 0;padding:0 28px" data-reveal>
  <img src="assets/img/service-mechanic.png" alt="A Lake Park Bicycles mechanic servicing a bike on the repair stand" style="width:100%;height:min(32vh,290px);object-fit:cover;border-radius:20px;box-shadow:var(--shadow)">
</div>
<div class="wiz">
  <div class="wizsteps"><i class="on"></i><i id="sb2"></i><i id="sb3"></i></div>

  <div class="wpanel on" id="wp1">
    <h2 class="wq">1. Your bikes</h2>
    <p class="wsub">Pick a tune-up - <strong>good, better or best</strong> - or choose <strong>Other</strong> for a specific repair. Add as many bikes as you like, each with its own service.</p>
    <div id="bikelist"></div>
    <div style="text-align:center;margin-top:6px"><button type="button" class="addbike" onclick="addBike()">+ Add another bike</button></div>
    <div class="freehint" id="freehint"></div>
    <div class="wnext" id="nb1"><button class="btn btn-teal btn-lg" onclick="unlock(2,'nb1')">Next: how we get them &rarr;</button></div>
  </div>

  <div class="wpanel" id="wp2">
    <h2 class="wq">2. How should we get the bikes?</h2>
    <p class="wsub" id="delnote">Pickup + return is within 10 miles - Jupiter to Lake Park.</p>
    <div class="optrow">
      <div class="optcard" id="m-deliver" onclick="mode('deliver')"><div class="t">Come get them</div><div class="d" id="delfeetxt">Pickup + return</div></div>
      <div class="optcard" id="m-shop" onclick="mode('shop')"><div class="t">I'll drop them off - free</div><div class="d">910 Northlake Blvd</div></div>
    </div>
    <div class="wfield">
      <input type="date" id="f-date" aria-label="Preferred day">
      <select id="f-window" aria-label="Window"><option value="" disabled selected>2-hour window (Mon-Sat)</option><option>9:00 - 11:00 am</option><option>11:00 am - 1:00 pm</option><option>1:00 - 3:00 pm</option><option>2:00 - 4:00 pm</option></select>
      <div class="ac-wrap"><input type="text" id="f-address" placeholder="Start typing your address or hotel name" autocomplete="off"><div class="ac-list" id="f-addr-list"></div></div>
      <input type="text" id="f-name" placeholder="Your name">
      <input type="tel" id="f-phone" placeholder="Phone (to confirm your booking)">
      <input type="email" id="f-email" placeholder="Email (optional)">
    </div>
    <div class="wnext" id="nb2"><button class="btn btn-teal btn-lg" onclick="unlock(3,'nb2')">Review &rarr;</button></div>
  </div>

  <div class="wpanel" id="wp3">
    <h2 class="wq">3. Look good?</h2>
    <p class="wsub">Tap send and it comes straight to us; we'll be in touch within the hour to confirm your window (Mon-Sat, 9-4).</p>
    <div class="rvw" id="rvw"></div>
    <div class="wtotal"><div><div class="lab" id="t-lab">Total incl. 7% tax</div></div><div class="amt" id="t-amt">$0</div></div>
    <form name="tuneup" method="POST" data-netlify="true" action="https://api.web3forms.com/submit" id="nf-tuneup" style="display:none">
      <input type="hidden" name="access_key" value="dfacc1b4-52f3-4b47-bc9c-bbd01c81fdc1">
      <input type="hidden" name="subject" value="New Tune-Up / Repair Booking - Lake Park Bicycles">
      <input type="hidden" name="from_name" value="Lake Park Bicycles Website">
      <input type="hidden" name="redirect" value="https://lakeparkbicycles.com/thanks">
      <input type="checkbox" name="botcheck" style="display:none !important" tabindex="-1" autocomplete="off" aria-hidden="true">
      <input type="hidden" name="form-name" value="tuneup">
      <input type="hidden" name="the_package"><input type="hidden" name="pickup"><input type="hidden" name="address"><input type="hidden" name="day"><input type="hidden" name="name"><input type="hidden" name="phone"><input type="hidden" name="email"><input type="hidden" name="total">
    </form>
    <div class="wnext"><a class="btn btn-coral btn-lg" id="sendBtn" href="#">Send my booking &rarr;</a></div>
    <p id="sentMsg" style="display:none;max-width:520px;margin:18px auto 0;background:var(--teal-soft);border:1px solid rgba(18,163,160,.35);border-radius:14px;padding:16px 20px;text-align:center;color:var(--teal-d);font-weight:600;font-size:15px">&#10003; Got it! Your booking is in - we'll be in touch within the hour to confirm your window (Mon-Sat, 9-4).</p>
    <p class="wedit">Prefer to talk? Call <a href="tel:+15618420303" style="color:var(--teal-d);font-weight:600">561-842-0303</a>. You'll sign a quick service agreement at handoff.</p>
  </div>
</div>
<script>
var bikes=[{pkg:null,otype:'',onote:''}];
var md=null;
var PKG={safety:{n:'Safety Check',p:99},full:{n:'Full Tune-Up',p:129},overhaul:{n:'Signature Overhaul',p:199},other:{n:'Other / repair',p:0,est:true}};
var OPTS=[['safety','Safety Check','$99'],['full','Full Tune-Up','$129'],['overhaul','Overhaul','$199'],['other','Other / repair','']];
var REPAIRS=['Flat / tube replacement','Brake repair or adjustment','Gears / shifting problem','Wheel truing (wobble)','New tire(s)','Chain replacement','Bearing / hub / bottom bracket','E-bike diagnostic','Assembly (boxed bike)','Not sure - please take a look','Something else'];
function money(x){return '$'+(Math.round(x*100)/100).toFixed(2).replace(/\.00$/,'');}
function fmtDate(v){if(!v)return '';var d=new Date(v+'T12:00:00');return d.toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'});}
function renderBikes(){
  var el=document.getElementById('bikelist'),h='';
  bikes.forEach(function(b,i){
    h+='<div class="bikecard"><div class="bikehd"><span class="bikelabel">Bike '+(i+1)+'</span>'+(bikes.length>1?'<button type="button" class="bikerm" onclick="removeBike('+i+')">Remove</button>':'')+'</div><div class="pkgpills">';
    OPTS.forEach(function(o){h+='<button type="button" class="pkgpill'+(b.pkg===o[0]?' sel':'')+'" onclick="setPkg('+i+',\''+o[0]+'\')">'+o[1]+(o[2]?' <b>'+o[2]+'</b>':'')+'</button>';});
    h+='</div>';
    if(b.pkg==='other'){
      var opts='<option value="">What does it need?</option>';
      REPAIRS.forEach(function(r){opts+='<option'+(b.otype===r?' selected':'')+'>'+r+'</option>';});
      h+='<div class="otherbox"><select onchange="setOther('+i+',this.value)">'+opts+'</select><input type="text" placeholder="Tell us more (optional)" value="'+(b.onote||'').replace(/"/g,'&quot;')+'" oninput="setNote('+i+',this.value)"></div>';
    }
    h+='</div>';
  });
  el.innerHTML=h;updateHints();
}
function addBike(){bikes.push({pkg:null,otype:'',onote:''});renderBikes();}
function removeBike(i){bikes.splice(i,1);renderBikes();refresh();}
function setPkg(i,k){bikes[i].pkg=k;renderBikes();refresh();}
function setOther(i,v){bikes[i].otype=v;refresh();}
function setNote(i,v){bikes[i].onote=v;refresh();}
function calc(){
  var sub=0,anyBike=false,hasEst=false,items=[];
  bikes.forEach(function(b,i){if(b.pkg){anyBike=true;var P=PKG[b.pkg];sub+=P.p;if(P.est)hasEst=true;items.push({i:i,n:P.n,p:P.p,est:!!P.est,ot:b.otype,on:b.onote});}});
  var freeDel=sub>=129;
  var fee=(md==='deliver')?(freeDel?0:25):0;
  var tax=(sub+fee)*0.07;
  return {sub:sub,items:items,anyBike:anyBike,hasEst:hasEst,freeDel:freeDel,fee:fee,tax:tax,total:sub+fee+tax};
}
function updateHints(){
  var c=calc(),fh=document.getElementById('freehint');if(!fh)return;
  if(!c.anyBike){fh.style.display='none';return;}
  fh.style.display='block';
  if(c.sub>=129){fh.className='freehint on';fh.innerHTML='&#127881; That\'s '+money(c.sub)+' of service - <strong>free pickup &amp; delivery</strong> is on us!';}
  else if(c.hasEst){fh.className='freehint';fh.innerHTML='We\'ll price your repair once we see the bike. Doorstep pickup is a flat $25 (free once the ticket reaches $129).';}
  else{fh.className='freehint';fh.innerHTML='You\'re at '+money(c.sub)+'. Reach $129 (another bike, or bump one to a Full Tune-Up) and <strong>pickup &amp; delivery is free</strong>.';}
}
function mode(v){md=v;['deliver','shop'].forEach(function(x){document.getElementById('m-'+x).classList.toggle('sel',x===v);});document.getElementById('f-address').style.display=(v==='deliver')?'block':'none';updDelText();refresh();}
function updDelText(){var t=document.getElementById('delfeetxt'),c=calc();if(!t)return;if(!md){t.textContent='Pickup + return';return;}if(c.freeDel){t.innerHTML='Pickup + return: <s style="color:#9db3bb">$25</s> <strong style="color:var(--teal-d)">FREE</strong>';}else{t.textContent='Pickup + return: $25';}}
function opened(n){return document.getElementById('wp'+n).classList.contains('on');}
function unlock(n,btn){
  if(n===2){
    var c=calc();
    if(!c.anyBike){alert('Add at least one bike and pick what it needs.');return;}
    for(var i=0;i<bikes.length;i++){if(!bikes[i].pkg){alert('Pick a service for Bike '+(i+1)+' (or remove it).');return;}if(bikes[i].pkg==='other'&&!bikes[i].otype){alert('Tell us what Bike '+(i+1)+' needs - pick from the list (or "Not sure").');return;}}
  }
  if(n===3){
    if(!md){alert('Tell us - should we come get them, or will you drop them off?');return;}
    if(!document.getElementById('f-date').value){alert('Pick a day.');return;}
    if(!document.getElementById('f-window').value){alert('Pick a 2-hour window.');return;}
    if(md==='deliver'&&!document.getElementById('f-address').value.trim()){alert('We need the pickup address.');return;}
    if(!document.getElementById('f-name').value.trim()||!document.getElementById('f-phone').value.trim()){alert('We need your name and phone so we can confirm.');return;}
  }
  var pnl=document.getElementById('wp'+n);pnl.classList.add('on');
  if(btn)document.getElementById(btn).style.display='none';
  var sb=document.getElementById('sb'+n);if(sb)sb.classList.add('on');
  refresh();setTimeout(function(){pnl.scrollIntoView({behavior:'smooth',block:'start'});},60);
}
function refresh(){updateHints();updDelText();if(opened(3))build();}
function bikeSummary(){var c=calc();return c.items.map(function(it,idx){if(it.n==='Other / repair'){return 'Bike '+(idx+1)+': Repair - '+(it.ot||'unspecified')+(it.on?' ('+it.on+')':'');}return 'Bike '+(idx+1)+': '+it.n+' ('+money(it.p)+')';}).join('; ');}
function build(){
  var c=calc();
  var dt=document.getElementById('f-date').value,win=document.getElementById('f-window').value||'(window TBD)';
  var addr=document.getElementById('f-address').value.trim();
  var nm=document.getElementById('f-name').value.trim(),ph=document.getElementById('f-phone').value.trim(),em=document.getElementById('f-email').value.trim();
  var h='';
  h+='<div class="row"><b>Bikes</b><span>'+c.items.length+'</span></div>';
  h+='<div class="row"><b>Pickup</b><span>'+(md==='shop'?'Drop off at the shop (free)':'We come get them'+(addr?' - '+addr:''))+'</span></div>';
  h+='<div class="row"><b>Day</b><span>'+(dt?fmtDate(dt):'(TBD)')+' &middot; '+win+'</span></div>';
  h+='<div class="row"><b>Contact</b><span>'+(nm?nm+' &middot; ':'')+ph+(em?' &middot; '+em:'')+'</span></div>';
  h+='<div class="bh">The math</div>';
  c.items.forEach(function(it,idx){var lab=(it.n==='Other / repair'&&it.ot)?('Repair: '+it.ot):it.n;h+='<div class="row"><b>Bike '+(idx+1)+' &middot; '+lab+'</b><span>'+(it.est?'we quote it':money(it.p))+'</span></div>';});
  if(md==='deliver'){
    if(c.freeDel){h+='<div class="row free"><b>Pickup + delivery</b><span><s>$25</s> FREE &#127881;</span></div>';}
    else{h+='<div class="row"><b>Pickup + delivery</b><span>$25</span></div>';}
  }
  h+='<div class="row sub"><b>Subtotal</b><span>'+money(c.sub+c.fee)+(c.hasEst?'+':'')+'</span></div>';
  h+='<div class="row"><b>Sales tax (7%)</b><span>'+money(c.tax)+'</span></div>';
  h+='<div class="row grand"><b>Total</b><span>'+money(c.total)+(c.hasEst?'+':'')+'</span></div>';
  document.getElementById('rvw').innerHTML=h;
  document.getElementById('t-amt').textContent=money(c.total)+(c.hasEst?'+':'');
  document.getElementById('t-lab').textContent=(c.hasEst?'Estimate incl. 7% tax':'Total incl. 7% tax');
}
document.addEventListener('input',function(e){if(e.target&&/^f-/.test(e.target.id))refresh();});
document.getElementById('sendBtn').addEventListener('click',function(e){
  e.preventDefault();
  var c=calc();
  if(!c.anyBike||!md||!document.getElementById('f-date').value||!document.getElementById('f-window').value||(md==='deliver'&&!document.getElementById('f-address').value.trim())||!document.getElementById('f-name').value.trim()||!document.getElementById('f-phone').value.trim()){
    alert('Almost there - add your bikes + packages, pickup method, a day and window, and your name and phone.');return;}
  var btn=this;btn.textContent='Sending...';btn.style.pointerEvents='none';
  var f=document.getElementById('nf-tuneup');
  f.elements['the_package'].value=bikeSummary();
  f.elements['pickup'].value=(md==='shop'?'Shop drop-off (free)':('We pick up'+(c.freeDel?' - FREE (service over $129)':' - $25')));
  f.elements['address'].value=(md==='deliver'?document.getElementById('f-address').value.trim():'(shop drop-off)');
  f.elements['day'].value=fmtDate(document.getElementById('f-date').value)+' '+document.getElementById('f-window').value;
  f.elements['name'].value=document.getElementById('f-name').value.trim();
  f.elements['phone'].value=document.getElementById('f-phone').value.trim();
  f.elements['email'].value=document.getElementById('f-email').value.trim()||'(none)';
  f.elements['total'].value=money(c.total)+(c.hasEst?'+ (estimate)':'')+' incl 7% tax';
  f.submit();
});
(function(){
  var d=document.getElementById('f-date');if(d){d.min=new Date().toISOString().split('T')[0];
    d.addEventListener('change',function(){if(d.value&&new Date(d.value+'T12:00:00').getDay()===0){alert('We run pickups Monday through Saturday. Pick another day and we will make it work.');d.value='';}});}
  var hh=(location.hash||'').replace('#','');if(hh==='safety'||hh==='full'||hh==='overhaul'){bikes[0].pkg=hh;}
  renderBikes();
})();
</script>
"""
    return head("Book a Service or Repair - Lake Park Bicycles",
                "Book doorstep bike service: a tune-up (Safety Check $99, Full Tune-Up $129, Overhaul $199) or any repair - flats, brakes, gears, wheels, e-bikes. Pickup and delivery, free once your ticket reaches $129.",
                "service-hero.png","tuneup") + BODY + ADDR_AC + footer()

def build_thanks():
    body = '''
<section class="page-hero" style="padding-bottom:36px"><div class="in">
  <div class="eyebrow" data-reveal><span>Got it</span></div>
  <h1 data-reveal>You're all <em>set.</em></h1>
  <p class="lead" data-reveal>Thanks - your request came straight to us. We'll reach out within the hour during shop hours (Mon-Sat, 9-4) to confirm the details. Nothing is due now.</p>
</div></section>
<section class="section" style="padding-top:14px;padding-bottom:96px">
  <div data-reveal style="max-width:560px;background:var(--shell);border:1px solid var(--line);border-radius:20px;box-shadow:var(--shadow-s);padding:30px 30px 28px">
    <div style="display:flex;gap:14px;align-items:flex-start;padding-bottom:18px;border-bottom:1px solid var(--line)"><span style="font-size:22px">&#128222;</span><div style="color:var(--slate);font-size:15.5px;line-height:1.55">Want to talk sooner? Call the shop at <a href="tel:+15618420303" style="color:var(--teal-d);font-weight:600">561-842-0303</a>.</div></div>
    <div style="display:flex;gap:14px;align-items:flex-start;padding:18px 0 24px"><span style="font-size:22px">&#128241;</span><div style="color:var(--slate);font-size:15.5px;line-height:1.55">Keep an eye on your phone - Tony confirms your window personally, usually the same day.</div></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a href="index.html" class="btn btn-navy">Back to home</a><a href="rentals.html" class="btn btn-outline">See rentals</a></div>
  </div>
</section>
'''
    return head("Thank you - Lake Park Bicycles",
                "Thanks - we received your request and will be in touch within the hour to confirm.",
                "cat-city.png","") + body + footer()

BASE = "https://www.lakeparkbicycles.com"

CITIES = [
 {"slug":"jupiter","geo":(26.9342,-80.0942),"name":"Jupiter",
  "blurb":"From Abacoa to Jupiter Farms and out to the Island, the bike shop comes to your driveway.",
  "hoods":"Abacoa, Jupiter Farms, Jupiter Island, Admirals Cove &amp; Tequesta",
  "drive":"about 15 minutes up US-1",
  "ridesintro":"Jupiter is one of the best places to ride in the county - shady river trails, a breezy inlet, and quiet beach paths. Here are four we send folks to.",
  "rides":[("Riverbend Park","Ten miles of hard-packed shell trails winding along the Loxahatchee through shady oaks and marsh - the best family ride in Jupiter."),
           ("Jupiter Beach &amp; the Lighthouse","A flat, breezy spin past the historic Jupiter Inlet Lighthouse and down along the sand."),
           ("Ocean Cay Park","Quiet paved paths and a boardwalk out to the dune line - gentle enough for the littlest riders."),
           ("Jupiter Ridge Natural Area","Sandy trails and boardwalks through coastal scrub with surprise ocean overlooks - a quieter, wilder ride.")]},
 {"slug":"palm-beach-gardens","geo":(26.8234,-80.1387),"name":"Palm Beach Gardens",
  "blurb":"PGA National to Mirasol to Downtown at the Gardens, we bring tune-ups and rentals to your door.",
  "hoods":"PGA National, Mirasol, BallenIsles, Old Palm &amp; Downtown at the Gardens",
  "drive":"about 10 minutes west on Northlake",
  "ridesintro":"The Gardens is built for cyclists - wide landscaped pathways and real nature preserves minutes from the neighborhoods. A few favorites:",
  "rides":[("The Bluegill Trail","A sunny paved path along the C-18 canal reaching toward Grassy Waters Preserve - miles of uninterrupted riding."),
           ("Frenchman's Forest Natural Area","Shaded, easy nature trails through pine flatwoods and hardwood hammock, right in the middle of town."),
           ("PGA Boulevard pathways","Wide, protected bike paths connect the Gardens neighborhoods, shops and parks - easy cruising for the whole family."),
           ("Gardens North County District Park","Miles of flat, shady paved loops around lakes and ballfields - a great easy family spin.")]},
 {"slug":"juno-beach","geo":(26.8784,-80.0534),"name":"Juno Beach",
  "blurb":"Beachfront condos to Juno Isles, we deliver rentals and pick up tune-ups at your door.",
  "hoods":"Juno Beach, Juno Isles, Seminole Landing &amp; the beachfront condos",
  "drive":"about 10 minutes north on US-1",
  "ridesintro":"Juno Beach is made for a sunrise cruise - the ocean on one side, natural areas on the other. Start here:",
  "rides":[("Juno Beach Pier","Ride the oceanfront path to the pier and back - flat, scenic and impossible to get lost on."),
           ("Loggerhead Marinelife Center","Pedal over to see the sea turtles, then loop the shaded grounds - a favorite with kids."),
           ("Juno Dunes Natural Area","Boardwalk and sandy trails through coastal scrub with wide views over the dunes and ocean."),
           ("The A1A beach cruise","Point the bikes north along scenic A1A and ride the ocean breeze all the way toward Jupiter and back.")]},
 {"slug":"north-palm-beach","geo":(26.8176,-80.0581),"name":"North Palm Beach",
  "blurb":"We're right here at 910 Northlake Blvd - your neighborhood bike shop, come to you.",
  "hoods":"Old Port Cove, Lost Tree, the Country Club village &amp; Anchorage Park",
  "drive":"minutes from your door - this is home",
  "ridesintro":"This is our home turf, and we ride it every day. These are the spots we point neighbors to:",
  "rides":[("Anchorage Park","Waterfront paths, playgrounds and a boat ramp - an easy, breezy loop right in the village."),
           ("The Lake Trail","Hop across to Palm Beach and ride six traffic-free miles along the Intracoastal past the grand old estates."),
           ("John D. MacArthur Beach State Park","Just up on Singer Island - a boardwalk over the estuary to a wild, uncrowded beach."),
           ("Lakeside Park","A calm Intracoastal-front green space with easy paths and big water views, right in the Village.")]},
 {"slug":"lake-park","geo":(26.7998,-80.0678),"name":"Lake Park",
  "blurb":"Practically neighbors - Kelsey City to the marina district, we're minutes away.",
  "hoods":"the Kelsey City historic district, the marina district &amp; the Foundry",
  "drive":"just up the road - we're practically neighbors",
  "ridesintro":"Lake Park is small, walkable and right on the water - perfect for an easy roll. Our picks:",
  "rides":[("Lake Park Harbor Marina","Ride the waterfront out to the marina and Riverwalk for wide Intracoastal views and a bite to eat."),
           ("Kelsey Park","A shady green space on the water with easy paths - a nice, short family loop."),
           ("Singer Island hop","A quick pedal over the bridge puts you on Singer Island's beach and Riverwalk paths."),
           ("The Kelsey City loop","An easy roll through the historic Kelsey City streets past 1920s Mediterranean architecture and the marina.")]},
 {"slug":"singer-island","geo":(26.7889,-80.0342),"name":"Singer Island",
  "blurb":"Beaches, oceanfront resorts and Peanut Island - we bring rental bikes to your hotel or condo and pick up tune-ups right at the door.",
  "hoods":"the oceanfront resorts, Ocean Mall, the Ocean Avenue condos &amp; MacArthur Beach",
  "drive":"a quick hop over the Blue Heron bridge - about 10 minutes",
  "ridesintro":"Singer Island is a barrier-island gem - ocean on one side, the Intracoastal on the other, and Peanut Island a short ferry away. Our picks:",
  "rides":[("John D. MacArthur Beach State Park","A boardwalk over the estuary to nature trails and a wild, uncrowded beach - the best ride on the island."),
           ("The Ocean Avenue beachfront","Flat, breezy cruising past the sand, Ocean Mall and the resort strip - easy for every rider."),
           ("Peanut Island","Hop the ferry and loop the island's paved path past the snorkel lagoon and the old Coast Guard station."),
           ("Riviera Beach Marina & the Riverwalk","A waterfront path along the Intracoastal with wide views, boats and a bite to eat.")]},
]

def weather_widget(c):
    lat,lng=c["geo"]; name=c["name"]
    return ('''
<section class="section" style="padding-top:38px;padding-bottom:0">
  <div class="rideweather" id="rwCard" style="display:none">
    <div class="rw-now"><div class="rw-label">Right now in '''+name+'''</div>
      <div class="rw-temprow"><span class="rw-temp" id="rwTemp">--&deg;</span><span class="rw-cond" id="rwCond"></span></div></div>
    <div class="rw-air"><span class="rw-dot" id="rwDot"></span><div class="rw-airtxt"><span class="rw-airlab">Air quality</span><span id="rwAqi">--</span></div></div>
    <div class="rw-verdict" id="rwVerdict"></div>
  </div>
</section>
<script>
(function(){var LAT='''+str(lat)+''',LNG='''+str(lng)+''',K="AIzaSyDiVe3XM2xLD2TY-JGQP4tu9RduPyYKFWI",NM="'''+name+'''";
var card=document.getElementById("rwCard");if(!card){return;}
fetch("https://weather.googleapis.com/v1/currentConditions:lookup?key="+K+"&location.latitude="+LAT+"&location.longitude="+LNG+"&unitsSystem=IMPERIAL").then(function(r){return r.json();}).then(function(w){
if(!w||!w.temperature){return;}
var t=Math.round(w.temperature.degrees);var c=(w.weatherCondition&&w.weatherCondition.description&&w.weatherCondition.description.text)||"";var ty=(w.weatherCondition&&w.weatherCondition.type)||"";
document.getElementById("rwTemp").innerHTML=t+"&deg;";document.getElementById("rwCond").textContent=c;card.style.display="";
var v,rain=/RAIN|THUNDERSTORM|SHOWER|HAIL|SNOW/.test(ty)||/rain|storm|shower|thunder/i.test(c);
if(rain){v="\\u2614 Wet out there - maybe grab that bike tomorrow.";}else if(t>=92){v="\\u2600\\uFE0F Toasty - ride early, and bring water.";}else if(t<=55){v="\\uD83E\\uDDE5 Cool for Florida - layer up and roll.";}else{v="\\uD83D\\uDEB2 Great day to ride "+NM+".";}
document.getElementById("rwVerdict").textContent=v;
fetch("https://airquality.googleapis.com/v1/currentConditions:lookup?key="+K,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({location:{latitude:LAT,longitude:LNG}})}).then(function(r){return r.json();}).then(function(a){
var i=a&&a.indexes&&a.indexes[0];if(!i){return;}document.getElementById("rwAqi").textContent=(i.category||"").replace(/ air quality/i,"")||"--";
if(i.color){var cc=i.color;document.getElementById("rwDot").style.background="rgb("+Math.round((cc.red||0)*255)+","+Math.round((cc.green||0)*255)+","+Math.round((cc.blue||0)*255)+")";}}).catch(function(){});
}).catch(function(){});
})();
</script>
''')

def build_city(c):
    name = c["name"]; slug = c["slug"]
    rides_html = "".join(
      '<div class="scard" data-reveal><div class="cat">Ride</div><div class="n">'+r[0]+'</div><div class="d">'+r[1]+'</div></div>'
      for r in c["rides"])
    ld = ('<script type="application/ld+json">'
      '{"@context":"https://schema.org","@type":"Service",'
      '"serviceType":"Mobile bike repair, tune-ups and bike rental delivery",'
      '"name":"Bike repair and bike rental in '+name+'",'
      '"provider":{"@type":"BikeStore","name":"Lake Park Bicycles",'
      '"image":"'+BASE+'/assets/img/logo-badge.png","telephone":"+1-561-842-0303","url":"'+BASE+'/","priceRange":"$$",'
      '"address":{"@type":"PostalAddress","streetAddress":"910 Northlake Blvd","addressLocality":"North Palm Beach","addressRegion":"FL","postalCode":"33408","addressCountry":"US"},'
      '"geo":{"@type":"GeoCoordinates","latitude":26.8106,"longitude":-80.0710}},'
      '"areaServed":{"@type":"City","name":"'+name+', Florida"},'
      '"url":"'+BASE+'/'+slug+'"}'
      '</script>')
    body = f'''
<section class="page-hero"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Service areas / {name}</div>
  <div class="eyebrow" data-reveal><span>{name}, Florida</span></div>
  <h1 data-reveal>Bike repair &amp; rentals in <em>{name}.</em></h1>
  <p class="lead" data-reveal>We're the mobile bike shop that comes to {name}. {c["blurb"]} We pick up your bike, tune it on our bench and bring it back - and we deliver rental cruisers, e-bikes and kids' bikes right to your door. No trip to a shop, no loading the car.</p>
  <div class="acts" style="display:flex;gap:14px;flex-wrap:wrap;margin-top:28px" data-reveal><a href="book.html" class="btn btn-coral btn-lg">Book a tune-up &rarr;</a><a href="rent.html" class="btn btn-outline btn-lg">Reserve a rental</a></div>
</div></section>

<section class="towns"><div class="in">
  <span class="lbl">Doorstep service across</span>
  <span class="town">{c["hoods"]}</span>
</div></section>

{weather_widget(c)}

<section class="section" style="padding-top:76px">
  <div class="split" style="align-items:center;gap:48px">
    <div data-reveal>
      <div class="eyebrow"><span>Mobile bike repair in {name}</span></div>
      <h2 class="sub-h">Tune-ups, right to your door.</h2>
      <p style="color:var(--slate);font-size:16.5px;line-height:1.7">Our most-popular <strong>Full Tune-Up is $129 this summer</strong> (regularly $169) with <strong>free pickup and delivery to {name}</strong> - or a quick Safety Check for $99. Any make, any age: beach cruisers, kids' bikes, hybrids, road and mountain bikes. We collect it from your driveway, tune it on the bench, and have it back within 72 hours. 100% happy or we fix it free. E-bikes serviced separately: $20 battery evaluation, electrical diagnostics from $75.</p>
      <a href="tune-up.html" class="btn btn-teal" style="margin-top:22px">See the $129 tune-up &rarr;</a>
    </div>
    <div data-reveal><img src="assets/img/service-mechanic.png" alt="Mobile bike tune-up and repair delivered in {name}, Florida" style="width:100%;border-radius:20px;box-shadow:var(--shadow)"></div>
  </div>
</section>

<section class="sec-tint"><div class="section" style="padding:70px 28px">
  <div class="split" style="align-items:center;gap:48px">
    <div data-reveal><img src="assets/img/fleet.jpg" alt="Bike and e-bike rentals delivered in {name}, Florida" style="width:100%;border-radius:20px;box-shadow:var(--shadow)"></div>
    <div data-reveal>
      <div class="eyebrow"><span>Bike rentals delivered in {name}</span></div>
      <h2 class="sub-h">Bikes to your door.</h2>
      <p style="color:var(--slate);font-size:16.5px;line-height:1.7">Visiting {name} or just want to ride without the hassle? We deliver comfortable men's, women's and kids' bikes plus easy e-bikes to your hotel, condo or home - helmet and lock included free. Daily, weekly and snowbird-season rates. <strong>Free delivery on rentals of 3 days or more</strong>, otherwise a flat $25, or pick up at the shop for free.</p>
      <a href="rent.html" class="btn btn-coral" style="margin-top:22px">Reserve a bike &rarr;</a>
    </div>
  </div>
</div></section>

<section class="section" style="padding-top:76px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Where to ride in {name}</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center;margin-bottom:12px">Our favorite {name} rides.</h2>
  <p style="text-align:center;color:var(--slate);font-size:16px;max-width:640px;margin:0 auto 40px" data-reveal>{c["ridesintro"]}</p>
  <div class="simplegrid rides-grid">{rides_html}</div>
</section>

{GUARANTEE}

<section class="section" style="padding-top:70px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>{name} questions</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center">Good to know.</h2>
  <div class="faq" data-reveal>
    <details><summary>Do you really come all the way to {name}?</summary><p>Yes - {name} is well within our service area, {c["drive"]}. Free doorstep pickup and delivery on the Full Tune-Up and Signature Overhaul; a flat $25 on the $99 Safety Check.</p></details>
    <details><summary>Can you deliver rental bikes to my {name} hotel or rental?</summary><p>Absolutely. Cruisers, e-bikes and kids' bikes delivered to your door anywhere in {name}, helmet and lock included. Delivery is free on rentals of three days or more.</p></details>
    <details><summary>Do you work on bikes you did not sell?</summary><p>Always - any make, any model, any age. Department-store bike or boutique build, it gets the same bench and the same care.</p></details>
    <details><summary>Do you service e-bikes in {name}?</summary><p>Yes, but separately from the pedal-bike packages. The mechanical work is the same; on the electric side it is a $20 battery evaluation or a full electrical diagnostic from $75. We do not source proprietary batteries or controllers, but we will gladly install a part you supply.</p></details>
  </div>
</section>

{cta("Bring the bike shop<br>to " + name + ".", '<a href="book.html" class="btn btn-navy btn-lg">Book my pickup &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')}
'''
    return head(f"{name} Bike Repair &amp; Rentals | Lake Park Bicycles",
                f"Mobile bike repair and bike &amp; e-bike rental delivery in {name}, Florida. $129 doorstep tune-up with free delivery, rentals to your door, any make. Serving {c['hoods']}. Call 561-842-0303.",
                "cat-city.png","",ld) + body + footer()

def build_terms():
    body = '''
<section class="page-hero" style="padding-bottom:26px"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Terms &amp; Conditions</div>
  <div class="eyebrow" data-reveal><span>The fine print</span></div>
  <h1 data-reveal>Terms &amp; <em>Conditions.</em></h1>
</div></section>
<section class="section" style="padding-top:18px"><div class="legal">
  <p class="eff">Effective July 24, 2026</p>
  <p>Welcome to Lake Park Bicycles. These Terms &amp; Conditions ("Terms") govern your use of our website (lakeparkbicycles.com) and the services we provide, including doorstep tune-ups, bicycle repairs, and bicycle and e-bike rentals. By booking a service, renting a bicycle, or using this website, you agree to these Terms. If you do not agree, please do not use our services.</p>

  <h2>1. Who we are</h2>
  <p>Lake Park Bicycles is a family-owned bicycle service and rental business at 910 Northlake Blvd, North Palm Beach, FL 33408, serving North Palm Beach, Lake Park, Palm Beach Gardens, Juno Beach, Jupiter and the surrounding area (generally within about 10 miles of the shop). Reach us at <a href="tel:+15618420303">561-842-0303</a> or lakeparkbicycle@gmail.com.</p>

  <h2>2. Our services</h2>
  <p>We offer mobile bicycle tune-ups and repairs - we pick up, service, and return your bike - and bicycle and e-bike rentals delivered to your location or available for pickup at the shop. Service descriptions, package contents, and prices are shown on our website and are subject to change without notice. E-bike diagnostics and service are quoted separately.</p>

  <h2>3. Booking, scheduling &amp; confirmation</h2>
  <p>Requests made through our website forms, by phone, or by text are <strong>requests, not confirmed appointments</strong>. A booking is confirmed only when we contact you to arrange a date and a two-hour pickup or delivery window. Pickups and deliveries generally run Monday through Saturday, 9 a.m. to 4 p.m. We will do our best to accommodate your preferred time but cannot guarantee a specific slot.</p>

  <h2>4. Pricing, payment &amp; taxes</h2>
  <ul>
    <li>Prices are as listed at the time of booking. Promotional pricing (such as seasonal or summer-sale pricing) is available for a limited time and may end or change without notice.</li>
    <li>Package prices cover labor only. <strong>Parts are extra</strong> and are added only after we contact you with the cost and you approve.</li>
    <li>Applicable Florida state and Palm Beach County sales tax (currently 7%) is added where required.</li>
    <li>Payment is due upon completion of service or at the start of a rental unless otherwise agreed.</li>
  </ul>

  <h2>5. Repairs &amp; tune-ups</h2>
  <ul>
    <li>If additional parts or work are needed beyond the package you selected, <strong>we call you with a price before doing the work</strong>. We never perform unapproved extra work.</li>
    <li>Turnaround times (for example, a 72-hour target) are estimates, not guarantees, and may be longer if parts must be ordered.</li>
    <li><strong>Our guarantee:</strong> if something we serviced is not right - a brake that still rubs, a gear that still skips, a wheel that still wobbles - tell us and we will make it right at no additional charge. This covers the specific work we performed; it does not cover new issues, normal wear, damage, or problems unrelated to our service.</li>
    <li>Bikes not retrieved or paid for within 30 days of notice that service is complete may be treated as abandoned to the extent permitted by Florida law.</li>
  </ul>

  <h2>6. Bicycle rentals</h2>
  <ul>
    <li>All rentals require a signed rental agreement and liability waiver, a valid government-issued photo ID, and a valid form of payment on file. You must be at least 18 to rent. Bikes rented for minors are the responsibility of the renting adult, who signs on the minor's behalf.</li>
    <li>Every rental includes a helmet and lock at no charge. We strongly recommend all riders wear a helmet at all times.</li>
    <li>You are responsible for the bicycle and all included equipment from delivery or pickup until return, and agree to pay the reasonable cost of repair, or the full replacement value, for any damage, loss, or theft during your rental - normal wear excepted.</li>
    <li>Bikes must be returned in the condition received, at the agreed time and place. Late returns may incur an additional day's rate. Delivery and pickup is free on rentals of three days or more, otherwise a flat $25; shop pickup is free.</li>
  </ul>

  <h2>7. Assumption of risk &amp; release</h2>
  <p>Cycling involves inherent risks, including falls, collisions, injury, and property damage. By renting or riding a bicycle from Lake Park Bicycles, you acknowledge these risks and agree to ride safely, obey all traffic laws, and use the equipment properly. To the fullest extent permitted by Florida law, you assume all risk of injury or loss arising from your use of a rented bicycle and release Lake Park Bicycles from liability for such injury or loss except where caused by our gross negligence or willful misconduct. The signed rental waiver contains the complete release terms.</p>

  <h2>8. Limitation of liability</h2>
  <p>To the fullest extent permitted by law, Lake Park Bicycles is not liable for indirect, incidental, or consequential damages, and our total liability for any claim relating to our services or a rental will not exceed the amount you paid for that service or rental.</p>

  <h2>9. Cancellations &amp; no-shows</h2>
  <p>Please give us as much notice as possible if you need to cancel or reschedule a pickup, delivery, or rental. Repeated missed windows or no-shows may require prepayment for future bookings.</p>

  <h2>10. Website content</h2>
  <p>The content, logo, images, and text on this website are the property of Lake Park Bicycles and may not be copied or reused without permission. We aim to keep information accurate but do not warrant that everything is error-free.</p>

  <h2>11. Governing law</h2>
  <p>These Terms are governed by the laws of the State of Florida. Any dispute will be handled in the state or county courts located in Palm Beach County, Florida.</p>

  <h2>12. Changes to these Terms</h2>
  <p>We may update these Terms from time to time. The version posted on this page, with its effective date, is the current one.</p>

  <h2>13. Contact us</h2>
  <p>Questions about these Terms? Call <a href="tel:+15618420303">561-842-0303</a> or email lakeparkbicycle@gmail.com, or stop by 910 Northlake Blvd, North Palm Beach, FL 33408.</p>
</div></section>
'''
    return head("Terms &amp; Conditions - Lake Park Bicycles",
                "Terms and conditions for Lake Park Bicycles doorstep tune-ups, bicycle repairs, and bike and e-bike rentals in North Palm Beach, Florida.",
                "cat-city.png","") + body + footer()

def build_privacy():
    body = '''
<section class="page-hero" style="padding-bottom:26px"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / Privacy Policy</div>
  <div class="eyebrow" data-reveal><span>Your privacy</span></div>
  <h1 data-reveal>Privacy <em>Policy.</em></h1>
</div></section>
<section class="section" style="padding-top:18px"><div class="legal">
  <p class="eff">Effective July 24, 2026</p>
  <p>Lake Park Bicycles ("we," "us") respects your privacy. This policy explains what information we collect through our website and services, how we use it, and the choices you have.</p>

  <h2>1. Information we collect</h2>
  <ul>
    <li><strong>Information you give us.</strong> When you submit a form, book a service, or reserve a rental, we collect the details you provide - typically your name, phone number, email address, delivery or pickup address, bike details, and any message you send.</li>
    <li><strong>Information collected automatically.</strong> Like most websites, we automatically receive basic technical data such as your device type, browser, approximate location, the pages you view, and how you found us, through Google Analytics.</li>
    <li><strong>Cookies.</strong> Our site and Google Analytics use cookies and similar technologies to understand site usage and improve the experience.</li>
  </ul>

  <h2>2. How we use your information</h2>
  <ul>
    <li>To respond to your requests and schedule pickups, deliveries, tune-ups, repairs, and rentals.</li>
    <li>To contact you by phone, text, or email to confirm and coordinate your booking.</li>
    <li>To process payment and provide our services.</li>
    <li>To understand how our website is used and improve it.</li>
  </ul>

  <h2>3. Text messages &amp; calls</h2>
  <p>By giving us your phone number, you agree that we may call or text you about your specific booking - for example, to confirm a pickup window. Message and data rates may apply. You can opt out of texts at any time by replying STOP or letting us know. We do not send marketing texts without your consent.</p>

  <h2>4. How we share information</h2>
  <p>We do <strong>not</strong> sell your personal information. We share it only with the service providers that help us run the business - such as our website and form host (Netlify) and our analytics provider (Google) - and only as needed to provide our services. We may also disclose information if required by law or to protect our rights.</p>

  <h2>5. Analytics &amp; your choices</h2>
  <p>We use Google Analytics to measure website traffic. You can opt out using the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics opt-out browser add-on</a>, or block cookies in your browser settings. Either way, you can still use our services.</p>

  <h2>6. Data retention</h2>
  <p>We keep booking and contact information for as long as needed to provide our services, keep accurate business records, and comply with the law, then delete or anonymize it.</p>

  <h2>7. Children's privacy</h2>
  <p>Our website is not directed to children under 13, and we do not knowingly collect their information. Parents or guardians book services and rentals on behalf of minors.</p>

  <h2>8. Your rights</h2>
  <p>You may ask us to access, correct, or delete the personal information we hold about you. Contact us using the details below and we will respond as required by applicable law.</p>

  <h2>9. Security</h2>
  <p>We take reasonable measures to protect your information, but no method of transmission or storage is completely secure, and we cannot guarantee absolute security.</p>

  <h2>10. Changes to this policy</h2>
  <p>We may update this policy from time to time. The version posted here, with its effective date, is the current one.</p>

  <h2>11. Contact us</h2>
  <p>Questions about your privacy? Call <a href="tel:+15618420303">561-842-0303</a> or email lakeparkbicycle@gmail.com, or write to Lake Park Bicycles, 910 Northlake Blvd, North Palm Beach, FL 33408.</p>
</div></section>
'''
    return head("Privacy Policy - Lake Park Bicycles",
                "How Lake Park Bicycles collects, uses, and protects your information when you use our website and book tune-ups, repairs, or bike rentals.",
                "cat-city.png","") + body + footer()

TONY_TIPS = [
 {"cat":"E-bikes","t":"Keep your e-bike's bolts tight","b":"E-bikes are heavier and faster, so vibration backs bolts out quicker than on a regular bike. Once a month, run a 4, 5 and 6mm allen key over the stem, bar clamp, seatpost and any rack or motor-mount bolts and snug them until firm - most cockpit bolts want about 5 to 6 Nm if you have a torque wrench. A dab of blue threadlocker on rack and fender bolts keeps them from rattling loose."},
 {"cat":"Tires","t":"Check your pressure before every ride","b":"The right number is printed right on the tire's sidewall. Low tires are the number-one cause of flats and make you work twice as hard for the same speed. A thirty-second squeeze-and-pump saves you a tube and a tired ride."},
 {"cat":"Drivetrain","t":"A dry chain is a slow chain","b":"If you hear squeaking, your chain is already crying for help. Wipe it down, add a few drops of lube, then wipe off the excess - or you'll turn your chain into a grit magnet that wears out fast."},
 {"cat":"Brakes","t":"Rim brakes squealing? Toe the pads in","b":"That squeal is usually the pad hitting the rim dead flat. Loosen the pad bolt, slip a folded business card behind the back edge of the pad, then tighten so the front of the pad touches the rim a hair first. That tiny angle - 'toe-in' - kills the noise. And if the grooves in the pad are worn smooth, swap them before they start eating the rim."},
 {"cat":"Care","t":"Salt air is a drivetrain's worst enemy","b":"Living this close to the water is a gift, but salt and sand eat metal. Keep your bike out of the weather when you can, and give the chain a quick wipe after a beach ride - it'll last years longer."},
 {"cat":"Safety","t":"The 30-second ABC check","b":"Before every ride: Air (tires firm), Brakes (both grab), Chain (spins clean and quiet). Do those three and you'll catch most problems before they ever leave the driveway."},
 {"cat":"Drivetrain","t":"More lube isn't better","b":"A dripping, greasy chain collects sand and grit and actually wears out faster. A little lube, wiped clean, beats a lot every single time."},
 {"cat":"Kids","t":"Kids' bike left out in the rain? Dry it and oil the pivots","b":"Wipe it dry, then get a little oil into the moving parts: a drop on each chain link (spin the pedals, then wipe the outside dry), a drop on each brake pivot and lever, and a shot on the little springs at the brake arms. Squeeze the brakes and spin the wheels - a stiff chain or rusty pads are what make a kid quit riding it. Two minutes keeps it rolling."},
 {"cat":"Safety","t":"Give it a wiggle","b":"Grab the seat, the handlebars and each wheel and give them a firm wiggle. Anything that moves is a bolt that needs attention - and on e-bikes, vibration works bolts loose faster than you'd think."},
 {"cat":"Shifting","t":"Sloppy shifting? Reach for the barrel adjuster","b":"Find the knurled knob where the shifter cable enters the rear derailleur - that's the barrel adjuster. If the chain is slow to climb to an easier gear, turn it a quarter-turn counter-clockwise; if it overshoots, go clockwise. Quarter-turns only, and test after each. Most 'bad shifting' is just grit in the cable housing, so a few drops of light oil where the cable enters the housing helps too."},
]

def tony_tip(tip):
    return ('<div class="tonytip"><img src="assets/img/tony.jpg" alt="Tony, owner of Lake Park Bicycles">'
            '<div><div class="lab">Tony\'s tip</div><div class="tt">'+tip["t"]+'</div>'
            '<div class="tb">'+tip["b"]+' <a href="tips.html" style="color:var(--teal-d);font-weight:600;white-space:nowrap">More of Tony\'s tips &rarr;</a></div></div></div>')

def tony_tip_month():
    import json
    tj=json.dumps([{"t":t["t"],"b":t["b"]} for t in TONY_TIPS])
    return ('''
<section class="section" style="padding-top:60px;padding-bottom:10px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>From Tony's bench</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center;margin-bottom:28px">A tip from Tony.</h2>
  <div class="tonytip tonytip-feat">
    <img src="assets/img/tony.jpg" alt="Tony, owner of Lake Park Bicycles">
    <div>
      <div class="lab">Tony's tip of the month</div>
      <div class="tt" id="mt-t">'''+TONY_TIPS[0]["t"]+'''</div>
      <div class="tb" id="mt-b">'''+TONY_TIPS[0]["b"]+'''</div>
      <a href="tips.html" style="display:inline-block;margin-top:12px;color:var(--teal-d);font-weight:700;font-size:14.5px">See all of Tony's tips &rarr;</a>
    </div>
  </div>
</section>
<script>
(function(){var T='''+tj+''';var n=new Date();var m=n.getFullYear()*12+n.getMonth();var t=T[((m%T.length)+T.length)%T.length];var a=document.getElementById('mt-t'),b=document.getElementById('mt-b');if(a){a.textContent=t.t;b.textContent=t.b;}})();
</script>
''')

def tony_tip_week():
    import json
    tj=json.dumps([{"t":t["t"],"b":t["b"]} for t in TONY_TIPS])
    return ('''
<section class="section" style="padding-top:64px;padding-bottom:12px">
  <div class="eyebrow center" data-reveal style="justify-content:center"><span>Tip Tuesday</span></div>
  <h2 class="sub-h" data-reveal style="text-align:center;margin-bottom:28px">Straight from Tony's bench.</h2>
  <div class="tonytip tonytip-feat">
    <img src="assets/img/tony.jpg" alt="Tony, owner of Lake Park Bicycles">
    <div>
      <div class="lab">Tony's tip &middot; <span id="ht-d">this Tuesday</span></div>
      <div class="tt" id="ht-t">'''+TONY_TIPS[0]["t"]+'''</div>
      <div class="tb" id="ht-b">'''+TONY_TIPS[0]["b"]+'''</div>
      <a href="tips.html" style="display:inline-block;margin-top:12px;color:var(--teal-d);font-weight:700;font-size:14.5px">See all of Tony's tips &rarr;</a>
    </div>
  </div>
</section>
<script>
(function(){var T='''+tj+''';var n=new Date();function tue(k){var d=new Date(n.getFullYear(),n.getMonth(),n.getDate());var back=(d.getDay()-2+7)%7;d.setDate(d.getDate()-back-k*7);return d;}function fmt(d){return d.toLocaleDateString('en-US',{weekday:'short',month:'short',day:'numeric'});}var epoch=new Date(2020,0,7);var w=Math.round((tue(0)-epoch)/6048e5);var t=T[(((w)%T.length)+T.length)%T.length];var a=document.getElementById('ht-t'),b=document.getElementById('ht-b'),d=document.getElementById('ht-d');if(a){a.textContent=t.t;b.textContent=t.b;d.textContent=fmt(tue(0));}})();
</script>
''')

def build_tips():
    import json
    lib="".join('<div class="tipcard" data-reveal><div class="tc-cat">'+t["cat"]+'</div><div class="tc-t">'+t["t"]+'</div><div class="tc-b">'+t["b"]+'</div></div>' for t in TONY_TIPS)
    tipsjson=json.dumps([{"t":t["t"],"b":t["b"],"c":t["cat"]} for t in TONY_TIPS])
    body=('''
<section class="page-hero" style="padding-top:46px;padding-bottom:56px"><div class="in">
  <div class="tips-hero">
    <div>
      <div class="crumb" data-reveal><a href="index.html">Home</a> / Tony's Tips</div>
      <div class="eyebrow" data-reveal><span>Tony's Tips</span></div>
      <h1 data-reveal>50 years of <em>wrench time.</em></h1>
      <p class="lead" data-reveal>Boiled down to what actually keeps you rolling - and out of the shop. A fresh tip drops every Tuesday. Here's this week's, plus every one before it.</p>
      <a href="book.html" class="btn btn-coral" style="margin-top:24px" data-reveal>Book a tune-up &rarr;</a>
    </div>
    <div data-reveal>
      <div class="tonytip tonytip-feat">
        <img src="assets/img/tony.jpg" alt="Tony, owner of Lake Park Bicycles">
        <div><div class="lab">Tony's tip &middot; <span id="wt-d">this Tuesday</span></div>
        <div class="tt" id="wt-t">'''+TONY_TIPS[0]["t"]+'''</div>
        <div class="tb" id="wt-b">'''+TONY_TIPS[0]["b"]+'''</div></div>
      </div>
    </div>
  </div>
</div></section>
<section class="section" style="padding-top:60px">
  <div class="eyebrow" data-reveal><span>The archive</span></div>
  <h2 class="sub-h" data-reveal style="margin-bottom:8px">Past Tip Tuesdays.</h2>
  <p style="color:var(--slate);font-size:15.5px;margin:0 0 32px" data-reveal>Miss one? They're all here - and a new one lands every Tuesday, automatically.</p>
  <div class="tiplib" id="tip-archive">'''+lib+'''</div>
</section>
<script>
(function(){
  var T='''+tipsjson+''';var N=T.length,n=new Date();
  function tue(k){var d=new Date(n.getFullYear(),n.getMonth(),n.getDate());var back=(d.getDay()-2+7)%7;d.setDate(d.getDate()-back-k*7);return d;}
  function fmt(d){return d.toLocaleDateString('en-US',{weekday:'short',month:'short',day:'numeric'});}
  var epoch=new Date(2020,0,7);var w=Math.round((tue(0)-epoch)/6048e5);
  function tip(i){return T[(((i)%N)+N)%N];}
  var f=tip(w),et=document.getElementById('wt-t'),eb=document.getElementById('wt-b'),ed=document.getElementById('wt-d');
  if(et){et.textContent=f.t;eb.textContent=f.b;ed.textContent=fmt(tue(0));}
  var arch=document.getElementById('tip-archive');
  if(arch){arch.innerHTML='';for(var k=1;k<N;k++){var t=tip(w-k),c=document.createElement('div');c.className='tipcard';c.innerHTML='<div class="tc-date">'+fmt(tue(k))+'</div><div class="tc-cat">'+t.c+'</div><div class="tc-t">'+t.t+'</div><div class="tc-b">'+t.b+'</div>';arch.appendChild(c);}}
})();
</script>
''')
    return head("Tony's Tips - Bike &amp; E-Bike Maintenance | Lake Park Bicycles",
                "Tony's Tips: 50 years of bike wrench wisdom on e-bike care, tire pressure, chain lube, brakes and more - a fresh maintenance tip every Tuesday from Lake Park Bicycles.",
                "cat-city.png","")+body+footer()

def build_newbikes():
    # Exactly the bikes Lake Park Bicycles stocks, ordered smallest-to-largest.
    # (category, css-class, image, name, spec, price)
    BIKES = [
      ("Kids","cat-kids","b01-mini.jpg","Beaumont Mini 16&quot;","Ages 4-6 &middot; 16&quot; wheels &middot; single-speed","$159.99"),
      ("Kids","cat-kids","b02-koda20.jpg","Koda 20&quot;","Ages 6-8 &middot; 20&quot; wheels &middot; single-speed","$199.99"),
      ("Kids","cat-kids","b03-dart20.jpg","Dart 20&quot; 7-Speed","Ages 6-8 &middot; 20&quot; wheels &middot; 7-speed","$239.99"),
      ("Kids","cat-kids","b04-chatham20.jpg","Chatham 20&quot; Cruiser","Ages 6-8 &middot; 20&quot; wheels &middot; single-speed","$229.99"),
      ("Kids","cat-kids","b05-dart24.jpg","Dart 24&quot; 7-Speed","Ages 8-11 &middot; 24&quot; wheels &middot; 7-speed","$259.99"),
      ("Kids","cat-kids","b06-chatham24.jpg","Chatham 24&quot; Cruiser","Ages 8-11 &middot; 24&quot; wheels &middot; single-speed","$259.99"),
      ("Cruiser","cat-cruiser","b07-chatham-cruiser.jpg","Chatham Step-Through Cruiser","Adult &middot; 26&quot; wheels &middot; single-speed","$299.99"),
      ("City &amp; hybrid","cat-city","b08-beaumont-st.jpg","Beaumont Step-Through City","7-speed &middot; easy step-through frame","$379.99"),
      ("City &amp; hybrid","cat-city","b09-beaumont-diamond.jpg","Beaumont City","7-speed &middot; classic diamond frame","$379.99"),
      ("City &amp; hybrid","cat-city","b10-barron.jpg","Barron Plus Comfort Hybrid","21-speed &middot; step-through frame","$419.99"),
      ("Electric","cat-electric","b11-beaumont-rev.jpg","Beaumont Rev 3 Electric City","Step-through &middot; pedal-assist e-bike","$999.99"),
    ]
    tiles = ""
    for cat, ccls, img, name, spec, price in BIKES:
        tiles += (
          '<article class="tile" data-reveal>'
          '<div class="ph"><img src="assets/img/retrospec/%s" alt="Retrospec %s" loading="lazy"></div>'
          '<div class="tb"><span class="cat %s">%s</span><h3>%s</h3><p class="spec">%s</p>'
          '<div class="price">%s<small>MSRP</small></div></div></article>'
        ) % (img, name.replace('&quot;','in'), ccls, cat, name, spec, price)
    tiles += ('<article class="tile tile-cta" data-reveal><div class="cta-in">'
              '<h3>Don\'t see it here?</h3>'
              '<p>We can order almost any Retrospec model, size or color. Tell us what you\'re after and we\'ll get it in.</p>'
              '<a href="contact.html" class="btn btn-teal">Ask Tony &rarr;</a></div></article>')
    lineup = '<div class="biketiles">' + tiles + '</div>'

    body = '''
<section class="page-hero"><div class="in">
  <div class="crumb" data-reveal><a href="index.html">Home</a> / New Bikes</div>
  <div class="eyebrow" data-reveal><span>Now a Retrospec dealer</span></div>
  <h1 data-reveal>New bikes, <em>for the whole family.</em></h1>
  <p class="lead" data-reveal style="max-width:700px">We're proud to carry the <strong>Retrospec</strong> line - a genuinely well-made, honestly-priced range that runs from a kid's first 16-inch bike all the way to a pedal-assist electric. Come see them in the shop and we'll help you find the right fit.</p>
</div></section>

<section class="sec-tint"><div class="split section" style="padding-top:60px;padding-bottom:60px">
    <div data-reveal>
      <div class="eyebrow"><span>Why Retrospec</span></div>
      <h2 class="sub-h">Good bikes that don't cost a fortune.</h2>
      <p style="color:var(--slate);font-size:16px;line-height:1.75">Retrospec has been building good-looking, dependable bikes at down-to-earth prices since 2008. Clean design, solid parts, and a bike for every age and ability. It's a line we're happy to put our name behind.</p>
      <p style="color:var(--slate);font-size:16px;line-height:1.75;margin-top:16px">We picked it because it fits how this shop has always worked: get a good bike under someone at a fair price, set it up right, and stand behind it. Every new bike leaves here fully assembled, tuned and safety-checked by Tony - not flat-packed in a box.</p>
      <div class="acts" style="margin-top:20px"><a href="contact.html" class="btn btn-teal">Come see the lineup &rarr;</a><a href="tel:+15618420303" class="btn btn-outline">Call 561&middot;842&middot;0303</a></div>
    </div>
    <div data-reveal><div class="mediaframe" style="aspect-ratio:4/5"><img src="assets/img/retrospec/spotlight.jpg" alt="A rider on a Retrospec Beaumont Rev electric city bike"></div></div>
</div></section>

<section class="section" style="padding-top:70px">
  <div class="eyebrow center" style="justify-content:center" data-reveal><span>The lineup</span></div>
  <h2 class="sub-h" style="text-align:center" data-reveal>A bike for every rider in the family.</h2>
  <p style="text-align:center;color:var(--slate);font-size:16px;max-width:700px;margin:10px auto 34px" data-reveal>Everything we stock, smallest to largest. Prices shown are Retrospec's suggested retail - ask us for our price and what's on the floor today.</p>
''' + lineup + '''
  <div class="dealernote" data-reveal>
    <div>
      <p class="dn-k">Not an online store - your local dealer.</p>
      <p>There's no checkout button here on purpose. We'd rather get you on the right size, set it up properly, and give you a real out-the-door price. Find the models you like, then <a href="contact.html">stop by the shop</a> or <a href="tel:+15618420303">call 561-842-0303</a> - we'll tell you what's on the floor and what we can bring in for you.</p>
    </div>
  </div>
</section>

'''
    body += cta("Come find the right bike.<br>We'll fit it and tune it.", '<a href="contact.html" class="btn btn-navy btn-lg">Visit the shop &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')
    jsonld = ('\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList",'
              '"itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.lakeparkbicycles.com/"},'
              '{"@type":"ListItem","position":2,"name":"New Bikes","item":"https://www.lakeparkbicycles.com/new-bikes"}]}</script>')
    return head("New Bikes - Retrospec Bikes &amp; E-Bikes | Lake Park Bicycles",
                "Now a Retrospec dealer in North Palm Beach. Kids' bikes, beach cruisers, city and hybrid bikes, and the Beaumont Rev electric - from $159. See them at Lake Park Bicycles or call 561-842-0303.",
                "retrospec/spotlight.jpg","newbikes",jsonld) + body + footer()

EBIKES = [
 {"slug":"vetus-1","name":"Vetus 1 Fat Tire","type":"Fat-tire e-bike","stock":True,"pa":"749","pb":"699","colors":[],
  "imgs":["vetus-1-1.webp","vetus-1-2.webp","vetus-1-3.webp","vetus-1-4.webp","vetus-1-5.webp"],
  "tag":"Full suspension, 20-inch fat tires, and a 1000W punch that goes well past the city.",
  "blurb":"The Vetus 1 is our go-anywhere fat-tire e-bike. Full suspension and 20-inch by 4-inch tires soak up sand, gravel and curbs, while a 1000W peak motor and adjustable 28 mph top speed give it real muscle. It is TUV and UL 2849 certified, and every one leaves the shop fully built, tuned and safety-checked by Tony.",
  "specs":[("Motor","1000W peak rear hub, 60 Nm"),("Battery","48V 13Ah (624Wh)"),("Range","Up to 50 mi assist / 30 mi throttle"),("Top speed","20 mph, adjustable to 28 mph"),("Throttle","Yes"),("Tires","20\" x 4\" fat"),("Suspension","Full - front fork + dual rear shocks"),("Drivetrain","Shimano 7-speed"),("Brakes","Disc"),("Display","4\" LCD"),("Rider height","5'5\" to 6'5\""),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"otium-m5l","name":"Otium M5L Step-Through","type":"Step-through commuter","stock":True,"pa":"599","pb":"549","colors":["Steel Blue","Pink"],
  "imgs":["otium-m5l-1.jpg","otium-m5l-2.jpg","otium-m5l-3.jpg","otium-m5l-4.jpg","otium-m5l-5.jpg"],
  "tag":"A low step-through frame that is easy on, easy off, with up to 50 miles of range.",
  "blurb":"The Otium M5L is the friendliest way into e-bikes. The ultra-low step-through frame makes hopping on and off effortless, an easy-swap 480Wh battery delivers up to 50 miles, and 26-inch city tires keep the ride smooth and stable. A great pick for cruising the neighborhood or running errands.",
  "specs":[("Motor","350W rated / 750W peak"),("Battery","48V 10Ah (480Wh), swappable"),("Range","Up to 50 mi"),("Top speed","20 mph"),("Tires","26\" x 2.125\" city"),("Frame","Low step-through"),("Rear rack","Holds up to 77 lb"),("Display","3\" LCD"),("Rider height","5'1\" to 6'1\""),("Colors","Steel Blue, Pink"),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"otium-m5","name":"Otium M5 Commuter","type":"City commuter","stock":True,"pa":"599","pb":"549","colors":["Black","Navy Blue"],
  "imgs":["otium-m5-1.jpg","otium-m5-2.jpg","otium-m5-3.jpg","otium-m5-4.jpg","otium-m5-5.jpg"],
  "tag":"A dependable daily commuter with front suspension and mechanical disc brakes.",
  "blurb":"The Otium M5 is a do-it-all city commuter. A 750W peak motor with a front suspension fork and mechanical disc brakes handles stop-and-go streets with confidence, while a Shimano 7-speed drivetrain and 480Wh battery give you up to 50 relaxed miles. Simple, solid, and ready every morning.",
  "specs":[("Motor","750W peak rear hub, 45 Nm"),("Battery","48V 10Ah (480Wh)"),("Range","Up to 50 mi assist / 30 mi throttle"),("Top speed","20 mph"),("Throttle","Yes"),("Tires","26\" x 2.125\""),("Suspension","100mm front fork"),("Drivetrain","Shimano TZ500 7-speed"),("Brakes","Mechanical disc"),("Weight","55.9 lb"),("Display","3\" LCD"),("Colors","Black, Navy Blue"),("Warranty","2-year")]},
 {"slug":"otium-1","name":"Otium 1 Cruiser","type":"City cruiser","stock":False,"pa":"699","pb":"649","colors":["Pink","Mint Blue","White"],
  "imgs":["otium-1-1.webp","otium-1-2.webp","otium-1-3.webp","otium-1-4.webp","otium-1-5.webp"],
  "tag":"A comfortable step-thru cruiser for relaxed city miles.",
  "blurb":"The Otium 1 is a comfort-first step-through cruiser. A 1000W peak motor and 624Wh battery give it plenty of pep and up to 50 miles of range, while 24-inch wheels and an upright ride make it easy and fun for everyday trips. Add the front basket and rear rack and it is ready for anything.",
  "specs":[("Motor","500W rated / 1000W peak, 65 Nm"),("Battery","48V 13Ah (624Wh)"),("Range","Up to 50 mi assist / 30 mi throttle"),("Top speed","20 mph, adjustable to 28 mph"),("Throttle","Yes"),("Tires","24\" x 1.95\" city"),("Frame","Step-through steel"),("Drivetrain","Shimano TZ500 7-speed"),("Brakes","Disc, 160mm"),("Weight","64 lb"),("Display","2.2\" LCD"),("Colors","Pink, Mint Blue, White"),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"otium-2","name":"Otium 2 Cruiser","type":"City cruiser","stock":False,"pa":"949","pb":"899","colors":["Creamy Yellow","Navy Blue"],
  "imgs":["otium-2-1.webp","otium-2-2.webp","otium-2-3.webp","otium-2-4.webp","otium-2-5.webp"],
  "tag":"More battery, more comfort - up to 60 miles on an ultra-low step-through.",
  "blurb":"The Otium 2 steps everything up: a bigger 768Wh battery for up to 60 miles, a full aluminum ultra-low step-through frame, and a crisp 2.4-inch color display. It is the premium cruiser for riders who want extra range and a plush, upright ride around town.",
  "specs":[("Motor","1000W peak, 65 Nm"),("Battery","48V 16Ah (768Wh)"),("Range","Up to 60 mi assist / 38 mi throttle"),("Top speed","20 mph, adjustable to 28 mph"),("Throttle","Yes"),("Tires","26\" x 2.125\" cruiser"),("Frame","Ultra-low step-through, aluminum"),("Drivetrain","Shimano TZ500 7-speed"),("Brakes","Disc"),("Weight","64 lb"),("Display","2.4\" TFT color"),("Colors","Creamy Yellow, Navy Blue"),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"vetus-2","name":"Vetus 2 Fat Tire","type":"Fat-tire e-bike","stock":False,"pa":"749","pb":"699","colors":[],
  "imgs":["vetus-2-1.webp","vetus-2-2.webp","vetus-2-3.webp","vetus-2-4.jpg","vetus-2-5.webp"],
  "tag":"Fat-tire capability with a big 4.3-inch display and NFC smart unlock.",
  "blurb":"The Vetus 2 brings fat-tire versatility with a few smart touches: a large 4.3-inch color display, NFC smart unlock, and a front fork with a mid-spring shock to smooth out the bumps. A 1000W peak motor and up to 50 miles of range make it just as happy on the trail as in town.",
  "specs":[("Motor","1000W peak, 60 Nm"),("Battery","48V 13Ah (624Wh)"),("Range","Up to 50 mi assist / 30 mi throttle"),("Top speed","20 mph, adjustable to 28 mph"),("Throttle","Yes"),("Tires","20\" x 4\" fat"),("Suspension","Front fork + mid-spring shock"),("Drivetrain","Shimano 7-speed"),("Brakes","160mm disc"),("Display","4.3\" TFT color"),("Extras","NFC smart unlock"),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"lumeo-2","name":"Lumeo 2 Carbon Fiber","type":"Carbon-fiber e-bike","stock":False,"pa":"1549","pb":"1499","colors":["Sky Blue","Beige","Gray"],
  "imgs":["lumeo-2-1.webp","lumeo-2-2.webp","lumeo-2-3.webp","lumeo-2-4.webp","lumeo-2-5.webp"],
  "tag":"Carbon-fiber light, with a dual battery and up to 120 miles of range.",
  "blurb":"The Lumeo 2 is the premium pick: a genuine carbon-fiber frame keeps it light, while a dual-battery system delivers a remarkable 120 miles of range. Hydraulic disc brakes, a lockable front fork and a color display round out a bike built for long, effortless rides.",
  "specs":[("Motor","1000W peak, 65 Nm"),("Battery","Dual 48V 10Ah x2 (921Wh)"),("Range","Up to 120 mi assist / 50 mi throttle"),("Top speed","20 mph, adjustable to 28 mph"),("Throttle","Yes"),("Tires","26\" x 2.5\""),("Frame","Carbon fiber"),("Suspension","Lockable alloy front fork"),("Drivetrain","Shimano M310 7-speed"),("Brakes","Hydraulic disc"),("Weight","67 lb"),("Display","2.4\" TFT color"),("Colors","Sky Blue, Beige, Gray"),("Warranty","2-year, UL 2849 certified")]},
 {"slug":"terrn-2","name":"Terrn 2 Pro","type":"Off-road e-bike","stock":False,"pa":"2649","pb":"2599","colors":[],
  "imgs":["terrn-2-1.webp","terrn-2-2.webp","terrn-2-3.webp","terrn-2-4.webp"],
  "tag":"5500W of peak power, 40 mph, full suspension - a true off-road machine.",
  "blurb":"The Terrn 2 Pro is the beast of the lineup: a 5500W peak motor, 40 mph top speed, and a massive 1920Wh removable battery for up to 70 miles. Full hydraulic suspension, moto-style knobby tires and 180mm hydraulic brakes make it a serious off-road ride. This one is for experienced riders who want it all.",
  "specs":[("Motor","5500W peak, 135 Nm"),("Battery","60V 32Ah (1920Wh), removable"),("Range","Up to 70 mi assist / 45 mi throttle"),("Top speed","40 mph"),("Throttle","Yes"),("Tires","70/100-19 moto knobby"),("Suspension","Full - hydraulic front + rear"),("Drivetrain","Shimano TZ500 7-speed"),("Brakes","Hydraulic, 180mm"),("Weight","127.6 lb"),("Display","4\" LCD"),("Warranty","2-year, UL 2849 certified")]},
]

RESERVE_JS = """
<script>
(function(){
  var p=new URLSearchParams(location.search), b=p.get('reserve');
  if(!b) return;
  b=b.replace(/[<>]/g,'');
  var f=document.getElementById('contactForm'); if(!f) return;
  var m=f.querySelector('[name="message"]'); if(m) m.value="I'd like to reserve the "+b+" e-bike. Please contact me about availability, color and pickup.";
  var s=f.querySelector('[name="subject"]'); if(s) s.value="E-Bike Reservation: "+b+" - Lake Park Bicycles";
  var banner=document.createElement('div'); banner.className='reserve-banner';
  banner.innerHTML="You're reserving: <strong>"+b+"</strong>";
  f.parentNode.insertBefore(banner,f);
})();
</script>
"""

RESERVE_MODAL_JS = """
<script>
function openReserve(){var m=document.getElementById('rmodal');if(!m)return;m.hidden=false;document.body.style.overflow='hidden';var n=m.querySelector('[name=name]');if(n){setTimeout(function(){n.focus();},60);}}
function closeReserve(){var m=document.getElementById('rmodal');if(!m)return;m.hidden=true;document.body.style.overflow='';}
document.addEventListener('keydown',function(e){if(e.key==='Escape'||e.keyCode===27)closeReserve();});
window.addEventListener('load',function(){if(location.hash==='#reserve')openReserve();});
</script>
"""

INFO_ASSEMBLY = ('<span class="infowrap"><button type="button" class="infodot" aria-label="Why professional assembly matters">?</button>'
 '<span class="infopop" role="tooltip">These e-bikes need to be assembled at the correct torque, with every bolt tight, the brakes and gears properly adjusted, and a full safety inspection before the first ride. We highly recommend letting our trained technicians handle it for you.</span></span>')

def _reserve_modal(b):
    cf=""
    if b["colors"]:
        cf='<label>Color<select name="color">'+"".join('<option>'+c+'</option>' for c in b["colors"])+'</select></label>'
    return ('<div class="rmodal" id="rmodal" hidden><div class="rmodal-ov" onclick="closeReserve()"></div>'
      '<div class="rmodal-card" role="dialog" aria-modal="true" aria-label="Reserve '+b["name"]+'">'
      '<button class="rmodal-x" type="button" onclick="closeReserve()" aria-label="Close">&times;</button>'
      '<div class="rmodal-head"><img src="assets/img/ebikes/'+b["imgs"][0]+'" alt="'+b["name"]+'">'
      '<div><div class="rm-eyebrow">Reserve this e-bike</div><h3>'+b["name"]+'</h3>'
      '<div class="rm-price">$'+b["pa"]+' assembled &middot; $'+b["pb"]+' in the box</div></div></div>'
      '<form class="rform" name="ebike-reservation" method="POST" data-netlify="true" action="https://api.web3forms.com/submit">'
      '<input type="hidden" name="access_key" value="dfacc1b4-52f3-4b47-bc9c-bbd01c81fdc1">'
      '<input type="hidden" name="subject" value="E-Bike Reservation: '+b["name"]+' - Lake Park Bicycles">'
      '<input type="hidden" name="from_name" value="Lake Park Bicycles Website">'
      '<input type="hidden" name="redirect" value="https://lakeparkbicycles.com/thanks">'
      '<input type="checkbox" name="botcheck" style="display:none !important" tabindex="-1" autocomplete="off" aria-hidden="true">'
      '<input type="hidden" name="bike" value="'+b["name"]+'">'
      +cf+
      '<label><span class="lbl-cap">Build option '+INFO_ASSEMBLY+'</span><select name="build"><option>Professional assembly - ready to ride ($'+b["pa"]+')</option><option>In the box - save $50 ($'+b["pb"]+')</option></select></label>'
      '<label>Your name<input type="text" name="name" placeholder="First and last" required></label>'
      '<div class="rform-2"><label>Phone<input type="tel" name="phone" placeholder="(561) 000-0000" required></label>'
      '<label>Email<input type="email" name="email" placeholder="you@email.com" required></label></div>'
      '<label>Anything else? <span class="opt">(optional)</span><textarea name="message" rows="2" placeholder="Questions, timing, a trade-in..."></textarea></label>'
      '<button type="submit" class="btn btn-coral btn-lg">Reserve Mine &rarr;</button>'
      '<p class="rform-note">No payment now - Tony will call to confirm the color, timing and pickup.</p>'
      '</form></div></div>')

def _ebike_card(b, related=False):
    ov = '<span class="stock-ov">In stock</span>' if b["stock"] else ''
    tail = '' if related else '<p class="spec">'+b["tag"]+'</p>'
    reslink = '' if related else '<span class="reserve-link">View &amp; reserve &rarr;</span>'
    return ('<a class="tile ebike-card" href="ebike-'+b["slug"]+'.html"><div class="ph">'+ov
            +'<img src="assets/img/ebikes/'+b["imgs"][0]+'" alt="'+b["name"]+'" loading="lazy"></div>'
            +'<div class="tb"><span class="cat cat-electric">'+b["type"]+'</span><h3>'+b["name"]+'</h3>'
            +tail+'<div class="price">$'+b["pa"]+'<small>assembled</small></div>'+reslink+'</div></a>')

def build_ebike(b):
    imgs=b["imgs"]
    thumbs="".join(
      '<img src="assets/img/ebikes/%s" alt="%s"%s onclick="document.getElementById(&#39;pdp-main-img&#39;).src=this.src">'
      % (im, b["name"], (' class="on"' if i==0 else '')) for i,im in enumerate(imgs))
    stock='<span class="stockbadge">In stock - ready to ride</span>' if b["stock"] else ''
    colors=('<div class="pdp-colors"><span>Colors</span>'+' &middot; '.join(b["colors"])+'</div>') if b["colors"] else ''
    specrows="".join('<tr><td>'+k+'</td><td>'+v+'</td></tr>' for k,v in b["specs"])
    rname=b["name"].replace(' ','%20')
    rel=[x for x in EBIKES if x["slug"]!=b["slug"]][:4]
    relcards="".join(_ebike_card(r, related=True) for r in rel)
    body=('<section class="page-hero" style="padding-bottom:10px"><div class="in">'
     '<div class="crumb" data-reveal><a href="index.html">Home</a> / <a href="ebikes.html">E-Bikes</a> / '+b["name"]+'</div>'
     '</div></section>'
     '<section class="section" style="padding-top:8px"><div class="pdp">'
     '<div class="pdp-gallery" data-reveal><div class="pdp-main"><img id="pdp-main-img" src="assets/img/ebikes/'+imgs[0]+'" alt="'+b["name"]+'"></div>'
     '<div class="pdp-thumbs">'+thumbs+'</div></div>'
     '<div class="pdp-info" data-reveal>'+stock
     +'<div class="eyebrow"><span>Eclio &middot; '+b["type"]+'</span></div>'
     '<h1>'+b["name"]+'</h1><p class="pdp-tag">'+b["tag"]+'</p>'
     '<div class="pdp-price"><div class="pp-row"><span class="pp-num">$'+b["pa"]+'</span><span class="pp-lbl">assembled &amp; ready to ride</span></div>'
     '<p class="pp-note">Includes professional assembly '+INFO_ASSEMBLY+', a full tune, and a safety check by Tony. Prefer to build it yourself? Take it home in the box for <strong>$'+b["pb"]+'</strong> and save $50.</p></div>'
     +colors
     +'<div class="pdp-acts"><button type="button" onclick="openReserve()" class="btn btn-coral btn-lg">Reserve Mine &rarr;</button>'
     '<a href="tel:+15618420303" class="btn btn-outline btn-lg">Call 561&middot;842&middot;0303</a></div>'
     '<ul class="pdp-assure"><li>Built, tuned &amp; safety-checked by Tony</li><li>Local service and support, right here in town</li><li>2-year manufacturer warranty</li></ul>'
     '</div></div></section>'
     '<section class="section" style="padding-top:22px"><div class="split pdp-detail" style="align-items:start">'
     '<div data-reveal><div class="eyebrow"><span>About this bike</span></div><h2 class="sub-h">'+b["name"]+'</h2>'
     '<p style="color:var(--slate);font-size:16px;line-height:1.7">'+b["blurb"]+'</p>'
     '<p style="color:var(--muted);font-size:13.5px;line-height:1.6;margin-top:16px">Reserve online with no payment now - we will call to confirm the color, timing and pickup. Prices include professional assembly by Tony; we are not selling e-bikes for online checkout yet.</p></div>'
     '<div data-reveal><div class="spectable"><h3>Specifications</h3><table>'+specrows+'</table><p class="spec-note">Specs are from the manufacturer and can change. Ask us anything.</p></div></div>'
     '</div></section>'
     '<section class="section" style="padding-top:18px"><div class="eyebrow" data-reveal><span>More e-bikes</span></div>'
     '<h2 class="sub-h" data-reveal style="margin-bottom:22px">Keep looking.</h2><div class="biketiles">'+relcards+'</div></section>')
    body += cta("Come ride it in the shop.<br>We build it, you enjoy it.", '<button type="button" onclick="openReserve()" class="btn btn-navy btn-lg">Reserve Mine &rarr;</button><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')
    desc=(b["name"]+" electric bike at Lake Park Bicycles, North Palm Beach. $"+b["pa"]+" assembled and ready to ride, or $"+b["pb"]+" in the box. "+b["tag"]+" Reserve yours: call 561-842-0303.")
    jsonld=('\n<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product","name":"'+b["name"]
            +'","brand":{"@type":"Brand","name":"Eclio"},"image":"https://www.lakeparkbicycles.com/assets/img/ebikes/'+imgs[0]
            +'","description":"'+b["tag"]+'"}</script>')
    body += _reserve_modal(b) + RESERVE_MODAL_JS
    return head(b["name"]+" E-Bike | Lake Park Bicycles", desc, "ebikes/"+imgs[0], "ebikes", jsonld) + body + footer()

def build_ebikes():
    cards="".join(_ebike_card(b) for b in EBIKES)
    body=('<section class="page-hero"><div class="in">'
     '<div class="crumb" data-reveal><a href="index.html">Home</a> / E-Bikes</div>'
     '<div class="eyebrow" data-reveal><span>Now carrying Eclio electric bikes</span></div>'
     '<h1 data-reveal>E-bikes for <em>every ride.</em></h1>'
     '<p class="lead" data-reveal style="max-width:730px">Commuters, cruisers, fat-tire adventure, long-range carbon and a full-on off-road machine - a whole line of Eclio e-bikes, each one built, tuned and safety-checked by Tony before you ever throw a leg over it. Find the one you love and reserve it.</p>'
     '</div></section>'
     '<section class="section" style="padding-top:18px"><div class="biketiles">'+cards+'</div>'
     '<div class="dealernote" data-reveal><div><p class="dn-k">Reserved, not checked out.</p>'
     '<p>We are not taking e-bike payments online yet - and honestly, you would not want to buy one sight unseen. Tap <strong>Reserve Mine</strong> on any bike, tell us the color you like, and we will get it built and ready for you to come ride. Every e-bike is assembled and safety-checked by Tony, with local service if you ever need it. Questions? <a href="/contact">Message us</a> or call <a href="tel:+15618420303">561-842-0303</a>.</p></div></div>'
     '</section>')
    body += cta("Find your ride.<br>We'll have it built and ready.", '<a href="/contact" class="btn btn-navy btn-lg">Ask about e-bikes &rarr;</a><a href="tel:+15618420303" class="btn btn-ghost-light btn-lg">Call 561&middot;842&middot;0303</a>')
    return head("Electric Bikes - Eclio E-Bikes, Assembled &amp; Ready | Lake Park Bicycles",
                "Shop the Eclio e-bike line at Lake Park Bicycles in North Palm Beach: commuters, cruisers, fat-tire and long-range electric bikes from $599, professionally assembled and safety-checked by Tony. Reserve yours - call 561-842-0303.",
                "ebikes/"+EBIKES[0]["imgs"][0], "ebikes") + body + footer()

pages = {
  "index.html": build_index(),
  "thanks.html": build_thanks(),
  "rent.html": build_rent(),
  "tune-up.html": build_tuneup(),
  "book.html": build_book(),
  "service.html": build_service(),
  "rentals.html": build_rentals(),
  "new-bikes.html": build_newbikes(),
  "about.html": build_about(),
  "contact.html": build_contact(),
  "terms.html": build_terms(),
  "privacy.html": build_privacy(),
  "tips.html": build_tips(),
  "ebikes.html": build_ebikes(),
}
for c in CITIES:
    pages[c["slug"]+".html"] = build_city(c)
for b in EBIKES:
    pages["ebike-"+b["slug"]+".html"] = build_ebike(b)

import re
def _slug(fn): return "" if fn=="index.html" else fn[:-5]
def _cleanlinks(h):
    h = re.sub(r'href="/?index\.html(#[\w-]*)?"', r'href="/\1"', h)   # index.html -> /
    h = re.sub(r'href="/?([\w-]+)\.html(#[\w-]*)?"', r'href="/\1\2"', h)  # X.html -> /X
    h = h.replace('action="/thanks.html"', 'action="/thanks"')
    return h

NOINDEX = {"thanks.html"}
for fn, html in pages.items():
    canon = BASE + "/" + _slug(fn)
    inject = '<meta name="theme-color" content="#12a3a0">\n<link rel="canonical" href="'+canon+'">'
    if fn in NOINDEX:
        inject += '\n<meta name="robots" content="noindex, follow">'
    html = html.replace('<meta name="theme-color" content="#12a3a0">', inject, 1)
    html = _cleanlinks(html)
    with open(os.path.join(OUT, fn), "w") as f:
        f.write(html)
    print("wrote", fn, len(html))

# _redirects: force old .html URLs to the clean URL (301)
red = []
for fn in pages:
    red.append("/index.html / 301!" if fn=="index.html" else "/"+fn+" /"+_slug(fn)+" 301!")
with open(os.path.join(OUT,"_redirects"),"w") as f:
    f.write("\n".join(red)+"\n")

# sitemap.xml (clean URLs, exclude noindex pages)
prio = {"index.html":"1.0","tune-up.html":"0.9","rentals.html":"0.9","new-bikes.html":"0.9","ebikes.html":"0.9","service.html":"0.8","terms.html":"0.3","privacy.html":"0.3"}
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for fn in pages:
    if fn in NOINDEX: continue
    loc = BASE + "/" + _slug(fn)
    p = prio.get(fn) or ("0.7" if (fn.startswith("ebike-") or fn in [c["slug"]+".html" for c in CITIES]) else "0.6")
    sm.append('  <url><loc>'+loc+'</loc><changefreq>weekly</changefreq><priority>'+p+'</priority></url>')
sm.append('</urlset>')
with open(os.path.join(OUT,"sitemap.xml"),"w") as f:
    f.write("\n".join(sm)+"\n")

with open(os.path.join(OUT,"robots.txt"),"w") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: "+BASE+"/sitemap.xml\n")

print("wrote sitemap.xml + robots.txt + _redirects")
print("done ->", OUT)
