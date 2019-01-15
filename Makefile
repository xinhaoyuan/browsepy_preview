.PHONY: package

package:
	python3 setup.py sdist

clean:
	-rm -rf dist browsepy_preview.egg-info
