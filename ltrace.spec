Summary: Tracks runtime library calls from dynamically linked executables.
Name: ltrace
Version: 0.3.8
Release: 1
Source: ftp://ftp.debian.org/debian/dists/unstable/main/source/utils/ltrace_%{version}.tar.gz
Copyright: GPL
Group: Development/Debuggers
ExclusiveArch: i386
ExclusiveArch: i486
ExclusiveArch: i586
ExclusiveArch: i686
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root

%description
Ltrace is a debugging program which runs a specified command until the
command exits.  While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process and
the signals received by the executed process.  Ltrace can also intercept
and print system calls executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%prep
%setup -q

%build
#./configure --prefix=/usr

%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README TODO BUGS
%{_prefix}/bin/ltrace
%{_prefix}/man/man1/ltrace.1
%config /etc/ltrace.conf
