Name:           unfs3
Version:        0.9.22
Release:        1%{?dist}
Summary:        User-space NFSv3 Server

License:        BSD
URL:            http://unfs3.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/unfs3/unfs3/%{version}/unfs3-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex

%description
UNFS3 is a user-space implementation of the NFS (Network File System) version 3
server specification. It provides a daemon that supports both the MOUNT and NFS
protocol.


%prep
%setup -q


%build
%configure
# parallel build is broken
make
#make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc CREDITS LICENSE NEWS README contrib/ doc/
%{_sbindir}/unfsd
%{_mandir}/man7/tags.7*
%{_mandir}/man8/unfsd.8*


%changelog
* Sat Aug 05 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.9.22-1
- Initial release
