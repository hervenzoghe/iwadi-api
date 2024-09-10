from schemas import Parcours
from typing import List


def generateParcours(
        niveau_etude: str,
        specialite: str | None = None,
        matieres: str | None = None,
        metier: str | None = None,
        passions: str | None = None,
) -> List[Parcours | None]:
    """
    Function for generating a list of paths based on user request

    Args (Form): the entry request with user data

    Returns (JSON): a list of JSON objects withe the proposed paths
    """
    return [
        {
            "category": "Excellence",
            "formations": [
                {
                    "filiere": "Licence statistique",
                    "ecoles": [
                        "African School of Economics",
                        "Ecole Nationale d'Economie ",
                    ],
                    "domaine": "Statistiques & Economie",
                    "niveau": "Licence",
                }
            ],
        },
        {
            "category": "Ecole privée",
            "formations": [
                {
                    "filiere": "Licence statistique",
                    "ecoles": [
                        "African School of Economics",
                        "Ecole Nationale d'Economie ",
                    ],
                    "domaine": "Statistique & Economie",
                    "niveau": "Licence",
                }
            ],
        },
    ]
