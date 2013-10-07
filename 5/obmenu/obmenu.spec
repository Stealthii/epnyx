%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		obmenu
Version:	1.0
Release:	3%{?dist}
Summary:	A graphical menu editor for Openbox
Group:		User Interface/Desktops
License:	GPL
URL:		http://obmenu.sourceforge.net/

Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:	%{name}.desktop
Patch0:		%{name}-copy-default-xdg-menu.patch 

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	pygtk2-libglade

BuildRequires:	desktop-file-utils

%description
obmenu is a graphical menu editor for the Openbox window manager. Openbox uses
XML to store its menu preferences, and editing these by hand can quickly become
tedious; and even moreso when generating an entire menu for oneself! However,
this utility provides a convenient method of editing the menu in a graphical
interface, while not losing the powerful features of Openbox such as its
pipe menus. 

This also provides a Python module named obxml that can be used to further
script Openbox's menu system. 


%prep
%setup -q
%patch0 -p0


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
chmod +x %{buildroot}%{python_sitelib}/obxml.py
desktop-file-install --vendor fedora	\
	--dir %{buildroot}%{_datadir}/applications	\
	--add-category	X-Fedora	\
	%{SOURCE2}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/%{name}
%{_bindir}/obm-*
%{_datadir}/%{name}/
%{_datadir}/applications/fedora-%{name}.desktop
%{python_sitelib}/obxml.py
%{python_sitelib}/obxml.pyc
%{python_sitelib}/obxml.pyo


%changelog
* Sun Oct 15 2006 Peter Gordon <peter@thecodergeek.com> - 1.0-3
- Some minor aesthetic spec cleanups
- Add a patch from upstream to copy the default /etx/xdg menu stuff if one
  does not exist on the first run:
  + copy-default-xdg-menu.patch
- Drop unneeded README.Fedora file:
  - README.Fedora


* Fri Sep 01 2006 Peter Gordon <peter@thecodergeek.com> - 1.0-2
- Don't %%ghost the .pyo file(s) to comply with the new Extras Python
  packaging guidelines
- Package a README.Fedora file and a .desktop file:
  + README.Fedora
  + %{name}.desktop

* Sun Jun 14 2006 Peter Gordon <peter@thecodergeek.com> - 1.0-1
- Initial packaging
