%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	2
%define libname  %mklibname %{name} %{major}
%define devname  %mklibname -d %{name}

Summary:	GNOME magnifier
Name:		gnome-mag
Version:	0.16.3
Release:	6
License:	LGPLv2+
Group:		Accessibility
Url:		http://developer.gnome.org/projects/gap/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-ma/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires: intltool
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libspi-1.0)
BuildRequires: pkgconfig(popt)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrender)

%description
GNOME Magnifier

%package -n %{libname}
Summary:	GNOME magnifier shared library
Group:		System/Libraries
Suggests:	%{name} >= %{version}-%{release}

%description -n %{libname}
GNOME Magnifier shared library.

%package -n %{devname}
Summary:	Development libraries, include files for gnome-mag
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development libraries and , include files for GNOME magnifier.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

mv %buildroot%_datadir/doc/gnome-mag-* installed-docs

%files -f %{name}.lang
%doc README AUTHORS ChangeLog
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/orbit-2.0/*
%{_datadir}/gnome-mag
%{_datadir}/dbus-1/services/org.freedesktop.gnome.Magnifier.service
%{_datadir}/idl/*
%{_mandir}/man1/magnifier.1*

%files -n %{libname}
%{_libdir}/libgnome-mag.so.%{major}*

%files -n %{devname}
%doc installed-docs/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

