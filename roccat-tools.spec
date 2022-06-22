Name:           roccat-tools
Version:	5.9.0
Release:        4
Summary:        Common files shared by all Roccat tools
License:        GPL-2.0+ AND CC-BY-3.0
Group:          System/Configuration/Other
Url:            http://roccat.sourceforge.net
Source:         http://downloads.sourceforge.net/roccat/%{name}-%{version}.tar.bz2
Patch0:		0001-Fix-build-with-recent-pango-releases.patch
Patch1:		https://patch-diff.githubusercontent.com/raw/roccat-linux/roccat-tools/pull/6.patch

BuildRequires:  cmake >= 2.6.4
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(pango)
BuildRequires:  pkgconfig(gaminggear-0) >= 0.15.1
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
Requires(pre):  shadow
BuildRequires:  lua-devel

%package -n     roccat-arvo
Summary:        Roccat Arvo userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-isku
Summary:        Roccat Isku userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-iskufx
Summary:        Roccat IskuFX userland tools
Group:          System/Configuration/Other
Requires:       roccat-isku = %{version}
Requires:       roccat-tools = %{version}

%package -n     roccat-kone
Summary:        Roccat Kone userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-koneplus
Summary:        Roccat Kone[+] userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-konepure
Summary:        Roccat KonePure userland tools
Group:          System/Configuration/Other
Requires:       roccat-konextd = %{version}
Requires:       roccat-tools = %{version}

%package -n     roccat-konextd
Summary:        Roccat KoneXTD userland tools
Group:          System/Configuration/Other
Requires:       roccat-koneplus = %{version}
Requires:       roccat-tools = %{version}

%package -n     roccat-kovaplus
Summary:        Roccat Kova[+] userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-kova2016
Summary:        Roccat Kova 2016 userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-lua
Summary:        Roccat Lua userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-pyra
Summary:        Roccat Pyra userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-ryos
Summary:        Roccat Ryos userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-savu
Summary:        Roccat Savu userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-sova
Summary:        Roccat Sova userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-tyon
Summary:        Roccat Tyon userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-nyth
Summary:        Roccat Nyth userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-kiro
Summary:        Roccat Kiro userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-suora
Summary:        Roccat Suora userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%package -n     roccat-skeltr
Summary:        Roccat Skeltr userland tools
Group:          System/Configuration/Other
Requires:       roccat-tools = %{version}

%description
Roccat consists of a shared library and other files shared by device-specific
applications for Roccat hardware.

%description -n roccat-arvo
Arvo consists of a shared library, a console application and a GUI application.
It helps users of the arvo kernel driver to manipulate the profiles and settings
of a Roccat Arvo keyboard.

%description -n roccat-isku
Isku consists of a shared library, a console application and a GUI application.
It helps users of the isku kernel driver to manipulate the profiles and settings
of a Roccat Isku keyboard.

%description -n roccat-iskufx
IskuFX consists of a shared library, a console application and a GUI application.
It helps users of the isku kernel driver to manipulate the profiles and settings
of a Roccat IskuFX keyboard.

%description -n roccat-kone
Kone consists of a shared library, a console application and a GUI application.
It helps users of the kone kernel driver to manipulate the profiles and settings
of a Roccat Kone mouse.

%description -n roccat-koneplus
Koneplus consists of a shared library, a console application and a GUI application.
It helps users of the koneplus kernel driver to manipulate the profiles and settings
of a Roccat Kone[+] mouse.

%description -n roccat-konepure
Konepure consists of a shared library, a console application and a GUI application.
It helps users of the koneplus kernel driver to manipulate the profiles and settings
of a Roccat KonePure mouse.

%description -n roccat-konextd
Konextd consists of a shared library, a console application and a GUI application.
It helps users of the koneplus kernel driver to manipulate the profiles and settings
of a Roccat KoneXTD mouse.

