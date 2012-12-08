%define lib_major 2
%define libname  %mklibname %{name} %{lib_major}
%define libnamedev  %mklibname -d %{name}

Summary:	GNOME magnifier
Name:		gnome-mag
Version:	0.16.3
Release:	3
License:	LGPLv2+
Group:		Accessibility
URL:		http://developer.gnome.org/projects/gap/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(libspi-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: popt-devel
BuildRequires: intltool
#gw libtool dep:
BuildRequires: pkgconfig(gconf-2.0)

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
Requires:   pkgconfig(libbonobo-2.0)
Requires:	pkgconfig(gtk+-2.0)

%description -n %{libnamedev}
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
%defattr(-,root,root,-)
%{_libdir}/libgnome-mag.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%doc installed-docs/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.3-2mdv2011.0
+ Revision: 664872
- mass rebuild

* Sat Oct 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.3-1mdv2011.0
+ Revision: 590529
- update to new version 0.16.3

* Wed Sep 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.2-1mdv2011.0
+ Revision: 581968
- update build deps
- update to new version 0.16.2

* Wed Mar 31 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.1-1mdv2010.1
+ Revision: 530505
- update build deps
- update to new version 0.16.1

* Mon Feb 01 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.16.0-1mdv2010.1
+ Revision: 499219
- new version
- update build deps
- update file list

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.9-1mdv2010.0
+ Revision: 446799
- update to new version 0.15.9

* Tue Jul 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.8-1mdv2010.0
+ Revision: 401389
- update to new version 0.15.8

* Mon Jun 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.7-1mdv2010.0
+ Revision: 390707
- update to new version 0.15.7

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.6-1mdv2009.1
+ Revision: 366998
- update to new version 0.15.6

* Fri Mar 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.5-1mdv2009.1
+ Revision: 354477
- update to new version 0.15.5

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.4-1mdv2009.0
+ Revision: 287378
- new version
- update build deps

* Mon Sep 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.3-1mdv2009.0
+ Revision: 278075
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.2-1mdv2009.0
+ Revision: 262942
- new version

* Sun Jul 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1-1mdv2009.0
+ Revision: 232162
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.15.0-3mdv2009.0
+ Revision: 221087
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.15.0-2mdv2008.1
+ Revision: 189627
- Fix lib group

* Fri Dec 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.0-1mdv2008.1
+ Revision: 138900
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.10-1mdv2008.0
+ Revision: 89216
- new version

* Mon Sep 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.9-1mdv2008.0
+ Revision: 84258
- new version

* Tue Aug 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.8-1mdv2008.0
+ Revision: 72373
- new version

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.7-1mdv2008.0
+ Revision: 71591
- new version
- new devel name

* Mon Jun 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.6-1mdv2008.0
+ Revision: 41020
- new version
- update file list

* Mon Jun 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.5-2mdv2008.0
+ Revision: 35045
- new version

* Fri May 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.4-1mdv2008.0
+ Revision: 30973
- new version


* Sat Mar 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.3-1mdv2007.1
+ Revision: 140332
- new version

* Sat Mar 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.2-1mdv2007.1
+ Revision: 131764
- new version

* Tue Jan 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.1-1mdv2007.1
+ Revision: 106278
- new version
- fix buildrequires

* Fri Dec 29 2006 Frederic Crozat <fcrozat@mandriva.com> 0.14.0-2mdv2007.1
+ Revision: 102474
- Fix buildrequires for iurt

* Sun Dec 17 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.14.0-1mdv2007.1
+ Revision: 98219
- Import gnome-mag

* Sun Dec 17 2006 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2007.1
- update file list
- New version 0.14.0

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.1-1mdv2007.0
- New release 0.13.1

* Fri Jul 14 2006 Frederic Crozat <fcrozat@mandriva.com> 0.13.0-2mdv2007.0
- Rebuild with latest libgail

* Thu Jul 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.13.0-1mdv2007.0
- Release 0.13.0

* Wed Jul 12 2006 Götz Waschk <waschk@mandriva.org> 0.12.6-2mdv2007.0
- fix major

* Wed Jul 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.6-1mdk
- New release 0.12.6

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 0.12.5-1mdk
- update file list
- New release 0.12.5

* Mon Mar 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.4-1mdk
- New release 0.12.4

* Fri Jan 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.3-1mdk
- New release 0.12.3
- use mkrel

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 0.12.2-1mdk
- Release 0.12.2
- Remove patch0 (no longer needed)

* Thu Feb 17 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.11.14-1mdk 
- Release 0.11.14
- Regenerate patch0

* Wed Feb 16 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.11.10-2mdk
- fix requires
- nuke lib64 rpaths

* Wed Nov 10 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.11.10-1mdk
- New release 0.11.10

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.11.8-1mdk
- reenable libtoolize
- New release 0.11.8
- bump major

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.11-2mdk
- Fix BuildRequires

* Wed Apr 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.11-1mdk
- New release 0.10.11

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.10.10-1mdk
- New release 0.10.10

