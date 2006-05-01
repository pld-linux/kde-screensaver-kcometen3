%define		vendor_name kcometen3
Summary:	KCometen3 - OpenGL screensaver for KDE
Summary(de):	KCometen3 - ein KDE Bildschirmschoner
Summary(pl):	KCometen3 - wygaszacz ekranu oparty na OpenGL dla KDE
Name:		kde-screensaver-%{vendor_name}
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://user.cs.tu-berlin.de/~pmueller/files/%{vendor_name}-%{version}.tar.gz
# Source0-md5:	36f846b6a3e5f71c4532070b1f17b717
URL:		http://www.kde-apps.org/content/show.php?content=30313
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.229
Requires:	kdebase-screensavers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCometen3 is an OpenGL screensaver for KDE.

%description -l de
KCometen3 ist ein OpenGL KDE Bildschirmschoner.

%description -l pl
KCometen3 to oparty na OpenGL wygaszacz ekranu dla KDE.

%prep
%setup -q -n %{vendor_name}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kscreensaver

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	desktopdir=%{_datadir}/apps/kscreensaver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kcometen3.kss
%{_datadir}/apps/kcometen3
%{_datadir}/apps/kscreensaver/kcometen3.desktop
