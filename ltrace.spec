Summary:	Tracks runtime library calls from dynamically linked executables
Summary(es):	Enseña información sobre las llamadas a funciones de bibliotecas en binarios dinámicamente conectados
Summary(pl):	¦ledzenie odwo³añ do bibliotek w plikach linkowanych dynamicznie
Summary(pt_BR):	Mostra informações sobre as chamadas à funções de bibliotecas em binários dinamicamente ligados
Name:		ltrace
Version:	0.3.16
Release:	1
License:	GPL
Group:		Development/Debuggers
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

%description -l es
ltrace es un programa que sencillamente ejecuta un comando
especificado hasta su término. Intercepta y registra las llamadas, a
las funciones de las bibliotecas compartidas, hechas por el programa
en ejecución, y los señales recibidos por el proceso. También puede
interceptar y enseñar las llamadas al sistema operativo hechas por el
programa.

%description -l pl
Ltrace jest programem wspomagaj±cym debugowanie programów. Ltrace
uruchamia dane polecenie przechwytuj±c i zapisuj±c odwo³ania do
bibliotek linkowanych dynamicznie oraz sygna³y otrzymane przez
program. Ltrace potrafi tak¿e przechwytywaæ i wy¶wietlaæ odwo³ania
systemowe wykonywane przez program. Je¶li potrzebujesz narzêdzia
administracyjnego, przydatnego do ¶ledzenia dzia³ania programów,
powiniene¶ zainstalowaæ ltrace.

%description -l pt_BR
ltrace é um programa que simplesmente executa um comando especificado
até seu término. Ele intercepta e registra as chamadas à funções a
bibliotecas compartilhadas feitas pelo programa em execução e os
sinais recebidos pelo processo. Também pode interceptar e mostrar as
chamadas ao sistema operacional feitas pelo programa.

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
