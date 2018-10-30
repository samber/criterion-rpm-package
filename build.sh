#!/bin/bash

cd /root/rpmbuild

# build
dnf builddep -y SPECS/libcriterion.spec
rpmbuild -ba --clean SPECS/libcriterion.spec

# sign
rpm --addsign RPMS/x86_64/libcriterion-devel-*
rpm --addsign SRPMS/libcriterion-devel-v2.3.2-0.src.rpm
rpm --checksig RPMS/x86_64/libcriterion-devel-*
rpm --checksig SRPMS/libcriterion-devel-v2.3.2-0.src.rpm
