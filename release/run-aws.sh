#!/bin/bash
set -e

cat > ./inventory.ini <<EOF
[local]
localhost

[blbox]

EOF

cat > ./vars/run-vars.yml <<EOF
---
rel: $1
aaki: ${AWS_ACCESS_KEY}
asak: ${AWS_SECRET_ACCESS_KEY}
EOF

cat ./inventory.ini

CMD="ansible-playbook -vv -i ./inventory.ini  ./aws.yml"

echo $CMD
$CMD