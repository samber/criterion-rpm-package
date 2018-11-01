#!/bin/bash

cd /root/rpmbuild

# build
dnf builddep -y SPECS/libcriterion.spec
rpmbuild -ba --clean --target=x86_64 SPECS/libcriterion.spec

# sign
rpm --addsign RPMS/x86_64/libcriterion-devel-*
rpm --addsign SRPMS/libcriterion-devel-*
rpm --checksig RPMS/x86_64/libcriterion-devel-*
rpm --checksig SRPMS/libcriterion-devel-*
