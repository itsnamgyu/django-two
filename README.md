# django-two
Django 2.0 Tutorial etc.

# Environment Setup
Using _AWS Instance template Ubuntu Server 16.04.3 LTS_

## Update apt and (optionally) upgrade packages
The AWS instance default apt is too old to find pip (TODO: is it technically 'too old'?). You need to update it.
```
sudo apt update
sudo apt upgrade
```

## Install python2 and both pips
Just to practice dealing with python version issues.

The `-y` option automatically selects yes for prompts.

```
sudo apt install python2 -y
sudo apt install python-pip -y
sudo apt install python3-pip -y
```

## Python Aliases
Add this to your bash profile, i.e. `vi ~/.bashrc`
```
alias python="python3"
alias py="python"
alias py2="python2"
alias py3="python3"
```
## Update pip3
```
pip3 install --upgrade pip
```

## Install virtualenv
```
sudo pip3 install virtualenv
```

## Install virtualenvwrapper
```
sudo pip3 install virtualenvwrapper
```
Add this to your bash profile, i.e. `vi ~/.bashrc`
```
export VIRTUALENVWRAPPER_PYTHON=`which python3`
export WORKON_HOME="~/venvs"
export PROJECT_HOME=`echo ~/.`
source /usr/local/bin/virtualenvwrapper.sh
```
Source your bash profile, i.e. `source ~/.bashrc`

## Make virtualenvwrapper project
For those of you not familiar with `virtualenvwrapper`, the following command creates a `venvwrapper` project `django-two`; which means you have a project directory `~/django-two` and a virtualenv for your project somewhere in `~/venvs`.
```
mkproject django-two
```
The following command `cd`'s to the project directory and activates the virtualenv for project `django-two`
```
workon django-two
```

## Install Django
```
pip install django
```
Note that the `pip` command is aliased (TODO: is it technically alias?) to pip3 due to the venv. Try this:
```
pip --version
```

## Git Clone!
Clone this repo into the project directory `~/django-two`
```
git clone https://github.com/itsnamgyu/django-two.git
```

## Do the Django 2.0 tutorial!
[Writing your first Django app](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)

## Thanks to
[sudo apt update](https://www.rosehosting.com/blog/how-to-install-pip-on-ubuntu-16-04/)

[virualenvwrapper docs](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

[virtualenvwrapper fix](https://stackoverflow.com/questions/11507186/python-virtualenv-no-module-named-virtualenvwrapper-hook-loader)
