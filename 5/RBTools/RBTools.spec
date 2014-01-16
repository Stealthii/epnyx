%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           RBTools
Version:        0.5.5
Release:        1%{?dist}
Summary:        Tools for use with ReviewBoard

Group:          Applications/Internet
License:        MIT
URL:            http://www.review-board.org
Source0:        http://downloads.reviewboard.org/releases/%{name}/0.5/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-setuptools
Requires:       python-simplejson

### Patches ###

# Don't use ez_setup, since RPM provides equivalent functionality
Patch1001: 0001-Python-2.4-compatibility.patch

%description
RBTools provides client tools for interacting with a ReviewBoard
code-review server.

%prep
%setup -q -n %{name}-%{version}

# Apply patches
%patch1001 -p1

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# While /usr/bin/post-review also exists for this purpose,
# it is still sensible to make postreview.py executable
chmod +x $RPM_BUILD_ROOT/%{python_sitelib}/rbtools/postreview.py

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README
%{_bindir}/post-review
%{_bindir}/rbt
%{python_sitelib}/rbtools/
%{python_sitelib}/RBTools*.egg-info/

%changelog
* Thu Jan 16 2014 Daniel Porter <dporter@nyx.com> - 0.5.5-1
- New upstream 0.5.5 release
- Removed unnecessary patch
- Add patch for Python 2.4 compatibility

* Fri Nov 08 2013 Daniel Porter <dporter@nyx.com> - 0.5.2-1
- New upstream 0.5.2 release

* Tue Sep 27 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.4-1
- New upstream 0.3.4 release
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3.4/
- New Features:
-   post-review:
-     Added a --change-description option for setting the Change Description
      text on drafts
- Bugfixes:
-   post-review:
-     Newlines in summaries on Git are now converted to spaces, preventing
      errors when using --guess-summary
-     Fixed authentication failures when accessing a protected /api/info/
      URL. This was problematic particularly on RBCommons
-     Fixed diff upload problems on Python 2.7

* Mon Aug 22 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.3-1
- New upstream 0.3.3 release
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3.3/
- Notable Changes:
-   Rewrote the Clear Case implementation to be cleaner, more maintainable,
    and less buggy
- New Features:
-   post-review:
-      Added --http-username and --http-password for providing defaults for
       Basic HTTP Authentication
-   Clear Case:
-      Added proper support for --tracking-branch and --revision-range
-      Clear Case configuration has moved to .reviewboardrc
-   Git:
-      Added automatic parent diff determination when using --revision-range
-      Added support for working against bare repositories when using
       --revision-range
-      Enhanced --revision-range to take any valid Git revisions
-      Support --repository-url for overriding the git origin URL
-   Mercurial:
-      Added support for --guess-summary and --guess-description
-      Allow a single revision to be passed to --revision-range
-   Subversion:
-      Added support for --svn-changelist for specifying SVN changelists
- Bug Fixes:
-   post-review:
-      Fixed authentication problems with some versions of Review Board
-   Clear Case:
-      The view is properly recognized
-      Removed the dependency on xargs and cygwin
-      Fixed breakages with binary files
-      Removed support for --label, which was useless
-      Running just post-review will now produce a working diff of checked
       out files
-      Diffs generate properly now under Windows
-      The diffs no longer hard-code a fake date, but instead use the real
       time/date of the file
-      Files that were renamed no longer breaks the diff. OID/UUIDs are used
       instead of file paths
-      Fixed diff generation to use the diff program instead of hand-crafting
       the diffs
-      Running with --revision-range with paths that don't exist no longer
       produces unreadable IOException errors
-   Git:
-      Use real URLs when using git prefixes
-      Fixed compatibility with versions of Git older than 1.6
-      Added compatibility with msysgit
-      The correct SVN remote tracking branch is now used for git-svn
       repositories
-   Mercurial:
-      Fixed an error when posting inside a Mercurial branch
-   Perforce:
-      Fixed Review Board version detection when checking for Perforce
       changeset support. This forced usage of the old API, preventing the new
       API from being used, which prevented usage with Review Board 1.6
-   Subversion:
-      Lines starting with --- and +++ in diffs that aren't diff control lines
       no longer results in broken diffs

* Wed Feb 09 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.2-1
- New upstream 0.3.2 release
- Fixed using Perforce change numbers with Review Board 1.5.2
- Fixed parsing CVSROOTs with :ext: schemes not containing a username
- Mercurial no longer takes precedence over Perforce if a valid Mercurial
- user configuration is found

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3.1-1
- New upstream 0.3.1 release
- Added a .reviewboardrc setting for specifying the repository to use
- Fixed a crash when using the old, deprecated API and accessing an existing
- review request

* Tue Feb 01 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.3-1
- New upstream release
- Support for new ReviewBoard 1.5.x API
- Support for Plastic SCM
- Full release notes:
- http://www.reviewboard.org/docs/releasenotes/dev/rbtools/0.3/

* Fri Jul 30 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-6
- Rebuild for python 2.7

* Mon Apr 19 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-5
- Update to 0.2 final release

* Tue Apr 06 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-3.rc1
- Add runtime requirement for python-setuptools

* Mon Apr 05 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-2.rc1
- Remove git-patchset patch
- Add patch to check for GNU diff
- Add patch to give more useful error messages on failure

* Mon Mar 15 2010 Stephen Gallagher <sgallagh@redhat.com> - 0.2-1.rc1
- Import upstream release 0.2rc1
- Add patches from upstream
- Add patch to support git patchsets
