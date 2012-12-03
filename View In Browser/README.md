# Sublime Text 2 - View In Browser

*View In Browser* is a Sublime Text 2 plugin that will open whatever is in your
current view/tab. If the file current open is new and has not been saved a temporary 
file is created (in your default temp directory for your OS) with the extension of 
**.htm** and your browser will open it. However if the current open file is saved
and has a name this plugin will open it in whatever you have set to handle
its type.

By default the keystroke assigned to this plugin is *CTRL + ALT + V*.

## Installation
Using the Sublime Text 2 Package Control plugin (http://wbond.net/sublime_packages/package_control)
press *CTRL + SHIFT + P* and find **Package Control: Install Package** and press *Enter*.
Find this plugin in the list by name **View In Browser**.

## Configuring Browsers
By default this plugin will open files in Firefox. You can configure it to open
using another browser of your choice. To do this find the *settings.json* file
located in your Sublime configuration directory. This location varies by OS. For 
example, in Ubuntu you will find the *settings.json* file at
**/home/<username>/.config/sublime-text-2/Packages/View in Browser**. In Windows this
file will reside in **C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages\View in Browser**.

The browser you wish to use to open files can be found at the bottom of the file
*settings.json* and is set in the key named **selectedBrowser**. The list of browsers
you can use and configure are in the key named **supportedBrowsers**. 

The **supportedBrowsers** values can be configured to have paths to your browser installations.
Each browser listed is an array (list) of configurations that allow you to setup a browser
for multiple operating systems. For example under *chrome* there are two configurations.
The first is for your average Linux system. The second is for Windows. You'll notice the
Windows path is incorrect and must be changed for your system.

## Configure to View on Local Server
The View In Browser plugin also supports the ability to view files in the context of
a local server. So if you have a local Apache, Tomcat, or some other server application running
you can configure this plugin to open your file prefixed with a URL. 

To configure this the View In Browser plugin reads the configuration of your currently
loaded project. You can edit a project file by opening the *sublime-project* file
by choosing **Project** -> **Edit Project**. In your project file you will need to specify 
two things:

* **baseUrl** - The root URL to prefix files with 
* **basePath** - The base path where your site/application lives

Here's how that looks.

```javascript
{
	"folders":
	[
		{
			"path": "/home/<username>/code/python/my-cool-website"
		}
	],
	"settings": {
		"sublime-view-in-browser": {
			"baseUrl": "http://localhost:8080",
			"basePath": "/home/<username>/code/python/my-cool-website"
		}
	}
}
```

Notice the key named **settings** which is a dictionary that contains another key named
**sublime-view-in-browser**. This is where you will put your **baseUrl** and **basePath**
settings.

Now when you activate View In Browser your file will open with the HTTP protocol instead
of the FILE protocol.

## Change History

* 11/01/2012:
   * Altered command to open Safari on Mac
   * When invoked the current view is auto-saved
* 10/25/2012:
   * New settings.json file to map browser/commands to OSes
   * Plugin will use the specified browser to open files, or default to OS default when browser is unsupported
   * Addressed encoding issue when calling open_new_tab
   * Added ability to specify and respect local server config per project
* 05/21/2012:
   * Temp file only created if view is unsaved
* 05/18/2012:
   * Initial code


## License
See the file LICENSE
