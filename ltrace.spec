Summary:	Tracks runtime library calls from dynamically linked executables
Summary(pl):	¦ledzenie odwo³añ do bibliotek w plikach linkowanych dynamicznie
Name:		ltrace
Version:	0.3.15
Release:	1
License:	GPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://ftp.debian.org/debian/pool/main/l/%{name}/%{name}_%{version}.tar.gz
ExclusiveArch:	%{ix86} m68k armv4b armv4l
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ltrace is a debugging program which runs a specified command until the
command exits. While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process. Ltrace can also
intercept and print system calls executed by the process. You should
install ltrace if you need a sysadmin tool for tracking the execution
of processes.

%description -l pl
Ltrace jest programem wspomagaj±cym debugowanie programów. Ltrace
uruchamia dane polecenie przechwytuj±c i zapisuj±c odwo³ania do
bibliotek linkowanych dynamicznie oraz sygna³y otrzymane przez
program. Ltrace potrafi tak¿e przechwytywaæ i wy¶wietlaæ odwo³ania
systemowe wykonywane przez program. Je¶li potrzebujesz narzêdzia
administracyjnego, przydatnego do ¶ledzenia dzia³ania programów,
powiniene¶ zainstalowaæ ltrace.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README TODO BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,BUGS}.gz
%config %verify(not size mtime md5) %{_sysconfdir}/ltrace.conf
%attr(755,root,root) %{_bindir}/ltrace

%{_mandir}/man1/*
