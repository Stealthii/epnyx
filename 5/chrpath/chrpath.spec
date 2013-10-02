Summary: Modify rpath of compiled programs
Name: chrpath
Version: 0.13
Release: 5%{?dist}
License: GPL+
Group: Development/Tools
URL: ftp://ftp.hungry.com/pub/hungry/chrpath/
Patch0: chrpath-0.13-NULL-entry.patch
Source0: ftp://ftp.hungry.com/pub/hungry/chrpath/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
chrpath allows you to modify the dynamic library load path (rpath) of
compiled programs.  Currently, only removing and modifying the rpath
is supported.

%prep
%setup -q
%patch0 -p1 -b .NULL

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -fr %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README NEWS ChangeLog*
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1*

%changelog
* Thu Jul 23 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-5
- Fix last entry in .dynamic (by Christian Krause <chkr@plauener.de>).

* Sat Sep  8 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.13-2
- License: GPL+

* Sun Mar 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.13-1
- Initial build.
