def calculer_moyenne_unite(composantes):
    """Calcule la moyenne d'une matière à partir de ses composantes."""
    if not composantes:
        return 0.0
    total = sum(comp["note"] for comp in composantes)
    return round(total / len(composantes), 2)

def calculer_moyenne_generale(matières):
    """Calcule la moyenne générale de l'élève."""
    total_points = 0
    total_coefs = 0
    details = []
    
    for matiere in matières:
        moy_unite = calculer_moyenne_unite(matiere["composantes"])
        coef = matiere["coefficient_unite"]
        
        total_points += moy_unite * coef
        total_coefs += coef
        
        details.append({"matiere": matiere["nom"], "moyenne": moy_unite})
        
    if total_coefs == 0:
        return 0.0, []
        
    return round(total_points / total_coefs, 2), details
