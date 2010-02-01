%define lib_major 2
%define libname  %mklibname %{name} %{lib_major}
%define libnamedev  %mklibname -d %{name}

Summary: GNOME magnifier
Name: gnome-mag
Version: 0.16.0
Release: %mkrel 1
License: LGPLv2+
Group: Accessibility
URL: http://developer.gnome.org/projects/gap/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: at-spi-devel >= 1.6.0
BuildRequires: dbus-glib-devel
BuildRequires: libxdamage-devel
BuildRequires: libxcomposite-devel
BuildRequires: intltool

%description
GNOME Magnifier

%package -n %{libname}
Summary:	GNOME magnifier shared library
Group:		System/Libraries

Provides:	lib%{name} = %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
GNOME Magnifier shared library.

%package -n %{libnamedev}
Summary:	Static libraries, include files for gnome-mag
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:   libbonobo2_x-devel
Requires:	gtk+2-devel
Obsoletes: %mklibname -d %{name} %{lib_major}

%description -n %{libnamedev}
Development libraries and , include files for GNOME magnifier.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs

%makeinstall_std

%find_lang %{name}

mv %buildroot%_datadir/doc/gnome-mag-* installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/orbit-2.0/*
%{_datadir}/gnome-mag
%_datadir/dbus-1/services/org.freedesktop.gnome.Magnifier.service
%{_datadir}/idl/*
%_mandir/man1/magnifier.1*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libgnome-mag.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%doc installed-docs/*
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

