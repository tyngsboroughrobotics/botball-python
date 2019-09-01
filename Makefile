documentation:
	# Remove existing folders
	rm -rf docs/core docs/libwallaby
	rm -f docs/index.html

	# Build documentation
	pdoc --template docs -o docs --html . --force
	mv docs/botball/** docs

	# Remove temp directory
	rm -rf docs/botball

build-for-py2:
	# Remove existing folders
	rm -rf _py2_build

	# Build "core" folder
	py-backwards -i core -o _py2_build/core -t 2.7

	# Build "libwallaby" folder
	mkdir -p _py2_build/libwallaby
	cp libwallaby/__init__.py _py2_build/libwallaby/__init__.py
	cp libwallaby/_bindings.py _py2_build/libwallaby/bindings.py

	# Add __init__.py to build
	echo "from . import core, libwallaby" > _py2_build/__init__.py
