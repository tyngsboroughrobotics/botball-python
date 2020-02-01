pdoc:
	@# Remove existing folders
	@rm -rf docs/components
	@rm -rf docs/create
	@rm -rf docs/helpers
	@rm -rf docs/procedure
	@rm -f docs/index.html

	@# Build documentation
	@pdoc3 --template docs -o docs --html botball --force
	@mv docs/botball/** docs/
	@rm -rf docs/botball/