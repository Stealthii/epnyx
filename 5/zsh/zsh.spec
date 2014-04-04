Name: 		zsh		
Version:	5.0.2
Release:	14.1%{?dist}
Summary:	Zsh is a shell designed for interactive use, although it is also a powerful scripting language

Group:		System/Shells
License:	MIT
URL:		http://zsh.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ncurses-devel
Requires:	ncurses

%description
Zsh  is  a  UNIX  command interpreter (shell) usable as an interactive login shell and as a shell script command processor.  Of the standard shells, zsh most closely resembles ksh but  includes  many  enhancements.   Zsh  has  command  line  editing, builtin spelling correction, programmable command completion, shell functions (with autoloading), a history mechanism, and a host of other features.

%prep
%setup -q


%build
%configure --without-tcsetpgrp
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -m 0755 -Dd  %{buildroot}/bin

# link zsh binary
mv %{buildroot}%{_bindir}/zsh %{buildroot}/bin/zsh
ln -s -f ../../bin/zsh %{buildroot}%{_bindir}/zsh

# Remove versioned zsh binary
rm -f %{buildroot}%{_bindir}/zsh-*

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/
/bin/zsh
%{_mandir}/man1
%{_datadir}/%{name}/%{version}
%{_libdir}/%{name}/%{version}/%{name}

%doc



%changelog
* Wed Oct 09 2013 Daniel Porter <dporter@nyx.com> - 5.0.2-14.1
- Initial release for EL5

