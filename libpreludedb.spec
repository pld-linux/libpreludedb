#
# Conditional build:
%bcond_without	python2		# Python 2.x bindings (needed by prewikka)
%bcond_without	python3		# Python 3.x bindings
%bcond_without	static_libs	# static library
%bcond_without	postgresql	# PostgreSQL plugin
%bcond_without	mysql		# MySQL plugin
%bcond_without	sqlite3		# SQLite3 plugin
#
Summary:	The PreludeDB Library
Summary(pl.UTF-8):	Biblioteka PreludeDB
Name:		libpreludedb
Version:	4.1.0
Release:	2
License:	GPL v2 or commercial
Group:		Libraries
#Source0Download: https://www.prelude-siem.org/projects/prelude/files
Source0:	https://www.prelude-siem.org/attachments/download/832/%{name}-%{version}.tar.gz
# Source0-md5:	d17807635724abb1d98ef592ef5fc3cf
Patch0:		%{name}-lt.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-python-install.patch
URL:		https://www.prelude-siem.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libprelude-devel >= %{version}
BuildRequires:	libprelude-c++-devel >= %{version}
BuildRequires:	libprelude-swig >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	pkgconfig
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_python2:BuildRequires:	python-devel >= 1:2.5}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3.0.0}
BuildRequires:	swig-python
Requires(post):	/sbin/ldconfig
Requires:	%{name}(DB_driver) = %{version}-%{release}
Requires:	libprelude-libs >= %{version}
Obsoletes:	perl-libpreludedb
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
Requires:	libprelude-devel >= %{version}

%description devel
Header files and development documentation for libpreludedb.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programistyczna do libpreludedb.

%package static
Summary:	Static libpreludedb library
Summary(pl.UTF-8):	Statyczna biblioteka libpreludedb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpreludedb library.

%description static -l pl.UTF-8
Statyczna biblioteka libpreludedb.

%package c++
Summary:	C++ binding for libpreludedb
Summary(pl.UTF-8):	Interfejs C++ do libpreludedb
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libprelude-c++ >= %{version}

%description c++
C++ binding for libpreludedb.

%description c++ -l pl.UTF-8
Interfejs C++ do libpreludedb.

%package c++-devel
Summary:	Header files for libpreludedbcpp
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpreludedbcpp
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libprelude-c++-devel >= %{version}
Requires:	libstdc++-devel

%description c++-devel
Header files for libpreludedbcpp.

%description c++-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpreludedbcpp.

%package c++-static
Summary:	Static libpreludedbcpp library
Summary(pl.UTF-8):	Statyczna biblioteka libpreludedbcpp
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
Static libpreludedbcpp library.

%description c++-static -l pl.UTF-8
Statyczna biblioteka libpreludedbcpp.

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

%package -n python-libpreludedb
Summary:	Python 2.x bindings for libpreludedb
Summary(pl.UTF-8):	Wiązania Pythona 2.x do libpreludedb
Group:		Development/Languages/Python
Requires:	%{name}-c++ = %{version}-%{release}

%description -n python-libpreludedb
Python 2.x bindings for libpreludedb.

%description -n python-libpreludedb -l pl.UTF-8
Wiązania Pythona 2.x do libpreludedb.

%package -n python3-libpreludedb
Summary:	Python 3.x bindings for libpreludedb
Summary(pl.UTF-8):	Wiązania Pythona 3.x do libpreludedb
Group:		Development/Languages/Python
Requires:	%{name}-c++ = %{version}-%{release}

%description -n python3-libpreludedb
Python 3.x bindings for libpreludedb.

%description -n python3-libpreludedb -l pl.UTF-8
Wiązania Pythona 3.x do libpreludedb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if %{with python3}
%{__rm} bindings/python/{_preludedb.cxx,preludedb.py}
%endif

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4 -I libmissing/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}/libpreludedb \
	--with-mysql%{!?with_mysql:=no} \
	--with-postgresql%{!?with_postgresql:=no} \
	--with-python2%{!?with_python2:=no} \
	--with-python3%{!?with_python3:=no} \
	--with-sqlite%{!?with_sqlite3:=no} \
	--with-swig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitescriptdir} \
	pyexecdir=%{py_sitedir} \
	python3dir=%{py3_sitescriptdir} \
	py3execdir=%{py3_sitedir}

%if %{without postgresql} && %{without mysql} && %{without sqlite3}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/sql
%endif

# no *.la for plugins
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*/*.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*/*.a}

%if %{with python2}
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

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE.README NEWS README
%attr(755,root,root) %{_bindir}/preludedb-admin
%attr(755,root,root) %{_libdir}/libpreludedb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpreludedb.so.7
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/formats
%attr(755,root,root) %{_libdir}/%{name}/plugins/formats/classic.so
%dir %{_libdir}/%{name}/plugins/sql
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/classic
%{_mandir}/man1/preludedb-admin.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpreludedb-config
%attr(755,root,root) %{_libdir}/libpreludedb.so
%{_libdir}/libpreludedb.la
%dir %{_includedir}/libpreludedb
%{_includedir}/libpreludedb/*.h
%{_aclocaldir}/libpreludedb.m4
%{_gtkdocdir}/libpreludedb
%{_mandir}/man1/libpreludedb-config.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpreludedb.a
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludedbcpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpreludedbcpp.so.2

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpreludedbcpp.so
%{_libdir}/libpreludedbcpp.la
%{_includedir}/libpreludedb/*.hxx

%if %{with static_libs}
%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libpreludedbcpp.a
%endif

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

%if %{with python2}
%files -n python-libpreludedb
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_preludedb.so
%{py_sitedir}/preludedb.py[co]
%{py_sitedir}/preludedb-*-py*.egg-info
%endif

%if %{with python3}
%files -n python3-libpreludedb
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_preludedb.cpython-*.so
%{py3_sitedir}/preludedb.py
%{py3_sitedir}/__pycache__/preludedb.cpython-*.py[co]
%{py3_sitedir}/preludedb-*-py*.egg-info
%endif
