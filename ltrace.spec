Summary:	Tracks runtime library calls from dynamically linked executables
Summary(es):	EnseЯa informaciСn sobre las llamadas a funciones de bibliotecas en binarios dinАmicamente conectados
Summary(pl):	╕ledzenie odwoЁaЯ do bibliotek w plikach linkowanych dynamicznie
Summary(pt_BR):	Mostra informaГУes sobre as chamadas Ю funГУes de bibliotecas em binАrios dinamicamente ligados
Summary(ru):	Выводит трассу библиотечных и системных вызовов программы
Summary(uk):	Вида╓ трасу б╕бл╕отечних та системних виклик╕в програми
Name:		ltrace
Version:	0.3.23
Release:	1
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.debian.org/debian/pool/main/l/%{name}/%{name}_%{version}.tar.gz
Patch0:		%{name}-nsyscals0.patch
Patch1:		%{name}-Makefile.in.patch
BuildRequires:	autoconf
BuildRequires:	automake
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
especificado hasta su tИrmino. Intercepta y registra las llamadas, a
las funciones de las bibliotecas compartidas, hechas por el programa
en ejecuciСn, y los seЯales recibidos por el proceso. TambiИn puede
interceptar y enseЯar las llamadas al sistema operativo hechas por el
programa.

%description -l pl
Ltrace jest programem wspomagaj╠cym debugowanie programСw. Ltrace
uruchamia dane polecenie przechwytuj╠c i zapisuj╠c odwoЁania do
bibliotek linkowanych dynamicznie oraz sygnaЁy otrzymane przez
program. Ltrace potrafi tak©e przechwytywaФ i wy╤wietlaФ odwoЁania
systemowe wykonywane przez program. Je╤li potrzebujesz narzЙdzia
administracyjnego, przydatnego do ╤ledzenia dziaЁania programСw,
powiniene╤ zainstalowaФ ltrace.

%description -l pt_BR
ltrace И um programa que simplesmente executa um comando especificado
atИ seu tИrmino. Ele intercepta e registra as chamadas Ю funГУes a
bibliotecas compartilhadas feitas pelo programa em execuГЦo e os
sinais recebidos pelo processo. TambИm pode interceptar e mostrar as
chamadas ao sistema operacional feitas pelo programa.

%description -l ru
Ltrace - это отладочная программа, которая запускает указанную
программу, перехватывает и записывает как вызовы динамических
библиотек, так и сигналы, получаемые выполняющимся процессом. Ltrace
может также перехватывать и печатать системные вызовы, выполняемые
процессом.

%description -l uk
Ltrace - це програма, яка запуска╓ вказану програму та перехвачу╓ й
запису╓ як виклики динам╕чних б╕бл╕отек, так ╕ сигнали, як╕ отриму╓
запущений процес. Ltrace може також перехвачувати ╕ друкувати системн╕
виклики цього процесу.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure
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
