pdoc:
	@# Remove existing folders
	@rm -rf docs/core docs/wallaby
	@rm -f docs/index.html

	@# Build documentation
	@pdoc3 --template docs -o docs --html botball --force
	@mv docs/botball/** docs

	@# Remove temp directory
	@rm -rf docs/botball
