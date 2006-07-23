# TODO:
# - mpi support
# - inter-library linking (if possible at all - cross-dependencies?)
Summary:	The Massively Parallel Quantum Chemistry Program
Summary(pl):	Program do r�wnoleg�ych oblicze� z zakresu chemii kwantowej
Name:		mpqc
Version:	2.3.1
Release:	1
License:	LGPL/GPL (see LICENSE)
Group:		Libraries
Source0:	http://dl.sourceforge.net/mpqc/%{name}-%{version}.tar.bz2
# Source0-md5:	2f9b4f7487387730d78066a53764f848
URL:		http://www.mpqc.org/
# -lsB_BLAS ?
# cca-chem-config (http://www.cca-forum.org/~cca-chem/)
# niama-config ??? not found by google
# -lessl is preferred over -lblas? (then -lf77blas -latlas)
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel
BuildRequires:	libint-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
# check: flex >= 2.5.31, bison >= 1.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPQC is the Massively Parallel Quantum Chemistry Program. It computes
properties of atoms and molecules from first principles using the time
independent Schroedinger equation. It runs on a wide range of
architectures ranging from individual workstations to symmetric
multiprocessors to massively parallel computers. Its design is object
oriented, using the C++ programming language.

%description -l en
MPQC is the Massively Parallel Quantum Chemistry Program. It computes
properties of atoms and molecules from first principles using the time
independent Schr�dinger equation. It runs on a wide range of
architectures ranging from individual workstations to symmetric
multiprocessors to massively parallel computers. Its design is object
oriented, using the C++ programming language.

%description -l pl
MPQC (Massively Parallel Quantum Chemistry Program) to program do
r�wnoleg�ych oblicze� z zakresu chemii kwantowej. Oblicza w�a�ciwo�ci
atom�w i cz�steczek z pierwszych zasad przy u�yciu niezale�nego od
czasu r�wnania Schr�dingera. Dzia�a na wielu architekturach od
osobistych stacji roboczych poprzez maszyny wieloprocesorowe SMP do
komputer�w do oblicze� r�wnoleg�ych. Jest zaprojektowany w spos�b
zorientowany obiektowo przy u�yciu j�zyka C++.

%package devel
Summary:	Header files for MPQC library
Summary(pl):	Pliki nag��wkowe biblioteki MPQC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	blas-devel
# XXX: should be libgfortran-devel
Requires:	gcc-fortran
Requires:	lapack-devel
Requires:	libint-devel
Requires:	libstdc++-devel

%description devel
Header files for MPQC library.

%description devel -l pl
Pliki nag��wkowe biblioteki MPQC.

%package static
Summary:	Static MPQC library
Summary(pl):	Statyczna biblioteka MPQC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MPQC library.

%description static -l pl
Statyczna biblioteka MPQC.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--with-cc-optflags="%{rpmcflags}" \
	--with-cxx-optflags="%{rpmcxxflags}" \
	--with-sc-includedir=%{_includedir}/mpqc
# --enable-components (requires cca-chem-config)
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install_devel \
	installroot=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CITATION LICENSE README
%attr(755,root,root) %{_bindir}/ccarun
%attr(755,root,root) %{_bindir}/chkmpqcout
%attr(755,root,root) %{_bindir}/molrender
%attr(755,root,root) %{_bindir}/mpqc
%attr(755,root,root) %{_bindir}/mpqcrun
%attr(755,root,root) %{_bindir}/scls
%attr(755,root,root) %{_bindir}/scpr
%attr(755,root,root) %{_bindir}/tkmolrender
%attr(755,root,root) %{_libdir}/libSC*.so.*.*.*
%attr(755,root,root) %{_libdir}/libmpqc.so.*.*.*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{version}
%{_datadir}/%{name}/%{version}/basis
%{_datadir}/%{name}/%{version}/elisp
%{_datadir}/%{name}/%{version}/perl
%attr(755,root,root) %{_datadir}/%{name}/%{version}/ccarunproc
%attr(755,root,root) %{_datadir}/%{name}/%{version}/mpqcrunproc
%{_datadir}/%{name}/%{version}/atominfo.kv
# XXX: add to system file database?
%{_datadir}/%{name}/%{version}/magic

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sc-config
%attr(755,root,root) %{_bindir}/sc-libtool
%attr(755,root,root) %{_bindir}/sc-mkf77sym
%attr(755,root,root) %{_libdir}/libSC*.so
%attr(755,root,root) %{_libdir}/libmpqc.so
%{_libdir}/libSC*.la
%{_libdir}/libmpqc.la
%{_includedir}/mpqc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSC*.a
%{_libdir}/libmpqc.a