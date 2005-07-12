%include	/usr/lib/rpm/macros.perl
Summary:	The PreludeDB Library
Summary(pl):	Biblioteka PreludeDB
Name:		libpreludedb
%define	_rc	rc8
Version:	0.9.0
Release:	0.%{_rc}.1
License:	GPL
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	cbc7a78a5fbdb8efc640131abbb95d21
URL:		http://www.prelude-ids.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc
BuildRequires:	libprelude-devel >= 0.9.0
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PreludeDB Library provides an abstraction layer upon the type and
the format of the database used to store IDMEF alerts. It allows
developers to use the Prelude IDMEF database easily and efficiently
without worrying about SQL, and to access the database independently
of the type/format of the database.

%description -l pl
Biblioteka PreludeDB dostarcza warstwê abstrakcji ponad rodzajem i
formatem bazy danych u¿ywanej do przechowywania alarmów IDMEF.
Pozwala programistom ³atwo i wydajnie u¿ywaæ bazy danych IDMEF Prelude
nie martwi±c siê o SQL i dostawaæ siê do bazy niezale¿nie od jej
rodzaju/formatu.

%package devel
Summary:	Header files and development documentation for libpreludedb
Summary(pl):	Pliki nag³ówkowe i dokumentacja programistyczna do libpreludedb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libpreludedb.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programistyczna do libpreludedb.

%package static
Summary:	Static libpreludedb library
Summary(pl):	Statyczna biblioteka libpreludedb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpreludedb library.

%description static -l pl
Statyczna biblioteka libpreludedb.

%package -n perl-libpreludedb
Summary:	libpreludedb Perl bindings
Summary(pl):	Dowi±zania Perla do libpreludedb
Group:		Development/Languages/Perl

%description -n perl-libpreludedb
libpreludedb Perl bindings.

%description -n perl-libpreludedb -l pl
Dowi±zania Perla do libpreludedb.

%package -n python-libpreludedb
Summary:	libpreludedb Python bindings
Summary(pl):	Dowi±zania Pythona do libpreludedb
Group:		Development/Languages/Python

%description -n python-libpreludedb
libpreludedb Python bindings.

%description -n python-libpreludedb -l pl
Dowi±zania Pythona do libpreludedb.

%prep
%setup -q -n %{name}-%{version}-%{_rc}

%build
%configure \
	--enable-shared \
	--enable-static \
	--enable-perl \
	--enable-python \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/libpreludedb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd bindings/perl && %{__perl} Makefile.PL \
        INSTALLDIRS=vendor
cd ../..
%{__make} -C bindings/perl install \
	DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/prelude-db-create.sh
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/*
%attr(755,root,root) %{_libdir}/%{name}/plugins/*/*.so
%{_libdir}/%{name}/plugins/*/*.la
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpreludedb-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libpreludedb
%{_aclocaldir}/*.m4
%{_gtkdocdir}/libpreludedb

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n perl-libpreludedb
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/PreludeDB
%attr(755,root,root) %{perl_vendorarch}/auto/PreludeDB/*.so
%{perl_vendorarch}/auto/PreludeDB/*.bs
%{perl_vendorarch}/PreludeDB.pm

%files -n python-libpreludedb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
 %{py_sitedir}/*.py[co]
