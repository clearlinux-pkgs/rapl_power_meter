#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rapl_power_meter
Version  : 1.02
Release  : 2
URL      : https://github.com/spandruvada/rapl_power_meter/archive/v1.02.tar.gz
Source0  : https://github.com/spandruvada/rapl_power_meter/archive/v1.02.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: rapl_power_meter-bin

%description
Software Power Meter using RAPL feature
This utility implements a software power meter. This uses Linux IntelÂ® RAPL
(Running Average Power Limit) driver using power capping sysfs.
Intel RAPL driver and power cap sysfs is available from Linux kernel 3.13
release.

%package bin
Summary: bin components for the rapl_power_meter package.
Group: Binaries

%description bin
bin components for the rapl_power_meter package.


%prep
%setup -q -n rapl_power_meter-1.02

%build
export LANG=C
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rapl_power_meter
