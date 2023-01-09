# bumpfontversion

Version-bump your *source* font files.

This tool, patterned after the wonderful [bumpversion](https://github.com/c4urself/bump2version), allows you to update the version of your font source files, as well as create commits and tags in git.

It currently supports UFO and Glyphs format font files.

## Installation

You can download and install the latest version of this software from the Python package index (PyPI) as follows:

```
pip install --upgrade bumpfontversion
```

## Usage

For users of bump2version, please note that the interface is slightly different. You can *either* use:

```
bumpfontversion --new-version 0.5 MyFont.ufo
```

to set the version directly, or

```
bumpfontversion --part minor MyFont.glyphs # Upgrade the minor version
bumpfontversion --part major MyFont.glyphs # Upgrade the major version
```

As per bump2version, you can use `--commit` to commit the new version to git, and `--tag` to add a new git tag.

## See also

* [bumpversion](https://github.com/c4urself/bump2version)
* [font-v](https://github.com/source-foundry/font-v): Similar tool for font *binary* files

## License

[Apache license](http://www.apache.org/licenses/LICENSE-2.0)
