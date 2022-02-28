
FROM fedora:latest

WORKDIR /root
CMD ./build.sh

RUN dnf install -y 'dnf-command(builddep)' rpm-build rpm-sign rpmlint gpg pinentry pkg-config

# These dependencies will be requested by builddep anyway (listed in SPECS/libcriterion.spec).
# Installing binaries here allow a better use of docker layer caching.
RUN dnf install -y make cmake gcc clang meson ninja-build libgit2 libffi-devel

ADD build.sh /root
