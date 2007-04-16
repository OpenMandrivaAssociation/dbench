Summary: DBench is a filesystem benchmark similar to Netbench
Name: dbench
Version: 3.04
Release: %mkrel 1
Source: http://samba.org/ftp/tridge/dbench/dbench-3.04.tar.gz
License: GPL
URL: http://samba.org/ftp/tridge/dbench/README
Group: System/Kernel and hardware
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
dbench is a filesystem benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring
a lab of Windows load generators to run. It is now considered a de-facto
standard for generating load on the Linux VFS.

%prep
%setup -q

%build
%configure --datadir=/usr/share/dbench
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -c -m 0755 -s dbench $RPM_BUILD_ROOT%{_bindir}/dbench
install -c -m 0755 -s tbench $RPM_BUILD_ROOT%{_bindir}/tbench
install -c -m 0755 -s tbench_srv $RPM_BUILD_ROOT%{_bindir}/tbench_srv
install -c -m 0644 dbench.1 $RPM_BUILD_ROOT%{_mandir}/man1/dbench.1
install -c -m 0644 client.txt $RPM_BUILD_ROOT%{_datadir}/%{name}/client.txt
cd $RPM_BUILD_ROOT%{_mandir}/man1/
ln -sf dbench.1 tbench.1
ln -sf dbench.1 tbench_srv.1
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL README
%attr(755,root,root) %{_bindir}/dbench
%attr(755,root,root) %{_bindir}/tbench
%attr(755,root,root) %{_bindir}/tbench_srv
%attr(644,root,root) %{_mandir}/man1/dbench.1.*
%attr(644,root,root) %{_mandir}/man1/tbench.1.*
%attr(644,root,root) %{_mandir}/man1/tbench_srv.1.*
%attr(644,root,root) %{_datadir}/%{name}/client.txt
