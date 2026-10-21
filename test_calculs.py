from calculs import calculer_moyenne_generale

def test_bulletin_reel_marocain():
    # Les données exactes du bulletin de l'élève "Amina"
    matieres = [
        {"nom": "التربية الإسلامية", "coefficient_unite": 1, "composantes": [{"note": 9.0}]},
        {"nom": "اللغة العربية", "coefficient_unite": 1, "composantes": [
            {"note": 8.0}, {"note": 8.0}, {"note": 9.5}, {"note": 6.0}, {"note": 8.5}, {"note": 8.0}
        ]},
        {"nom": "اللغة الفرنسية", "coefficient_unite": 1, "composantes": [
            {"note": 8.0}, {"note": 7.0}, {"note": 6.75}, {"note": 7.0}
        ]},
        {"nom": "النشاط العلمي", "coefficient_unite": 1, "composantes": [{"note": 8.25}]},
        {"nom": "التربية الفنية", "coefficient_unite": 1, "composantes": [{"note": 8.5}]},
        {"nom": "الرياضيات", "coefficient_unite": 1, "composantes": [{"note": 9.75}]},
        {"nom": "التربية البدنية", "coefficient_unite": 1, "composantes": [{"note": 8.5}]}
    ]
    
    moyenne, details = calculer_moyenne_generale(matieres)
    
    # La moyenne du bulletin est 8.46
    assert moyenne == 8.46, f"Erreur : Attendu 8.46, obtenu {moyenne}"
    assert len(details) == 7, "Il doit y avoir 7 matières"
    
    print("✅ Le calcul est parfait ! Prêt pour le marché marocain.")
