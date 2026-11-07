#!/bin/sh
set -e
cd "$(dirname "$0")"
python3 gen.py
mkdir -p dist && rm -f dist/sublime-mariana-theme.jar
python3 -m json.tool src/Mariana.theme.json >/dev/null
xmllint --noout src/META-INF/plugin.xml src/Mariana.xml
(cd src && zip -qr ../dist/sublime-mariana-theme.jar .)
echo "dist/sublime-mariana-theme.jar"
