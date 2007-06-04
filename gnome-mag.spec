%define lib_major 2
%define lib_name  %mklibname %{name} %{lib_major}

Summary: GNOME magnifier
Name: gnome-mag
Version: 0.14.5
Release: %mkrel 2
License: GPL
Group: Accessibility
URL: http://developer.gnome.org/projects/gap/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: at-spi-devel >= 1.6.0
BuildRequires: libxdamage-devel
BuildRequires: libxcomposite-devel
BuildRequires: perl-XML-Parser

%description
GNOME Magnifier

%package -n %{lib_name}
Summary:	GNOME magnifier shared library
Group:		%{group}

Provides:	lib%{name} = %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description -n %{lib_name}
GNOME Magnifier shared library.

%package -n %{lib_name}-devel
Summary:	Static libraries, include files for gnome-mag
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Requires:   libbonobo2_x-devel
Requires:	gtk+2-devel

%description -n %{lib_name}-devel
Development libraries and , include files for GNOME magnifier.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{lib_name}
%postun -p /sbin/ldconfig -n %{lib_name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_libdir}/orbit-2.0/*
%{_datadir}/gnome-mag
%{_datadir}/idl/*
%_mandir/man1/magnifier.1*

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/libgnome-mag.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-,root,root,-)
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