%description -n roccat-kova2016
Kova2016 consists of a console application and a GUI application. It helps users
to manipulate the Profiles and Settings of a Roccat Kova 2016 mouse.

%description -n roccat-kovaplus
Kovaplus consists of a shared library, a console application and a GUI application.
It helps users of the kovaplus kernel driver to manipulate the profiles and settings
of a Roccat Kova[+] mouse.

%description -n roccat-lua
Lua consists of a shared library, a console application and a GUI application.
It helps users of the lua kernel driver to manipulate the Settings of a Roccat Lua
mouse.

%description -n roccat-pyra
Pyra consists of a shared library, a console application and a GUI application.
It helps users of the pyra kernel driver to manipulate the profiles and settings
of a Roccat Pyra mouse.

%description -n roccat-ryos
Ryos consists of a shared library, a console application and a GUI application.
It helps users of the ryos kernel driver to manipulate the profiles and settings
of a Roccat Ryos mouse.

%description -n roccat-savu
Savu consists of a shared library, a console application and a GUI application.
It helps users of the savu kernel driver to manipulate the profiles and settings
of a Roccat Savu mouse.

%description -n roccat-sova
Sova consists of a shared library, a console application and a GUI application.
It helps users of the sova kernel driver to manipulate the profiles and settings
of a Roccat Sova mouse.

%description -n roccat-tyon
Tyon consists of a shared library, a console application and a GUI application.
It helps users of the tyon kernel driver to manipulate the profiles and settings
of a Roccat Tyon mouse.

%description -n roccat-nyth
Nyth consists of a shared library, a console application and a GUI application.
It helps users of the Nyth kernel driver to manipulate the profiles and settings
of a Roccat Nyth mouse.

%description -n roccat-kiro
Kiro consists of a shared library, a console application and a GUI application.
It helps users of the Kiro kernel driver to manipulate the profiles and settings
of a Roccat Kiro mouse.

%description -n roccat-suora
Suora consists of a shared library, a console application and a GUI application.
It helps users of the Suora kernel driver to manipulate the profiles and settings
of a Roccat Suora mechanical keybard.

%description -n roccat-skeltr
Skeltr consists of a shared library, a console application and a GUI application.
It helps users of the Skeltr kernel driver to manipulate the profiles and settings
of a Roccat Skeltr mechanical keybard.

%prep
%setup -q -n roccat-tools-%{version}
%autopatch -p1
perl -p -i -e 's|\r\n|\n|g' skeltr/roccatskeltrconfig/roccatskeltrconfig.desktop

%build
%cmake \
    -DWITH_LUA=5.3 
   
%make_build

%install
cd build
%{__make} %{?_smp_mflags} DESTDIR="%{buildroot}" install
%{__mkdir} -p "%{buildroot}/var/lib/roccat"

%pre
getent group roccat >/dev/null || %{_sbindir}/groupadd roccat
getent passwd roccat >/dev/null || \
	%{_sbindir}/useradd -g roccat -s /bin/false -r -c "Roccat Hardware" \
	-d %{_localstatedir}/lib/roccat roccat

%post
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
echo 'You need to add yourself to the roccat group and relogin to let the userland tools gain access to the drivers.'

%postun
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun

%post -n roccat-arvo
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-arvo
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-isku
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-isku
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-iskufx
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-iskufx
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-kone
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-kone
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-koneplus
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-koneplus
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-konepure
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-konepure
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-konextd
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-konextd
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-kovaplus
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-kovaplus
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-kova2016
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-kova2016
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-lua
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-lua
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-pyra
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-pyra
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-ryos
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-ryos
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-savu
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-savu
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-sova
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-sova
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-tyon
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-tyon
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-nyth
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-nyth
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-kiro
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-kiro
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-suora
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-suora
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%post -n roccat-skeltr
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%{?udev_rules_update:%udev_rules_update}

%postun -n roccat-skeltr
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%{?udev_rules_update:%udev_rules_update}

