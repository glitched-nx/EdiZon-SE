import os
import subprocess

def update_gitmodules_url(account_name="glitched-nx"):
    """
    Aktualisiert die URL-Einträge in der .gitmodules-Datei, um den GitHub-Account-Namen anzupassen.
    Der Repository-Name und andere Einstellungen bleiben unverändert.
    """
    gitmodules_path = ".gitmodules"

    if not os.path.exists(gitmodules_path):
        print(f"{gitmodules_path} file not found.")
        return

    with open(gitmodules_path, "r") as file:
        content = file.readlines()

    updated_content = []
    for line in content:
        if line.strip().startswith("url ="):
            # Die alte URL durch die neue mit dem 'glitched-nx'-Account ersetzen
            parts = line.split('/')
            if len(parts) > 3:  # Sicherstellen, dass die URL gut strukturiert ist
                parts[3] = account_name
                new_url = '/'.join(parts)
                updated_content.append(new_url)
            else:
                updated_content.append(line)
        else:
            updated_content.append(line)

    with open(gitmodules_path, "w") as file:
        file.writelines(updated_content)

    print(f"Updated URLs in {gitmodules_path} with GitHub account: {account_name}")


def ensure_master_branch_in_gitmodules():
    """
    Überprüft die Datei '.gitmodules', um sicherzustellen, dass jedes Submodul auf den Master-Branch zeigt.
    Falls nicht, wird 'branch = master' direkt unter der URL eingefügt.
    """
    gitmodules_path = ".gitmodules"

    if not os.path.exists(gitmodules_path):
        print(f"{gitmodules_path} file not found.")
        return

    with open(gitmodules_path, "r") as file:
        content = file.readlines()

    updated_content = []
    for i, line in enumerate(content):
        updated_content.append(line)
        if line.strip().startswith("url =") and (i + 1 >= len(content) or not content[i + 1].strip().startswith("branch =")):
            updated_content.append("	branch = master\n")

    with open(gitmodules_path, "w") as file:
        file.writelines(updated_content)

    print("Ensured all submodules are set to 'master' branch in .gitmodules.")

def update_submodules():
    """
    Aktualisiert alle Submodule des aktuellen Git-Repositories auf den neuesten Commit des Master-Branches
    und committet die Änderungen.
    """
    print("Updating all submodules to the latest commit on their respective branches...")
    subprocess.run(['git', 'submodule', 'update', '--init', '--remote', '--recursive'], check=True)

    print("Adding updated submodules to the staging area...")
    subprocess.run(['git', 'add', '.'], check=True)

    commit_message = "Updated all submodules to the latest commits"
    print(f"Committing changes with message: '{commit_message}'")
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

    print("Submodule status after update:")
    subprocess.run(['git', 'submodule', 'status'], check=True)


if __name__ == "__main__":
    # Aktualisieren der Submodule-URLs in .gitmodules
    update_gitmodules_url(account_name="glitched-nx")
    
    # Sicherstellen, dass Submodule auf den Master-Branch zeigen
    ensure_master_branch_in_gitmodules()
    
    # Submodule aktualisieren und commiten
    update_submodules()

    print("All submodules updated to the latest master commits successfully.")
