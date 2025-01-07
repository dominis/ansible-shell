# As of Ansible 2.1 ansible-shell is part of the official ansible release: https://github.com/ansible/ansible/blob/devel/lib/ansible/cli/console.py

# ansible-shell  &nbsp;  [![buildstatus][travis-buildstatus] ][1]

Interactive shell for Ansible with built-in tab completion for all the modules.

This version works with 1.x version of ansible.

![yolo](http://i.imgur.com/rxYlS9T.gif)

[travis-buildstatus]: https://travis-ci.org/dominis/ansible-shell.svg?branch=master
[1]: https://travis-ci.org/dominis/ansible-shell/builds/74308181

## Installation

For the latest release version:

    $ pip install ansible-shell

For the latest development version:

    $ pip install git+https://github.com/dominis/ansible-shell.git#egg=ansible-shell

You can upgrade an existing installation by specifying an `--upgrade` option
with the same command for whichever method you used above.

If you wish to hack on `ansible-shell`, you can install with pip's "editable"
mode -- the `ansible-shell` command available on your system will be linked to
your working copy of the code:

    $ git clone https://github.com/dominis/ansible-shell.git
    $ pip install -e ./ansible-shell

See [the pip documentation] if you need to learn more about pip.

[the pip documentation]: http://pip.readthedocs.org/en/latest/reference/pip_install.html

## Available commands:

```
cd
become
forks
list
list groups
serial
!  - force shell module instead of the ansible module of the same name (!yum update -y)
```

## Usage:

```
[root@aaa ~]# ansible-shell --one-line
Welcome to the ansible-shell.
Type help or ? to list commands.

ansible# /> cd app-pool
ansible# /app-pool (12)> list
app01.bfc.kinja.com
app02.bfc.kinja.com
app03.bfc.kinja.com
app04.bfc.kinja.com
app05.bfc.kinja.com
app06.bfc.kinja.com
app07.bfc.kinja.com
app08.bfc.kinja.com
app09.bfc.kinja.com
app10.bfc.kinja.com
app11.bfc.kinja.com
app12.bfc.kinja.com
ansible# /app-pool (12)> date
UP ***********
app12.bfc.kinja.com >>> Fri May 24 12:01:20 EDT 2013
app04.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app07.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app06.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app08.bfc.kinja.com >>> Fri May 24 12:01:20 EDT 2013
app10.bfc.kinja.com >>> Fri May 24 12:01:20 EDT 2013
app11.bfc.kinja.com >>> Fri May 24 12:01:20 EDT 2013
app09.bfc.kinja.com >>> Fri May 24 12:01:20 EDT 2013
app05.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app01.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app03.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
app02.bfc.kinja.com >>> Fri May 24 12:01:19 EDT 2013
FAILED *******
DOWN *********
ansible# /app-pool (12)> <TAB>
Display all 100 possibilities? (y or n)
EOF                  cd                   exit                 group_by             macports             openbsd_pkg          rabbitmq_parameter   service              virt
add_host             cloudformation       facter               help                 mail                 opkg                 rabbitmq_plugin      set_fact             wait_for
apt                  command              fail                 hg                   mongodb_user         osx_say              rabbitmq_user        setup                yum
apt_key              copy                 fetch                hipchat              mount                pacman               rabbitmq_vhost       shell                zfs
apt_repository       cron                 file                 homebrew             mqtt                 pause                raw                  slurp
assemble             debug                filesystem           ini_file             mysql_db             ping                 rax                  subversion
async_status         django_manage        fireball             irc                  mysql_user           pip                  rhn_channel          supervisorctl
async_wrapper        easy_install         flowdock             jabber               nagios               pkgin                riak                 svr4pkg
authorized_key       ec2                  gem                  lineinfile           netscaler            pkgng                s3                   sysctl
bigip_pool           ec2_elb              get_url              list                 newrelic_deployment  postgresql_db        script               template
bzr                  ec2_facts            git                  lvg                  npm                  postgresql_privs     seboolean            uri
campfire             ec2_vol              group                lvol                 ohai                 postgresql_user      selinux              user
ansible# /app-pool (12)> netscaler <TAB>
action        name          nsc_host      nsc_protocol  password      type          user
ansible# /app-pool (12)> netscaler nsc_
```
