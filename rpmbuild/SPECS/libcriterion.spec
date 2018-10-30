%define _prefix /usr
%define _libdir %{_prefix}/lib
%define libname criterion

Name:           lib%{libname}-devel
Version:        v2.3.2
Release:        0
Summary:        A cross-platform C and C++ unit testing framework for the 21th century
Group:          Development/Libraries
License:        MIT
URL:            https://github.com/Snaipe/Criterion
Vendor:         Snaipe
Source:         criterion-v2.3.2.tar.bz2
Prefix:         %{_prefix}
Packager:       %{packager}
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      x86_64
BuildRequires:  make, cmake, gcc, clang
Requires:       gcc

%description
Most test frameworks for C require a lot of boilerplate code to set up tests and test suites -- you need to create a main, then register new test suites, then register the tests within these suits, and finally call the right functions.

This gives the user great control, at the unfortunate cost of simplicity.

Criterion follows the KISS principle, while keeping the control the user would have with other frameworks:

- C99 and C++11 compatible.
- Tests are automatically registered when declared.
- Implements a xUnit framework structure.
- A default entry point is provided, no need to declare a main unless you want to do special handling.
- Test are isolated in their own process, crashes and signals can be reported and tested.
- Unified interface between C and C++: include the criterion header and it just works.
- Supports parameterized tests and theories.
- Progress and statistics can be followed in real time with report hooks.
- TAP output format can be enabled with an option.
- Runs on Linux, FreeBSD, Mac OS X, and Windows (Compiling with MinGW GCC and Visual Studio 2015+).

Full documentation here: https://criterion.readthedocs.io

%prep
%setup -q -n %{libname}-%{version}

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} ..
cmake --build .

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

cd build
make install DESTDIR=%{buildroot}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/lib%{libname}.so*
%{_includedir}/%{libname}/*.h
%{_includedir}/%{libname}/internal/*.h
%{_includedir}/%{libname}/internal/*.hxx
%{_datarootdir}/pkgconfig/*.pc
