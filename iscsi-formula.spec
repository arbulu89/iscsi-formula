#
# spec file for package iscsi-formula
#
# Copyright (c) 2018 SUSE LLC, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           iscsi-formula
Version:        0.1.0
Release:        1
Summary:        Configure iSCSI targets and initiator on GNU/Linux and FreeBSD

License:        Apache-2.0
Url:            https://github.com/saltstack-formulas/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%define fname iscsi
%define fdir  %{_datadir}/susemanager/formulas

%description
Configure iSCSI targets and initiator on GNU/Linux and FreeBSD

# package to deploy on SUMA specific path.
%package suma
Summary:        Configure iSCSI targets and initiator on GNU/Linux and FreeBSD (SUMA specific)

%description suma
Configure iSCSI targets and initiator on GNU/Linux and FreeBSD (SUMA specific)

%prep
%setup -q

%build

%install
pwd
mkdir -p %{buildroot}/srv/salt/
cp -R %{fname} %{buildroot}/srv/salt/

# SUMA Specific
mkdir -p %{buildroot}%{fdir}/states/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states


%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
/srv/salt/%{fname}

%dir %attr(0755, root, salt) /srv/salt

%files suma
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%dir %{_datadir}/susemanager
%dir %{fdir}
%dir %{fdir}/states
%{fdir}/states/%{fname}

%dir %attr(0755, root, salt) %{_datadir}/susemanager
%dir %attr(0755, root, salt) %{fdir}
%dir %attr(0755, root, salt) %{fdir}/states

%changelog
