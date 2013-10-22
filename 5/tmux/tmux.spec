Name:           tmux
Version:        1.8
Release:        1%{?dist}
Summary:        A terminal multiplexer

Group:          Applications/System
# Most of the source is ISC licensed; some of the files in compat/ are 2 and
# 3 clause BSD licensed.
License:        ISC and BSD
URL:            http://sourceforge.net/projects/tmux
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  ncurses-devel
BuildRequires:  libevent-devel >= 1.4.14b

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or
windows) to be accessed and controlled from a single terminal.  tmux is
intended to be a simple, modern, BSD-licensed alternative to programs such
as GNU Screen.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} LDFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLBIN="install -p -m 755" INSTALLMAN="install -p -m 644"

%post
if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/tmux" > %{_sysconfdir}/shells
else
    grep -q "^%{_bindir}/tmux$" %{_sysconfdir}/shells || echo "%{_bindir}/tmux" >> %{_sysconfdir}/shells
fi

%postun
if [ $1 -eq 0 ] && [ -f %{_sysconfdir}/shells ]; then
    sed -i '\!^%{_bindir}/tmux$!d' %{_sysconfdir}/shells
fi

%files
%defattr(-,root,root,-)
%doc CHANGES FAQ TODO examples/
%doc %{_mandir}/man1/tmux.1.*
%{_bindir}/tmux

%changelog
* Tue Oct 22 2013 Daniel Porter <dporter@nyx.com> - 1.8-1
- new upstream release

* Tue Oct 22 2013 Daniel Porter <dporter@nyx.com> - 1.7-1
- new upstream release

* Tue Oct 22 2013 Daniel Porter <dporter@nyx.com> - 1.6-2
- Remove outdated packages and improve setup

* Mon Jan 23 2012 David Hrbáč <david@hrbac.cz> - 1.6-1
- new upstream release

* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Mon Apr 11 2011 David Hrbáč <david@hrbac.cz> - 1.4-2
- CVE-2011-1496 fix
- imported Fedora patches
- added examples

* Mon Apr 11 2011 David Hrbáč <david@hrbac.cz> - 1.4-1
- new upstream release

* Tue Jul 20 2010 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Fri Nov 13 2009 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Thu Jun 19 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
