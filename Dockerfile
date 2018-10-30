
FROM fedora:latest

WORKDIR /root
CMD ./build.sh

RUN dnf install -y 'dnf-command(builddep)' rpm-build rpm-sign rpmlint gpg pinentry

ADD build.sh /root
