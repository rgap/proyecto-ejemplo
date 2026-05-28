import csv
import subprocess
import tempfile
from pathlib import Path

OWNER = "rgap"
REPO = "proyecto-ejemplo"

def make_checklist(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(f"- [ ] {line}" for line in lines)


def build_body(row):
    return f"""## Historia de usuario

Como {row["rol"]},
quiero {row["quiero"]},
para {row["para"]}.

## Criterios de aceptación

{make_checklist(row["criterios_aceptacion"])}

## Tareas técnicas

{make_checklist(row["tareas_tecnicas"])}
"""


with open("user_stories.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["titulo"].strip()
        body = build_body(row)

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".md",
            delete=False,
            encoding="utf-8"
        ) as temp_file:
            temp_file.write(body)
            body_file_path = temp_file.name

        print(f"Creando issue: {title}")

        subprocess.run(
            [
                "gh",
                "issue",
                "create",
                "--repo",
                f"{OWNER}/{REPO}",
                "--title",
                title,
                "--body-file",
                body_file_path,
            ],
            check=True
        )

        Path(body_file_path).unlink()