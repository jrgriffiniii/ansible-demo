import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_deploy_user_has_uid(host):
    deploy_user = host.user('deploy')

    assert 102 in deploy_user.uid
