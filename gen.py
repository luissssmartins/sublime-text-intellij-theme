# Based on Sublime Mariana Theme
# Author: pessoal.luismartins@gmail.com | @luissssmartins
import colorsys, json, pathlib

def hsl(h, s, l, a=1.0):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return (r * 255, g * 255, b * 255, a)

def over(c, base, keep=None):
    a = c[3] if keep is None else 1 - keep / 100
    return tuple(c[i] * a + base[i] * (1 - a) for i in range(3)) + (1.0,)

def hx(c):
    return "".join(f"{round(v):02x}" for v in c[:3])

blue, blue_vibrant = hsl(210, 50, 60), hsl(210, 60, 60)
blue3, blue4, blue5, blue6 = hsl(210, 15, 22), hsl(210, 13, 45), hsl(180, 36, 54), hsl(221, 12, 69)
blue2 = over(hsl(210, 13, 40, 0.7), blue3)  # hsla(210, 13%, 40%, 0.7)
green, grey = hsl(114, 31, 68), hsl(0, 0, 20)
orange, orange2, orange3 = hsl(32, 93, 66), hsl(32, 85, 55), hsl(40, 94, 68)
pink, red, red2 = hsl(300, 30, 68), hsl(357, 79, 65), hsl(13, 93, 66)
white, white2, white3 = hsl(0, 0, 100), hsl(0, 0, 97), hsl(219, 28, 88)
bg, fg = blue3, white3
guide = over(fg + (0,), bg, keep=85)[:3] + (1.0,)  # this fixes original Mariana theme

colors = {
    "CARET_COLOR": orange,
    "CARET_ROW_COLOR": bg,
    "SELECTION_BACKGROUND": blue2,
    "GUTTER_BACKGROUND": bg, "LINE_NUMBERS_COLOR": blue4, "LINE_NUMBER_ON_CARET_ROW_COLOR": fg,
    "INDENT_GUIDE": guide, "VISUAL_INDENT_GUIDE": guide, "SELECTED_INDENT_GUIDE": blue5,  # active_guide
    "RIGHT_MARGIN_COLOR": guide, "TEARLINE_COLOR": guide, "METHOD_SEPARATORS_COLOR": guide,
    "WHITESPACES": blue2, "CONSOLE_BACKGROUND_KEY": bg, "DOCUMENTATION_COLOR": bg, "LOOKUP_COLOR": bg,
    "ADDED_LINES_COLOR": green, "MODIFIED_LINES_COLOR": orange, "DELETED_LINES_COLOR": red,
    "WHITESPACES_MODIFIED_LINES_COLOR": orange,
    "FILESTATUS_ADDED": green, "FILESTATUS_MODIFIED": orange, "FILESTATUS_DELETED": red,
}

I, B, U, BOX, WAVE = 2, 1, "underline", "box", "wave"

