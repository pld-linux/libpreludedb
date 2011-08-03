# TODO:
# build with --enable-static instead of --disable-static
#
# Conditional build:
%bcond_without	perl		# don't build perl bindings
%bcond_without	python		# don't build python bindings (needed by prewikka)
%bcond_without	postgresql	# don't build postgresql plugin
%bcond_without	mysql		# don't build mysql plugin
%bcond_without	sqlite3		# don't build sqlite3 plugin
#
%include	/usr/lib/rpm/macros.perl
Summary:	The PreludeDB Library
Summary(pl.UTF-8):	Biblioteka PreludeDB
Name:		libpreludedb
Version:	1.0.0
Release:	1
License:	GPL v2 or commercial
Group:		Libraries
#Source0Download: http://www.prelude-ids.com/developpement/telechargement/index.html
Source0:	http://www.prelude-ids.com/download/releases/libpreludedb/%{name}-%{version}.tar.gz
# Source0-md5:	e2b38dfe2efb2008fcb5e2ce51f6638b
Patch0:		%{name}-mysql-innodb.patch
URL:		http://www.prelude-ids.com/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libprelude-devel >= %{version}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_sqlite3:BuildRequires:	sqlite3-devel}
Requires(post):	/sbin/ldconfig
Requires:	%{name}(DB_driver) = %{version}-%{release}
Requires:	libprelude-libs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PreludeDB Library provides an abstraction layer upon the type and
the format of the database used to store IDMEF alerts. It allows
developers to use the Prelude IDMEF database easily and efficiently
without worrying about SQL, and to access the database independently
of the type/format of the database.

%description -l pl.UTF-8
Biblioteka PreludeDB dostarcza warstwę abstrakcji ponad rodzajem i
formatem bazy danych używanej do przechowywania alarmów IDMEF. Pozwala
programistom łatwo i wydajnie używać bazy danych IDMEF Prelude nie
martwiąc się o SQL i dostawać się do bazy niezależnie od jej
rodzaju/formatu.

%package devel
Summary:	Header files and development documentation for libpreludedb
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programistyczna do libpreludedb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libprelude-devel >= 0.9.9

%description devel
Header files and development documentation for libpreludedb.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programistyczna do libpreludedb.

#%package static
#Summary:	Static libpreludedb library
#Summary(pl.UTF-8):	Statyczna biblioteka libpreludedb
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}-%{release}

#%description static
#Static libpreludedb library.

#%description static -l pl.UTF-8
#Statyczna biblioteka libpreludedb.

%package pgsql
Summary:	PostgreSQL backend for libpreludedb
Summary(pl.UTF-8):	Interfejs do PostgreSQL dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description pgsql
PostgreSQL backend for libpreludedb

%description pgsql -l pl.UTF-8
Interfejs do PostgreSQL do libpreludedb

%package mysql
Summary:	MySQL backend for libpreludedb
Summary(pl.UTF-8):	Interfejs do MySQL dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description mysql
MySQL backend for libpreludedb

%description mysql -l pl.UTF-8
Interfejs do MySQL do libpreludedb

%package sqlite3
Summary:	SQLite3 backend for libpreludedb
Summary(pl.UTF-8):	Interfejs do SQLite3 dla libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}(DB_driver) = %{version}-%{release}

%description sqlite3
SQLite3 backend for libpreludedb

%description sqlite3 -l pl.UTF-8
Interfejs do SQLite3 do libpreludedb

%package -n perl-libpreludedb
Summary:	libpreludedb Perl bindings
Summary(pl.UTF-8):	Dowiązania Perla do libpreludedb
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-libpreludedb
libpreludedb Perl bindings.

%description -n perl-libpreludedb -l pl.UTF-8
Dowiązania Perla do libpreludedb.

%package -n python-libpreludedb
Summary:	libpreludedb Python bindings
Summary(pl.UTF-8):	Dowiązania Pythona do libpreludedb
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-libpreludedb
libpreludedb Python bindings.

%description -n python-libpreludedb -l pl.UTF-8
Dowiązania Pythona do libpreludedb.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-gtk-doc \
	--disable-static \
	--with%{!?with_perl:out}-perl \
	--with%{!?with_python:out}-python \
	--with%{!?with_postgresql:out}-postgresql \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_sqlite3:out}-sqlite3 \
	--with-html-dir=%{_gtkdocdir}/libpreludedb \
	--with-perl-installdirs=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la are generating wrong dependencies (and are not needed anyway)
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*/*.{la,a}

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF

Create new database and database user for prelude
(or update an existing one if needed) using templates from
%{_datadir}/%{name}/classic
for reference visit %{url}

EOF
fi

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE.README NEWS README
%attr(755,root,root) %{_bindir}/preludedb-admin
%attr(755,root,root) %{_libdir}/libpreludedb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpreludedb.so.0
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/formats
%attr(755,root,root) %{_libdir}/%{name}/plugins/formats/classic.so
%if %{with postgresql} || %{with mysql} || %{with sqlite3}
%dir %{_libdir}/%{name}/plugins/sql
%endif
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic
%{_mandir}/man1/preludedb-admin.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpreludedb-config
%attr(755,root,root) %{_libdir}/libpreludedb.so
%{_libdir}/libpreludedb.la
%{_includedir}/libpreludedb
%{_aclocaldir}/libpreludedb.m4
%{_gtkdocdir}/libpreludedb

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/libpreludedb.a

%if %{with postgresql}
%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sql/pgsql.so
%attr(755,root,root) %{_datadir}/%{name}/classic/mysql2pgsql.sh
%{_datadir}/%{name}/classic/pgsql*.sql
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sql/mysql.so
%{_datadir}/%{name}/classic/mysql*.sql
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sql/sqlite3.so
%attr(755,root,root) %{_datadir}/%{name}/classic/mysql2sqlite.sh
%{_datadir}/%{name}/classic/sqlite*.sql
%endif

%if %{with perl}
%files -n perl-libpreludedb
%defattr(644,root,root,755)
%{perl_vendorarch}/PreludeDB.pm
%dir %{perl_vendorarch}/auto/PreludeDB
%attr(755,root,root) %{perl_vendorarch}/auto/PreludeDB/PreludeDB.so
%{perl_vendorarch}/auto/PreludeDB/PreludeDB.bs
%endif

%if %{with python}
%files -n python-libpreludedb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_preludedb.so
%{py_sitedir}/preludedb.py[co]
%{py_sitedir}/preludedb-*.egg-info
%endif
