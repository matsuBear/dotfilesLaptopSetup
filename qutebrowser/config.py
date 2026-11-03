import sys, importlib
sys.path.insert(0, str(config.configdir))
import colors
importlib.reload(colors)

config.load_autoconfig(False)

prim, secd, acct = colors.prim, colors.secd, colors.acct
hi, lo = colors.high_tone, colors.low_tone

def addAlpha(alpha: float, s: str) -> str:
    h = s.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    h = h[-6:]
    return f"#{round(alpha * 255):02x}{h}"

loAlpha=addAlpha(0.85,lo)
secdAlpha=addAlpha(0.85,secd)
acctAlpha=addAlpha(0.85, acct)
primAlpha=addAlpha(0.85, prim)

c.window.transparent = True

# Statusbar (nvim StatusLine: prim on secd)
c.colors.statusbar.normal.bg =secd 
c.colors.statusbar.command.fg = prim
c.colors.statusbar.command.bg = secd 
c.colors.statusbar.passthrough.bg = primAlpha
c.colors.statusbar.passthrough.fg = hi
c.colors.statusbar.url.fg = prim
c.colors.statusbar.url.success.https.fg = hi
c.colors.statusbar.progress.bg = acct
c.statusbar.padding = {'top': 3, 'bottom': 3, 'left': 6, 'right': 6}
c.statusbar.show = 'in-mode'
c.colors.statusbar.insert.bg = acctAlpha
c.colors.statusbar.insert.fg = hi

# Tabs (selected = StatusLine, inactive = StatusLineNC)
c.tabs.show='always'
c.colors.tabs.bar.bg = loAlpha
c.colors.tabs.even.bg = "#00000000"
c.colors.tabs.odd.bg = "#00000000"
c.colors.tabs.even.fg = acct
c.colors.tabs.odd.fg = acct
c.colors.tabs.selected.even.bg = secd
c.colors.tabs.selected.odd.bg = secd
c.colors.tabs.selected.even.fg = hi
c.colors.tabs.selected.odd.fg = hi
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 8, 'right': 8}
c.tabs.position='right'
c.tabs.width='14%'
c.tabs.title.format='{audio}{current_title}'
c.tabs.title.alignment='left'


# Completion (Pmenu / PmenuSel / Search)
c.colors.completion.fg = prim
c.colors.completion.even.bg = loAlpha
c.colors.completion.odd.bg = "#00000000"
c.colors.completion.category.bg = secdAlpha
c.colors.completion.category.fg = hi
c.colors.completion.category.border.top = secdAlpha
c.colors.completion.category.border.bottom = secdAlpha
c.colors.completion.item.selected.bg = acct
c.colors.completion.item.selected.fg = loAlpha
c.colors.completion.item.selected.match.fg = hi
c.colors.completion.item.selected.border.top = acct
c.colors.completion.item.selected.border.bottom = acct
c.colors.completion.match.fg = hi
c.colors.completion.scrollbar.bg = loAlpha
c.colors.completion.scrollbar.fg = acct

# Hints (Visual for the label, IncSearch for the matched part)
c.colors.hints.bg = acct
c.colors.hints.fg = hi
c.colors.hints.match.fg = loAlpha

# Messages, prompts, downloads
for kind in ('info', 'warning', 'error'):
    msg = getattr(c.colors.messages, kind)
    msg.bg = loAlpha
    msg.border = secdAlpha
    match kind:
        case 'warning':
            msg.fg="red"
        case 'error':
            msg.fg="yellow"
        case __:
            msg.fg=prim
c.colors.prompts.bg = loAlpha
c.colors.prompts.fg = prim
c.colors.prompts.border = f'1px solid {secd}'
c.colors.prompts.selected.bg = acct
c.colors.prompts.selected.fg = loAlpha
c.colors.downloads.bar.bg = loAlpha
c.colors.downloads.start.bg = acct
c.colors.downloads.start.fg = hi
c.colors.downloads.stop.bg = secd
c.colors.downloads.stop.fg = hi

# Pages
c.colors.webpage.bg = lo
c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.threshold.background = 150

#Font
c.fonts.default_family='ShureTechMono Nerd Font Mono'
c.fonts.default_size='12pt'

#Extra styling
c.scrolling.bar = 'never'
c.window.hide_decoration = True

#Search Engine
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'ddg': 'https://duckduckgo.com/?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
}
c.url.start_pages = ['about:blank']       # no start page to load
c.url.default_page = 'about:blank'        # what new tabs show
c.content.blocking.method = 'both'        # adblock + hosts; run :adblock-update once


#Performance
c.content.cache.size = 52428800                # 50 MB disk cache hint
c.qt.chromium.process_model = 'process-per-site'   # fewer renderer processes
c.content.webgl =False
c.content.canvas_reading = True                 # minor
c.content.prefers_reduced_motion = False
