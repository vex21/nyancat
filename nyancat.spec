Name:          nyancat
Version:       1.5.2
Release:       8%{?dist}
Summary:       Nyancat rendered in your terminal

License:       NCSA
URL:           https://github.com/klange/nyancat
Source0:       %{URL}/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires: make
BuildRequires: gcc
BuildRequires: gawk

%description
Nyan Cat is the name of a YouTube video uploaded in April 2011, which became an
internet meme. The video merged a Japanese pop song with an animated cartoon
cat with a Pop-Tart for a torso, flying through space, and leaving a rainbow
trail behind it.


%prep
%autosetup -p1
awk '1;/\*\//{exit}' < src/nyancat.c > LICENSE


%build
%set_build_flags
make %{?_smp_mflags} nyancat


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 0755 src/nyancat %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 nyancat.1 %{buildroot}/%{_mandir}/man1/


%files
%license LICENSE
%doc README.md
%{_bindir}/nyancat
%{_mandir}/man1/nyancat.1*


%changelog
* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Tomas Tomecek <ttomecek@redhat.com> - 1.5.2-4
- correct manpage perms
- use %%set_build_flags before make
- move LICENSE generation to %%prep

* Wed Jan 29 2020 Tomas Tomecek <ttomecek@redhat.com> - 1.5.2-3
- include manpage

* Tue Jan 28 2020 Tomas Tomecek <ttomecek@redhat.com> - 1.5.2-2
- improve packaging:
  - summary doesn't end with a dot
  - files -> manpage uses a wildcard now
  - extract license with awk

* Fri Jan 24 2020 Tomas Tomecek <ttomecek@redhat.com> - 1.5.2
- Initial RPM packaging

