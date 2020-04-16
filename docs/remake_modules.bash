VABENE_DIR=$(readlink -e "$0")
VABENE_DIR=${VABENE_DIR%/*/*}

rm -- $VABENE_DIR/docs/source/{vabene.*.rst,vabene.rst}
sphinx-apidoc -feEM -o "$VABENE_DIR/docs/source" "$VABENE_DIR/src/vabene"