%files
%doc README COPYING Changelog
%{_sysconfdir}/xdg/autostart/roccateventhandler.desktop
%{_bindir}/roccateventhandler
%dir %{_datadir}/roccat/
%{_datadir}/roccat/sounds/
%{_datadir}/icons/hicolor/*/apps/roccat.png
%dir %{_libdir}/gaminggear_plugins/
%dir %{_libdir}/roccat/
%dir %{_mandir}/*/
%dir %{_mandir}/*/man1/
%{_datadir}/locale/*/LC_MESSAGES/roccat-tools.mo
%attr(2770, roccat, roccat) %{_localstatedir}/lib/roccat
%{_libdir}/libroccat.so.*
%{_libdir}/libroccat.so
%{_libdir}/libroccatwidget.so.*
%{_libdir}/libroccatwidget.so

%files -n roccat-arvo
%{_bindir}/roccatarvoconfig
%{_bindir}/roccatarvocontrol
%{_libdir}/libroccatarvo.so.*
%{_libdir}/libroccatarvo.so
%{_libdir}/roccat/libarvoeventhandler.so
%{_udevrulesdir}/90-roccat-arvo.rules
%{_mandir}/*/man1/roccatarvocontrol.1*
%{_datadir}/applications/roccatarvoconfig.desktop

%files -n roccat-isku
%{_bindir}/roccatiskuconfig
%{_bindir}/roccatiskucontrol
%{_libdir}/libroccatisku.so.*
%{_libdir}/libroccatisku.so
%{_libdir}/libroccatiskuwidget.so.*
%{_libdir}/libroccatiskuwidget.so
%{_libdir}/roccat/libiskueventhandler.so
%{_udevrulesdir}/90-roccat-isku.rules
%{_mandir}/*/man1/roccatiskucontrol.1*
%{_datadir}/applications/roccatiskuconfig.desktop

%files -n roccat-iskufx
%{_bindir}/roccatiskufxconfig
%{_bindir}/roccatiskufxcontrol
%{_libdir}/libroccatiskufx.so.*
%{_libdir}/libroccatiskufx.so
%{_libdir}/gaminggear_plugins/libiskufxgfxplugin.so
%{_libdir}/roccat/libiskufxeventhandler.so
%{_udevrulesdir}/90-roccat-iskufx.rules
%{_mandir}/*/man1/roccatiskufxcontrol.1*
%{_datadir}/applications/roccatiskufxconfig.desktop

%files -n roccat-kone
%{_bindir}/roccatkoneconfig
%{_bindir}/roccatkonecontrol
%{_libdir}/libroccatkone.so.*
%{_libdir}/libroccatkone.so
%{_libdir}/roccat/libkoneeventhandler.so
%{_udevrulesdir}/90-roccat-kone.rules
%{_mandir}/*/man1/roccatkonecontrol.1*
%{_datadir}/applications/roccatkoneconfig.desktop

