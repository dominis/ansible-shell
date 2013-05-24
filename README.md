# ansible-shell


Interactive ansible shell

## Availabe commands:

```
cd
list
```
## Usage:
```
[root@aaa ~]# ansible-shell
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
ansible# /app-pool (12)>
```