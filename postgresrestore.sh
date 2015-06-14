#!/bin/bash
#made with using:
#pg_dumpall > postgresfulldump
#!!!!!change /var/lib/postgresql to yours default Postgres DIR!!!!!
sudo cp ./postgresfulldump /var/lib/postgresql/postgresfulldump
sudo su - postgres  <<'EOF'
psql -f postgresfulldump postgres
EOF
