Name:           epnyx-release       
Version:        5 
Release:        1
Summary:        Extra Packages for NYX on Enterprise Linux repository config

Group:          System Environment/Base 
License:        GPL 
URL:            http://skutecz.belfast.wombatfs.com/epnyx

Source0:        RPM-GPG-KEY-EPNYX
Source1:        GPL	
Source2:        epnyx.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version} 
Conflicts:     fedora-release

%description
This package contains the Extra Packages for NYX on Enterprise Linux (EPNYX)
repository GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPNYX

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Wed Oct 02 2013 Daniel Porter <dporter@nyx.com> - 5-1
- Initial version of EPNYX yum repo files.
