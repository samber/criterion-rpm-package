# Criterion repository for RHEL

## Usage

```bash
$ rpm -ivh https://github.com/samber/criterion-rpm-package/releases/download/2.4.0/libcriterion-devel-2.4.0-3.el7.x86_64.rpm
```

## Build package

```
docker-compose run --rm rpm
```

or:

```
# tools
dnf install -y 'dnf-command(builddep)' rpm-build rpm-sign rpmlint gpg pinentry

# build
dnf builddep -y SPECS/libcriterion.spec
rpmbuild -ba --clean --target=x86_64 SPECS/libcriterion.spec

# sign
gpg --export -a 'contact@samuel-berthe.fr' > /tmp/RPM-GPG-KEY-samber
rpm --import /tmp/RPM-GPG-KEY-samber

rpm --addsign RPMS/x86_64/libcriterion-devel-*
rpm --addsign SRPMS/libcriterion-devel-v2.4.0-3.src.rpm
rpm --checksig RPMS/x86_64/libcriterion-devel-*
rpm --checksig SRPMS/libcriterion-devel-v2.4.0-3.src.rpm
```

## Test RPM package

```
cd rpmbuild/
rpm -ivh RPMS/x86_64/libcriterion-devel-v2.4.0-3.x86_64.rpm
```

```
cd test/
gcc hello_world.c test_hello_world.c -o test_suite -lcriterion
./test_suite
```

## Upgrade

- Update rpmbuild/SPECS/libcriterion.spec:
  - Set `version` attribute
  - Increment `release` attribute
  - Comment the changelogs
- Update README.md with new version

```
cd ./rpmbuild/SOURCES
wget 'https://github.com/Snaipe/Criterion/releases/download/v2.4.0/criterion-2.4.0.tar.xz'
docker-compose run --rm rpm
```

## Contribute

```
rpmlint libcriterion.spec
```

or for more comments:

```
rpm -ivh <file>.rpm
rpmlint libcriterion
```
