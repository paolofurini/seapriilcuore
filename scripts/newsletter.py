"""Invia la newsletter Se Apri il Cuore tramite Brevo quando esce un nuovo articolo.

Uso:
  python scripts/newsletter.py send <file_post> [<file_post> ...]   # invia agli iscritti
  python scripts/newsletter.py test [<file_post>]                     # invia una prova al mittente
La chiave arriva dalla variabile d'ambiente BREVO_API_KEY (segreto GitHub).
"""
import json, os, re, sys, glob, html, datetime, urllib.request, urllib.error
import yaml, markdown

API = "https://api.brevo.com/v3"
SITE = "https://paolofurini.it"
LIST_NAME = "Se Apri il Cuore"
KEY = os.environ.get("BREVO_API_KEY", "")
LOG = []

def log(msg):
    print(msg); LOG.append(msg)

def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"api-key": KEY, "accept": "application/json", "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read().decode()
            return r.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:500]}

def read_post(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    fm, body = yaml.safe_load(m.group(1)), m.group(2)
    name = os.path.basename(path)[11:-3]
    fm["url"] = f"{SITE}/blog/{name}/"
    # tolgo liquid, figure e immagini dal corpo per l'estratto
    clean = re.sub(r"\{%.*?%\}|<figure.*?</figure>|<div[^>]*>|</div>|<p class=\"stacco\".*?</p>", "", body, flags=re.S)
    clean = re.sub(r"\(\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}\)", lambda x: f"({SITE}{x.group(1)})", clean)
    clean = re.sub(r"\{\{.*?\}\}", "", clean)
    paras = [p.strip() for p in clean.split("\n\n") if p.strip() and not p.strip().startswith(("#", "<", ">"))]
    fm["excerpt_html"] = "".join(markdown.markdown(p) for p in paras[:3])
    fm["cover_url"] = f"{SITE}{fm['cover']}-900.jpg" if fm.get("cover") else None
    return fm

def email_html(p):
    e = html.escape
    cover = f'<tr><td><a href="{p["url"]}"><img src="{p["cover_url"]}" width="600" alt="{e(p.get("cover_alt", ""))}" style="display:block;width:100%;max-width:600px;height:auto;border:0"></a></td></tr>' if p["cover_url"] else ""
    dek = f'<p style="margin:0 0 22px;font-size:19px;line-height:1.45;font-style:italic;color:#545c6a">{e(p.get("description",""))}</p>' if p.get("description") else ""
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head>
<body style="margin:0;padding:0;background:#f5f0e7">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f5f0e7"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#fffdf8">
<tr><td style="background:#1a2a4a;padding:22px 32px;font-family:Georgia,serif;color:#e9e3d6;font-size:18px">Paolo Furini<br><span style="font-family:Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:2px;color:#b9b6ae">SE APRI IL CUORE</span></td></tr>
{cover}
<tr><td style="padding:32px 32px 8px;font-family:Georgia,serif;color:#1b2433">
<h1 style="margin:0 0 12px;font-size:28px;line-height:1.15;font-weight:normal">{e(p["title"])}</h1>
{dek}
<div style="font-size:17px;line-height:1.65">{p["excerpt_html"]}</div>
</td></tr>
<tr><td style="padding:12px 32px 36px"><a href="{p["url"]}" style="display:inline-block;background:#1b2433;color:#f5f0e7;font-family:Helvetica,Arial,sans-serif;font-size:15px;font-weight:bold;text-decoration:none;padding:13px 22px">Continua a leggere</a></td></tr>
<tr><td style="padding:22px 32px;border-top:1px solid #d8cfbf;font-family:Helvetica,Arial,sans-serif;font-size:12px;line-height:1.6;color:#545c6a">
Ricevi questa lettera perché ti sei iscritto a Se Apri il Cuore su <a href="{SITE}" style="color:#8f520f">paolofurini.it</a>.<br>
<a href="{{{{ unsubscribe }}}}" style="color:#545c6a">Annulla l'iscrizione</a></td></tr>
</table></td></tr></table></body></html>"""

def sender():
    s, d = call("GET", "/senders")
    act = [x for x in d.get("senders", []) if x.get("active")]
    if not act:
        log(f"ERRORE: nessun mittente attivo in Brevo ({s} {d})"); return None
    return {"name": "Paolo Furini", "email": act[0]["email"]}

def list_id():
    s, d = call("GET", "/contacts/lists?limit=50")
    for l in d.get("lists", []):
        if l["name"].strip().lower() == LIST_NAME.lower():
            return l["id"]
    log(f"ERRORE: lista '{LIST_NAME}' non trovata in Brevo. Liste presenti: {[l['name'] for l in d.get('lists', [])]}")
    return None

def campaign(p, snd, lid):
    body = {"name": f"Blog · {p['title']}"[:240], "subject": p["title"], "previewText": p.get("description", "")[:150],
            "sender": snd, "htmlContent": email_html(p), "inlineImageActivation": False}
    if lid: body["recipients"] = {"listIds": [lid]}
    s, d = call("POST", "/emailCampaigns", body)
    if s >= 300:
        log(f"ERRORE creazione campagna: {s} {d}"); return None
    return d["id"]

def main():
    if not KEY:
        log("ERRORE: manca BREVO_API_KEY"); return 1
    mode, files = sys.argv[1], sys.argv[2:]
    snd = sender()
    if not snd: return 1
    log(f"Mittente: {snd['email']}")
    if mode == "test":
        files = files or sorted(glob.glob("_posts/*.md"))[-1:]
        p = read_post(files[0]); cid = campaign(p, snd, None)
        if not cid: return 1
        s, d = call("POST", f"/emailCampaigns/{cid}/sendTest", {"emailTo": [snd["email"]]})
        log(f"Prova di '{p['title']}' inviata a {snd['email']}: {s} {d if s >= 300 else 'ok'}")
        lid = list_id(); log(f"Lista iscritti: {'trovata, id ' + str(lid) if lid else 'MANCANTE'}")
        return 0 if s < 300 else 1
    lid = list_id()
    if not lid: return 1
    today = datetime.date.today()
    for f in files:
        p = read_post(f)
        d0 = datetime.date.fromisoformat(os.path.basename(f)[:10])
        if p.get("newsletter") is False or (today - d0).days > 3:
            log(f"Salto {f}: newsletter disattivata o articolo vecchio"); continue
        cid = campaign(p, snd, lid)
        if not cid: continue
        s, d = call("POST", f"/emailCampaigns/{cid}/sendNow")
        log(f"Newsletter '{p['title']}': {'inviata' if s < 300 else 'ERRORE ' + str(s) + ' ' + str(d)}")
    return 0

if __name__ == "__main__":
    rc = main()
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    with open(".github/newsletter/log.md", "a", encoding="utf-8") as fh:
        fh.write(f"\n## {stamp} · {sys.argv[1]}\n" + "\n".join(f"- {l}" for l in LOG) + "\n")
    sys.exit(rc)
