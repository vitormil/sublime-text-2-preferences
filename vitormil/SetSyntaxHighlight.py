import sublime, sublime_plugin
import os
import re
from functools import partial

class SetSyntaxHighlightCommand(sublime_plugin.EventListener):

  def on_load(self, view):
    path = view.file_name()

    if not path:
      return

    path = path.lower()
    name = os.path.basename(path)
    syntax = partial(self.set_syntax, view)

    syntax(name == "gemfile", "ruby")
    syntax(name == "vagrantfile", "ruby")
    syntax(name == "rakefile", "ruby")
    syntax(name == "capfile", "ruby")
    syntax(name == ".caprc", "ruby")
    syntax(name == ".irbrc", "ruby")
    syntax(name == ".pryrc", "ruby")
    syntax(name == ".zshrc", "ruby")

    syntax(re.match(r'.*?/spec/.*?\.rb', path), "rspec")
    syntax(re.match(r'.*?/(app|config|db)/.*?\.rb', path), "rails")

  def set_syntax(self, view, apply, syntax):
    syntaxes = {
      "rspec": "Ruby/Ruby.tmLanguage",
      "ruby": "Ruby/Ruby.tmLanguage",
      "rails": "Rails/Ruby on Rails.tmLanguage",
      "coffee": "CoffeeScript/Syntaxes/CoffeeScript.tmLanguage",
      "erb" : "Rails/HTML (Rails).tmLanguage",
      "yml" : "YAML/YAML.tmLanguage"
    }

    if not apply:
      return

    if not syntax in syntaxes:
      print "[vitormil] not '" + syntax + "' in syntaxes"
      return

    language_file = "Packages/" + syntaxes[syntax]
    view.settings().set("syntax", language_file)

    print "[vitormil] Switched syntax to '" + syntax + "' using " + language_file