%files -n roccat-koneplus
%{_bindir}/roccatkoneplusconfig
%{_bindir}/roccatkonepluscontrol
%{_libdir}/libroccatkoneplus.so.*
%{_libdir}/libroccatkoneplus.so
%{_libdir}/libroccatkonepluswidget.so.*
%{_libdir}/libroccatkonepluswidget.so
%{_libdir}/gaminggear_plugins/libkoneplusgfxplugin.so
%{_libdir}/roccat/libkonepluseventhandler.so
%{_udevrulesdir}/90-roccat-koneplus.rules
%{_mandir}/*/man1/roccatkonepluscontrol.1*
%{_datadir}/applications/roccatkoneplusconfig.desktop

%files -n roccat-konepure
%{_bindir}/roccatkonepureconfig
%{_bindir}/roccatkonepurecontrol
%{_bindir}/roccatkonepuremilitaryconfig
%{_bindir}/roccatkonepuremilitarycontrol
%{_bindir}/roccatkonepureopticalconfig
%{_bindir}/roccatkonepureopticalcontrol
%{_libdir}/libroccatkonepuremilitary.so.*
%{_libdir}/libroccatkonepuremilitary.so
%{_libdir}/libroccatkonepuremilitarywidget.so.*
%{_libdir}/libroccatkonepuremilitarywidget.so
%{_libdir}/libroccatkonepureoptical.so.*
%{_libdir}/libroccatkonepureoptical.so
%{_libdir}/libroccatkonepure.so.*
%{_libdir}/libroccatkonepure.so
%{_libdir}/libroccatkonepurewidget.so.*
%{_libdir}/libroccatkonepurewidget.so
%{_libdir}/gaminggear_plugins/libkonepuregfxplugin.so
%{_libdir}/gaminggear_plugins/libkonepuremilitarygfxplugin.so
%{_libdir}/gaminggear_plugins/libkonepureopticalgfxplugin.so
%{_libdir}/roccat/libkonepureeventhandler.so
%{_libdir}/roccat/libkonepuremilitaryeventhandler.so
%{_libdir}/roccat/libkonepureopticaleventhandler.so
%{_udevrulesdir}/90-roccat-konepuremilitary.rules
%{_udevrulesdir}/90-roccat-konepureoptical.rules
%{_udevrulesdir}/90-roccat-konepure.rules
%{_mandir}/*/man1/roccatkonepurecontrol.1*
%{_mandir}/*/man1/roccatkonepuremilitarycontrol.1*
%{_mandir}/*/man1/roccatkonepureopticalcontrol.1*
%{_datadir}/applications/roccatkonepureconfig.desktop
%{_datadir}/applications/roccatkonepuremilitaryconfig.desktop
%{_datadir}/applications/roccatkonepureopticalconfig.desktop

%files -n roccat-konextd
%{_bindir}/roccatkonextdconfig
%{_bindir}/roccatkonextdcontrol
%{_bindir}/roccatkonextdopticalconfig
%{_bindir}/roccatkonextdopticalcontrol
%{_libdir}/libroccatkonextdoptical.so.*
%{_libdir}/libroccatkonextdoptical.so
%{_libdir}/libroccatkonextd.so.*
%{_libdir}/libroccatkonextd.so
%{_libdir}/libroccatkonextdwidget.so.*
%{_libdir}/libroccatkonextdwidget.so
%{_libdir}/gaminggear_plugins/libkonextdgfxplugin.so
%{_libdir}/gaminggear_plugins/libkonextdopticalgfxplugin.so
%{_libdir}/roccat/libkonextdeventhandler.so
%{_libdir}/roccat/libkonextdopticaleventhandler.so
%{_udevrulesdir}/90-roccat-konextdoptical.rules
%{_udevrulesdir}/90-roccat-konextd.rules
%{_mandir}/*/man1/roccatkonextdcontrol.1*
%{_mandir}/*/man1/roccatkonextdopticalcontrol.1*
%{_datadir}/applications/roccatkonextdconfig.desktop
%{_datadir}/applications/roccatkonextdopticalconfig.desktop

%files -n roccat-kovaplus
%{_bindir}/roccatkovaplusconfig
%{_bindir}/roccatkovapluscontrol
%{_libdir}/libroccatkovaplus.so.*
%{_libdir}/libroccatkovaplus.so
%{_libdir}/roccat/libkovapluseventhandler.so
%{_udevrulesdir}/90-roccat-kovaplus.rules
%{_mandir}/*/man1/roccatkovapluscontrol.1*
%{_datadir}/applications/roccatkovaplusconfig.desktop

%files -n roccat-kova2016
%{_udevrulesdir}/90-roccat-kova2016.rules
%{_bindir}/roccatkova2016*
%{_libdir}/libroccatkova2016.so.*
%{_libdir}/libroccatkova2016.so
%{_libdir}/roccat/libkova2016eventhandler.so
%{_libdir}/gaminggear_plugins/libkova2016gfxplugin.so
%{_datadir}/applications/roccatkova2016config.desktop
%{_mandir}/*/man1/roccatkova2016*

