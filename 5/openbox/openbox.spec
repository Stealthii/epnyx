Name:		openbox
Version:	3.4.7.2
Release:	5%{?dist}
Summary:	A highly configurable and standards-compliant X11 window manager

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://openbox.org/
Source0:	http://openbox.org/dist/openbox/%{name}-%{version}.tar.gz
Source1:	http://openbox.org/dist/tools/setlayout.c
Source2:	xdg-menu
Source3:	menu.xml

Patch0:		openbox-3.4.7.1-autostartdir.patch
Patch1:		openbox-3.4.7.2-gdm.patch
Patch2:		openbox-3.4.7.2-gnomesession.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	%{name}-libs = %{version}-%{release}

BuildRequires:	gettext
BuildRequires:	pango-devel
BuildRequires:	startup-notification-devel
BuildRequires:	libxml2-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXt-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXinerama-devel

%description
Openbox is a window manager designed explicity for standards-compliance and
speed. It is fast, lightweight, and heavily configurable (using XML for its
configuration data). It has many features that make it unique among window
managers: window resistance, chainable key bindings, customizable mouse
actions, multi-head/Xinerama support, and dynamically generated "pipe menus."

For a full list of the FreeDesktop.org standards with which it is compliant,
please see the COMPLIANCE file in the included documentation of this package. 
For a graphical configuration editor, you'll need to install the obconf
package. For a graphical menu editor, you'll need to install the obmenu
package.


%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig
Requires:	pango-devel
Requires:	libxml2-devel
Requires:	glib2-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package	libs
Summary:	Shared libraries for %{name}
Group:		Development/Libraries

%description	libs
The %{name}-libs package contains shared libraries used by %{name}.


%prep
%setup -q
%patch0 -p1 -b .autostartdir
%patch1 -p1 -b .gdm
%patch2 -p1 -b .gnomesession


%build
%configure \
	--disable-static
## Fix RPATH hardcoding.
sed -ie 's|^hardcode_libdir_flag_spec=.*$|hardcode_libdir_flag_spec=""|g' libtool
sed -ie 's|^runpath_var=LD_RUN_PATH$|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

gcc %{optflags} -o setlayout %{SOURCE1} -lX11

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install setlayout %{buildroot}%{_bindir}
install -p %{SOURCE2} %{buildroot}%{_datadir}/%{name}/xdg-menu
sed 's|_XDGMENU_|%{_datadir}/%{name}/xdg-menu|g' < %{SOURCE3} \
	> %{buildroot}%{_sysconfdir}/xdg/%{name}/menu.xml

%find_lang %{name}
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_datadir}/doc/%{name}


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COMPLIANCE COPYING README
%doc data/*.xsd data/menu.xml doc/rc-mouse-focus.xml
%dir %{_sysconfdir}/xdg/%{name}/
%config(noreplace) %{_sysconfdir}/xdg/%{name}/*
%{_bindir}/gnome-panel-control
%{_bindir}/gdm-control
%{_bindir}/%{name}*
%{_bindir}/setlayout
%dir %{_datadir}/openbox
%{_datadir}/openbox/xdg-autostart
%{_datadir}/openbox/xdg-menu
%{_datadir}/themes/*/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/gnome/wm-properties/
%{_datadir}/xsessions/%{name}*.desktop
%{_mandir}/man1/%{name}*.1*

%files	libs
%{_libdir}/libobrender.so.*
%{_libdir}/libobparser.so.*

