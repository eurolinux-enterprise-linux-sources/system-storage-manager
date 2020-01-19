Name:           system-storage-manager
Version:        0.4
Release:        9%{?dist}
Summary:        A single tool to manage your storage

Group:          System Environment/Base
License:        GPLv2+
URL:            http://storagemanager.sf.net
Source0:        http://downloads.sourceforge.net/storagemanager/%{name}-%{version}.tar.gz


Patch1: ssm-0.4-ssm-big-update-no-1.patch
Patch2: ssm-0.4-misc-get_unit_size-accept-different-unit-formats.patch
Patch3: ssm-0.4-ssm-btrfs-backend-try-to-find-the-real-device.patch
Patch4: ssm-0.4-ssm-force-btrfs-device-add.patch
Patch5: ssm-0.4-tests-Fix-they-way-we-gather-information-about-btrfs.patch
Patch6: ssm-0.4-tests-Make-btrfs-recognize-devices-from-tests-suite-.patch
Patch7: ssm-0.4-test-008-Device-count-should-go-down-after-removing-.patch
Patch8: ssm-0.4-misc-Fix-get_device_size-to-work-with-partitions-cor.patch
Patch9: ssm-0.4-ssm-Suppress-backtrace-if-command-failed.patch
Patch10: ssm-0.4-ssm-Add-SSM_PRINT_BACKTRACE-environment-variable.patch
Patch11: ssm-0.4-misc-Use-wipefs-a-in-misc.wipefs-helper.patch
Patch12: ssm-0.4-ssm-Fix-various-problems-found-by-pylint.patch
Patch13: ssm-0.4-ssm-Remove-unnecessary-usr-bin-env-python.patch
Patch14: ssm-0.4-lvm-Ask-user-when-shrining-inactive-logical-volume.patch
Patch15: ssm-0.4-ssm-tests-Use-udevadm-settle-to-avoid-race-with-udev.patch
Patch16: ssm-0.4-ssm-tests-Set-wipe_signatures_when_zeroing_new_lvs-t.patch
Patch17: ssm-0.4-misc-Run-udevadm-settle-prior-running-wipefs.patch
Patch18: ssm-0.4-ssm-Use-xfs_reparir-to-check-xfs-file-system-consist.patch
Patch19: ssm-0.4-ssm-big-update-no-2.patch
Patch20: ssm-0.4-ssm-Close-file-descriptors-on-popen.patch
Patch21: ssm-0.4-crypt-Remove-resize-support.patch
Patch22: ssm-0.4-misc-Return-stderr-output-in-run-as-well.patch
Patch23: ssm-0.4-lvm-Move-lvm-specific-error-handling-to-lvm-backend.patch
Patch24: ssm-0.4-tests-Test-ssm-list-with-exported-volume-groups.patch
Patch25: ssm-0.4-tests-fix-bashtests-008-btrfs-remove.sh.patch
Patch26: ssm-0.4-tests-Do-not-attpemt-to-mknod-loop-devices-if-not-ne.patch
Patch27: ssm-0.4-0027-ssm-use-LC_ALL-C-when-running-tools-from-ssm.patch
Patch28: ssm-0.4-0028-resize-fix-extN-crash-when-no-size-was-provided.patch
Patch29: ssm-0.4-0029-ssm-Fix-a-case-where-xfs-growing-could-fail.patch
Patch30: ssm-0.4-0030-ssmlib-change-how-stdin-data-are-passed-to-subproces.patch
Patch31: ssm-0.4-0031-ssmlib-use-pwquality-to-test-password-strength-for-c.patch
Patch32: ssm-0.4-0032-tests-add-a-test-case-for-crypt-and-a-weak-password.patch
Patch33: ssm-0.4-0033-lvm-index-thinpools-as-vg-lv-pair-instead-of-just-lv.patch
Patch34: ssm-0.4-0034-ssmlib-do-not-use-xfs_db-for-mounted-filesystems-use.patch
Patch35: ssm-0.4-0035-ssmlib-correctly-use-real-devname-in-xfs_get_info.patch
Patch36: ssm-0.4-0036-ssmlib-fix-sizes-in-xfs_get_info-for-mounted-devices.patch
Patch37: ssm-0.4-0037-ssmlib-missing-pwquality-should-not-crash-the-whole-.patch
Patch38: ssm-0.4-0038-ssmlib-partitions-detecting-for-loopback-devices.patch
Patch39: ssm-0.4-0039-lvm-Remove-pool_name-key-if-pv-not-in-pool.patch
Patch40: ssm-0.4-0040-lvm-fix-backtrace-when-vg-lv-is-inactive-or-broken.patch
Patch41: ssm-0.4-0041-btrfs-Send-udev-change-event-for-every-device-after-.patch
Patch42: ssm-0.4-0042-btrfs-send-udev-change-event-after-some-more-btrfs-o.patch
Patch43: ssm-0.4-0043-ssmlib-fix-not_supported-error.patch
Patch44: ssm-0.4-0044-ssmlib-better-error-message-when-bdev-is-required-bu.patch
Patch45: ssm-0.4-0045-ssmlib-add-__str__-to-DeviceInfo-and-Item.patch
Patch46: ssm-0.4-0046-lvm-fix-undefined-variable.patch
Patch47: ssm-0.4-0047-ssm-add-a-workaround-for-lvm-and-exported-volumes.patch
Patch48: ssm-0.4-0048-ssmlib-extend-CommandFailed-exception-with-exit-code.patch
Patch49: ssm-0.4-0049-Big-tests-update-for-0.4-9.patch


