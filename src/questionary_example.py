import questionary

language = questionary.select(
    "Choose a language",
    choices=["Python","TypeScript","Go","Rust"],
).ask()

print(f"Scaffolding a {language} project...")