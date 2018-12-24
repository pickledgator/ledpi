
# set the default locale for rpi
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
dpkg-reconfigure locales

sudo apt-get install python-pip python3-pip

pip install supervisor
wget https://gist.githubusercontent.com/danmackinlay/176149/raw/d60b505a585dda836fadecca8f6b03884153196b/supervisord.sh
sudo mv supervisord.sh /etc/init.d/supervisord
sudo update-rc.d supervisord defaults
