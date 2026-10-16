#!/usr/bin/env python3
"""Turn the Claude-artifact version of Fraction Lab into the GitHub Pages index.html.

Adds the Home Screen install tags and the offline service-worker registration.
Safe to run more than once.

usage: make_site.py <artifact.html> <out/index.html>
"""
import sys

HEAD = '''<meta name="theme-color" content="#141312">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/icon-180.png">
<link rel="icon" type="image/svg+xml" href="icons/icon.svg">
'''
SW = '''<script>
if('serviceWorker' in navigator){window.addEventListener('load',()=>{navigator.serviceWorker.register('sw.js').catch(()=>{})})}
</script>
'''

def main(src, dst):
    s = open(src, encoding='utf-8').read()
    if s.count('<title>') != 1 or s.count('</body>') != 1:
        sys.exit('Expected exactly one <title> and one </body>; is this the full app file?')
    if 'manifest.webmanifest' not in s:
        s = s.replace('<title>', HEAD + '<title>', 1)
    if 'serviceWorker' not in s:
        s = s.replace('</body>', SW + '</body>', 1)
    open(dst, 'w', encoding='utf-8').write(s)
    print('wrote', dst)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
