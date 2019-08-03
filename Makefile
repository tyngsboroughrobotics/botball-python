documentation:
	rm -rf ./docs/core ./docs/libwallaby
	rm -f ./docs/index.html
	pdoc --template ./docs -o docs --html . --force
	mv ./docs/botball/** ./docs
	rm -rf ./docs/botball