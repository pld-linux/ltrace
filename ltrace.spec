Summary:	Tracks runtime library calls from dynamically linked executables
Summary(es.UTF-8):	Enseña información sobre las llamadas a funciones de bibliotecas en binarios dinámicamente conectados
Summary(pl.UTF-8):	Śledzenie odwołań do bibliotek w plikach konsolidowanych dynamicznie
Summary(pt_BR.UTF-8):	Mostra informações sobre as chamadas à funções de bibliotecas em binários dinamicamente ligados
Summary(ru.UTF-8):	Выводит трассу библиотечных и системных вызовов программы
Summary(uk.UTF-8):	Видає трасу бібліотечних та системних викликів програми
Name:		ltrace
Version:	0.5.3
Release:	1
License:	GPL v2+
Group:		Development/Debuggers
Source0:	ftp://ftp.debian.org/debian/pool/main/l/ltrace/%{name}_%{version}.orig.tar.gz
# Source0-md5:	3fa7fe715ab879db08bd06d1d59fd90f
Patch0:		%{name}-Makefile.in.patch
Patch1:		%{name}-debian.patch
Patch2:		poor-mans-autoconf.patch
Patch3:		ptrace-headers.patch
URL:		http://ltrace.alioth.debian.org/
BuildRequires:	elfutils-devel
# for libsupc++ (used for symbols demangling)
BuildRequires:	gcc-c++
ExclusiveArch:	alpha armv4b armv4l %{ix86} ia64 m68k ppc s390 sparc %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ltrace is a debugging program which runs a specified command until the
command exits. While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process. Ltrace can also
intercept and print system calls executed by the process. You should
install ltrace if you need a sysadmin tool for tracking the execution
of processes.

%description -l es.UTF-8
ltrace es un programa que sencillamente ejecuta un comando
especificado hasta su término. Intercepta y registra las llamadas, a
las funciones de las bibliotecas compartidas, hechas por el programa
en ejecución, y los señales recibidos por el proceso. También puede
interceptar y enseñar las llamadas al sistema operativo hechas por el
programa.

%description -l pl.UTF-8
Ltrace jest programem wspomagającym debugowanie programów. Ltrace
uruchamia dane polecenie przechwytując i zapisując odwołania do
bibliotek konsolidowanych dynamicznie oraz sygnały otrzymane przez
program. Ltrace potrafi także przechwytywać i wyświetlać odwołania
systemowe wykonywane przez program. Jeśli potrzebujesz narzędzia
administracyjnego, przydatnego do śledzenia działania programów,
powinieneś zainstalować ltrace.

%description -l pt_BR.UTF-8
ltrace é um programa que simplesmente executa um comando especificado
até seu término. Ele intercepta e registra as chamadas à funções a
bibliotecas compartilhadas feitas pelo programa em execução e os
sinais recebidos pelo processo. Também pode interceptar e mostrar as
chamadas ao sistema operacional feitas pelo programa.

%description -l ru.UTF-8
Ltrace - это отладочная программа, которая запускает указанную
программу, перехватывает и записывает как вызовы динамических
библиотек, так и сигналы, получаемые выполняющимся процессом. Ltrace
может также перехватывать и печатать системные вызовы, выполняемые
процессом.

%description -l uk.UTF-8
Ltrace - це програма, яка запускає вказану програму та перехвачує й
записує як виклики динамічних бібліотек, так і сигнали, які отримує
запущений процес. Ltrace може також перехвачувати і друкувати системні
виклики цього процесу.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ltrace.conf
%attr(755,root,root) %{_bindir}/ltrace
%{_mandir}/man1/*
