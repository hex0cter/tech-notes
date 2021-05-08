# How to create a git repository

```
apt-get install git-core
apt-get install python-setuptools
apt-get install gitosis
git clone git://eagain.net/gitosis
cd gitosis
python setup.py install
sudo adduser --system --shell /bin/sh --gecos 'git version control' --group --disabled-password --home /home/git git
ssh-keygen -t rsa (ran by administrator, for example, root)
sudo -H -u git gitosis-init < $HOME/.ssh/id_rsa.pub
git clone git@127.0.0.1:gitosis-admin.git (server address may vary. This command is only usable for the administrator for now.)
