Summary:	Filesystem benchmark similar to Netbench
Name:		dbench
Version:	4.0
Release:	4
License:	GPLv3+
Group:		System/Kernel and hardware
Url:		http://samba.org/ftp/tridge/dbench/README
Source0:	http://samba.org/ftp/tridge/dbench/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(popt)

%description
dbench is a filesystem benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring
a lab of Windows load generators to run. It is now considered a de-facto
standard for generating load on the Linux VFS.

%files
%doc COPYING README
%attr(755,root,root) %{_bindir}/dbench
%attr(755,root,root) %{_bindir}/tbench
%attr(755,root,root) %{_bindir}/tbench_srv
%attr(644,root,root) %{_mandir}/man1/dbench.1.*
%attr(644,root,root) %{_mandir}/man1/tbench.1.*
%attr(644,root,root) %{_mandir}/man1/tbench_srv.1.*
%attr(644,root,root) %{_datadir}/%{name}/client.txt

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./autogen.sh
%configure2_5x --datadir=/usr/share/dbench
%make CC="cc %ldflags"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/%{name}
install -c -m 0755 dbench %{buildroot}%{_bindir}/dbench
install -c -m 0755 tbench %{buildroot}%{_bindir}/tbench
install -c -m 0755 tbench_srv %{buildroot}%{_bindir}/tbench_srv
install -c -m 0644 dbench.1 %{buildroot}%{_mandir}/man1/dbench.1
install -c -m 0644 client.txt %{buildroot}%{_datadir}/%{name}/client.txt
pushd %{buildroot}%{_mandir}/man1/
ln -sf dbench.1 tbench.1
ln -sf dbench.1 tbench_srv.1
popd

