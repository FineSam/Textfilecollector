#!/bin/sh
HOMEPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
FILES="$(ls $HOMEPATH | grep list)"

while ((1)) ; do
    for FILE in $FILES
    do
        python $HOMEPATH/dnsrequesttime.py $HOMEPATH/$FILE google.com
        sleep 1
    done
done
