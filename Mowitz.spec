Summary:	This is the Mowitz ("More widgets") library
Summary(pl.UTF-8):   Biblioteka Mowitz ("More widgets" - "więcej widgetów")
Name:		Mowitz
Version:	0.3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://siag.nu/pub/mowitz/%{name}-%{version}.tar.gz
# Source0-md5:	447ea53a67eb4356438e80494e550a3b
URL:		http://siag.nu/mowitz/
BuildRequires:	neXtaw-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The project's goal is to create a library of widgets for X
applications to use. The widgets have been snarfed from various
sources and are all open source (GPL or MIT licenses).

%description -l pl.UTF-8
Celem projektu jest stworzenie biblioteki widgetów do używania przez
aplikacje X. Widgety zostały ściągnięte z różnych źródeł i mają
otwarte źródła (na licencji GPL lub MIT).

%package devel
Summary:	Header files for Mowitz library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki Mowitz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Mowitz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Mowitz.

%package static
Summary:	Static Mowitz library
Summary(pl.UTF-8):   Statyczna biblioteka Mowitz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Mowitz library.

%description static -l pl.UTF-8
Statyczna biblioteka Mowitz.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/Slider.man $RPM_BUILD_ROOT%{_mandir}/man3/Slider.3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc doc/[!MS]* doc/Slider.README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
