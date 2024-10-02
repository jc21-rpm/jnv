%global debug_package %{nil}

Name:           jnv
Version:        0.3.0
Release:        1%{?dist}
Summary:        interactive JSON filter using jq
Group:          Applications/System
License:        MIT
URL:            https://github.com/ynqa/%{name}
BuildRequires:  cmake
BuildRequires:  cargo, rust, clang-devel, clang-libs
Source:         https://github.com/ynqa/%{name}/archive/refs/tags/v%{version}.tar.gz

%description
jnv is designed for navigating JSON, offering an interactive JSON
viewer and jq filter editor.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 target/release/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
%{_bindir}/%{name}

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 0.3.0-1
- v0.3.0

* Wed Mar 20 2024 Jamie Curnow <jc@jc21.com> - 0.1.0-1
- v0.1.0
