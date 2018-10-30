# Criterion repository for RHEL

## Usage

1- Go to `release` section
2- Download libcriterion-devel-v2.3.2-0.x86_64.rpm
3- `rpm -ivh libcriterion-devel-v2.3.2-0.x86_64.rpm`

## Build package

```
docker-compose run --rm rpm
```

or:

```
# tools
dnf install 'dnf-command(builddep)' rpm-build rpm-sign rpmlint gpg pinentry

# build
dnf builddep -y SPECS/libcriterion.spec
rpmbuild -ba --clean SPECS/libcriterion.spec

# sign
gpg --export -a 'contact@samuel-berthe.fr' > /tmp/RPM-GPG-KEY-samber
rpm --import /tmp/RPM-GPG-KEY-samber

rpm --addsign RPMS/x86_64/libcriterion-devel-*
rpm --addsign SRPMS/libcriterion-devel-v2.3.2-0.src.rpm
rpm --checksig RPMS/x86_64/libcriterion-devel-*
rpm --checksig SRPMS/libcriterion-devel-v2.3.2-0.src.rpm
```

## Test RPM package

```
cd rpmbuild/
rpm -ivh RPMS/x86_64/libcriterion-devel-v2.3.2-0.x86_64.rpm
```

```
cd test/
gcc hello_world.c test_hello_world.c -o test_suite -lcriterion
./test_suite
```

## Contribute

```
rpmlint libcriterion.spec
```