%files -n roccat-lua
%{_bindir}/roccatluaconfig
%{_bindir}/roccatluacontrol
%{_libdir}/libroccatlua.so.*
%{_libdir}/libroccatlua.so
%{_libdir}/roccat/libluaeventhandler.so
%{_udevrulesdir}/90-roccat-lua.rules
%{_mandir}/*/man1/roccatluacontrol.1*
%{_datadir}/applications/roccatluaconfig.desktop

%files -n roccat-pyra
%{_bindir}/roccatpyraconfig
%{_bindir}/roccatpyracontrol
%{_libdir}/libroccatpyra.so.*
%{_libdir}/libroccatpyra.so
%{_libdir}/roccat/libpyraeventhandler.so
%{_udevrulesdir}/90-roccat-pyra.rules
%{_mandir}/*/man1/roccatpyracontrol.1*
%{_datadir}/applications/roccatpyraconfig.desktop

%files -n roccat-ryos
%{_bindir}/roccatryosmkconfig
%{_bindir}/roccatryosmkcontrol
%{_bindir}/roccatryostklconfig
%{_bindir}/roccatryostklcontrol
%{_bindir}/roccatryosmkfxcontrol
%{_bindir}/roccatryosmkfxconfig
%{_libdir}/libroccatryosmk.so.*
%{_libdir}/libroccatryosmk.so
%{_libdir}/libroccatryosmkwidget.so.*
%{_libdir}/libroccatryosmkwidget.so
%{_libdir}/libroccatryostkl.so.*
%{_libdir}/libroccatryostkl.so
%{_libdir}/libroccatryosmkfx.so.*
%{_libdir}/libroccatryosmkfx.so
%{_libdir}/gaminggear_plugins/libryosmkfxgfxplugin.so
%{_libdir}/roccat/libryosmkeventhandler.so
%{_libdir}/roccat/libryostkleventhandler.so
%{_libdir}/roccat/libryosmkfxeventhandler.so
%{_udevrulesdir}/90-roccat-ryosmk.rules
%{_udevrulesdir}/90-roccat-ryostkl.rules
%{_udevrulesdir}/90-roccat-ryosmkfx.rules
%{_mandir}/*/man1/roccatryosmkcontrol.1*
%{_mandir}/*/man1/roccatryostklcontrol.1*
%{_mandir}/*/man1/roccatryosmkfxcontrol.1*
%{_datadir}/applications/roccatryosmkconfig.desktop
%{_datadir}/applications/roccatryostklconfig.desktop
%{_datadir}/applications/roccatryosmkfxconfig.desktop
%{_datadir}/roccat/ryos_effect_modules/

%files -n roccat-savu
%{_bindir}/roccatsavuconfig
%{_bindir}/roccatsavucontrol
%{_libdir}/libroccatsavu.so.*
%{_libdir}/libroccatsavu.so
%{_libdir}/roccat/libsavueventhandler.so
%{_udevrulesdir}/90-roccat-savu.rules
%{_mandir}/*/man1/roccatsavucontrol.1*
%{_datadir}/applications/roccatsavuconfig.desktop

%files -n roccat-sova
%{_bindir}/roccatsovaconfig
%{_bindir}/roccatsovacontrol
%{_libdir}/libroccatsova.so.*
%{_libdir}/libroccatsova.so
%{_libdir}/roccat/libsovaeventhandler.so
%{_udevrulesdir}/90-roccat-sova.rules
%{_mandir}/*/man1/roccatsovacontrol.1*
%{_datadir}/applications/roccatsovaconfig.desktop

%files -n roccat-tyon
%{_bindir}/roccattyonconfig
%{_bindir}/roccattyoncontrol
%{_libdir}/libroccattyon.so.*
%{_libdir}/libroccattyon.so
%{_libdir}/gaminggear_plugins/libtyongfxplugin.so
%{_libdir}/roccat/libtyoneventhandler.so
%{_udevrulesdir}/90-roccat-tyon.rules
%{_mandir}/*/man1/roccattyoncontrol.1*
%{_datadir}/applications/roccattyonconfig.desktop

