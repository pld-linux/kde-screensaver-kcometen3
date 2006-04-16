%define		vendor_name kcometen3
Summary:	KCometen3 - OpenGL screensaver for KDE
Name:		kde-screensaver-%{vendor_name}
Version:	1.0
Release:	0.1
License:	GPL
Group:		X11/Amusements
Source0:	http://user.cs.tu-berlin.de/~pmueller/files/%{vendor_name}-%{version}.tar.gz
# Source0-md5:	ec7471f64c9140d1b6994f2fa3c7a919
URL:		http://www.kde-apps.org/content/show.php?content=30313
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KCometen3 is an OpenGL screensaver for KDE.

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
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	desktopdir=%{_desktopdir} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcometen3.kss
%{_desktopdir}/kcometen3.desktop
%{_datadir}/apps/kcometen3
