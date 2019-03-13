# DO NOT EDIT
# This makefile makes sure all linkable targets are
# up-to-date with anything they link to
default:
	echo "Do not invoke directly"

# Rules to remove targets that are older than anything to which they
# link.  This forces Xcode to relink the targets from scratch.  It
# does not seem to check these dependencies itself.
PostBuild._pyswice.Debug:
PostBuild.SimUtilities.Debug: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so
PostBuild.SimMessaging.Debug: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so
/Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so:\
	/opt/local/lib/libpython2.7.dylib\
	/Users/iancooke/basilisk_mag/dist/Basilisk/libSimUtilities.a\
	/Users/iancooke/basilisk_mag/dist/Basilisk/libSimMessaging.dylib\
	/Users/iancooke/basilisk_mag/src/../libs/cspice/lib/cspice_osx.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_filesystem.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_serialization.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_thread.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_system.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_chrono.a
	/bin/rm -f /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so


PostBuild._pyswice.Release:
PostBuild.SimUtilities.Release: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so
PostBuild.SimMessaging.Release: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so
/Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so:\
	/opt/local/lib/libpython2.7.dylib\
	/Users/iancooke/basilisk_mag/dist/Basilisk/libSimUtilities.a\
	/Users/iancooke/basilisk_mag/dist/Basilisk/libSimMessaging.dylib\
	/Users/iancooke/basilisk_mag/src/../libs/cspice/lib/cspice_osx.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_filesystem.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_serialization.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_thread.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_system.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_chrono.a
	/bin/rm -f /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/_pyswice.so


PostBuild._pyswice.MinSizeRel:
PostBuild.SimUtilities.MinSizeRel: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/MinSizeRel/_pyswice.so
PostBuild.SimMessaging.MinSizeRel: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/MinSizeRel/_pyswice.so
/Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/MinSizeRel/_pyswice.so:\
	/opt/local/lib/libpython2.7.dylib\
	/Users/iancooke/basilisk_mag/dist/Basilisk/MinSizeRel/libSimUtilities.a\
	/Users/iancooke/basilisk_mag/dist/Basilisk/MinSizeRel/libSimMessaging.dylib\
	/Users/iancooke/basilisk_mag/src/../libs/cspice/lib/cspice_osx.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_filesystem.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_serialization.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_thread.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_system.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_chrono.a
	/bin/rm -f /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/MinSizeRel/_pyswice.so


PostBuild._pyswice.RelWithDebInfo:
PostBuild.SimUtilities.RelWithDebInfo: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/RelWithDebInfo/_pyswice.so
PostBuild.SimMessaging.RelWithDebInfo: /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/RelWithDebInfo/_pyswice.so
/Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/RelWithDebInfo/_pyswice.so:\
	/opt/local/lib/libpython2.7.dylib\
	/Users/iancooke/basilisk_mag/dist/Basilisk/RelWithDebInfo/libSimUtilities.a\
	/Users/iancooke/basilisk_mag/dist/Basilisk/RelWithDebInfo/libSimMessaging.dylib\
	/Users/iancooke/basilisk_mag/src/../libs/cspice/lib/cspice_osx.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_filesystem.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_serialization.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_thread.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_system.a\
	/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_chrono.a
	/bin/rm -f /Users/iancooke/basilisk_mag/dist/Basilisk/pyswice/RelWithDebInfo/_pyswice.so




# For each target create a dummy ruleso the target does not have to exist
/Users/iancooke/basilisk_mag/dist/Basilisk/MinSizeRel/libSimMessaging.dylib:
/Users/iancooke/basilisk_mag/dist/Basilisk/MinSizeRel/libSimUtilities.a:
/Users/iancooke/basilisk_mag/dist/Basilisk/RelWithDebInfo/libSimMessaging.dylib:
/Users/iancooke/basilisk_mag/dist/Basilisk/RelWithDebInfo/libSimUtilities.a:
/Users/iancooke/basilisk_mag/dist/Basilisk/libSimMessaging.dylib:
/Users/iancooke/basilisk_mag/dist/Basilisk/libSimUtilities.a:
/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_chrono.a:
/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_filesystem.a:
/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_serialization.a:
/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_system.a:
/Users/iancooke/basilisk_mag/libs/boost_1_61_0/lib64-osx/libboost_thread.a:
/Users/iancooke/basilisk_mag/src/../libs/cspice/lib/cspice_osx.a:
/opt/local/lib/libpython2.7.dylib:
