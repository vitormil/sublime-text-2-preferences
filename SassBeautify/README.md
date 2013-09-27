# SassBeautify

https://sublime.wbond.net/packages/SassBeautify

A Sublime Text plugin that beautifies Sass files. (Compatible with Sublime Text 2 & 3.)

![ScreenShot](https://raw.github.com/badsyntax/SassBeautify/master/assets/screenshot.png)

## Dependencies

You need to have sass installed. Read the [sass download page](http://sass-lang.com/download.html) to view the installation options.

## Installation

**Option 1 (recommended)**

Install via package control:

1. Ensure you have package control installed, see here: https://sublime.wbond.net/installation
2. Install the package: open up the command palette (ctrl/cmd + shift + p), execute the following command:
'Package Control: Install Package', then enter 'SassBeautify'

**Option 2**

Manual download:

1. Download the zip file file here: https://github.com/badsyntax/SassBeautify/archive/master.zip
2. Unzip the archive, rename the 'SassBeautify-master' folder to 'SassBeautify' and move it into your
Sublime Text 'Packages' directory.

## Usage

**Default usage**

Run the plugin from the command palette:

1. Open the command palette (ctrl/cmd + shift + p)
2. Enter 'SassBeautify'

**Conversion usage**

You can use this plugin to convert from different types. For example, if you create a blank .scss file, then 
copy in a block of CSS code, you can use this plugin to convert the CSS to SCSS. Note that the entire file 
will have to be in the correct format for the conversion to work correctly.

Run the conversion commands from the command palette:

1. Open the command palette (ctrl/cmd + shift + p)
2. Type 'SassBeautify'
3. Choose one of the following options:
  * Convert from CSS to current type
  * Convert from SCSS to current type
  * Convert from SASS to current type

## Settings

Once installed, you can customize how the beautification works by changing the package settings.

1. Open the default settings from the preferences menu: `Preferences >> Package Settings >> SassBeautify >> Settings - Default`
2. Copy the settings and paste them into your user settings file: `Preferences >> Package Settings >> SassBeautify >> Settings - User`
3. Change the user settings.

### Settings overview

The following settings can be adjusted:

```javascript
{
  "indent": 4,        // How many spaces to use for each level of indentation. "t" means use hard tabs.
  "dasherize": false, // Convert underscores to dashes.
  "old": false,       // Output the old-style ":prop val" property syntax. Only meaningful when generating Sass.
  "path": false       // Custom environment PATH.
}
```

## How it works

This plugin is simply a wrapper around the `sass-convert` utility. The `sass-convert `utility will *compile your Sass/Scss
to Sass/Scss*, and thus there's a chance values might change. (For example, see [issue #7](https://github.com/badsyntax/SassBeautify/issues/7).) 

## Compatibility with RVM 

(This does not apply to Windows users.)

RVM uses a shell login script to modify the environment PATH, so you will need to manually add this path to the package
settings if you want this plugin to use the same ruby and gem versions. 

To get this plugin to work with RVM, follow the steps below:

1. Open up terminal.
2. Run the following `echo $PATH`
3. Copy the entire PATH and add this to the package 'path' setting.

## Issues

This plugin should work on Linux (tested on Ubuntu 12.04), Windows (tested on Windows 7) and OSX (tested on 10.5.7).
Please [create an issue](https://github.com/badsyntax/SassBeautify/issues) if you find it doesn't work
as expected on your setup.

## License

Licensed under the MIT license. Created by [Richard Willis](http://badsyntax.co/)
