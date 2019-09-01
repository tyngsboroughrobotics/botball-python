documentation:
	# Remove existing folders
	rm -rf docs/core docs/libwallaby
	rm -f docs/index.html

	# Build documentation
	pdoc --template docs -o docs --html botball/ --force
	mv docs/botball/** docs

	# Remove temp directory
	rm -rf docs/botball

build-for-py2:
	# Remove existing folders
	rm -rf _py2_build

	# Build "core" folder
	py-backwards -i botball/core -o _py2_build/botball/core -t 2.7

	# Build "libwallaby" folder
	mkdir -p _py2_build/botball/libwallaby
	cp botball/libwallaby/__init__.py _py2_build/botball/libwallaby/__init__.py
	cp botball/libwallaby/_bindings.py _py2_build/botball/libwallaby/bindings.py

	# Add __init__.py to build
	echo "from . import core, libwallaby" > _py2_build/botball/__init__.py
