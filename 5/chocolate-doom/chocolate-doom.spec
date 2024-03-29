Name:		chocolate-doom
Version:	1.7.0
Release:	2%{?dist}
Group:		Amusements/Games
Summary:	Historically compatible Doom engine
License:	GPLv2+
URL:		http://chocolate-doom.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       SDL, SDL_mixer, SDL_net, libsamplerate
BuildRequires:	SDL-devel, SDL_mixer-devel, SDL_net-devel
BuildRequires:	libsamplerate-devel desktop-file-utils
Provides:	bundled(md5-plumb)
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Chocolate Doom is a game engine that aims to accurately reproduce the experience 
of playing vanilla Doom. It is a conservative, historically accurate Doom source 
port, which is compatible with the thousands of mods and levels that were made 
before the Doom source code was released. Rather than flashy new graphics, 
Chocolate Doom's main features are its accurate reproduction of the game as it
was played in the 1990s. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags};

%install
make install DESTDIR=%{buildroot} \
     iconsdir="%{_datadir}/icons/hicolor/64x64/apps" \
     docdir="%{_docdir}/%{name}-%{version}";
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}/%{_prefix}/games/* %{buildroot}/%{_bindir}/

#desktop-file-validate %{buildroot}%{_datadir}/applications/chocolate-doom.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/chocolate-setup.desktop

%files
%doc CMDLINE ChangeLog NEWS NOT-BUGS README README.OPL 
%{_bindir}/chocolate-doom
%{_bindir}/chocolate-server
%{_bindir}/chocolate-setup
%{_datadir}/applications/chocolate-doom.desktop
%{_datadir}/applications/chocolate-setup.desktop
%exclude %{_datadir}/applications/screensavers/chocolate-doom-screensaver.desktop
%{_datadir}/icons/hicolor/64x64/apps/chocolate-doom.png
%{_datadir}/icons/hicolor/64x64/apps/chocolate-setup.png
%{_mandir}/man5/chocolate-doom.cfg.5.gz
%{_mandir}/man5/default.cfg.5.gz
%{_mandir}/man6/chocolate-doom.6.gz
%{_mandir}/man6/chocolate-server.6.gz
%{_mandir}/man6/chocolate-setup.6.gz

%changelog
* Thu Oct 10 2013 Daniel Porter <dporter@nyx.com> - 1.7.0-2
- Fixed dependencies

* Thu Oct 10 2013 Daniel Porter <dporter@nyx.com> - 1.7.0-1
- Updated to v1.7.0
- Enterprise Linux 5 fixes

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 20 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-2
- use dist tag and added provides on bundled(md5-plumb) as per review

* Tue Aug 16 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6.0-1
- initial spec 
