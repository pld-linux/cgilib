Summary:	A CGI (Common Gateway Interface) library for C++
Summary(pl):	Biblioteka CGI dla C++
Name:		cgilib
Version:	0.1.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/cgilib/%{name}-%{version}.tar.bz2
# Source0-md5:	961308218b6e19ed98aacfd397a0f062
Patch0:		%{name}-misc.patch
Patch1:		%{name}-am_ac.patch
Patch2:		%{name}-gcc3.patch
URL:		http://cgilib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cgilib is a library for programming CGIs (Common Gateway Interface,
most commonly used for server-side web page scripting) in C++

%description -l pl
cgilib jest bibliotek± do programowania CGI (Common Gateway Interface,
najbardziej popularny sposób uruchamiania skryptów po stronie serwera
www) napisan± w C++.

%package devel
Summary:	Header files and develpment documentation for cgilib
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja developerska dla cgilib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for cgilib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja developerska dla cgilib.

%package static
Summary:	Static cgilib library
Summary(pl):	Biblioteka statyczna cgilib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static cgilib library.

%description static -l pl
Biblioteka statyczna cgilib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f *.m4 missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cgilib

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
