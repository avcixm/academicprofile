publications = [
    {"title": "Generalized Volatility Models", "authors": "M. Avci", "year": 2025},
    {"title": "Variable Exponent Diffusions", "authors": "M. Avci, A. Smith", "year": 2024},
]

with open("publications.md", "w") as f:
    f.write("# 📄 Publications\n\n")
    for pub in publications:
        line = f"- **{pub['title']}** ({pub['year']}), *{pub['authors']}*\n"
        f.write(line)
