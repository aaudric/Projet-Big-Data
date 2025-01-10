# Projet Big Data : Analyse des ventes avec PySpark

## Description
Ce projet explore et analyse des données de ventes provenant de Kaggle pour identifier des tendances, améliorer les stratégies de stock, et comprendre les facteurs influençant les revenus. L'objectif inclut l'utilisation de **PySpark** pour traiter efficacement de grands volumes de données, analyser les performances produits, et mettre en œuvre des flux en temps réel.

---

## Fonctionnalités clés
1. **Nettoyage et préparation des données :**
   - Filtrage des transactions improbables.
   - Transformation des données pour garantir leur qualité.

2. **Analyse descriptive :**
   - Identification des produits les plus vendus et rentables.
   - Étude des tendances mensuelles des ventes.
   - Analyse des performances produits par ville.

3. **Analyses avancées :**
   - Matrices de corrélation pour comprendre les relations entre variables.
   - Tests statistiques comme le **Chi-deux** pour valider l'indépendance entre les variables.

4. **Machine Learning :**
   - Clustering (KMeans) pour regrouper les produits en segments.
   - Réduction de dimension avec l'Analyse en Composantes Principales (ACP).

5. **Flux en temps réel :**
   - Mise en place de **PySpark Streaming** pour analyser les données au fil de leur arrivée.

---

## Installation

### Prérequis
- Python 3.7 ou supérieur
- PySpark 3.x
- Librairies Python :
  - pandas
  - matplotlib
  - seaborn
  - plotly
  - scipy
  - statsmodels

### Étapes
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/aaudric/Projet-Big-Data.git
   ```
2. Installez les dépendances :
   ```bash
   pip install pyspark pandas matplotlib seaborn plotly scipy statsmodels
    ```

---
## Visualisations

1. Tendance des ventes mensuelles

    - Graphique des revenus mensuels, mettant en évidence les pics de ventes.

2. Performance des produits par ville

    -Barplot comparant les 5 produits les plus rentables dans différentes localités.

3. Clustering des produits

    - Scatterplot interactif montrant la segmentation des produits en clusters.