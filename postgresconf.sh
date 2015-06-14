#!/bin/bash

sudo su - postgres  <<'EOF'
createuser library_app
createdb librarydb
psql -c "ALTER ROLE library_app WITH password '12345librarydb67890'"
psql -c "GRANT ALL PRIVILEGES ON DATABASE librarydb TO library_app"
exit
EOF