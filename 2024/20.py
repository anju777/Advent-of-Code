e = """
broadcaster -> a, b, c
$a -> b
$b -> c
$c -> inv
&inv -> a
"""

e2 = """
broadcaster -> a
$a -> inv, con
&inv -> b
$b -> con
&con -> output
"""