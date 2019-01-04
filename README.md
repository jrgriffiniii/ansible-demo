# ansible-demo
Ansible Demo

## Status of the Repo

### Components

- [x] Create Vagrant and Ansible
- [x] Testinfra
- [x] Molecule
- [x] CI

## Quick Intro to Ansible

This repo is primarily an introduction to Ansible and CI testing with Molecule
using Testinfra. Most of the lessons learned here will be incorporated into
[pulibrary/princeton_ansible](https://github.com/pulibrary/princeton_ansible) It
is left here mostly to allow others interested in applying these locally.

## TDD for Infrastructure code with Molecule

[Molecule](https://molecule.readthedocs.io/en/latest/#) is a TDD framework for
testing Infrastructure as code using Ansible. In [September of 2018](https://groups.google.com/forum/#!topic/ansible-project/ehrb6AEptzA) Ansible began
treating the project as a first class citizen which made the decision to use it
much simpler

## Prerequisites

This repo has been tested almost **only** on MacOS :frowning: and is highly
opinionated. Clone this repo.

 * `brew install virtualbox`
 * `brew install vagrant`
 * `brew install pyenv`
 * `brew install pyenv-virtualenv`

## Setup your environment

To setup your virtual environment install the current version of Python using
the following command:

`pyenv install 3.7.1`

Create a virtual environment of the Python version you just installed using:

`pyenv virtualenv 3.7.1 ansible-demo-3.7.1`

This will create a virtualenv based on Python 3.7.1 under $(pyenv root)/versions
in a directory called `ansible-demo-3.7.1`

Activate your environment using the following command

`pyenv activate ansible-demo-3.7.1`

Then install all the required packages for this repo by running:

`pip install -r requirements.txt`

Molecule will only run under the `roles/pulibrary.apache2` directory, so do the
following to test:

```
cd roles/pulibrary.apache2
molecule test
```

it defaults to Ubuntu bionic or run:

```
cd roles/pulibrary.apache2
MOLECULE_DISTRO=ubuntu1604 molecule test
```

### TO DO

* Try Vagrant driver (Docker won't always) work
