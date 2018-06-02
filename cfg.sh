#!/bin/sh

cp $pwd'boot.sh' /etc/init.d/
if [ ! -f /etc/init.d/boot.sh ]; then
    echo "boot not found!"
fi

chmod +x /etc/init.d/boot.sh
sh boot.sh
apt-get install vim


