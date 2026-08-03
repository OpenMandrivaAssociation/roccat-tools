Name:           roccat-tools
Version:	5.9.1
Release:        1
Summary:        Common files shared by all Roccat tools
License:        GPL-2.0+ AND CC-BY-3.0
Group:          System/Configuration/Other
Url:            https://roccat.sourceforge.net
Source:         http://downloads.sourceforge.net/roccat/%{name}-%{version}.tar.bz2
# dropped (no longer applies): Patch0:		0001-Fix-build-with-recent-pango-releases.patch
# dropped (no longer applies): Patch1:		https://patch-diff.githubusercontent.com/raw/roccat-linux/roccat-tools/pull/6.patch

BuildRequires:	make
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
# Lua 5.4 is not supported yet
BuildRequires:  lua5.3-devel

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
