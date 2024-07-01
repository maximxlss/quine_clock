import questionary


def escape_single_quotes(s):
    s = repr('"' + s)
    assert s[0] == s[-1] == "'"
    return s[2:-1]

rect_width = 100

rect_code = fr"'\\\n'.join([s[i:i+{rect_width}] for i in range(0, len(s), {rect_width})])"

with open("./code_to_execute.py") as f:
    source = f.read()

no_exec = questionary.select(
    "What type of quine to generate?",
    choices=["With exec (DRY and one-line)", s:="Without exec (repeats, but code is visible)"],
).ask() == s

do_rect = not no_exec and questionary.confirm("Transform into a rectangle?").ask()
    
if do_rect:
    source = f"s={rect_code}\n{source}"

if no_exec:
    quine = f"s=(s:='s=(s:={{}}).format(repr(s))\\n{escape_single_quotes(source)}').format(repr(s))\n{source}"
else:
    quine = fr"""exec(s:='s=f\'exec(s:={{repr(s)}})\'\n""\n{escape_single_quotes(source)}')"""

if do_rect:
    while True:
        for i in range(rect_width - 1, len(quine), rect_width):
            if quine[i] == "\\":
                quine = quine[:i] + " " + quine[i:]
                break
        else:
            break
    quine = eval(rect_code, {"s": quine})

with open("./quine.py", "w") as f:
    f.write(quine)




        
