Name:           rhel-nyx-mirror
Version:        5
Release:        1
Summary:        RHEL NYX Mirror configuration

Group:          System Environment/Base 
URL:            http://skutecz.belfast.wombatfs.com/rhel

Source0:        rhel-nyx-mirror.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       redhat-release >=  %{version} 
Conflicts:      rhel55-nyx-mirror
Obsoletes:      rhel55-nyx-mirror

%description
This package contains the yum configurationfor the NYX RHEL repository mirror.

%prep
%setup -q  -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*

%changelog
* Wed Oct 02 2013 Daniel Porter <dporter@nyx.com> - 5-1
- Initial version of RHEL yum mirror repo files.
