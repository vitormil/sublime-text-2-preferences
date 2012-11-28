#!/usr/bin/python
import re
import sublime
import sublime_plugin

from hayaku import get_hayaku_options

__all__ = [
    'HayakuSingleCaretContext',
    'HayakuAtCssContext',
    'HayakuAddCodeBlockContext',
    'HayakuAddCodeBlockCommand',
    'HayakuExpandCodeBlockCommand',
]

REGEX_WHITESPACES = re.compile(r'^\s*$')

# Context
class HayakuSingleCaretContext(sublime_plugin.EventListener):
    def on_query_context(self, view, key, *args):
        if key != "hayaku_single_caret":
            return None

        # Multiple blocks inserting doesn't make sense
        if len(view.sel()) > 1:
            return None

        # TODO: understand selection, but don't replace it on code block inserting
        if not view.sel()[0].empty():
            return None

        return True

class HayakuAtCssContext(sublime_plugin.EventListener):
    def on_query_context(self, view, key, *args):
        if key != "hayaku_at_css":
            return None

        # Looking for the scope
        if not view.score_selector(view.sel()[0].begin(),'source.css, source.stylus, source.sass, source.scss'):
            return None

        return True

class HayakuAddCodeBlockContext(sublime_plugin.EventListener):
    def on_query_context(self, view, key, *args):
        if key != "hayaku_add_code_block":
            return None

        # Determining the left and the right parts
        region = view.sel()[0]
        line = view.line(region)
        left_part = view.substr(sublime.Region(line.begin(), region.begin()))
        right_part = view.substr(sublime.Region(region.begin(), line.end()))

        # Check if the line isn't just a line of whitespace
        if REGEX_WHITESPACES.search(left_part + right_part) is not None:
            return None
        # Simple check if the left part is ok
        if left_part.find(';') != -1:
            return None
        # Simple check if the right part is ok
        if right_part.find(';') != -1:
            return None

        return True

def hayaku_get_block_snippet(options, inside = False):
    start_before = options["CSS_whitespace_block_start_before"]
    start_after = options["CSS_whitespace_block_start_after"]
    end_before = options["CSS_whitespace_block_end_before"]
    end_after = options["CSS_whitespace_block_end_after"]
    opening_brace = "{"
    closing_brace = "}"

    if options["CSS_syntax_no_curly_braces"]:
        opening_brace = ""
        closing_brace = ""
        start_before = ""
        end_before = ""

    if inside:
        opening_brace = ""
        closing_brace = ""
        start_before = ""
        end_after = ""

    return ''.join([
          start_before
        , opening_brace
        , start_after
        , "$0"
        , end_before
        , closing_brace
        , end_after
    ])

# Command
class HayakuExpandCodeBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # TODO: consume the braces and whitespaces around and inside
        self.view.run_command("insert_snippet", {"contents": hayaku_get_block_snippet(get_hayaku_options(self),True)})

class HayakuAddCodeBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        result = '/* OVERRIDE ME */'

        # Determine the limits for place searching
        regions = self.view.sel()
        region = regions[0]
        line = self.view.line(region)
        stop_point = self.view.find('[}]\s*',line.begin())
        if stop_point is not None:
            end = stop_point.end()
        else:
            end = self.view.find('[^}]*',line.begin()).end()
        where_to_search = self.view.substr(
            sublime.Region(
                line.begin(),
                end
            )
        )

        options = get_hayaku_options(self)

        # Insert a code block if we must
        found_insert_position = re.search('^([^}{]*?[^;,}{\s])\s*(?=\n|$)',where_to_search)
        if found_insert_position is not None:
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(len(found_insert_position.group(1)) + line.begin(), len(found_insert_position.group(1)) + line.begin()))

            result = hayaku_get_block_snippet(options)
        else:
            # Place a caret + create a new line otherwise
            # FIXME: the newline is not perfectly inserted. Must rethink it so there wouldn't
            # be replacement of all whitespaces and would be better insertion handling
            found_insert_rule = re.search('^(([^}]*?[^;]?)\s*)(?=\})',where_to_search)
            if found_insert_rule:
                self.view.sel().clear()
                self.view.sel().add(sublime.Region(len(found_insert_rule.group(2)) + line.begin(), len(found_insert_rule.group(1)) + line.begin()))

                result = ''.join([
                      options["CSS_whitespace_block_start_after"]
                    , "$0"
                    , options["CSS_whitespace_block_end_before"]
                ])

        self.view.run_command("insert_snippet", {"contents": result})
