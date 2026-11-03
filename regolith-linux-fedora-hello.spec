Name:           regolith-linux-fedora-hello
Version:        0.1.0
Release:        1%{?dist}
Summary:        Throwaway package that proves the Regolith Fedora build pipeline

License:        GPL-3.0-or-later
URL:            https://github.com/regolith-linux-fedora/regolith-linux-fedora-hello
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
A one-line shell script. It exists only so the build pipeline and the package
workflows can build, publish and install something without real packaging work.

%prep
%autosetup

%build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Oct 14 2026 Joseph Moon <joemoonmeta@meta.com> - 0.1.0-1
- Initial package
