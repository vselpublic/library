#!/bin/bash

export FLASK_CONFIG="production"
export SECRET_KEY="4bs^7bre5aq8%$&JFDgtfd4#@"
#export DEV_DATABASE_URL="postgresql://library_app:12345librarydb67890@fordevpurpose.cn2hbxgdnr5i.eu-west-1.rds.amazonaws.com:5432/librarydb"
export DEV_DATABASE_URL="postgresql://library_app:12345librarydb67890@109.251.117.59:5432/librarydb"
export TEST_DATABASE_URL="postgresql://library_app:12345librarydb67890@localhost/librarydbtest"
export PROD_DATABASE_URL="postgresql://library_app:12345librarydb67890@fordev.cwwcbs15un0t.eu-central-1.rds.amazonaws.com:5432/librarydb"
