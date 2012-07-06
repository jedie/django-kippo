#!/bin/bash

set -x

./manage.py syncdb --noinput
./manage.py createsuperuser --username=test --email=test@example.tld