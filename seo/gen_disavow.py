raw = """mail.domainsc.com
all-aged-domains.com
mail.runningwebsites.net
www.runningwebsites.net
mail.blacksonwhites.com
www.indians.cc
www.getonline.co.in
www.gamerkun.com
www.blacksonwhites.com
mail.bestwebstats.com
getonline.co.in
gamerkun.com
blacksonwhites.com
lydiaroyrealestate.com
mail.allwebsitesdirectory.com
wonvision.com
www.wonvision.com
www.indexaward.com
indexaward.com
www.thirty.co.in
mail.wallpapers.pro
www.domains.com.bz
domainanalysis.org
www.domainanalysis.org
www.homefinance.co.in
www.taxies.biz
nivira.shop
www.theface.in
mail.domainanalysis.org
www.cheapsmmprovider.online
www.preparation.co.in
prashikshan.in
www.wallpapers.pro
wallpapers.pro
preparation.co.in
www.tyres.pro
www.prashikshan.in
thirty.co.in
www.australianwebdirectory.shop
australianwebdirectory.shop
mail.australianwebdirectory.shop
mail.linksnatcher.com
mail.domain.com.lc
www.domain.com.lc
domain.com.lc
www.way2check.art
www.tyre.pro
www.procycling.org
www.themumbai.in
procycling.org
mail.way2check.cv
mail.musweb.org
indians.cc
www.linksnatcher.com
linksnatcher.com
mail.globalecommerce.org
jobsapp.info
bestwebstats.com
www.bestwebstats.com
www.websiterace.com
pagesearch.net
www.pagesearch.net
websiterace.com
www.allwebsitesdirectory.com
plumeriamarketing.com
domainsc.com
www.domainsc.com
allwebsitesdirectory.com
mp3fresh.net
www.websitescrawl.art
www.mp3fresh.net
www.linksnatcher.art
linksnatcher.art
www.hebagh.cv
hebagh.cv"""

roots = set()
for d in raw.splitlines():
    d = d.strip().lower()
    for pre in ("www.", "mail."):
        if d.startswith(pre):
            d = d[len(pre):]
    roots.add(d)

roots = sorted(roots)
header = (
"# Google disavow file for lakeparkbicycles.com\n"
"# Property: lakeparkbicycles.com (Domain property in Google Search Console)\n"
"# Created: 2026-07-27  |  Source: SEMrush backlink audit (toxic score 60-100)\n"
"# Reason: unsolicited spam link networks - 'aged domains / buy backlinks / PBN' pages.\n"
"# All entries disavowed at the domain level, which also covers www., mail. and any other subdomain.\n"
"# Submit at: https://search.google.com/search-console/disavow-links\n"
"#\n"
"# %d spam domains\n\n" % len(roots)
)
with open("disavow-lakeparkbicycles.txt","w") as f:
    f.write(header + "\n".join("domain:%s" % r for r in roots) + "\n")
print("wrote disavow-lakeparkbicycles.txt with %d domains" % len(roots))
