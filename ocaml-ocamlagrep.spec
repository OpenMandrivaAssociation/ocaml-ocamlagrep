%define up_name ocamlagrep
%define name    ocaml-%{up_name}

Name:           %{name}
Version:        1.0
Release:        3

Summary:        string searching with errors
License:        LGPL
Group:          Development/Other
URL:            https://pauillac.inria.fr/~xleroy/software.html#agrep
Source0:        http://caml.inria.fr/distrib/bazar-ocaml/%{up_name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This OCaml library implements the Wu-Manber algorithm for string searching
with errors, popularized by the "agrep" Unix command and the "glimpse" file
indexing tool.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
%make
cat > META <<EOF
name = "ocamlagrep"
description = "string searching with errors"
version = "%{version}"
archive(byte) = "agrep.cma"
archive(native) = "agrep.cmxa"
directory = "+agrep"
EOF

%install
rm -rf %{buildroot}
%define destdir %{buildroot}/%{_libdir}/ocaml/agrep
install -d -m 755 %{destdir}
cp agrep.cmi agrep.cma agrep.cmxa %{destdir}/
cp libagrep.a %{destdir}/
cp dllagrep.so %{destdir}/
cp META %{destdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/agrep
%{_libdir}/ocaml/agrep/META
%{_libdir}/ocaml/agrep/*.cmi
%{_libdir}/ocaml/agrep/*.cma
%{_libdir}/ocaml/agrep/*.so

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/agrep/*
%exclude %{_libdir}/ocaml/agrep/META
%exclude %{_libdir}/ocaml/agrep/*.cmi
%exclude %{_libdir}/ocaml/agrep/*.cma
%exclude %{_libdir}/ocaml/agrep/*.so



%changelog
* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2010.0
+ Revision: 390296
- rebuild

* Tue Jan 06 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-1mdv2009.1
+ Revision: 326348
- META file
- import ocaml-ocamlagrep


* Sun Dec 21 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.0-1mdv
- Initial RPM release.
