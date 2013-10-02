Name:           rhel-nyx-mirror
Version:        5
Release:        2
Summary:        RHEL NYX Mirror configuration

Group:          System Environment/Base 
License:        Copyright
URL:            http://skutecz.belfast.wombatfs.com/rhel

Source0:        rhel-nyx-mirror.repo	
Source1:        rhel55-nyx-mirror.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       redhat-release >=  %{version} 
Conflicts:      rhel-nyx-mirror-55
Obsoletes:      rhel-nyx-mirror-55

%description
This package contains the yum configurationfor the NYX RHEL repository mirror.

%package	55
Summary:	RHEL NYX Mirror configuration
Group:          System Environment/Base 
Requires:       redhat-release >=  %{version} 
Conflicts:      rhel-nyx-mirror

%description	55
This package contains the yum configurationfor the NYX RHEL repository mirror.

%prep
%setup -q  -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/rhel-nyx-mirror.repo

%files 55
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/rhel55-nyx-mirror.repo

%changelog
* Thu Oct 03 2013 Daniel Porter <dporter@nyx.com> - 5-2
- Added extra package for forcing RHEL 5.5.

* Wed Oct 02 2013 Daniel Porter <dporter@nyx.com> - 5-1
- Initial version of RHEL yum mirror repo files.
