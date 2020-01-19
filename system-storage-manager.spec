Name:           system-storage-manager
Version:        0.4
Release:        2%{?dist}
Summary:        A single tool to manage your storage

Group:          System Environment/Base
License:        GPLv2+
URL:            http://storagemanager.sf.net
Source0:        http://downloads.sourceforge.net/storagemanager/%{name}-%{version}.tar.gz


Patch1: ssm-0.4-ssm-big-update-no-1.patch


BuildArch:      noarch
BuildRequires:  python-devel >= 2.6
Requires:       python >= 2.6
Requires:       python-libs >= 2.6
Requires:       util-linux
Requires:       which
Requires:       xfsprogs
Requires:       e2fsprogs


%description
System Storage Manager provides an easy to use command line interface to manage
your storage using various technologies like lvm, btrfs, encrypted volumes and
more.

In more sophisticated enterprise storage environments, management with Device
Mapper (dm), Logical Volume Manager (LVM), or Multiple Devices (md) is becoming
increasingly more difficult.  With file systems added to the mix, the number of
tools needed to configure and manage storage has grown so large that it is
simply not user friendly.  With so many options for a system administrator to
consider, the opportunity for errors and problems is large.

The btrfs administration tools have shown us that storage management can be
simplified, and we are working to bring that ease of use to Linux file systems
in general.

You should install the ssm if you need to manage your storage with various
technologies via a single unified interface.


%prep
%setup -q

# Contains upstream patches
# 39eb3058a02a2b482c4c5bdf0120b70605a6b23a..4210d7560585f2a241eaa5ebc364c98d49f565d2
%patch1 -p1

%build
# nothing to build


%install
rm -rf ${RPM_BUILD_ROOT}
%{__python} setup.py install --root=${RPM_BUILD_ROOT}


%check
make test


%files
%{_bindir}/ssm
%{_docdir}/%{name}-%{version}/
%{_mandir}/man8/ssm.8*
%{python_sitelib}/ssmlib/
%{python_sitelib}/*.egg-info


%changelog
* Wed Oct 9 2013 Lukas Czerner <lczerner@redhat.com> 0.4-2
- Remove btrfs resize support (#986116)
- Unmount all btrfs subvolumes when removing a filesystem
- Fix size argument parsing for create and snapshot command
- Fix list output for some cases
- Add support to create encrypted volumes with crypt backend (#1012523)
- Add dry-run option
- Fix removing volumes with crypt backend
- Add raid1 and raid10 support for lvm backend (#1012518)
- Allow to check btrfs volumes (#986105)
- Fix error handling when trying to resize btrfs subvolume (#986111)
- Fix ssm mount command so it detects directory properly

* Wed Aug 7 2013 Lukas Czerner <lczerner@redhat.com> 0.4-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jun  1 2012 Lukas Czerner <lczerner@redhat.com> 0.2-1
- Initial version of the package