%files -n roccat-nyth
%{_bindir}/roccatnythconfig
%{_bindir}/roccatnythcontrol
%{_libdir}/libroccatnyth.so.*
%{_libdir}/libroccatnyth.so
%{_libdir}/gaminggear_plugins/libnythgfxplugin.so
%{_libdir}/roccat/libnytheventhandler.so
%{_udevrulesdir}/90-roccat-nyth.rules
%{_mandir}/*/man1/roccatnythcontrol.1*
%{_datadir}/applications/roccatnythconfig.desktop

%files -n roccat-kiro
%{_bindir}/roccatkiroconfig
%{_bindir}/roccatkirocontrol
%{_libdir}/libroccatkiro.so.*
%{_libdir}/libroccatkiro.so
%{_libdir}/gaminggear_plugins/libkirogfxplugin.so
%{_libdir}/roccat/libkiroeventhandler.so
%{_udevrulesdir}/90-roccat-kiro.rules
%{_mandir}/*/man1/roccatkirocontrol.1*
%{_datadir}/applications/roccatkiroconfig.desktop

%files -n roccat-suora
%{_bindir}/roccatsuoraconfig
%{_bindir}/roccatsuoracontrol
%{_libdir}/libroccatsuora.so.*
%{_libdir}/libroccatsuora.so
%{_libdir}/roccat/libsuoraeventhandler.so
%{_udevrulesdir}/90-roccat-suora.rules
%{_mandir}/*/man1/roccatsuoracontrol.1*
%{_datadir}/applications/roccatsuoraconfig.desktop

%files -n roccat-skeltr
%{_bindir}/roccatskeltrconfig
%{_bindir}/roccatskeltrcontrol
%{_libdir}/libroccatskeltr.so.*
%{_libdir}/libroccatskeltr.so
%{_libdir}/roccat/libskeltreventhandler.so
%{_libdir}/gaminggear_plugins/libskeltrgfxplugin.so
%{_udevrulesdir}/90-roccat-skeltr.rules
%{_mandir}/*/man1/roccatskeltrcontrol.1*
%{_datadir}/applications/roccatskeltrconfig.desktop

%changelog
* Mon Aug 21 2017 tchvatal@suse.com
- Version bump to 5.7.0
  * Various firmware updates
- Raise dependency on gaminggear version
- Use lua5.3 rather than lua5.2 on new openSUSE releases
* Sun Aug 20 2017 zaitor@opensuse.org
- Drop obsolete and unused pkgconfig(unique-1.0) BuildRequires:
  According to .changes this was supposed to be dropped in version
  0.17.0 already.
* Fri Mar 31 2017 jengelh@inai.de
- Stop installation when user creation fails
* Wed Mar 15 2017 mrueckert@suse.de
- update to 5.6.0
  * Added: Support for Skeltr
  * Improved: Nyth calibration assistant gives hints on errors
  * Fixed: Missing Sova key settings
  * Fixed: Suora desktop link started RyosTKL config
- fix line endings in skeltr desktop file
* Sun Oct 30 2016 jengelh@inai.de
- Update to new upstream release 5.5.0
  * Added: Support for Sova Membrane and Mechanical
* Sun Sep 18 2016 mailaender@opensuse.org
- Update to version 5.4.0
- Add roccat-suora sub-package.
* Mon Aug  1 2016 mailaender@opensuse.org
- add missing post macros for roccat-kiro
* Sun Jul 31 2016 jengelh@inai.de
- Remove header-less (and therefore practically useless)
  devel subpackages
