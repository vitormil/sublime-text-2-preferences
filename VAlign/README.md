# Sublime VAlign

A plugin for Sublime Text 2 that adds a shortcut to easily vertically-align the text around the cursor. Just press `Cmd+\` (Mac) or `Ctrl+\` (Windows/Linux) and the code around you will align itself.

This plugin is originally based on [wbond](https://github.com/wbond/)'s [Alignment](https://github.com/wbond/sublime_alignment) plugin.

The primary feature that this plugin offers over Alignment is intelligent alignment based on context. With other plugins, you need to explicitly highlight the lines of code that you want to align. That's not necessary with VAlign -- it will investigate the code surrounding the cursor and figure out which lines to align for you. This makes alignment very quick and simple.

## Examples

**From:**
```
x = 10.0
y = 20.0
width = 100.0
height = 100.0
```

**To:**
```
x      = 10.0
y      = 20.0
width  = 100.0
height = 100.0
```

**From:**
```
rectangle =
	x: 10.0
	y: 20.0
	width: 100.0
	height: 100.0
```

**To:**
```
rectangle =
	x:      10.0
	y:      20.0
	width:  100.0
	height: 100.0
```

**From:**
```
.my-stylus-class
	width 100px
	height 100px
	margin-left 10px
	margin-right 10px
	padding 5px
```

**To:**
```
.my-stylus-class
	width        100px
	height       100px
	margin-left  10px
	margin-right 10px
	padding      5px
```

## Installation

Installation is simple with the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) plugin. Just open the command palette, choose "Install Package" and search for "Valign".

## Changelog

#### v1.1.3

* Added support for Sublime Text 3 by changing the way default preference values are loaded.

#### v1.1.2

* Improved alignment support in JavaScript with "var" prefixes.

#### v1.1.1

* Fixed a crash that happened when aligning lines at the end of a file.
* Namespaced settings to avoid conflicts with other plugins.

#### v1.1.0

* Alignment characters are now configurable.
* Added support for prefixes.

#### v1.0.0

* Initial release.

## License

Copyright (c) 2012 Jarod Long

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
