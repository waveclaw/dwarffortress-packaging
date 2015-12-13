#
# Makefile for installing DwarfFortress using Linux Stanards Base locations
#
# Copyright (c) 2013-2015 Jeremiah Powell <waveclaw@waveclaw.net>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. 
# The license for this file, and modifications and additions to the
# file are Apache 2.0 per in LICENSE.md.
#

DESTDIR=
PREFIX=/usr
VERSION=0.40.06
DOCS_SRC='command line.txt' 'file changes.txt' 'release notes.txt' README.linux
LIBS_SRC=libs
SCRIPT=dwarffortress
SRC_SRC=g_src
DATA_SRC=data raw
ICON=DwarfFortress.png
APPCON=DwarfFortress.desktop

DIR=DwarfFortress/${VERSION}
DATA_TARGET=${DESTDIR}/${PREFIX}/share/${DIR}
DOCS_TARGET=${DESTDIR}/${PREFIX}/share/doc/${DIR}
LIBS_TARGET=${DESTDIR}/${PREFIX}/lib/${DIR}
BIN_TARGET=${DESTDIR}/${PREFIX}/bin
SRC_TARGET=${DESTDIR}/${PREFIX}/src/${DIR}
ICON_TARGET=${DESTDIR}/${PREFIX}/share/pixmaps
APPCON_TARGET=${DESTDIR}/${PREFIX}/share/applications

all:
	@echo

makedirs: 
	mkdir -p ${LIBS_TARGET} ${DOCS_TARGET} ${DATA_TARGET} ${SRC_TARGET} ${BIN_TARGET} ${ICON_TARGET} ${APPCON_TARGET}

copydata: 
	cp -rp ${DATA_SRC} ${DATA_TARGET}

copydocs:
	cp -rp ${DOCS_SRC} ${DOCS_TARGET}

# expect xxd patch to Dwarf_Fortress
# also have to link libSDL_image-1.2.so, libsndfile.so, libopenal.so
copylibs: 
	cp -rp ${LIBS_SRC}/* ${LIBS_TARGET}
	ln -s `find /lib /usr/lib -type f -name libSDL_image-1.2.so* |head -1` ${LIBS_TARGET}/libSDL_image-1.2.so
	ln -s `find /lib /usr/lib -type f -name libsndfile.so\* |head -1` ${LIBS_TARGET}/libsndfile.so
	ln -s `find /lib /usr/lib -type f -name libopenal.so\* |head -1` ${LIBS_TARGET}/libopenal.so


copysrc: 
	cp -rp ${SRC_SRC}/* ${SRC_TARGET}

install: makedirs copydata copydocs copylibs copysrc ${SCRIPT}.in
	sed -e 's|@VERSION@|${VERSION}|' \
		  -e 's|@DATA@|${PREFIX}/share/${DIR}|' \
		  -e 's|@BINDIR@|${PREFIX}/lib/${DIR}|' \
		  -e 's|@DESTDIR@|${PREFIX}|' <${SCRIPT}.in >${SCRIPT}
	chmod 0555 ${SCRIPT}
	cp -p ${SCRIPT} ${BIN_TARGET}
	sed -e 's|@VERSION@|${VERSION}|' \
		-e 's|@DESTDIR@|${PREFIX}|'  <${APPCON}.in >${APPCON}
	cp -p ${ICON}  ${ICON_TARGET}
	cp ${APPCON} ${APPCON_TARGET}


clean:
	rm -rf ${LIBS_TARGET} ${DOCS_TARGET} ${DATA_TARGET} ${SRC_TARGET}
	test -f ${BIN_TARGET}/${SCRIPT} && rm ${BIN_TARGET}/${SCRIPT}

.PHONY: all clean
