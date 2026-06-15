---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=fr
fetched_at: 2026-06-15T06:18:57.730495+00:00
title: "Facturation \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Facturation

Ce guide présente les différentes options de facturation de l'API Gemini. Il explique comment activer la facturation et surveiller l'utilisation, et répond aux questions fréquentes sur la facturation.

## À propos de la facturation et des niveaux

La facturation de l'API Gemini dépend de votre historique de paiements.

| Niveau d'utilisation | Qualification | [Plafond du niveau de facturation](#spend-caps) |
| --- | --- | --- |
| **Free** | [Projet actif](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) ou essai sans frais | N/A |
| **Niveau 1** | [Configurer et associer un compte de facturation actif](#setup-billing) | 250 $ |
| **Niveau 2** | Paiement de 100 $ effectué trois jours après le premier paiement réussi | 2 000 $ |
| **Niveau 3** | 1 000 $ payés + 30 jours à compter du premier paiement réussi | 20 000 $ - 100 000 $ et plus |

Les nouveaux comptes commencent avec le niveau sans frais, qui permet d'accéder à [certains modèles](https://ai.google.dev/gemini-api/docs/pricing?hl=fr) dans l'API Gemini et AI Studio, dans la limite des [limites de débit](https://aistudio.google.com/rate-limit?hl=fr) du niveau sans frais des modèles.

Pour déployer vos applications directement depuis le mode Création, vous pouvez utiliser le **niveau Starter de Google Cloud**. Ce niveau vous permet de publier jusqu'à deux applications Full Stack sans configurer de projet Google Cloud ni de compte de facturation.
Pour en savoir plus, consultez [Déployer à partir de Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=fr) et la [documentation sur le niveau Starter de Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=fr).

Pour accéder à des limites de taux plus élevées, utiliser des modèles avancés et vous assurer que vos requêtes et vos réponses **ne sont pas** utilisées pour améliorer les produits Google\*, vous pouvez [associer un compte de facturation](#setup-billing) et [prépayer](#prepay) pour passer aux niveaux payants.
Vous passerez ensuite aux niveaux supérieurs en fonction de vos dépenses cumulées et de l'ancienneté de votre compte. Au niveau 3, vous pouvez peut-être passer à la facturation [postpay](#postpay).

Les niveaux, les limites de débit et les plafonds des comptes de facturation sont tous déterminés au niveau du [compte de facturation](#cloud-billing).

\* *Confidentialité des données de niveau Enterprise : pour en savoir plus sur l'utilisation des données pour les services payants, consultez les [Conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr#data-use-paid).*

## Configurer la facturation pour accéder au forfait payant

Pour passer au niveau payant dans [Google AI Studio](https://aistudio.google.com/projects?hl=fr), vous pouvez créer un projet et configurer la facturation, ou importer un projet existant.
Pour passer du niveau sans frais à la version payante, vous devez associer un compte de facturation et [prépayer](#prepay) au moins 10 $ (ou l'équivalent dans d'autres devises) de crédits à votre compte.

1. Accédez à la page [Clés API](https://aistudio.google.com/api-keys?hl=fr) ou [Projets](https://aistudio.google.com/projects?hl=fr) d'AI Studio, ou à tout autre endroit où le bouton **Configurer la facturation** s'affiche dans AI Studio.
   - Par défaut, un [projet et une clé API](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) sont créés pour les nouveaux utilisateurs.
   - Si vous avez besoin d'une nouvelle clé, cliquez sur [**Créer une clé API**](https://aistudio.google.com/api-keys?hl=fr) et suivez les instructions de la boîte de dialogue pour ajouter une paire clé/projet au tableau.
2. Recherchez le projet de niveau sans frais que vous souhaitez passer au niveau payant, puis cliquez sur **Configurer la facturation** sous la colonne *Niveau de facturation*.
3. Si vous n'avez jamais configuré de compte de facturation Google :
   - Vous serez invité à sélectionner votre pays pour accepter les conditions d'utilisation.
   - Ensuite, saisissez ou confirmez vos coordonnées et votre mode de paiement pour continuer.
4. Si vous avez déjà configuré des comptes de facturation Google :
   - Vous serez invité à choisir l'un de vos comptes de facturation existants.
   - Si vous ne souhaitez pas utiliser l'un de vos comptes existants, cliquez sur **Ajouter un compte de facturation**, puis saisissez ou confirmez vos coordonnées et votre mode de paiement pour continuer.
5. Ensuite, vous serez :
   - Il vous est demandé de prépayer un minimum de 10 $ pour terminer la configuration de la facturation (ce qui signifie que votre compte est automatiquement attribué au forfait de facturation [Prépaiement](#prepay)).
   - Vous avez le choix entre les forfaits de facturation [Prépaiement](#prepay) et [Post-paiement](#postpay) pour votre compte.
   - Vous êtes attribué à un forfait de facturation [postpayé](#postpay) pour une période intermédiaire jusqu'à ce que le nouveau système prépayé soit déployé pour tous les utilisateurs (à partir du 23 mars 2026).
6. Une fois le prépaiement effectué ou le postpaiement sélectionné, la configuration de votre compte est terminée.

### Passer au niveau payant supérieur

Si vous disposez déjà d'un forfait payant et que vous remplissez les [critères](#about-billing) pour changer de forfait, vous passerez automatiquement au forfait supérieur (sous réserve des [délais de traitement](#processing-times)).

## Vérifier l'état de facturation

Une fois que vous avez [associé un compte de facturation](#setup-billing) à votre projet, vous pouvez surveiller son état sur la [page de facturation AI Studio](https://aistudio.google.com/billing?hl=fr). Contrairement au niveau sans frais, l'état du niveau payant est dynamique. Bien que votre niveau d'utilisation soit déterminé par l'historique de votre compte, l'API Gemini ne traitera les requêtes que si vous disposez d'un solde de crédit [prépayé](#prepay) positif.

Sur la page [Projets](https://aistudio.google.com/projects?hl=fr), vous pouvez consulter le niveau et le forfait de facturation de votre projet dans la colonne *Niveau de facturation*. Toutes les actions liées à l'état de facturation que vous devrez peut-être effectuer pour un projet s'affichent dans les colonnes *Niveau de facturation* ou *État* :

- ***Configurer la facturation*** : si aucun compte de facturation n'est associé au projet.
- ***Configurer le prépaiement*** : si un compte de facturation est associé au projet, mais qu'il doit utiliser un forfait [avec prépaiement](#prepay) qui doit être configuré.
- "***Aucun crédit***" si le compte de facturation est requis pour acheter des crédits, mais que le compte de paiement prépayé n'est pas configuré ou que le solde de crédit disponible est épuisé.

Cliquez sur l'un des messages pour effectuer les actions nécessaires.

## Surveiller l'utilisation

Vous pouvez surveiller votre utilisation de l'API Gemini dans [Google AI Studio](https://aistudio.google.com/usage?hl=fr), en accédant à **Tableau de bord** > **Utilisation**.

## Forfaits

Les forfaits de facturation pour l'API Gemini et AI Studio se répartissent en deux catégories qui déterminent le moment où vous payez votre utilisation : prépaiement et post-paiement. Vous pouvez consulter votre forfait de facturation attribué et gérer vos modes de paiement sur la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr).

### Prépaiement

Dans le forfait de facturation avec prépaiement, vous achetez des crédits qui sont ajoutés à votre solde de prépaiement avant d'utiliser l'API Gemini. Les coûts d'utilisation de l'API sont déduits de votre solde de crédits de prépaiement [en temps quasi réel](#processing-times).
Vous pouvez effectuer un prépaiement en [ajoutant du crédit](#buy-credits) à votre compte ou en configurant la [recharge automatique](#auto-reload). Une fois les crédits achetés, ceux qui ne sont pas utilisés expirent au bout de 12 mois et ne sont [pas remboursables](#refunds), sauf après [être passé à un compte postpayé](#postpay).

Lorsque le solde de vos crédits prépayés sur le compte de facturation atteint 0 $, toutes les clés API de tous les projets associés à ce compte de facturation cessent de fonctionner simultanément. Les crédits prépayés ne s'appliquent qu'aux coûts d'utilisation de l'API Gemini. Vous ne pouvez pas les utiliser pour payer d'autres services Google Cloud.

Par défaut, les nouveaux utilisateurs sont associés au forfait avec prépaiement. Les projets antérieurs à l'introduction des forfaits avec prépaiement et post-paiement peuvent nécessiter la [mise à jour des informations de facturation du projet](#verify-billing) avant de pouvoir continuer à utiliser l'API Gemini.

*Notez que le prépaiement n'est pas disponible pour les comptes [avec paiement sur facture (ou hors connexion)](https://docs.cloud.google.com/billing/docs/concepts?hl=fr#billing_account_types).*

#### Acheter des crédits

Vous pouvez acheter manuellement des crédits avant d'utiliser l'API Gemini pour les ajouter au solde créditeur de votre compte avec prépaiement.

Pour acheter des crédits, accédez à la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr) et sélectionnez **Acheter des crédits**.
Le montant d'achat minimal est de 10 $. Le montant maximal des crédits que vous pouvez prépayer est de 5 000 $.

#### Actualisation automatique

Le rechargement automatique est une fonctionnalité facultative qui recharge automatiquement votre solde de crédit prépayé lorsqu'il est faible. Cela permet d'éviter les interruptions de service.

Vous pouvez configurer la recharge automatique et consulter son état dans la fiche *Crédits disponibles* de la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr). Cliquez sur **Configurer la recharge automatique** ou **Gérer la recharge automatique** pour définir votre mode de paiement, le montant de la recharge et le solde minimum qui déclenche un paiement de recharge.

#### Limite de recharge automatique mensuelle

La limite de recharge automatique mensuelle est disponible pour les utilisateurs du prépaiement. Elle permet d'éviter les coûts inattendus liés aux recharges automatiques fréquentes. Utilisez cette fonctionnalité pour définir une limite maximale pour les recharges automatiques au cours d'un même cycle de facturation. Une fois que le montant total des recharges automatiques au cours d'un cycle de facturation atteint cette limite, le système désactive la recharge automatique jusqu'au début du mois suivant. Les paiements ponctuels que vous initiez manuellement ne sont pas pris en compte dans cette limite.

Pour définir la limite de recharge automatique mensuelle lorsque la recharge automatique est activée :

1. Accédez à la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr).
2. Cliquez sur **Gérer la recharge automatique**.
3. Développez la section **Limite mensuelle** et saisissez la limite mensuelle maximale pour les recharges automatiques.
4. Cliquez sur **Enregistrer**.

### Post-paiement

Dans le forfait de facturation postpayé, votre compte de facturation Cloud génère des coûts et vous êtes automatiquement facturé à la fin du mois ou lorsque vos coûts atteignent un [plafond de dépenses automatiquement attribué](#tier-spend-caps) en fonction du niveau de votre compte.
Le paiement est débité du mode de paiement associé à votre compte de paiement post-paiement, que vous pouvez gérer sur la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr).

Lorsque vous remplissez les [critères du niveau 3](#about-billing), vous pouvez passer manuellement du forfait prépayé au forfait postpayé. Pour changer de forfait, vous devrez cliquer sur le bouton **Passer au post-paiement** qui s'affiche en haut à droite de la page [Facturation AI Studio](https://aistudio.google.com/billing?hl=fr) lorsque votre compte devient éligible.

Sur la page **Facturation**, vous pourrez ensuite consulter votre solde, les échéances et les paiements précédents, mais aussi effectuer des paiements et gérer vos modes de paiement.

Lorsque vous [configurez la facturation](#setup-billing) pour un nouveau projet, si vous êtes éligible au post-paiement, vous pouvez choisir entre le prépaiement et le post-paiement dans la boîte de dialogue [Configuration de la facturation](#setup-billing).

Une fois que vous avez modifié un compte de facturation Cloud pour utiliser le forfait de facturation postpayé, tous les projets associés à ce compte de facturation sont basculés vers le forfait postpayé. Vous ne pouvez pas rétablir le forfait de facturation prépayé pour ce compte de facturation. Vous pouvez déplacer un projet vers un compte de facturation avec un forfait de facturation différent pour modifier le cycle de facturation de ce projet. Pour en savoir plus, consultez la documentation Cloud sur la [gestion de la facturation des projets](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr).

Pour en savoir plus sur le cycle de facturation postpayé, consultez le [guide Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=fr).

## Plafonds de dépenses

L'API Gemini est compatible avec les plafonds de dépenses mensuels au niveau du compte de facturation et du projet. Ces contrôles sont conçus pour protéger votre compte contre les dépassements inattendus et l'écosystème pour assurer la disponibilité des services.

*Notez que les plafonds de dépenses ne sont pas disponibles pour les comptes [facturés (ou hors connexion)](https://docs.cloud.google.com/billing/docs/concepts?hl=fr#billing_account_types).*

### Plafonds de dépenses pour les projets

Vous pouvez définir vos propres [plafonds de dépenses au niveau du projet](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) dans AI Studio.
Cela peut être utile si vous avez plusieurs projets sous le même compte de facturation et que vous souhaitez vous assurer que chacun d'eux a accès à une part suffisante du plafond de dépenses cumulé.

Les comptes disposant des [rôles](https://docs.cloud.google.com/iam/docs/roles-overview?hl=fr) d'éditeur, de propriétaire ou d'administrateur de projet peuvent définir des limites de dépenses par projet dans AI Studio sur la page [Dépenses](https://aistudio.google.com/spend?hl=fr), sous **Limite de dépenses mensuelles** > **Modifier la limite de dépenses**.

Pour en savoir plus sur les autorisations Cloud IAM Google Cloud spécifiques requises pour afficher ou modifier les plafonds de dépenses et les informations de facturation dans AI Studio, consultez le [guide de dépannage AI Studio](https://ai.google.dev/gemini-api/docs/troubleshoot-ai-studio?hl=fr#iam-permissions).

Si vous [déplacez un projet vers un autre compte de facturation](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr#change_the_billing_account_for_a_project), tout plafond de dépenses que vous avez déjà défini pour ce projet sera conservé, mais toutes les dépenses cumulées seront réinitialisées à 0 € pour le nouveau cycle de facturation.

Les tâches de longue durée, comme les finalisations en [mode batch](https://ai.google.dev/gemini-api/docs/batch-api?hl=fr) et les sessions d'agent, peuvent entraîner des dépassements au-delà du plafond de dépenses de votre projet.

Le traitement des données de facturation peut être retardé dans AI Studio (jusqu'à environ 10 minutes). Vous pouvez dépasser le plafond de votre projet si les données de facturation n'ont pas été traitées avant que d'autres frais ne soient accumulés.

### Plafonds de dépenses des niveaux de compte de facturation

Chaque [niveau](#about-billing) est associé à une limite de dépenses mensuelles maximale :

| Niveau d'utilisation | Plafond de dépenses |
| --- | --- |
| **Free** | N/A |
| **Niveau 1** | 250 $ |
| **Niveau 2** | 2 000 $ |
| **Niveau 3** | Entre 20 000 € et 100 000 € |

Des limites d'utilisation mensuelles sont appliquées à l'API Gemini au niveau du [compte de facturation](#cloud-billing). Bien que des limites par défaut soient prédéfinies, vous pouvez [demander une augmentation](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=fr) pour faire face à une utilisation plus importante. Les dépenses totales sont agrégées pour tous les projets associés pour lesquels le service de l'API Gemini est activé. Une fois que le total cumulé du compte atteint la limite du niveau, le service est suspendu pour tous les projets associés à ce compte de facturation jusqu'au début du prochain cycle de facturation (le 1er de chaque mois).

#### Évaluer les dépenses de votre compte de facturation

Pour évaluer vos dépenses mensuelles historiques et déterminer si les nouveaux [plafonds de dépenses des comptes de facturation](#tier-spend-caps) auront un impact sur vos projets en cours, procédez comme suit :

1. Dans la console Google Cloud, accédez à la page [Rapports sur le compte de facturation Cloud](https://console.cloud.google.com/billing/reports?hl=fr).
   - Si vous disposez de plusieurs comptes de facturation, choisissez celui pour lequel vous souhaitez afficher des rapports sur les coûts lorsque vous y êtes invité.
2. Par défaut, le rapport est défini sur "Grouper par service" pour le mois en cours. Vous verrez **API Gemini** dans la colonne **Service** et les dépenses totales dans la colonne **Coût d'utilisation** du tableau.
3. Pour afficher des coûts précis limités à l'utilisation de l'API Gemini, définissez le filtre **Critère de regroupement** sur **SKU** et le filtre **Services** sur **API Gemini**.
4. Ajustez le filtre **Période par date d'utilisation** à la plage de dates souhaitée pour évaluer vos dépenses historiques au cours d'une période.

## Délais de traitement

Les signaux et les mises à jour de facturation ne sont pas toujours en temps réel.

- **Utilisation des crédits** : les coûts d'utilisation sont généralement débités de votre solde en quelques minutes.
- **Confirmation du paiement** : la plupart des paiements par carte sont instantanés, mais certains modes de paiement (comme les virements bancaires) peuvent prendre plusieurs jours à être traités. Les services ne sont réactivés ou mis à niveau qu'une fois l'achat de crédits officiellement confirmé.
- **Passage à un niveau supérieur** : une fois le paiement effectué ou lorsque vous remplissez les [critères de mise à niveau](#about-billing), le passage à un niveau supérieur est généralement effectif sous 10 minutes.
- **Graphiques de répartition du coût total** : les graphiques de répartition du coût total sur les pages [Facturation](https://aistudio.google.com/billing?hl=fr) et [Dépenses](https://aistudio.google.com/spend?hl=fr) peuvent mettre jusqu'à 24 heures à s'actualiser.

Consultez les guides Cloud Billing sur le [cycle de facturation](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=fr#delayed-billing) et les latences des [transactions](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=fr#missing-transactions) pour en savoir plus sur les éventuels retards de facturation.

## Remboursements

Les remboursements ne sont pas autorisés pour les comptes de facturation **prépayés**, sauf en cas de changement de type de compte.

**Lorsqu'un compte prépayé passe au type de compte postpayé** (après que vous avez rempli les [critères](#about-billing) et [mis à niveau manuellement](#postpay) votre compte), le compte prépayé est clôturé et tout crédit prépayé restant est automatiquement remboursé sur le mode de paiement enregistré.

Si vous [clôturez](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=fr#close-a-billing-account) votre compte prépayé pour une raison autre que le passage au postpayé, tous les crédits prépayés restants seront perdus.

Les crédits achetés expirent au bout d'un an. Une fois les crédits expirés, ils sont perdus et ne peuvent pas être récupérés.

Les comptes **post-paiement** sont soumis au [Règlement Google Cloud sur les remboursements](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=fr#request_a_refund).

## Comptes de facturation Cloud

L'API Gemini utilise des [comptes Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=fr) pour les services de facturation, que vous pouvez [configurer directement dans AI Studio](#setup-billing).
Vous pouvez utiliser AI Studio pour suivre vos dépenses, comprendre vos coûts et effectuer des paiements.

Les niveaux, les limites de débit et les plafonds de compte de facturation sont tous déterminés au niveau du compte de facturation.

### Projets et clés API

Tous les [projets](https://ai.google.dev/gemini-api/docs/api-key?hl=fr#google-cloud-projects) associés à un compte de facturation Cloud héritent du niveau d'utilisation, des limites de débit et des plafonds de compte associés. Si vous [modifiez le compte de facturation d'un projet](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr#change_the_billing_account_for_a_project), son niveau, et par conséquent ses limites de débit et ses plafonds de compte, passeront au niveau du nouveau compte de facturation.

Les dépenses cumulées (pour tous les produits Google Cloud) et l'ancienneté du compte pour tous les projets associés à un compte de facturation sont prises en compte pour les [critères d'éligibilité aux niveaux](#about-billing) de ce compte de facturation.

Vous pouvez [dissocier un projet](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr#disable_billing_for_a_project) de son compte de facturation pour revenir au forfait sans frais.

Les [clés API](https://ai.google.dev/gemini-api/docs/api-key?hl=fr) sont des identifiants générés dans un projet.
Ils ne disposent pas de paramètres de facturation indépendants. Ils héritent des limites de niveau et de l'état de facturation du projet. L'utilisation cumulée de toutes les clés d'un projet est prise en compte dans le plafond de dépenses de ce projet et dans les dépenses totales du compte de facturation.

## Questions fréquentes

Les sections suivantes répondent aux questions fréquentes.

### À quoi correspondent les frais qui me sont facturés ?

Les tarifs de l'API Gemini sont basés sur les éléments suivants :

- Nombre de jetons d'entrée
- Nombre de jetons de sortie
- Nombre de jetons mis en cache
- Durée de stockage des jetons mis en cache

Pour obtenir des informations sur la tarification, consultez la [page des tarifs](https://ai.google.dev/pricing?hl=fr).

### Où puis-je consulter mon quota ?

Vous pouvez consulter vos quotas et les limites du système dans [AI Studio](https://aistudio.google.com/usage?hl=fr).

### Comment passer à un niveau de limite de fréquence supérieur ou demander un quota plus important ?

Vous recevrez automatiquement un quota plus élevé lorsque votre compte atteindra les [conditions requises pour le niveau](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr#usage-tiers) suivant.

### Puis-je utiliser l'API Gemini sans frais dans l'EEE (y compris l'UE), au Royaume-Uni et en Suisse ?

Oui, nous proposons le niveau sans frais et le niveau payant dans [de nombreuses régions](https://ai.google.dev/gemini-api/docs/available-regions?hl=fr).

### Si je configure la facturation avec l'API Gemini, serai-je facturé pour mon utilisation de Google AI Studio ?

L'utilisation d'AI Studio reste sans frais, sauf si les utilisateurs associent une clé API payante pour accéder aux fonctionnalités payantes.
Une fois que vous avez associé une clé API payante à un projet payant dans AI Studio, l'utilisation d'AI Studio pour cette clé vous sera facturée. Vous pouvez passer d'un projet de niveau payant à un projet de niveau sans frais selon vos besoins en utilisant les clés API respectives associées à chaque type.

### Si je suis au niveau sans frais, comment passer à un niveau supérieur ?

Pour accéder aux niveaux supérieurs, vous devez configurer la facturation pour votre projet. Cliquez sur [**Configurer la facturation**](#setup-billing) dans Google AI Studio. Vous serez guidé pour sélectionner ou créer un compte de facturation Cloud. Si vous devez utiliser le modèle de facturation prépayé, la procédure **Configurer la facturation** vous guidera pour créer votre compte prépayé associé à votre compte de facturation Cloud.

### Puis-je utiliser 1 million de jetons dans le forfait sans frais ?

Le niveau sans frais de l'API Gemini varie en fonction du modèle sélectionné. Pour le moment, vous pouvez essayer la fenêtre de contexte d'un million de jetons de différentes manières :

- Dans Google AI Studio
- Avec des forfaits sans frais pour certains modèles
- Avec les forfaits postpayés

### Puis-je revenir au niveau sans frais après avoir opté pour un forfait supérieur (payant) ?

Pour passer au niveau sans frais, vous pouvez [désactiver la facturation](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr#disable_billing_for_a_project) sur chacun des projets que vous souhaitez rétrograder.

### Comment calculer le nombre de jetons que j'utilise ?

Utilisez la méthode [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=fr#count_tokens) pour compter le nombre de jetons. Pour en savoir plus sur les jetons, consultez le [guide sur les jetons](https://ai.google.dev/gemini-api/docs/tokens?hl=fr).

### Si je crée mon premier compte de facturation Cloud via AI Studio, bénéficierai-je toujours d'un essai sans frais de Google Cloud ?

Lorsque vous vous inscrivez à votre premier compte de facturation Cloud, votre [essai sans frais Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=fr#free-trial) commence et vous recevez un [crédit de bienvenue](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=fr#welcome-credits) de 300 $.
Toutefois, ces crédits ne peuvent pas être utilisés pour payer l'utilisation d'AI Studio. Vous pouvez utiliser le crédit de bienvenue pour payer d'autres services éligibles dans Google Cloud (notez qu'une fois ces crédits consommés ou expirés (sous 90 jours), tous les coûts d'utilisation supplémentaires sont automatiquement facturés selon le mode de paiement que vous avez défini).

### Puis-je utiliser mon crédit de bienvenue Google Cloud avec l'API Gemini ?

Non, le [crédit de bienvenue](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=fr#welcome-credits) ou le crédit d'essai sans frais Google Cloud ne peuvent pas être utilisés pour l'API Gemini ni AI Studio.

Si vous avez reçu un crédit de bienvenue Google Cloud avant de devenir inéligible, vous pouvez dépenser les crédits restants sur l'API Gemini et AI Studio jusqu'à leur expiration (au bout de 90 jours).

### L'essai sans frais de Google Cloud s'applique-t-il à l'utilisation de l'API Gemini ?

Non. À partir de mars 2026, les coûts d'utilisation de l'API Gemini seront spécifiquement exclus du programme d'[essai sans frais de Google Cloud pour bénéficier d'un crédit de 300 $](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=fr#free-trial).

### Comment les crédits Google Cloud fonctionnent-ils avec le prépaiement ?

Les utilisateurs du prépaiement doivent d'abord [acheter des crédits prépayés](#buy-credits) avant que des crédits Google Cloud éligibles puissent être appliqués à l'utilisation de l'API Gemini. Une fois que vous disposez d'un solde de crédits prépayés actif, les crédits Google Cloud éligibles à l'API Gemini sont utilisés avant votre solde de crédits prépayés. Lorsque le solde de crédits prépayés de votre compte de facturation atteint zéro, les crédits Google Cloud ne sont plus utilisés.

Tous les crédits Google Cloud, comme le [crédit de bienvenue Google Cloud](#cloud-credits), ne peuvent pas être utilisés avec l'API Gemini et AI Studio.

### Comment la facturation est-elle gérée ?

La facturation de l'API Gemini est gérée par le système [Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=fr). Pour en savoir plus sur la configuration de la facturation Cloud dans le produit, consultez la [documentation Cloud Billing](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=fr).

### Des frais me sont-ils facturés pour les requêtes ayant échoué ?

Si votre requête échoue et renvoie une erreur 400 ou 500, les jetons utilisés ne vous seront pas facturés. Toutefois, la requête sera quand même décomptée de votre quota.

### `GetTokens` est-il facturé ?

Les requêtes envoyées à l'API `GetTokens` ne sont pas facturées et ne sont pas comptabilisées dans le quota d'inférence.

### Comment mes données Google AI Studio sont-elles traitées si je possède un compte API payant ?

Consultez les [Conditions d'utilisation](https://ai.google.dev/gemini-api/terms?hl=fr#paid-services) pour en savoir plus sur le traitement des données lorsque la facturation Cloud est activée (voir "Comment Google utilise vos données" sous "Services payants"). Notez que vos requêtes Google AI Studio sont traitées selon les mêmes conditions des "Services payants" tant qu'au moins un projet d'API a activé la facturation. Vous pouvez le vérifier sur la [page des clés API Gemini](https://aistudio.google.com/api-keys?hl=fr) si vous voyez des projets marqués comme "Payant" sous "Forfait".

### Qu'est-ce que la facturation prépayée et qui doit l'utiliser ?

La facturation prépayée permet aux utilisateurs de l'API Gemini dans AI Studio de préacheter des crédits.
À partir du 23 mars 2026, les nouveaux utilisateurs d'AI Studio devront peut-être souscrire un forfait prépayé. Lors de la procédure de [configuration de la facturation](#setup-billing) dans AI Studio, l'interface utilisateur vous guidera tout au long de la procédure de configuration de la facturation et vous indiquera si vous devez effectuer un prépaiement.

### Comment acheter des crédits prépayés ? Y a-t-il un montant minimal ou maximal ?

Vous pouvez [acheter des crédits](#buy-credits) sur la page de facturation d'AI Studio. Lors du processus d'achat, l'UI indique le montant minimal de prépaiement requis pour votre région et votre niveau, ainsi que le montant maximal qui peut être présent dans votre compte à un moment donné.

### Puis-je configurer mon compte prépayé pour qu'il achète automatiquement des crédits supplémentaires si nécessaire ?

Oui, nous vous recommandons de configurer le [rechargement automatique](#auto-reload) dans les paramètres de facturation d'AI Studio. Vous spécifiez un solde de crédits "déclencheur" (par exemple, "lorsque mon solde descend en dessous de 30 $") et une "valeur de recharge" (par exemple, "ajouter 100 $").

### Puis-je limiter le montant des recharges automatiques ?

Oui, les utilisateurs du prépaiement peuvent définir une [limite de recharge automatique mensuelle](#monthly-auto-charge-limit) dans le widget **Recharge automatique**. Lorsque le montant total des recharges automatiques au cours d'un cycle de facturation atteint cette limite, le système désactive la recharge automatique jusqu'au mois suivant. Les achats manuels de crédits ne sont pas pris en compte dans cette limite.

### Puis-je me faire rembourser mes crédits inutilisés ?

Tous les crédits prépayés pour les API expirent au bout d'un an et ne peuvent pas être remboursés. Consultez les [conditions de remboursement pour les comptes prépayés](#refunds).

### Mes crédits prépayés ont-ils une date d'expiration ?

Oui, les crédits expirent 12 mois après leur date d'achat.

### Que se passe-t-il lorsque le solde de mon crédit prépayé atteint zéro ?

Tous les services de l'API Gemini dans tous les projets payés par ce compte Cloud Billing avec prépaiement seront immédiatement arrêtés pour éviter d'entraîner des frais supplémentaires. Vos projets ne sont pas automatiquement rétrogradés au niveau sans frais.

Pour rétablir le service à votre niveau payant actuel, vous devez [acheter des crédits supplémentaires](#buy-credits). Une fois que vous avez acheté des crédits, vous devriez pouvoir utiliser l'API Gemini. Notez qu'il peut y avoir un [délai](#processing-times) avant que nos systèmes ne mettent à jour votre solde créditeur.

Si vous le souhaitez, vous pouvez [désactiver la facturation](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=fr#disable_billing_for_a_project) pour les projets que vous souhaitez rétrograder vers le niveau sans frais.

### Pourquoi mon utilisation a-t-elle cessé alors que mon solde de crédit prépayé est supérieur à 0 € ?

Vous avez peut-être atteint la [limite d'utilisation](#tier-spend-caps) de votre forfait actuel.
Les limites d'utilisation augmentent automatiquement lorsque vous passez à un niveau supérieur. L'état de votre [compte de facturation Cloud](#missed-payment) peut également avoir un impact sur votre utilisation de l'API Gemini dans AI Studio.

### Pourquoi le solde de mon compte prépayé est-il négatif ?

En raison de la complexité de nos systèmes de facturation et de traitement, il peut y avoir des [retards](#processing-times) dans notre capacité à interrompre l'utilisation une fois que vous avez consommé tous vos crédits. Cette utilisation excédentaire peut apparaître sous la forme d'un solde créditeur négatif dans le tableau de bord de facturation AI Studio. Dans ce cas, votre service est suspendu et votre solde négatif sera déduit de votre prochain achat de crédit.

Pour éviter toute interruption de votre service d'API Gemini, nous vous recommandons de configurer le [rechargement automatique](#auto-reload) afin d'acheter automatiquement des crédits lorsque votre solde de crédits tombe en dessous d'une valeur que vous spécifiez.

### Puis-je utiliser mes crédits prépayés pour d'autres services Google Cloud, comme Gemini Enterprise Agent Platform ?

Non, les crédits prépayés sont strictement réservés à l'utilisation de l'API Gemini. Tous les autres services Google Cloud que vous utilisez (Compute, Storage, Gemini Enterprise Agent Platform) sont facturés selon le [cycle de facturation Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=fr) standard.

### Puis-je passer à un forfait avec post-paiement ?

Lorsque vous avez un historique de paiements et que vous [atteignez un niveau éligible](#about-billing) au forfait de facturation postpayé, vous pouvez choisir de transférer tous vos futurs coûts d'utilisation de l'API Gemini vers un [cycle de facturation postpayé](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=fr#view-your-charging-cycle) Google Cloud standard et consolidé.

### Qu'advient-il de mes crédits prépayés si je passe à un forfait postpayé ?

Lorsque vous passez à [Postpay](#postpay), Cloud Billing clôture votre compte de paiement prépayé, désactive le [rechargement automatique](#auto-reload) et vous rembourse automatiquement les crédits prépayés non utilisés (sous réserve du délai de traitement standard des remboursements).

### Où puis-je consulter mon solde de crédit prépayé actuel et l'historique de mes transactions ?

Toute gestion du solde et de l'historique des transactions pour l'API Gemini doit être effectuée directement dans l'onglet "Facturation" de Google AI Studio.

### Pourquoi le message "Le type de compte de facturation est inactif ou incompatible" s'affiche-t-il ?

Les interactions liées aux paiements sur la [page de facturation AI Studio](https://aistudio.google.com/billing?hl=fr) peuvent être bloquées et remplacées par le message "Le type de compte de facturation est inactif ou non compatible" si le type ou l'état du compte de facturation que vous avez sélectionné ne sont pas éligibles au niveau payant d'AI Studio.

Consultez la [console Cloud](https://console.cloud.google.com/billing/?hl=fr) pour connaître l'état de votre compte de facturation. Un type de compte non éligible peut être un *compte d'essai sans frais*. Dans ce cas, vous pouvez [activer la facturation](#setup-billing) dans AI Studio pour devenir éligible. L'état inactif peut être *Fermé*. Dans ce cas, vous pouvez [rouvrir le compte](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=fr).

### Les coûts d'utilisation de l'API Gemini s'afficheront-ils dans la console Google Cloud ?

Oui, les coûts de l'API Gemini, ainsi que ceux associés à tous les autres services Google Cloud payés par votre compte de facturation Cloud, sont visibles sur les [pages de gestion des coûts](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=fr#cost-reports) de la [console Cloud Billing](https://console.cloud.google.com/billing?hl=fr). Notez que vous ne pouvez gérer votre solde de crédit prépayé que dans AI Studio.

### Pourquoi mon utilisation de l'API Gemini ne s'affiche-t-elle pas dans la console Cloud Billing, alors que je peux la voir dans la facturation AI Studio, ainsi que la consommation de mes crédits ?

Google Cloud et AI Studio transmettent les données d'utilisation à Cloud Billing à des intervalles variables. En raison de la complexité de nos systèmes de facturation et de traitement, vous pouvez constater un délai entre votre utilisation des services et la disponibilité des données d'utilisation et de coût dans Cloud Billing. Généralement, vos informations sur les coûts sont disponibles dans la journée, mais cela peut parfois prendre plus de 24 heures.
Pour en savoir plus sur la facturation différée, consultez la [documentation Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=fr#delayed-billing).

### Si j'utilise d'autres services Google Cloud dont les coûts sont soumis à un cycle de facturation post-paiement, que se passe-t-il si je manque un paiement ?

Si vous n'effectuez pas un paiement pour d'autres services Google Cloud, votre accès à l'API Gemini dans AI Studio peut être suspendu, **quel que soit le nombre de crédits prépayés dont vous disposez**. L'utilisation d'AI Studio est alimentée par un compte de facturation Google Cloud, qui peut partager à la fois la facturation prépayée pour AI Studio et la facturation postpayée pour d'autres services Cloud. Un problème lié à votre solde postpayé interrompt tous les services associés à ce compte. Votre utilisation de l'API Gemini sera suspendue si votre compte de facturation Cloud est signalé pour des problèmes tels que :

- Un solde impayé ou en retard
- Un paiement refusé
- Un mode de paiement non valide ou expiré

Pour rétablir le service, vous devez [résoudre le problème lié au compte post-paiement](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=fr#resolving-declined-payments) dans la console Google Cloud Billing. Une fois le problème résolu, vous retrouverez l'accès à vos crédits et services API Gemini prépayés.

### Où puis-je obtenir de l'aide pour la facturation ?

Pour obtenir de l'aide concernant la facturation, consultez [Obtenir de l'aide sur Cloud Billing](https://cloud.google.com/support/billing?hl=fr).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/06/10 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/06/10 (UTC)."],[],[]]
