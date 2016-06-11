%define name DwarfFortress
%define version 0.43.03
%define release 1
%define prefix /usr

Summary: Slaves to Amarok II: God of Blood - Chapter II: Dwarf Fortress
Name: %{name}
Version: %{version}
Release: %{release}
Group: Amusements/Games/Other
License: All rights reserved.  Copyright (C) 2002-2015 by Tarn Adams.
#BuildArch: x86_64
BuildRoot: %{_builddir}
BuildRequires: make sed tar coreutils
URL: http://www.bay12games.com/dwarves/
Distribution: openSUSE 42.1
Vendor: Bay12Games (http://bay12games.com/dwarves)
#Packager: Waveclaw.net Buildteam
Prefix: %{prefix}
# http://www.bay12games.com/dwarves/df_42_03_linux.tar.bz2
Source0: df_43_03_linux.tar.bz2
Source1: configure
Source2: Makefile
Source3: DwarfFortress.desktop.in
Source4: dwarffortress.in
Source5: DwarfFortress.png
Patch0: df_bad_libgraphics.patch
Patch1: xxd-Dwarf_Fortress.patch
NoSource: 0
Provides: %{name}-32bit
Requires: %{name}-libs %{name}-data

%description
From https://www.bay12games.com/dwarves/features.html

Dwarf Fortress is a single-player fantasy game. You can control a dwarven outpost or an adventurer in a randomly generated, persistent world.

Slaves to Armok: God of Blood Chapter II: Dwarf Fortress Copyright (C) 2002-2016 by Tarn Adams.
FMOD Sound System Copyright (C) 1994-2006 Firelight Technologyes PTy, Ltd.
Simple DirectMedia Layer, SDL_Image, SDL_ttf Copytight (C) 1997-2006 Sam Lantiga.
FreeType fonts Copyright (C) 2007 The FreeType Project.

%prep -j
rm -rf %{_builddir}
mkdir %{_builddir}

%setup -q -n df_linux
cp %{SOURCE1} ./
cp %{SOURCE2} ./
cp %{SOURCE3} ./
cp %{SOURCE4} ./
cp %{SOURCE5} ./

#
# START PATCHES - if ToadyOne ever fixes
#  http://www.bay12games.com/dwarves/mantisbt/view.php?id=2688
# then delete all the patches, this whole secion condences to just 'build'
#

# patch from
#  tar xjf SOURCE0
#  cp -rp df_linux{,.orig}
# sed -e 's#png#bmp#g' df_linux/data/init/init.txt > t;mv t df_linux/data/init/init.txt
# diff -r -u df_linux.orig df_linux  > df_bad_libgraphics.patch
%patch -P 0 -p 1

# To make an xxd patch do
# cp df_linux/libs/Dwarf_Fortress{,.orig}
# sed -e 's#mouse.png#mouse.bmp#g' df_linux/libs/Dwarf_Fortress.orig > Dwarf_Fortress
# xxd df_linux/libs/Dwarf_Fortress.orig > orig.txt
# xxd Dwarf_Fortress > patched.txt
# diff orig.txt patched.txt | grep '>' | cut -d ' ' -f 2- > xxd-Dwarf_Fortress.patch
%build
xxd -r %PATCH1 libs/Dwarf_Fortress

#
# END PATCHES
#

%install
make DESTDIR=${RPM_BUILD_ROOT} PREFIX=/%{prefix} VERSION=%{version} install

%clean
rm -rf $RPM_BUILD_ROOT

# we don't mark init.txt as a config file because
# the script copies that version to the local user's dir
%files
%defattr(-,root,root)
/usr/bin/dwarffortress
/usr/share/applications/DwarfFortress.desktop
/usr/share/pixmaps/DwarfFortress.png

%package docs
BuildArch: noarch
Summary: Documentation for Dwarf Fortress
Group: Amusements/Games/Other
%description docs
Dwarf Fortress Documentation.

%files docs
%defattr(-,root,root)
%doc /usr/share/doc/DwarfFortress/%{version}/*

%package data
BuildArch: noarch
Summary: RAWS, fonts and default content.
Group: Amusements/Games/Other
%description data
Dwarf Fortress content including RAWs and default fonts.

%files data
%defattr(-,root,root)
/usr/share/DwarfFortress/%{version}/*

%package libs
Summary: Binaries and libraries to run DwarfFortress
Group: Amusements/Games/Other
Requires: libz1-32bit libsndfile1-32bit libopenal1-32bit libSDL_image-1_2-0-32bit libSDL_ttf-2_0-0-32bit
%description libs
Dwarf Fortress executables and libraries.

%files libs
%defattr(-,root,root)
/usr/lib/DwarfFortress/%{version}/*

%package src
BuildArch: noarch
Summary: Source code for Dwarf Fortress
Group: Amusements/Games/Other
%description src
Dwarf Fortress source files provided for license compatibility.

%files src
%defattr(-,root,root)
/usr/src/DwarfFortress/%{version}/*

%changelog

* Fri Jun 10 2016 Jeremiah Powell <waveclaw@waveclaw.net> 0.43.03-1
- Update for Dwarf Fortress 0.43.03

* Sat Dec 12 2015 Jeremiah Powell <waveclaw@waveclaw.net> 0.42.03-1
- Update for Dwarf Fortress 0.42.03

* Sun Dec 21 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.22-1
- Update for Dwarf Fortress 0.40.22
- Bugfixes by Bay12Games for chained jobs.

* Fri Dec 19 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.21-1
- Update for Dwarf Fortress 0.40.21
- Bugfixes by Bay12Games for chained hauling jobs.

* Sun Nov 16 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.16-2
- Update for Dwarf Fortress 0.40.16
- Seperate architectures for files

* Sun Nov 09 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.15-2
- Update for Dwarf Fortress 0.40.15
- subpackages for src, libs, data and the comically unhelpful help docs.

* Sat Sep 13 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.12-2
- Update for Dwarf Fortress 0.40.12, release 2

* Wed Sep 03 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.11-1
- Update for Dwarf Fortress 0.40.11

* Wed Aug 06 2014 Jeremiah Powell <waveclaw@waveclaw.net> 0.40.06-1
- Create specfile, Makefile, fake configure and patches