* Sun Jul 31 2016 jengelh@inai.de
- Do not suppress errors from useradd/groupadd. Guard the addition
  by prior calls to getent. Ensure shadow utilities are present.
* Sat Jul 30 2016 rpm@fthiessen.de
- Update to 5.2.0
* Mon Mar  7 2016 mrueckert@suse.de
- fix broken require of the kova2016 subpackage
* Sun Feb 28 2016 mrueckert@suse.de
- update to 3.9.0
  * Added: File KNOWN_LIMITATIONS
  * Added: Support for Kiro
  * Fixed: Kova2016 handedness switching
  * Fixed: Nyth and Kova2016 fixed colors
  * Fixed: Nyth fin left/right were interchanged
  * Fixed: Nyth sensitivity osd value display were off by one
  * Fixed: Volume up/down settings were interchanged
  * Fixed: Better Swarm RMP format support for Nyth, Kova2016, Kiro
* Wed Feb 24 2016 mrueckert@suse.de
- verbose make files seems to be in the macro
- do release build with debuginfo (-DCMAKE_BUILD_TYPE=RelWithDebInfo)
* Wed Feb 24 2016 mrueckert@suse.de
- use cmake macros
* Thu Feb  4 2016 mailaender@opensuse.org
- update to 3.8.0 (see Changelog)
- enable parallel build
* Wed Aug 19 2015 mrueckert@suse.de
- update to 3.6.0
  * Added: Support for Nyth
  * Added: New soundfiles
  * Added: Firmware updater for Ryos TKL Pro
  * Removed: Firmware updater for Tyon
* Tue Aug  4 2015 mrueckert@suse.de
- if you use a group in the filelist, also add it
* Mon Aug  3 2015 mrueckert@suse.de
- enable lua support
  - new BR lua 5.2 devel
  - we don't ship the .lc files yet as our rpmlint check thinks it
    is an ELF file
- add %%post/%%postin for roccat-tyon
* Mon Aug  3 2015 mrueckert@suse.de
- update to 3.5.0
  - 3.5.0 2015-06-26
  - Improved: Ryos multimedia button behaviour is now
    automatically corrected
  - Improved: Software shortcuts (Kova[+], Pyra) are now kept
    active as long as button is pressed.
  - Fixed: Kone udev rule now sets file permissions again
  - 3.4.0 2015-05-23
  - Added: Custom color support for KoneXTD and KonePure range
    devices
  - Changed: Updated to libgaminggear uinput interface
  - Fixed: Library dependencies
  - Fixed: Added missing strings to be translated
  - 3.3.0 2015-04-18
  - Added: German translations
  - Added: Options to correct Ryos Multimedia button behaviour
  - Added: Support for Roccat Kone Pure Black (handled by
    konepuremilitary)
  - Added: Support for Lua 5.2
  - Improved: Ryos range now supports keyboard layouts
  - Improved: Gaminggearfx plugins allow NULL parameters
  - Fixed: Build problems
  - Fixed: Library dependencies, eliminating unresolved symbols
    and reducing overlinking
  - Fixed: Gfx problems with some Kone range devices
  - Fixed: RyosTKL Lua modules path
  - 3.2.0 2015-03-11
  - Added: Support for Gaminggearfx
  - Changed: cleaned up dbus interface
  - Improved: spec file now uses standard macros
  - 3.1.0 2015-02-24
  - Added: Support for Ryos TKL Pro
  - Fixed: Dbus interface names
  - Fixed: Cpi handling for KonePureOptical
  - Fixed: OpenGui now opens right application
  - Fixed: Some typos in error messages and manpages
  - 3.0.0 2015-02-08
  - Added: Configuration option EVENTHANDLER_PLUGIN_DIR
  - Changed: Replaced Python with Lua as RyosMK ripple-scripting
    engine. Also support compilation has to be explicitly
    switched on with WITH_LUA
  - Changed: Everything got a roccat prefix to prevent
    ambiguities, libraries additionally got moved to library base
    folder, so no linker path modification is needed
