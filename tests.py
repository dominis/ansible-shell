import pytest
import imp
import os

ansible_shell_path = os.path.dirname(__file__) + '/ansible-shell'
with open(ansible_shell_path) as f:
    ansible_shell = imp.load_module(
        'ansible_shell', f, ansible_shell_path, ('', 'U', 1))


@pytest.mark.parametrize(('hosts', 'serial', 'result'), [
    (['a', 'b'], 1, [['a'], ['b']]),
    (['a', 'b', 'c'], 2, [['a', 'b'], ['c']]),
    ([], 1, []),
    ([], 0, []),
    (['a', 'b'], 0, [['a', 'b']]),
])
def test_generating_batches(hosts, serial, result):
    assert result == ansible_shell.get_hosts_batches(hosts, serial)
