# Hayaku <sup>[1.0.3](https://github.com/hayaku/hayaku/blob/master/CHANGELOG.md)</sup>

Hayaku is a bundle of useful scripts aiming for rapid front-end web development.

The main aim of Hayaku is to create the fastest way to write and maintain CSS code in an editor.

# Table of Contents

1. [Install Hayaku for Sublime Text](#install-hayaku-for-sublime-text)

2. [Features](#features)
    - [Smart CSS Abbreviations](#smart-css-abbreviations)
        - [Fuzzy CSS property abbreviations](#fuzzy-css-property-abbreviations)
        - [Smart CSS values abbreviations](#smart-css-values-abbreviations)
        - [Numeric values in abbreviations](#numeric-values-in-abbreviations)
        - [Color values in abbreviations](#color-values-in-abbreviations) with [RGBA values](#rgba-values)
        - [Importance modifier](#importance-modifier)
        - [Some default values](#some-default-values)
    - [Postexpands](#postexpands)
        - [Simple property postexpands](#simple-property-postexpands)
        - [Postexpands for units](#postexpands-for-units)
        - [Postexpands for colors](#postexpands-for-colors)
    - [Creating new CSS rule blocks](#creating-new-css-rule-blocks)
    - [Inline comments](#inline-comments)
    <br/><br/>

3. [Settings and Preferences](#settings-and-preferences)
    - [Autoguessing the code style](#autoguessing-the-code-style)
    - [Single code style](#single-code-style)
    - [Prefixes options](#prefixes-options)
    - [The aligning for the prefixes](#the-aligning-for-the-prefixes)
    - [Using only specific prefixes](#using-only-specific-prefixes)
    <br/><br/>

4. [Using Hayaku with CSS Preprocessors](#using-hayaku-with-css-preprocessors)

5. [License and copyrights](#license-and-copyrights)


# Install Hayaku for [Sublime Text](http://www.sublimetext.com/2)

Right now Hayaku is available only for Sublime Text, but when it would be complete, we would port it to some other editors.

#### Using [Package Control](http://wbond.net/sublime_packages/package_control):

1. Run `Package Control: Install Package` command
2. Search for `Hayaku - tools for writing CSS faster` (`Hayaku` should be enough) and wait for it to be installed
3. Restart Sublime Text (required to make default settings for different syntaxes to work)

#### Or manually, using git:

Clone repository into Packages directory (can be found using `Preferences: Browse Packages` command in Sublime Text)
``` sh
git clone git://github.com/hayaku/hayaku.git
```

And then restart Sublime Text.

# Features

## Smart CSS Abbreviations

Hayaku is not your average snippet engine. Most of the CSS snippets to date are static — you need to remember all the abbreviations if you want to use them.

Hayaku offers a better and faster way: you don't need to remember anything, you can just try to write the shortest abbreviation for a thing you want to write in CSS — and Hayaku would try to guess it when you press `tab`.

There are a lot of things Hayaku can do in abbeviations, here are some of them:

### Fuzzy CSS property abbreviations

This is the first basic thing: Hayaku don't have any premade snippets for CSS, it have a dictionary with a lot of CSS properties, so when you write some abrakadabra, it tries to parse it and guess what you meant. For most properties those abbreviations could be rather short, but you're not sticked to them: you can write as much letters for a property as you wish.

So, writing `w`, `wi` or `wid` would give you `width`. And don't forget about the fuzzy part: `wdt` and `wdth` would work too.

Sometimes you would guess that some abbreviations must become other things, but in most cases all the variants have some logic beyound. `b` could be expanded to `background` or `border`, but expanded to `bottom` instead — it's becouse all the “sides” values are abbreviated to just one letter: **l**eft,  **r**eft,  **t**op, so  **b**ottom goes by this path.

However, if you feel that some abbreviation just need to be not that is expands to, feel free to [fill up an issue](https://github.com/hayaku/hayaku/issues/new).

### Smart CSS values abbreviations

Here comes the second basic thing of Hayaku, the awesome one. You can expand abbreviations for the property+value parts, but you don't need to use any delimiters in those abbreviations! That's right — you can just write something like `por` and get `position: relative`!

This works also fuzzy, so to get `position: relative` you could use any number of letters: `pore`, `posrel`, `pstnrltv` etc. Also, if you want, you can still use a delimiter — just add a colon between the property and value and get the same result. So, if you want to stick to Zen style, use it — `pos:r` would work as intended. And `p:r` would work too — while `pr` would expand to `padding-right`, adding delimiter could help by removing ambiguity — padding can't have any values containing `r`, so hayaku falls to `position`.

### Numeric values in abbreviations

Hayaku understands a lot of ways of writing numeric abbreviations.

- You can just write a number after abbreviation to treat it as a value: `w10` would expand to `width: 10px` (see? automatic pixels!).

- Negative numbers supported too: `ml-10` would expand to `margin-left: -10px`.

- If you'd write a dot somewhere in abbreviation, Hayaku would guess what you need `em`s, so `w10.5` would expand to `width: 10.5em`.

- There are some abbreviations for some units, like `percents` for `%`, or `.` for em, so `100p` would expand to `100%` and `10.` to `10em`.

- All other units are supported, `h2pt` would expand to `height:2pt` and so on. Fuzzy guess is there too: if you'd want `vh` you could write just `w10h` and get `width: 10vh`.

### Color values in abbreviations

Actually, you can not only expand strings and numbers, you can expand even colors using abbreviations! You can use different ways to achieve that (as anything in Hayaku), so just look at those examples:

- `c0` → `color: #000`
- `cF` → `color: #FFF` (use uppercase to tell Hayaku it's a color)
- `cFA` → `color: #FAFAFA`
- `c#fa` → `color: #FAFAFA` (no need in uppercase if you use `#`)

And, of course, this works everywhere you would expect colors to work, so `brc0` would expand to `border-right-color: #000;`

#### RGBA values

There is also a way to expand `rgba` values for colors — you can either use rgba's alpha after the dot, either use hexadecimal alpha after the full color, if you'd like. This would look like this:

- `c0.5` → `color: rgba(0,0,0,.5)`
- `cF.2` → `color: rgba(255,255,255,.2)`
- `cABCD` → `color: rgba(170,187,204,0.87)`
- `cABC80` → `color: rgba(170,187,204,0.5)`

You can also write just the dot and get the placeholder on the `alpha` part of the `rgba`:

- `cF00.` → `color: rgba(255,0,0,.[5])`

### Importance modifier

A nice little feature: add `!` after abbreviation and get ` !important` at the end. Not that importance is something you would want to use everyday, but still.

`dn!` would give you `display:none !important;`, yeah.

### Automatic vendor prefixes

If you need some vendor prefixes, Hayaku could provide them!

`bra1.5` would expand to this:

``` CSS
-webkit-border-radius: 1.5em;
        border-radius: 1.5em;
```

Right now there are no prefixes for values (like gradients etc.) but someday they'd be there.

### Some default values

If you'd write something that is only a property (as Hayaku would guess), Hayaku would insert a snippet with some default value already selected for you, so you could start writing your own value to replace it or to press `tab` again to keep it and move forward. So, writing `w` would actually expand to `width: [100%]` (braces mean that this value is selected by default).

## Postexpands

“Postexpands” is a nice Hayaku's feature, that allows you to expand only the property at first and then use instant autocomplete for the values of numbers.

That must be said is that postexpand is a bit different from the usual abbreviation expands — it don't have any fuzzy search inside, so only the first letters matter. However, as you'd use it you would see that it is still a powerfull feature.

### Simple property postexpands

The simplest postexpand feature is autocomplete for the string values of different properties.

If you'd expand some property like `po` to `position: |;`, then you could start writing any of it's values and get they expanded right after the cursor. So, writing `a` would give you `position: a|bsolute;`.

### Postexpands for units

Another postexpand feature would allow you to firstly expand the property that can have numeric values, like `width` and then write only the digits and let Hayaku place the corresponding units automatically.

So, when you expand, for example, `w` to `width: |;`, you'd get different options:

- write any iteger like `10` and you'd get `width: 10|px;`
- write any float like `1.5` and you'd get `width: 1.5|em;`
- write an integer and them `e`, so you'd get `width: 10e|m;`
- if the value have any string values, you can also use them: writing `a` would give you `width: a|uto;`

Negative numbers could still be used and if you'd like any other unit, you could just write it down, the autocompleted units won't bother you.

### Postexpands for colors

As you can use shortcuts to colors in abbreviations, you could also write the color values after expanding only the property. The basics are the same: `color: |;` + `F` would give you `color: #F|FF;`, and so on. You can use or don't use the hash symbol.

Another somewhat obscure (but helpful) feature is postexpand for `rgba` colors. This is triggered by writing the comma after decimal value. There is also a shortcut to the alpha value.

- `color: 255,|` would transform to `color: rgba(255,|255,255,1);`
- `color: 255,.|` would transform to `color: rgba(255,255,255,.|5);`

There are a lot of things we could improve there, so stay tuned.

### Disabling postexpands

If you'd wish to disable postexpands at all for some reason, you could use this setting for this: `"hayaku_CSS_disable_postexpand": true`

## Creating new CSS rule blocks

In Hayaku there is a simple but powerful feature: when you wrote a selector, you could just press `CMD+Enter` to get a block for writing CSS here.

## Inline comments

Another little helper: write `//` in CSS to have it expanded to `/* | */` (where the pipe is a caret placement).

This feature is in development, we plan on adding a lot of things to make commenting fun.

# Settings and Preferences

Hayaku have **a lot** of different configurable options, both for your code style and for different features you'd wish to use.

## Autoguessing the code style

The easiest way to set the basic settings for your codestyle, is to use `hayaku_CSS_syntax_autoguess` option:

``` JSON
{
    "hayaku_CSS_syntax_autoguess": [
        "    selector {              ",
        "        property: value;    ",
        "        }                   "
    ]
}
```

There you can use any whitespaces between the predefined keywords and they would be used by Hayaku. A few notes regarding this setting:

- You should use the newline symbol `\n` or multiple array items, because JSON don't support multiline well.
- For your convenience you can use any leading of trailing spaces. Trailing spaces would be stripped at all, leading spaces would be stripped as if there weren't spaces at the start of the selector.

Maybe someday there'd be a _real_ autoguessing, that would read your open stylesheet and find what better suits it, but not today.

## Single code style

If you don't want to use autoguessing, then you could define single options one by one. This would also be helpful if you'd want to redefine only some of the code styling settings in other project or syntax.

Here is a JSON with all the available single code styling options:

``` JSON
{
    "hayaku_CSS_whitespace_after_colon":        " ",
    "hayaku_CSS_whitespace_block_start_before": " ",
    "hayaku_CSS_whitespace_block_start_after":  "\n\t",
    "hayaku_CSS_whitespace_block_end_before":   "\n\t",
    "hayaku_CSS_whitespace_block_end_after":    ""
}
```

The names speak for themselves there.

The important thing is that the single code style settings always override the autoguessed one.

## Prefixes options

If you don't want to use any prefixes at all (as if you're using some mixins for it in Stylus, or use prefix-free), you can disable them with that option:

``` JSON
{
    "hayaku_CSS_prefixes_disable": true
}
```

## The aligning for the prefixes

By default Hayaku aligns expanded prefixed properties in this nice way:

``` CSS
.foo {
    -webkit-transform: rotate(45deg);
       -moz-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
         -o-transform: rotate(45deg);
            transform: rotate(45deg);
    }
```

This way it's easier to spot changes to a single prefixed property and to use multiline edit on them.

However, if you'd want to expand such properties left aligned, set

``` JSON
{
    "hayaku_CSS_prefixes_align": false
}
```

## Using only specific prefixes

This is not something that you would use often, but if you'd need, you could use only prefixes for browsers you want. There are two settigns for this:

``` JSON
{
    "hayaku_CSS_prefixes_only": ["webkit","moz","o"],
    "hayaku_CSS_prefixes_no_unprefixed": true
}
```

- `hayaku_CSS_prefixes_only` is an array of the prefixes you'd want to use **only**. In the upper example I excuded `ms` prefix, so if you'd use meta to emulate all IE versions to IE7 for example, then you could remove `ms` prefix, so your CSS would be a bit cleaner.
- when `hayaku_CSS_prefixes_no_unprefixed` is set to `True`, such prefixed clusters won't contain the official unprefixed variant.

Right now there is no easy way to adjust prefixes per property, but it would be there in a near feature, so stay tuned!

# Using Hayaku with CSS Preprocessors

“Hey! I don't need to write CSS faster — I use Preprocessors!” you could say. But, well, you would still need to write all those extra symbols, so abbreviations would fit preprocessors well. And as Hayaku is highly customizable, you could use it with any preprocessor: Sass, Less, Stylus etc.

Right now only basic things are available, but in feature you could expand different mixins and functions too, so just wait for it.

- - -

And this is just the start, there would be a lot of other nice features, so still tuned and follow the [official bundle's twitter](http://twitter.com/#!/hayakubundle)!

# License and copyrights

This software is released under the terms of the [MIT license](https://github.com/hayaku/hayaku/blob/master/LICENSE).
