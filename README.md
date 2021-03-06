# dwarffortress-packaging

Example packaging for Dwarf Fortress, the medival fantasy simulator 
by Bay 12 Games

## /rpm

These are the parts to build a NOSRC rpm.

Rebuild the NOSRC rpm with the proprietary files from 
[Bay12Games](http://www.bay12games.com/dwarves) to create a working version.

The generic RPM has been tested to work on Fedora, openSuSE and Magia Linux 
desktop operating system distributions.

For instructions on using a NOSRC package, see the [RedHat Developer Blog](http://developerblog.redhat.com/2014/12/10/how-to-package-proprietary-software/)

## /debian

These are the parts to build a Debian Format package.

This package is intended to install on Debian based distributions such as 
Ubuntu, Kubuntu or Knoppix.

__TODO__: Finish the Debian Vanilla Package.

## Licensing and Useage

Since the game itself is not free or open source actual packages cannot
legally be built by a maintainer or included in a distribution of software.

End users are free to build their own packages.  These example files are
provided for use.

As [Bay12Games](http://bay12games.com) provides their games free of charge
and are very friendly to the developer community, please consider
supporting them.

## Alternatives

These packages are strictly vanilla content from Bay12Games.  No tilesets
or mod packs or edits to the RAWs are provided.

The included start script is designed to keep savegames in 
$HOME/.local/share/DwarfFortress/$DF\_VERSION/.  Libraries for the game
are also rellocated per the Linux Standards Base.

Lazy Newb Pack, DFHack and other tools require modification to use these
changes for savegames, new tilesets and customized RAWS.

## Notes

The package tries to re-organize vanilla Dwarf Fortress into a regular (Linux Standards Base comliant) Linux
application and does have to make two changes to the game.

* As of the 0.42.03 alpha release these packages have to patch the binaries in the game to replace Portable Network Graphics (PNG) images with bitmap (bmp) images.
* As of the 0.42.03 alpha release these application script takes care to handle the problematic libz library binding.  

If you are an application developer remember to do NOT bind your libraries staically on Linux if you can help it.

## Contributing

The packaging materials are Apache 2.0 licenses. 

Bug reports are welcome.  Patches more welcome but not expected or required. 

Complaints are less welcome, but no software is perfect.  Do let us know if it
does burn your house down, set you or the wife/hustband/boyfriend/girlfriend/cat/dog/hamster fire.
