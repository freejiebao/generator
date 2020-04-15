#!/bin/bash

ed virtual.f <<'EOF'
/update_as_param2/
s/^ /c /
/svirt_proc/
s/^ /c /
/virtual/
s/= /=0 !/
wq
EOF

ed init_couplings.f <<'EOF'
/setpara2/
s/^ /c /
wq
EOF


ed Makefile <<'EOF'
/-lMadLoop/
s/ -lMadLoop/ #-lMadLoop/
wq
EOF
