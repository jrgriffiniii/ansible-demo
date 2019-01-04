import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_deploy_user_is_part_of_group(host):
    deploy_user = host.user('deploy')

    assert "deploy" in deploy_user.group