attrs = {
    "TEXT": (fg, bg),
    "DEFAULT_LINE_COMMENT": (blue6,), "DEFAULT_BLOCK_COMMENT": (blue6,), "DEFAULT_DOC_COMMENT": (blue6,),  # comment
    "DEFAULT_DOC_COMMENT_TAG": (blue6,), "DEFAULT_DOC_COMMENT_TAG_VALUE": (blue6,), "DEFAULT_DOC_MARKUP": (blue6,),
    "DEFAULT_STRING": (green,),  # string
    "DEFAULT_VALID_STRING_ESCAPE": (pink,),  # constant.character
    "DEFAULT_INVALID_STRING_ESCAPE": (white2, red),  # invalid
    "DEFAULT_NUMBER": (orange,),  # constant.numeric
    "DEFAULT_CONSTANT": (pink,),  # constant.other
    "DEFAULT_PREDEFINED_SYMBOL": (blue, None, I),  # support.function
    "DEFAULT_KEYWORD": (pink,),  # keyword
    "DEFAULT_OPERATION_SIGN": (red2,),  # keyword.operator
    "DEFAULT_COMMA": (blue6,), "DEFAULT_SEMICOLON": (blue6,),  # punctuation.separator/terminator
    "DEFAULT_DOT": (blue6,),  # punctuation.accessor
    "DEFAULT_PARENTHS": (white,), "DEFAULT_BRACES": (white,), "DEFAULT_BRACKETS": (white,),  # punctuation.section
    "DEFAULT_FUNCTION_DECLARATION": (blue5,),  # entity.name.function
    "DEFAULT_FUNCTION_CALL": (blue,),  # variable.function
    "DEFAULT_CLASS_NAME": (orange,), "DEFAULT_INTERFACE_NAME": (orange,),  # entity.name
    "DEFAULT_CLASS_REFERENCE": (blue, None, I),  # support.class
    "DEFAULT_PARAMETER": (orange,),  # variable.parameter
    "DEFAULT_IDENTIFIER": (fg,), "DEFAULT_LOCAL_VARIABLE": (fg,), "DEFAULT_GLOBAL_VARIABLE": (fg,),
    "DEFAULT_INSTANCE_FIELD": (fg,), "DEFAULT_STATIC_FIELD": (fg,),
    "DEFAULT_METADATA": (blue,),  # variable.annotation
    "DEFAULT_LABEL": (fg,),
    "DEFAULT_TAG": (red,), "DEFAULT_ATTRIBUTE": (pink,), "DEFAULT_ENTITY": (pink,),  # entity.name.tag / attribute-name
    "JSON.PROPERTY_KEY": (blue5,), "YAML_SCALAR_KEY": (blue5,), "YAML_SCALAR_VALUE": (white3,),  # String Key / YAML
    "CSS.PROPERTY_NAME": (white3,),  # support.type.property-name
    "PY.SELF_PARAMETER": (red, None, I),  # variable.language
    "PY.BUILTIN_NAME": (blue, None, I),  # support.function
    "MARKDOWN_HEADER_LEVEL_1": (fg, None, B), "MARKDOWN_HEADER_LEVEL_2": (fg, None, B),
    "MARKDOWN_HEADER_LEVEL_3": (fg, None, B),
    "MATCHED_BRACE_ATTRIBUTES": (orange, None, 0, U, orange),  # brackets_options: underline
    "SEARCH_RESULT_ATTRIBUTES": (grey, orange3),  # find_highlight
    "TEXT_SEARCH_RESULT_ATTRIBUTES": (grey, orange3),
    "IDENTIFIER_UNDER_CARET_ATTRIBUTES": (None, None, 0, BOX, blue4),  # selection_border
    "WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES": (None, None, 0, BOX, orange2),
    "TYPO": (None, None, 0, WAVE, red),  # misspelling
    "DEPRECATED_ATTRIBUTES": (white2, orange2),  # invalid.deprecated
    "DIFF_INSERTED": (None, over(hsl(180, 45, 60, 0.15), bg)), "DIFF_DELETED": (None, over(hsl(357, 45, 60, 0.15), bg)),
    "DIFF_MODIFIED": (None, over(orange + (0,), bg, keep=85)),
}
EFFECT = {BOX: 0, U: 1, WAVE: 2}

out = ['<scheme name="Sublime Mariana" version="142" parent_scheme="Darcula">',
       '  <option name="EDITOR_FONT_SIZE" value="13"/>', '  <option name="EDITOR_FONT_NAME" value="Hack Nerd Font"/>',
       '  <colors>']
