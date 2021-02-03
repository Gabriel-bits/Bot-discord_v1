import json, os


def salvar_profil(Nome, ima1, ima2):
    perfil = {"nome":Nome, "not_speck":ima1, "speck":ima2}
    if not os.path.exists(f"{Nome}"):
        with open(f'{Nome}.json','w') as f:
            json.dump(perfil ,f)


def load_profi(nome ):

    with open(f"{nome}.json", "r") as f:
        p = json.load(f)
    return p