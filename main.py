# Exam grade calculator

print(" ---- Exam grade calculator ----")
t = input("""
\033[33mWhat's the name of the test? \033[0m
""")
print()
maxs = float(input("""
\033[33mWhat's the maximum score you could receive? \033[0m
"""))
print()
s = float(input("""
\033[33mHow many points you received? \033[0m
"""))
print()

per = s * 100 / maxs
per = round(per, 2)
if per <= 49:
  g = "U"
elif per >= 50 and per < 60:
  g = "D"
elif per >= 60 and per < 70:
  g = "C"
elif per >= 70 and per < 80:
  g = "B"
elif per >= 80 and per < 90:
  g = "A-"
elif per >= 90 and per <= 100:
  g = "A+"

print(
  """\033[33m
Name of exam:\033[0m""",t,"""
\033[33m
Max. possible score:\033[0m""",maxs,"""
\033[33m
Your score:\033[0m""",s,"""
\033[33m
You got:\033[0m""",per,"""\033[33m% which is a\033[0m""",g,"""
  \033[33m.\033[0m"""
)