out += [f'    <option name="{k}" value="{hx(v)}"/>' for k, v in colors.items()]
out += ['  </colors>', '  <attributes>']
for k, v in attrs.items():
    f, b, ft, eff, ec = (v + (None,) * 5)[:5]
    out.append(f'    <option name="{k}">\n      <value>')
    if f: out.append(f'        <option name="FOREGROUND" value="{hx(f)}"/>')
    if b: out.append(f'        <option name="BACKGROUND" value="{hx(b)}"/>')
    if ft: out.append(f'        <option name="FONT_TYPE" value="{ft}"/>')
    if eff:
        out.append(f'        <option name="EFFECT_COLOR" value="{hx(ec)}"/>')
        out.append(f'        <option name="EFFECT_TYPE" value="{EFFECT[eff]}"/>')
    out.append('      </value>\n    </option>')
out += ['  </attributes>', '</scheme>', '']

base = lambda l: hsl(215, 10, l)
ui_bg, sidebar_bg, row_sel, button_bg = base(20), base(15), base(25), base(30)
text_fg, sidebar_label, link = hsl(0, 0, 85), hsl(0, 0, 80), hsl(215, 45, 65)
tabset_bg = over(white, bg, keep=80)
tab_label = hsl(0, 0, 60)
border = base(12)  

p = lambda c: "#" + hx(c)
theme = {
    "name": "Sublime Mariana", "dark": True, "author": "Luis Martins", "editorScheme": "/Mariana.xml",
    "ui": {
        "*": {
            "background": p(ui_bg), "foreground": p(text_fg), "infoForeground": p(tab_label),
            "disabledForeground": p(hsl(0, 0, 50)),
            "selectionBackground": p(row_sel), "selectionForeground": p(hsl(0, 0, 90)),
            "selectionInactiveBackground": p(row_sel), "selectionBackgroundInactive": p(row_sel),
            "hoverBackground": p(base(22)), "borderColor": p(border), "separatorColor": p(border),
            "focusColor": p(blue_vibrant), "focusedBorderColor": p(blue_vibrant), "inactiveBackground": p(ui_bg),
        },
        "Editor.background": p(bg), "EditorPane.background": p(bg),
        "Tree.background": p(sidebar_bg), "Tree.foreground": p(sidebar_label),
        "ToolWindow.background": p(sidebar_bg), "ToolWindow.Header.background": p(sidebar_bg),
        "ToolWindow.Header.inactiveBackground": p(sidebar_bg),
        "Panel.background": p(ui_bg), "MainToolbar.background": p(ui_bg), "MainToolbar.inactiveBackground": p(ui_bg),
        "MainWindow.background": p(ui_bg), "StatusBar.background": p(ui_bg), "StatusBar.borderColor": p(border),
        "Popup.background": p(ui_bg), "List.background": p(ui_bg),
        "List.selectionBackground": p(base(30)),  # quick_panel_selected_row_bg
        "EditorTabs.background": p(tabset_bg), "EditorTabs.underlinedTabBackground": p(bg),
        "EditorTabs.underlineColor": p(bg), "EditorTabs.inactiveUnderlineColor": p(bg), "EditorTabs.underlineHeight": 0,
        "EditorTabs.hoverBackground": p(over(white, tabset_bg, keep=93)),  # white a(0.07)
        "EditorTabs.foreground": p(tab_label), "EditorTabs.selectedForeground": p(text_fg),
        "Button.background": p(button_bg), "Button.startBackground": p(button_bg), "Button.endBackground": p(button_bg),
        "Button.default.startBackground": p(base(50)), "Button.default.endBackground": p(base(50)),  # dialog_button_bg
        "Link.activeForeground": p(link), "Link.hoverForeground": p(link),
        "ProgressBar.progressColor": p(base(40)), "ProgressBar.indeterminateStartColor": p(base(40)),
        "ProgressBar.indeterminateEndColor": p(base(30)),
    },
}

root = pathlib.Path(__file__).parent / "src"
(root / "Mariana.xml").write_text("\n".join(out))
(root / "Mariana.theme.json").write_text(json.dumps(theme, indent=2) + "\n")

assert hx(bg) == "303841" and hx(fg) == "d8dee9" and hx(blue5) == "5fb4b4" and hx(green) == "99c794", hx(bg)
