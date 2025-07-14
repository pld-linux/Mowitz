Summary:	This is the Mowitz ("More widgets") library
Summary(pl.UTF-8):	Biblioteka Mowitz ("More widgets" - "więcej widgetów")
Name:		Mowitz
Version:	0.3.1
Release:	1
License:	GPL v2+, LGPL v2+, MIT
Group:		Libraries
Source0:	http://siag.nu/pub/mowitz/%{name}-%{version}.tar.gz
# Source0-md5:	35cfd18b05d45e0ba6b48896bd258138
Patch0:		%{name}-includes.patch
URL:		http://siag.nu/mowitz/
BuildRequires:	neXtaw-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
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
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Mowitz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	neXtaw-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXt-devel

%description devel
Header files for Mowitz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Mowitz.

%package static
Summary:	Static Mowitz library
Summary(pl.UTF-8):	Statyczna biblioteka Mowitz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Mowitz library.

%description static -l pl.UTF-8
Statyczna biblioteka Mowitz.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	LIBS="-lneXtaw -lXmu -lXt -lXpm -lXext -lX11"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed at runtime
%{__rm} $RPM_BUILD_ROOT%{_datadir}/Mowitz/mkt1cfg
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

install -Dp doc/Slider.man $RPM_BUILD_ROOT%{_mandir}/man3/Slider.3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libMowitz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMowitz.so.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/pixmaps
%attr(755,root,root) %{_datadir}/%{name}/any2xpm
%attr(755,root,root) %{_datadir}/%{name}/readpfa
%{_datadir}/%{name}/FontDataBase
%{_datadir}/%{name}/IsoLatin*.enc
%{_datadir}/%{name}/fonts.txt
%{_datadir}/%{name}/rgb.txt
%{_datadir}/%{name}/t1lib.config

%files devel
%defattr(644,root,root,755)
%doc doc/{*.README,*.html,*.gif}
%attr(755,root,root) %{_bindir}/mowitz-config
%attr(755,root,root) %{_libdir}/libMowitz.so
%{_libdir}/libMowitz.la
%{_includedir}/Mowitz
%{_mandir}/man3/Slider.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libMowitz.a
