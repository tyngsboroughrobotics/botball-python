documentation:
	# Remove existing folders
	rm -rf docs/core docs/wallaby
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

	# Build "wallaby" folder
	mkdir -p _py2_build/botball/wallaby
	cp botball/wallaby/__init__.py _py2_build/botball/wallaby/__init__.py
	cp botball/wallaby/_bindings.py _py2_build/botball/wallaby/bindings.py

	# Add __init__.py to build
	echo "from . import core, wallaby" > _py2_build/botball/__init__.py

	# Restore files that shouldn't be converted to Python 2 because they are
	# already compatible
	cp -f botball/core/helpers/enum.py _py2_build/botball/core/helpers/enum.py
