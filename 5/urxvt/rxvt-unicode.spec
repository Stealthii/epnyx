Name:           rxvt-unicode
Version:        9.05
Release:        1%{?dist}
Summary:        Rxvt-unicode is an unicode version of rxvt

Group:          User Interface/X
License:        GPLv2+
URL:            http://software.schmorp.de/
Source0:        http://dist.schmorp.de/%{name}/%{name}-%{version}.tar.bz2
Source1:        rxvt-unicode.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  /usr/bin/tic
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  perl
BuildRequires:  libAfterImage-devel

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%package ml
Summary:        Multi-language version of rxvt-unicode
Group:          User Interface/X
Requires:       %{name} = %{version}-%{release}

%description ml
Version of rxvt-unicode with enhanced multi-language support.

%prep
%setup -q -c %{name}-%{version}
pushd %{name}-%{version}
popd

cp -r %{name}-%{version} %{name}-%{version}-ml

%build
# standard version
pushd %{name}-%{version}
%configure \
 --enable-keepscrolling \
 --enable-selectionscrolling \
 --enable-pointer-blank \
 --enable-utmp \
 --enable-wtmp \
 --enable-lastlog \
 --enable-xft \
 --enable-font-styles \
 --enable-afterimage \
 --enable-transparency \
 --enable-fading \
 --enable-rxvt-scroll \
 --enable-next-scroll \
 --enable-xterm-scroll \
 --enable-plain-scroll \
 --enable-mousewheel \
 --enable-slipwheeling \
 --enable-smart-resize \
 --enable-frills \
 --enable-xim \
 --enable-resources \
 --with-codesets=all \
 --enable-iso14755 \
 --with-term=rxvt-unicode

make CFLAGS="%{optflags}" LDFLAGS="-lfontconfig" %{?_smp_mflags}
popd

# multi-language version
pushd %{name}-%{version}-ml
%configure \
 --enable-keepscrolling \
 --enable-selectionscrolling \
 --enable-pointer-blank \
 --enable-utmp \
 --enable-wtmp \
 --enable-lastlog \
 --enable-unicode3 \
 --enable-combining \
 --enable-xft \
 --enable-font-styles \
 --enable-afterimage \
 --enable-transparency \
 --enable-fading \
 --enable-rxvt-scroll \
 --enable-next-scroll \
 --enable-xterm-scroll \
 --enable-plain-scroll \
 --enable-mousewheel \
 --enable-slipwheeling \
 --enable-smart-resize \
 --enable-frills \
 --enable-xim \
 --enable-resources \
 --with-codesets=all \
 --enable-iso14755 \
 --with-term=rxvt-unicode \
 --with-name=urxvt-ml

make CFLAGS="%{optflags}" LDFLAGS="-lfontconfig" %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}


for ver in \
 %{name}-%{version} %{name}-%{version}-ml;
do
    pushd ${ver}
    make install DESTDIR=%{buildroot}
    popd
done;

#tic -o ${buildroot}/%_datadir/terminfo doc/etc/rxvt-unicode.terminfo
# install terminfo for 256color
mkdir -p %{buildroot}%{_datadir}/terminfo/r/
tic -e rxvt-unicode -s -o %{buildroot}%{_datadir}/terminfo/ \
 %{name}-%{version}/doc/etc/rxvt-unicode.terminfo

desktop-file-install \
  --vendor=fedora \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category=X-Fedora \
  %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/README.FAQ
%doc %{name}-%{version}/INSTALL
%doc %{name}-%{version}/doc/README.xvt
%doc %{name}-%{version}/doc/etc
%doc %{name}-%{version}/doc/changes.txt
%doc %{name}-%{version}/COPYING
%{_bindir}/urxvt
%{_bindir}/urxvtc
%{_bindir}/urxvtd
%{_datadir}/terminfo/r/*
%{_mandir}/man*/*
%{_datadir}/applications/*
%{_libdir}/urxvt

%files ml
%defattr(-,root,root,-)
%{_bindir}/urxvt-ml
%{_bindir}/urxvt-mlc
%{_bindir}/urxvt-mld

%changelog
* Mon Jun 16 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.05-1
- version upgrade
- add terminfo

* Sat Jan 26 2008 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 9.0-1
- version upgrade

* Thu Dec 27 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.9-1
- version upgrade

* Mon Dec 17 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.8-1
- version upgrade

* Wed Dec 12 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-2
- remove utempter patch for now

* Thu Nov 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.5a-1
- version upgrade

* Wed Nov 07 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-2
- fix #368921 (Rxvt.backgroundPixmap needs libAfterImage support BR now)
- add patch for utempter support

* Sun Oct 28 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.4-1
- version upgrade

* Wed Aug 22 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- 8.3-1
- version upgrade
- new license tag

* Sat Jun 02 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.2-1
- version upgrade (#239421)

* Sun Jan 21 2007 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-2
- drop terminfo file it is included in ncurses now

* Fri Dec 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.1-1
- version upgrade

* Thu Nov 02 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
8.0-1
- version upgrade

* Fri Sep 15 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-2
- FE6 rebuild

* Tue Aug 08 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.9-1
- version upgrade

* Tue Jul 18 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.8-1
- version upgrade

* Tue Feb 21 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.7-1
- version upgrade

* Thu Feb 16 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-2
- Rebuild for Fedora Extras 5

* Fri Feb 10 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.6-1
- version upgrade

* Tue Jan 31 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.5-1
- version upgrade

* Sat Jan 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.4-1
- version upgrade

* Fri Jan 27 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.3a-1
- version upgrade

* Mon Jan 23 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.2-1
- version upgrade (should resolve #178561)

* Thu Jan 19 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.1-1
- version upgrade

* Sat Jan 14 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
7.0-1
- version upgrade

* Thu Jan 05 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.3-1
- version upgrade

* Tue Jan 03 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.2-1 
- version upgrade

* Wed Dec 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.1-1
- version upgrade

* Sun Dec 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
6.0-1
- version upgrade

* Sun Dec 18 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.9-1
- version upgrade

* Fri Nov 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-2
- modular xorg integration

* Tue Oct 25 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.8-1
- version upgrade

* Sun Oct 16 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-3
- enable frills (#170965)

* Sat Sep 17 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-2
- enable iso14755 (#168548)

* Tue Aug 23 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.7-1
- version upgrade

* Sun Jun 05 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-3
- add dist

* Thu Jun 02 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-2
- minor cleanups

* Thu May 12 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
5.5-1
- Version upgrade (5.5)

* Mon Mar 28 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0:5.3-1
- Version upgrade (5.3)

* Wed Feb 09 2005 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- Initial RPM release.
