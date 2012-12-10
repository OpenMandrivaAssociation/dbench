Summary: Filesystem benchmark similar to Netbench
Name: dbench
Version: 4.0
Release: 2
Source: http://samba.org/ftp/tridge/dbench/%{name}-%{version}.tar.gz
License: GPLv3+
URL: http://samba.org/ftp/tridge/dbench/README
Group: System/Kernel and hardware
BuildRequires: pkgconfig(popt)
Requires(post): rpm-helper
Requires(preun): rpm-helper

%description
dbench is a filesystem benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring
a lab of Windows load generators to run. It is now considered a de-facto
standard for generating load on the Linux VFS.

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
install -c -m 0755 -s dbench %{buildroot}%{_bindir}/dbench
install -c -m 0755 -s tbench %{buildroot}%{_bindir}/tbench
install -c -m 0755 -s tbench_srv %{buildroot}%{_bindir}/tbench_srv
install -c -m 0644 dbench.1 %{buildroot}%{_mandir}/man1/dbench.1
install -c -m 0644 client.txt %{buildroot}%{_datadir}/%{name}/client.txt
cd %{buildroot}%{_mandir}/man1/
ln -sf dbench.1 tbench.1
ln -sf dbench.1 tbench_srv.1
cd -

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


%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 4.0-1mdv2011.0
+ Revision: 571916
- use configure2_5x

* Wed Jun 10 2009 Jérôme Brenier <incubusss@mandriva.org> 4.0-1mdv2010.0
+ Revision: 384596
- add BR : libpopt-devel
- update to new version 4.0
- execute autogen.sh
- clean spec file
- fix license

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.04-5mdv2009.0
+ Revision: 243963
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 3.04-3mdv2008.1
+ Revision: 170794
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.04-2mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 16 2007 Andreas Hasenack <andreas@mandriva.com> 3.04-2mdv2007.1
+ Revision: 13499
- Import dbench



* Thu Mar 30 2006 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 3.04-1mdk
- first package
