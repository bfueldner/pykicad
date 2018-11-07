#!/bin/sh

KICAD_LIBRARY_PATH=$(pwd)
KICAD_DOCUMENTS_PATH=$KICAD_LIBRARY_PATH/documents

echo "Changing to documents directory '$KICAD_DOCUMENTS_PATH'"
cd $KICAD_DOCUMENTS_PATH
python3 -m http.server --bind 127.0.0.1 8000
