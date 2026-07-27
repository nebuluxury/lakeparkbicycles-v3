# SEO / Backlink disavow records - lakeparkbicycles.com

This folder is the **source of truth** for the Google disavow list. Keep it in the repo so it
travels with the site (including the eventual move to Shopify).

## Files
- `disavow-lakeparkbicycles.txt` - the file you upload to Google. 42 spam domains, disavowed at
  the domain level (covers `www.`, `mail.`, and every other subdomain automatically).
- `gen_disavow.py` - regenerates the .txt from the raw domain list (the authoritative list of
  source domains lives in its `raw` block). Run `python3 gen_disavow.py` after adding new spam
  domains. The original data came from a SEMrush backlink audit dated 2026-07-27 (toxic score
  60-100); drop that CSV export in this folder too if you want the full record.

## What these links are
All 42 are unsolicited spam from "buy aged domains / cheap backlinks / PBN" networks pointing
dofollow at the homepage. We did not build them and they carry no value - only risk. Disavowing
tells Google to ignore them when assessing the site.

## How to submit (one time, ~2 minutes)
1. Make sure `lakeparkbicycles.com` is verified in **Google Search Console**
   (a Domain property is best - it covers http/https + www + non-www).
2. Go to the Disavow Tool: https://search.google.com/search-console/disavow-links
3. Select the `lakeparkbicycles.com` property.
4. Click **Upload disavow list** and choose `disavow-lakeparkbicycles.txt`.
5. Confirm. That's it - it can take a few weeks for Google to reprocess the links.

**Important:** uploading a new file *replaces* the old one. Always upload the complete,
current file from this folder - never a partial list.

## When new toxic links show up
1. Add the new source domains to the `raw` list in `gen_disavow.py`.
2. Run `python3 gen_disavow.py`.
3. Re-upload the regenerated `disavow-lakeparkbicycles.txt` (full file) to the Disavow Tool.

## Moving to Shopify (or any new host) - what carries over
The disavow list is tied to the **domain in Google Search Console**, NOT to the host (Netlify,
Shopify, etc.). So as long as:
- the domain stays `lakeparkbicycles.com`, and
- the same Google Search Console property stays verified,

then **the disavow file you already uploaded keeps working - you do not re-submit it just because
you switched to Shopify.** Nothing to migrate on Google's side.

You only re-verify Search Console if the verification method breaks during the move (e.g. the
DNS TXT record or the HTML verification file doesn't come across). Re-verify the same
`lakeparkbicycles.com` property and the existing disavow list stays intact.

Keep this whole `seo/` folder with the site repo so the file is always at hand if you ever need
to re-upload it.