%files	devel
%{_includedir}/%{name}/
%{_libdir}/libobrender.so
%{_libdir}/libobparser.so
%{_libdir}/pkgconfig/*.pc


%post libs -p /sbin/ldconfig


%postun libs -p /sbin/ldconfig


%changelog
* Thu Sep 04 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.2-5
- Don't use --choose-session option in gnome session script

* Fri Aug 01 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.2-4
- Remove field codes from commands in xdg-menu (#452403)
- Add support for launching applications in xterm to xdg-menu

* Tue Jun 10 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.2-3
- Clean up properties after gdm in session scripts (#444135)
- Add license to xdg-menu script

* Tue May 20 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.2-2
- Drop numdesks patch (#444135)

* Wed May 14 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.2-1
- Update to 3.4.7.2
- Use gnome menus by default (Luke Macken) (#443548)
- Force setting number of desktops (#444135)

* Thu Apr 17 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.7.1-1
- Update to 3.4.7.1
- Don't require /usr/share/themes

* Wed Feb 06 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.6.1-1
- Update to 3.4.6.1

* Sun Feb 03 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.6-1
- Update to 3.4.6

* Mon Jan 07 2008 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.5-1
- Update to 3.4.5

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.4-2
- Rebuild

* Sun Aug 05 2007 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.4-1
- Update to 3.4.4
- Update license tag

* Mon Jul 23 2007 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.3-1
- Update to 3.4.3
- Package setlayout tool

* Wed Jun 13 2007 Miroslav Lichvar <mlichvar@redhat.com> - 3.4.2-1
- Update to 3.4.2

* Mon Jun 04 2007 Peter Gordon <peter@thecodergeek.com> - 3.3.1-7
- Own %%{_datadir}/gnome/wm-properties instead of depending on gnome-session
  in order to reduce dependency bloat. (Resolves bug 242339; thanks to Miroslav
  Lichvar for the bug report.) 

* Tue Mar 27 2007 Peter Gordon <peter@thecodergeek.com> - 3.3.1-6
- Split shared libraries into a -libs subpackage to properly handle multilib
  setups. (This precludes the further need to %%ghost the byte-compiled
  themeupdate scripts which was introduced in the previous release.)
- Fix handling of the startup_notification build conditional. It will actually
  work properly now. :)
- Remove the hardcoded RPATH using some sed invocations from the packaging
  guidelines. 

* Mon Feb 12 2007 Peter Gordon <peter@thecodergeek.com> - 3.3.1-5
- %%ghost the byte-compiled themeupdate scripts to fix multilib conflict
  (bug #228379).

* Thu Nov 23 2006 Peter Gordon <peter@thecodergeek.com> - 3.3.1-4
- Don't own %%{_datadir}/gnome/wm-properties anymore, as that's now owned
  by gnome-session in Rawhide and we should not have ownership conflicts with
  Core packages.

* Mon Oct 02 2006 Peter Gordon <peter@thecodergeek.com> - 3.3.1-3
- Rebuild to pick up unwind info generation fixes in new GCC

* Wed Sep 20 2006 Peter Gordon <peter@thecodergeek.com> - 3.3.1-2
- Allow building with startup-notification as an rpmbuild option (though it is
  disabled by default as recommended by upstream).

* Sun Sep 09 2006 Peter Gordon <peter@thecodergeek.com> - 3.3.1-1
- Update to new 3.3.1 from upstream

* Sun Aug 27 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-3
- Mass FC6 rebuild

* Sat Aug 26 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-2
- Bump release to fix sources tagging issue

* Sat Aug 26 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-1
- Update to 3.3 final release from upstream
- Remove the slew of versioning macros, as it's overkill for this and just adds
  unneeded complexity to the spec.

* Wed Jun 28 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.8.rc2.1
- Add missing BuildRequires: libXxf86vm-devel

* Wed Jun 28 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.8.rc2
- Unconditionalize the BuildRequires for modular X.org, since it's branched
  for a specific Fedora release. 

* Mon Jun 26 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.7.rc2
- Own the %%{_datadir}/gnome/wm-properties directory (#195292)

* Fri Jun 23 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.6.rc2
- Add %%{_datadir}/themes to Requires (#195292)

* Tue Jun 20 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.5.rc2
- Own all created theme directories (#195292)
- Fix previous review bug IDs in this %%changelog to point to the recreated
  review bug (due to recent bugzilla outage) 

* Sun Jun 18 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.4.rc2
- Don't default to an executable xsession script (#195292)

* Mon Jun 12 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.3.rc2 
- Fix versioning to conform to the Extras packaging guidelines

* Mon Jun 12 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.rc2.2 
- Add %%{_datadir}/xsessions .desktop file for easy selection of Openbox at
  login screen (#195292)

* Fri Jun 09 2006 Peter Gordon <peter@thecodergeek.com> - 3.3-0.rc2.1 
- Unorphan, rewriting nearly all of the spec file
- Update to upstream 3.3 RC2

* Sun Jul 27 2003 Chris Ricker <kaboom@gatech.edu> 0:2.3.1-0.fdr.5
- Need to own /etc/X11/gdm/Sessions && /etc/X11/gdm (#440)
- Need to conflict with fluxbox (#422 / #440)

* Tue Jul 22 2003 Chris Ricker <kaboom@gatech.edu> 0:2.3.1-0.fdr.4
- Need to own /usr/share/apps/switchdesk (#422)

* Mon Jul 21 2003 Chris Ricker <kaboom@gatech.edu> 0:2.3.1-0.fdr.3
- More spec revisions (#422); change make and preserve timestamps

* Sun Jul 20 2003 Chris Ricker <kaboom@gatech.edu> 0:2.3.1-0.fdr.2
- Minor spec revisions (#422); add epoch and versions to changelogs

* Sun Jul 06 2003 Chris Ricker <kaboom@gatech.edu> 0:2.3.1-0.fdr.1
- Add switchdesk support
- Add display manager support
- Fix NLS build on Cambridge
- Fedora'ize the spec

* Sun Jun 29 2003 Chris Ricker <kaboom@gatech.edu>
- Rev to 2.3.1 release
- Make go with GCC 3.3

* Tue Mar 18 2003 Chris Ricker <kaboom@gatech.edu>
- Package of 2.3.0 release
