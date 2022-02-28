%define projectname criterion

Name:           lib%{projectname}-devel
Version:        2.4.0
Release:        3%{?dist}
Summary:        A cross-platform C and C++ unit testing framework for the 21th century
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/Snaipe/Criterion
Vendor:         Snaipe
Source:         https://github.com/Snaipe/Criterion/releases/download/v2.4.0/criterion-2.4.0.tar.xz
Prefix:         %{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  make, cmake, gcc, clang, meson, ninja-build, libgit2, libffi-devel
Requires:       gcc

%description
Most test frameworks for C require a lot of boilerplate code to set up tests
and test suites -- you need to create a main, then register new test suites,
then register the tests within these suits, and finally call the right
functions.

This gives the user great control, at the unfortunate cost of simplicity.

Criterion follows the KISS principle, while keeping the control the user would
have with other frameworks:

- C99 and C++11 compatible.
- Tests are automatically registered when declared.
- Implements a XUnit framework structure.
- A default entry point is provided, no need to declare a main unless you
want to do special handling.
- Test are isolated in their own process, crashes and signals can be
reported and tested.
- Unified interface between C and C++: include the criterion header and
it just works.
- Supports parameter tests and theories.
- Progress and statistics can be followed in real time with report hooks.
- TAP output format can be enabled with an option.
- Runs on Linux, FreeBSD, Mac OS X, and Windows
(Compiling with MinGW GCC and Visual Studio 2015+).

Full documentation here: https://criterion.readthedocs.io

%prep

%setup -q -n %{projectname}-%{version}

%build

# old build system (up to v2.3.3)
# mkdir build
# cd build
# cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} ..
# cmake --build .

# new build system (starting v2.4.0)
meson build --prefix /usr
ninja -C build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}

# old build system (up to v2.3.3)
# cd build
# make install DESTDIR=%{buildroot}
# mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/lib64

# new build system (starting v2.4.0)
meson install -C build/ --destdir %{buildroot}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/lib%{projectname}.so*
%{_includedir}/%{projectname}/*.h
%{_includedir}/%{projectname}/internal/*.h
%{_includedir}/%{projectname}/internal/*.hxx
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Feb 23 2022 Samuel Berthe <dev@samuel-berthe.fr> v2.4.0-3.samber
- Upgrade to libcriterion v2.4.0
* Sat Nov 16 2019 Samuel Berthe <dev@samuel-berthe.fr> v2.3.3-2.samber
- Upgrade to libcriterion v2.3.3
* Tue Oct 30 2018 Samuel Berthe <dev@samuel-berthe.fr> v2.3.2-1.samber
- Initial RPM release
