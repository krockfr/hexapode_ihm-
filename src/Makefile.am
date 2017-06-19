## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = hexapode_ihm.ui


## The main script
bin_SCRIPTS = hexapode_ihm.py

## Directory where .class files will be installed
hexapode_ihmdir = $(pythondir)/hexapode_ihm


hexapode_ihm_PYTHON = \
	hexapode_ihm.py \
	client.py \
	point.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
