Name:           synaTudor
Version:        1.0
Release:        1%{?dist}
Summary:        Synaptics Firmware Extraction Tool

License:        GPLv3+
URL:            https://github.com/Popax21/synaTudor
Source0:        %{url}/archive/refs/heads/main.tar.gz

BuildRequires:  meson, ninja, libgusb-devel, innoextract, perl-Digest-SHA, dbus-devel, glib2-devel, libseccomp-devel, libcap-devel, gcc, libusb-compat-0.1-devel, openssl-devel, libfprint-tod-devel
Requires:       libgusb, dbus, glib2, libseccomp, libcap, libusb-compat-0.1, openssl

%description
A tool for extracting and handling Synaptics firmware.

%prep
%autosetup -n %{name}-main

%build
meson build
cd build
ninja

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
/usr/local/bin/synaTudor

%changelog
* Mon Mar 3 2025 Nelson <darltrash@icloud.com> - 1.0-1
- Initial build
