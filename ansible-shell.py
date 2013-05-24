#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import cmd
import ansible.runner
import sys


class AnsibleShell(cmd.Cmd):

    ansible = ansible.runner.Runner()
    groups = ansible.inventory.groups_list().keys()
    hosts = ansible.inventory.groups_list()['all']

    cwd = ''

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to the ansible-shell.\nType help or ? to list commands.\n'
        self.set_prompt()

    def cmdloop(self):
        try:
            cmd.Cmd.cmdloop(self)
        except KeyboardInterrupt as e:
            self.intro = " "
            self.cmdloop()

    def do_EOF(self, args):
        sys.stdout.write('\n')
        return -1

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print self._hist

    def set_prompt(self):
        self.prompt = 'ansible# /' + self.cwd
        if self.cwd in self.groups:
            self.prompt += ' (' + str(len(self.ansible.inventory.groups_list()[self.cwd])) + ')'
        self.prompt += '> '

    def default(self, arg):
        results = ansible.runner.Runner(
            pattern=self.cwd, forks=1,
            module_name='shell', module_args=arg,
        ).run()

        if results is None:
            print "No hosts found"
            return -1

        print "UP ***********"
        for (hostname, result) in results['contacted'].items():
            if not 'failed' in result:
                print "%s >>> %s" % (hostname, result['stdout'])

        print "FAILED *******"
        for (hostname, result) in results['contacted'].items():
            if 'failed' in result:
                print "%s >>> %s" % (hostname, result['msg'])

        print "DOWN *********"
        for (hostname, result) in results['dark'].items():
            print "%s >>> %s" % (hostname, result)

    def do_cd(self, arg):
        if arg == '..':
            try:
                self.cwd = self.ansible.inventory.groups_for_host(self.cwd)[1].name
            except Exception:
                self.cwd = ''
        elif arg == '/':
            self.cwd = ''
        elif arg in self.hosts or arg in self.groups:
            self.cwd = arg
        else:
            print "incorrect path"

        self.set_prompt()

    def do_list(self, arg):
        for item in self.ansible.inventory.list_hosts('all' if self.cwd == '' else self.cwd):
            print item

    def complete_cd(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)

        if self.cwd == '':
            completions = self.hosts + self.groups
        else:
            completions = self.ansible.inventory.list_hosts(self.cwd)

        return [s[offs:] for s in completions if s.startswith(mline)]


if __name__ == '__main__':
    AnsibleShell().cmdloop()
