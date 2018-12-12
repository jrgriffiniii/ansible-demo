import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('pkg', [
    'apache2'
    ])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


def test_apache_listening_http(host):
    socket = host.socket('tcp://127.0.0.1:80')

    assert socket.is_listening
