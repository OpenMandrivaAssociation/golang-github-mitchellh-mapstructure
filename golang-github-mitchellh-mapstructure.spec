# http://github.com/mitchellh/mapstructure

%global goipath         github.com/mitchellh/mapstructure
%global commit          d0303fe809921458f417bcf828397a65db30a7e4

%gometa -i

Name:           %{goname}
Version:        0
Release:        0.20%{?dist}
Summary:        Go library for decoding generic map values into native Go structures
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data
until you read a part of it. You can therefore read a map[string]interface{}
and use this library to decode it into the proper underlying
native Go structure.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't quite know the structure of the underlying data
until you read a part of it. You can therefore read a map[string]interface{}
and use this library to decode it into the proper underlying
native Go structure.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.19.gitd0303fe
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gitd0303fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitd0303fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitd0303fe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gitd0303fe
- Bump to upstream d0303fe809921458f417bcf828397a65db30a7e4
  related: #1243892

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitca63d7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.gitca63d7c
- Bump to upstream ca63d7c062ee3c9f34db231e352b60012b4fd0c1
  related: #1243892

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.git281073e
- Polish the spec file
  related: #1243892

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.git281073e
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git281073e
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git281073e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 jchaloup <jchaloup@redhat.com> - 0-0.8.git281073e
- Update github.com/mitchellh/cli to 8102d0ed5ea2709ade1243798785888175f6e415
  related: #1243892

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.7.git281073e
- Bump to upstream 281073eb9eb092240d33ef253c404f1cca550309
  related: #1243892

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git740c764
- Update to spec-2.1
  related: #1243892

* Mon Aug 24 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git740c764
- Update spec file to spec-2.0
  related: #1243892

* Thu Jul 16 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git740c764
- Choose the correct architecture
- Update license
- Remove runtime-dep on golang
- Add temporary devel subpackage of mitchellh-cli
  resolves: #1243892

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git740c764
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 16 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git740c764
- First package for Fedora
  resolves: #1153724