BuildArch:      noarch
BuildRequires:  python-devel >= 2.6
BuildRequires:  python-pwquality
Requires:       python >= 2.6
Requires:       python-libs >= 2.6
Requires:       python-pwquality
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
# misc: get_unit_size() accept different unit formats
%patch2 -p1
# ssm: btrfs backend: try to find the real device
%patch3 -p1
# ssm: force btrfs device add
%patch4 -p1
# tests: Fix they way we gather information about btrfs
%patch5 -p1
# tests: Make btrfs recognize devices from tests suite properly
%patch6 -p1
# test 008: Device count should go down after removing a device
%patch7 -p1
# misc: Fix get_device_size to work with partitions correctly
%patch8 -p1
# ssm: Suppress backtrace if command failed
%patch9 -p1
# ssm: Add SSM_PRINT_BACKTRACE environment variable
%patch10 -p1
# misc: Use wipefs -a in misc.wipefs() helper
%patch11 -p1
# ssm: Fix various problems found by pylint
%patch12 -p1
# ssm: Remove unnecessary /usr/bin/env python
%patch13 -p1
# ssm: Remove unnecessary /usr/bin/env python
%patch14 -p1
# lvm: Ask user when shrining inactive logical volume
%patch15 -p1
# ssm tests: Use udevadm settle to avoid race with udev
%patch16 -p1
# ssm tests: Set wipe_signatures_when_zeroing_new_lvs to
%patch17 -p1
# misc: Run udevadm settle prior running wipefs
%patch18 -p1
# Contains upstream patches
# 2489d428831176a2fe90d584d3d1bec537cd34ec..a41b006ce484367df9d90f12f6b39d60e6485c0a
%patch19 -p1
# ssm: Close file descriptors on popen
%patch20 -p1
# crypt: Remove resize support
%patch21 -p1
# misc: Return stderr output in run() as well
%patch22 -p1
# lvm: Move lvm specific error handling to lvm backend
%patch23 -p1
# tests: Test ssm list with exported volume groups
%patch24 -p1
# tests: fix bashtests/008-btrfs-remove.sh
%patch25 -p1
# tests: Do not attpemt to mknod loop devices if not necessary
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1

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
* Mon Mar 11 2019 Jan Tulak <jtulak@redhat.com> 0.4-9
- Fix unhandled exception for some locales set through LC_ALL (#1679591)
- Fix ssm resize fails with python stack trace (#1654583)
- Fix poor luks password throwing an error (#1141871)
- Fix unable to list thinpools with the same name (#1619476)
- Fix ssm list delay in detecting xfs growth (#1664652)
- Fix exported lvm volumes issue
- Send udev change events for btrfs operations and on all fs creations
- Fix issues with partitions on loopback devices
- Better error reporting for some situations

* Fri Jun 22 2018 Lukas Czerner <lczerner@redhat.com> 0.4-8
- Fix error on ssm list when vg is exported (#1321236)
- Fix btrfs test and tests in general

* Thu Jul 21 2016 Lukas Czerner <lczerner@redhat.com> 0.4-7
- Fix leaked descriptor on lvm invocation
- Disallow resizing encrypted volumes

* Fri Jul 1 2016 Lukas Czerner <lczerner@redhat.com> 0.4-6
- Fix listing of snapshots created by yum-fs-snapshot (#1094646)
- Provide lvm thin provisioning support (#1115131)
- Create mount point if it does not exist (#1134983)
- Support percentage size argumetns (#1139263)
- Fix bug when deleting inactive lv (#1142292)
- Fix bug when listing empty dm tables (#1113584)

* Tue Mar 4 2014 Lukas Czerner <lczerner@redhat.com> 0.4-5
- Fix some "device or resource busy" failures in ssm test suite (#1071881)

* Thu Jan 16 2014 Lukas Czerner <lczerner@redhat.com> 0.4-4
- Suppress backtrace when a command fails (#1054349)
- Fix ssm to recognize units in new btrfs output properly (#1052327)
- Use correct sysfs file to get size for a partition (#1053651)
- Fix ssm to be able add a device with signature to btrfs file system (#1053741)
- Resognize btrfs devices from new btrfs output properly (#1052330)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4-3
- Mass rebuild 2013-12-27

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