* Fri Apr  3 2015 mailaender@opensuse.org
- fix boo#925799 http://sourceforge.net/p/roccat/bugs/35/
* Sun Feb  1 2015 mailaender@opensuse.org
- update to version 2.4.0
* Sun Jan 11 2015 mailaender@opensuse.org
- update to version 2.3.0
  + Adds support for Roccat Tyon
* Sat Jul  5 2014 mailaender@opensuse.org
- update to version 2.1.0
* Wed Jul  2 2014 mailaender@opensuse.org
- fix "nothing provides roccat = 2.0.0 needed by roccat-isku-2.0.0"
* Sat Jun 14 2014 mailaender@opensuse.org
- update to 2.0.0
  + Added support for Kone XTD Optical.
  + Fixed things for various devices.
  + All devices except Kone and Arvo are now completely handled by userspace code.
  + No more kernel module problems for these devices.
  + All userspace handled devices now have graphical firmware updaters.
  + Firmware update from text console is still supported and is merged in *control applications.
- changes from 1.6.0
  + Added support for Kone Pure Military. This is a userspace-only implementation so no kernel module is needed.
  + Ryos is now pure userspace too. No kernel module is needed anymore.
  + Ryos now supports Python scripted ripple effects.
* Wed Apr 16 2014 mailaender@opensuse.org
- update to 1.5.0
  + transition to libgaminggear with an improved version of the macro editor
* Fri Feb 28 2014 mailaender@opensuse.org
- update to 1.4.1
* Sun Feb 16 2014 mailaender@opensuse.org
- update to 1.4.0
* Sat Jan 11 2014 mailaender@opensuse.org
- update to version 1.3.0
  + Fixed: KonePure and KonePureOptical macro problems
  + Fixed: Actual profile changing twice when using settings tab
  + Fixed: Multiple device warnings on replug after firmware update
  + Improved: Default profile can now be switched off
  + Improved: Sound playback now with per-device configurable volume
  + Improved: Sensitivity change now supports audio notifications
  + Improved: Shortcut dialog allows toggling modifier checkboxes with key press
  + Improved: Profile save dialogs show filename proposition and add extension if needed
  + Changed: Device reset now lives in misc menu
* Sat Nov 23 2013 mailaender@opensuse.org
- update to version 1.1.0
  + A "live layer illumination editor" for Ryos MK Pro.
- changes from 1.0.0
  + gamefile settings handling is now more resource friendly
  + multi-user compatibility
  + The TalkFX interface changed
    and the SDK is now up-to-date with Roccats newest incarnation v0.2
- changes from 0.23.0
  + Talk has been updated to be compatible with Roccats Talk2.
  + Ryos now has all Talk features and got RippleFX support, remap now works as expected.
- changes from 0.22.0
  + adds support for RyosMK and a few fixes and improvements.
* Sat Sep 21 2013 mailaender@opensuse.org
- update to version 0.21.0
* Thu Jul  4 2013 mailaender@opensuse.org
- update to version 0.20.0
  + support for evdev and nothing else.
* Sat Apr 13 2013 mailaender@opensuse.org
- update to version 0.17.0
  + roccatgui has been completely replaced with it's new implementation roccateventhandler,
    removing libunique as a dependency.
  + Arvo and Kone now support media keys. Arvo now also supports mouse events in macro playback.
    These new features make use of the uinput kernel module.
* Sat Mar  9 2013 mailaender@opensuse.org
- remove sudo pop-up and remind user to add himself to the roccat group instead
* Sat Mar  9 2013 mailaender@opensuse.org
- update to version 0.16.0
- add sudo password popup to .desktop file (avoids "Error reading actual profile")
* Sun Dec 30 2012 mrueckert@suse.de
- package based on upstream spec file.
  changes:
  - spec cleaner
  - fixed file conflicts
  - moved cmake call to the build section
  - converted buildrequires to pkgconfig()
