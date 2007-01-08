#
%bcond_without	perl
%bcond_without	python		# needed by prewikka
%bcond_without	postgresql	# 
%bcond_without	mysql		# one from those is needed by prewikka
%bcond_without	sqlite3		# 

%include	/usr/lib/rpm/macros.perl
Summary:	The PreludeDB Library
Summary(pl):	Biblioteka PreludeDB
Name:		libpreludedb
Version:	0.9.11.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.prelude-ids.org/download/releases/%{name}-%{version}.tar.gz
# Source0-md5:	36c4a676f8b5e30c0b7cbe9a26535ba0
URL:		http://www.prelude-ids.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libprelude-devel >= 0.9.9
%{?with_perl:BuildRequires:	perl-devel}
%{?with_python:BuildRequires:	python-devel}
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
Requires:	%{name}(DB_driver) = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PreludeDB Library provides an abstraction layer upon the type and
the format of the database used to store IDMEF alerts. It allows
developers to use the Prelude IDMEF database easily and efficiently
without worrying about SQL, and to access the database independently
of the type/format of the database.

%description -l pl
Biblioteka PreludeDB dostarcza warstw� abstrakcji ponad rodzajem i
formatem bazy danych u�ywanej do przechowywania alarm�w IDMEF.
Pozwala programistom �atwo i wydajnie u�ywa� bazy danych IDMEF Prelude
nie martwi�c si� o SQL i dostawa� si� do bazy niezale�nie od jej
rodzaju/formatu.

%package libs
Summary:	Libpreludedb library
Summary(pl):	Biblioteka libpreludedb
Group:		Libraries

%description libs
Libpreludedb library

%description libs -l pl
Biblioteka libpreludedb

%package pgsql
Summary:	PostgreSQL backend for libpreludedb
Summary(pl):	Interfejs do PostgreSQL dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description pgsql
PostgreSQL backend for libpreludedb

%description pgsql -l pl
Interfejs do PostgreSQL do libpreludedb

%package mysql
Summary:	MySQL backend for libpreludedb
Summary(pl):	Interfejs do MySQL dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description mysql
MySQL backend for libpreludedb

%description mysql -l pl
Interfejs do MySQL do libpreludedb

%package sqlite3
Summary:	SQLite3 backend for libpreludedb
Summary(pl):	Interfejs do SQLite3 dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description sqlite3
SQLite3 backend for libpreludedb

%description sqlite3 -l pl
Interfejs do SQLite3 do libpreludedb

%package devel
Summary:	Header files and development documentation for libpreludedb
Summary(pl):	Pliki nag��wkowe i dokumentacja programistyczna do libpreludedb
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files and development documentation for libpreludedb.

%description devel -l pl
Pliki nag��wkowe i dokumentacja programistyczna do libpreludedb.

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
Summary(pl):	Dowi�zania Perla do libpreludedb
Group:		Development/Languages/Perl

%description -n perl-libpreludedb
libpreludedb Perl bindings.

%description -n perl-libpreludedb -l pl
Dowi�zania Perla do libpreludedb.

%package -n python-libpreludedb
Summary:	libpreludedb Python bindings
Summary(pl):	Dowi�zania Pythona do libpreludedb
Group:		Development/Languages/Python

%description -n python-libpreludedb
libpreludedb Python bindings.

%description -n python-libpreludedb -l pl
Dowi�zania Pythona do libpreludedb.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--enable-static \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_python:out}-python \
	--with%{!?with_postgresql:out}-pgsql \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_sqlite3:out}-sqlite3 \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}/libpreludedb \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# are generating wrong dependencies (and are not needed anyway)
find $RPM_BUILD_ROOT -iregex .*.la -exec rm {} \;

%if %{with perl}
cd bindings/perl && %{__perl} Makefile.PL \
        INSTALLDIRS=vendor
cd ../..
%{__make} -C bindings/perl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF

Create new database and database user for prelude
(or update an existing one if needed) using templates from
%{_datadir}/%{name}/classic
for reference visit %{url}

EOF
fi

%postun

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/preludedb-admin
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/formats
%if %{with postgresql} || %{with mysql} || %{with sqlite3}
%dir %{_libdir}/%{name}/plugins/sql
%endif
%attr(755,root,root) %{_libdir}/%{name}/plugins/formats/*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic

%if %{with postgresql}
%files pgsql
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/sql/*pgsql*
%exclude %{_libdir}/%{name}/plugins/sql/*pgsql*.a
%{_datadir}/%{name}/classic/*pgsql*
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/sql/*mysql*
%exclude %{_libdir}/%{name}/plugins/sql/*mysql*.a
%{_datadir}/%{name}/classic/*mysql*
%exclude %{_datadir}/%{name}/classic/mysql2pgsql.sh
%exclude %{_datadir}/%{name}/classic/mysql2sqlite.sh
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%{_libdir}/%{name}/plugins/sql/*sqlite*
%exclude %{_libdir}/%{name}/plugins/sql/*sqlite*.a
%{_datadir}/%{name}/classic/*sqlite*
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpreludedb-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libpreludedb
%{_aclocaldir}/*.m4
%{_gtkdocdir}/libpreludedb

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/%{name}/plugins/*/*.a

%if %{with perl}
%files -n perl-libpreludedb
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/auto/PreludeDB
%attr(755,root,root) %{perl_vendorarch}/auto/PreludeDB/*.so
%{perl_vendorarch}/auto/PreludeDB/*.bs
%{perl_vendorarch}/PreludeDB.pm
%endif

%if %{with python}
%files -n python-libpreludedb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%endif