---
source_url: https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fr
fetched_at: 2026-05-18T13:09:56.383470+00:00
title: "Strat\u00e9gies de conception des invites \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Stratégies de conception des invites

La *conception de requêtes* est le processus de création de requêtes, ou demandes en langage naturel, qui permettent d'obtenir des réponses précises et de haute qualité à partir d'un modèle de langage.

Cette page présente des concepts, des stratégies et des bonnes pratiques de base pour vous aider à concevoir des requêtes afin de tirer le meilleur parti des modèles d'IA Gemini.

## Guides de requêtes spécifiques à un thème

Vous recherchez des stratégies de requête plus spécifiques ? Consultez nos autres guides sur les prompts :

- [Utiliser des fichiers multimédias dans les requêtes](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide)
- Requêtes pour la génération d'images avec [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=fr#imagen-prompt-guide) et [Gemini Native Image Generation](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#prompt-guide)
- [Requêtes pour la génération de vidéos](https://ai.google.dev/gemini-api/docs/video?hl=fr#prompt-guide)

Vous trouverez d'autres exemples de requêtes dans la [galerie de requêtes](https://ai.google.dev/gemini-api/prompts?hl=fr), qui vise à présenter de manière interactive de nombreux concepts abordés dans ce guide.

## Instructions claires et spécifiques

Pour personnaliser le comportement d'un modèle de manière efficace, fournissez-lui des instructions claires et spécifiques. Les instructions peuvent se présenter sous la forme d'une question, de tâches détaillées ou être aussi complexes que de définir l'expérience et l'état d'esprit d'un utilisateur.

### Entrée

L'entrée est le texte obligatoire de la requête pour laquelle le modèle doit fournir une réponse. Les entrées peuvent être des questions auxquelles le modèle répond (entrée de question), une tâche effectuée par le modèle (entrée de tâche), une entité sur laquelle le modèle travaille (entrée d'entité) ou une entrée partielle que le modèle doit terminer ou continuer (entrée de saisie semi-automatique).

| **Type d'entrée** | **Prompt** (Requête) | **Résultat généré** |
| --- | --- | --- |
| Question | ```     What's a good name for a flower shop that specializes in selling bouquets of     dried flowers? Create a list of 5 options with just the names. ``` | ```     Here are 5 names for a flower shop specializing in dried flowers:      1. Everlasting Blooms     2. Dried & Delightful     3. The Petal Preserve     4. Whispers of Wildflowers     5. Forever Blooms ``` |
| Tâche | ```     Give me a simple list of just the things that I must bring on a camping trip. The list should have 5 items. ``` | ```     1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries. ``` |
| Entité | ```     Classify the following items as [large, small]: Elephant Mouse Snail ``` | ``` Here's the classification:  * **Elephant:** Large * **Mouse:** Small * **Snail:** Small ``` |

#### Saisie semi-automatique partielle

Les modèles de langage génératif fonctionnent comme un outil de saisie semi-automatique avancé. Lorsque vous fournissez un contenu partiel, le modèle peut fournir le reste du contenu ou ce qu'il considère comme une suite de ce contenu en tant que réponse. Ainsi, si vous incluez des exemples ou du contexte, le modèle peut prendre en compte ces exemples ou éléments de contexte.

L'exemple suivant fournit une requête avec une instruction et une entrée d'entité :

|  |
| --- |
| **Requête :**    ``` For the given order, return a JSON object that has the fields cheeseburger, hamburger, fries, or drink, with the value being the quantity.  Order: A burger and a drink. ```  **Réponse:**    ``` {   "cheeseburger": 0,   "hamburger": 1,   "fries": 0,   "drink": 1 } ```  (gemini-2.5-flash) |

Bien que le modèle ait respecté l'invite, il peut parfois être difficile d'écrire les instructions en langage naturel et cela laisse une marge d'interprétation au modèle.
Par exemple, le menu d'un restaurant peut contenir de nombreux plats. Pour réduire la taille de la réponse JSON, vous souhaiterez probablement omettre les éléments qui n'ont pas été commandés. Dans ce cas, vous pouvez fournir un exemple et un préfixe de réponse, puis laisser le modèle le terminer :

|  |
| --- |
| **Requête :**    ``` Valid fields are cheeseburger, hamburger, fries, and drink. Order: Give me a cheeseburger and fries Output: ``` {   "cheeseburger": 1,   "fries": 1 } ``` Order: I want two burgers, a drink, and fries. Output: ```  **Réponse:**    ``` ``` {   "hamburger": 2,   "drink": 1,   "fries": 1 } ``` ```  (gemini-2.5-flash) |

Notez que le "cheeseburger" a été exclu du résultat, car il ne faisait pas partie de la commande.

Bien que vous puissiez spécifier le format des objets de réponse JSON simples à l'aide d'invites, nous vous recommandons d'utiliser la fonctionnalité [Sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr) de l'API Gemini lorsque vous spécifiez un schéma JSON plus complexe pour la réponse.

### Contraintes

Spécifiez les contraintes liées à la lecture du prompt ou à la génération d'une réponse. Vous pouvez indiquer au modèle ce qu'il doit faire et ne pas faire. Par exemple, vous pouvez spécifier une contrainte dans la requête concernant la durée d'un résumé :

|  |
| --- |
| **Requête :**     ``` Summarize this text in one sentence: Text: A quantum computer exploits quantum mechanical phenomena to perform calculations exponentially faster than any modern traditional computer. At very tiny scales, physical matter acts as both particles and as waves, and quantum computing uses specialized hardware to leverage this behavior. The operating principles of quantum devices is beyond the scope of classical physics. When deployed at scale, quantum computers could be used in a wide variety of applications such as: in cybersecurity to break existing encryption methods while helping researchers create new ones, in meteorology to develop better weather forecasting etc. However, the current state of the art quantum computers are still largely experimental and impractical. ```     **Réponse :**     ```       Exploiting quantum mechanical phenomena, quantum computers can perform calculations exponentially faster than traditional computers for potential applications like cybersecurity and meteorology, although they are currently largely experimental and impractical. ```  (gemini-2.5-flash) |

### Format de réponse

Vous pouvez donner des instructions qui spécifient le format de la réponse. Par exemple, vous pouvez demander que la réponse soit mise en forme sous forme de tableau, de liste à puces, d'argumentaire éclair, de mots clés, de phrase ou de paragraphe. L'instruction système suivante indique au modèle d'être plus conversationnel dans sa réponse :

|  |
| --- |
| **Instruction système**    ```     All questions should be answered comprehensively with details, unless the user requests a concise response specifically. ```  **Requête**    ```     What is a smart way to make a business that sells DVD's in 2026? ```  **Réponse:**    ``` Starting a business selling DVDs in 2026 presents significant challenges due to the overwhelming dominance of digital streaming and on-demand services; a "smart" approach would therefore require a highly specialized niche, a strong value proposition beyond just the disc, and likely a focus on community or collector markets rather than mainstream consumption.  Here's a breakdown of what a smart DVD business in 2026 would likely entail:  1. Extreme Niche Specialization: You cannot compete with streaming libraries. Your business must focus on what digital doesn't offer easily or at all. This could include:      * Out-of-Print & Rare Titles: Sourcing films or TV shows that have never been released digitally or are currently unavailable on major streaming platforms.     .... ```  (gemini-2.5-flash) |

#### Mettre en forme les réponses avec la stratégie de complétion

La [stratégie de complémentation](#completion) peut également vous aider à formater la réponse.
L'exemple suivant demande au modèle de créer un plan de dissertation :

|  |
| --- |
| **Requête :**    ``` Create an outline for an essay about hummingbirds. ```  **Réponse:**    ``` Here is a possible outline for an essay about hummingbirds:  I. Introduction A. Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). B. Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds. C. Thesis Statement: State the main point of the essay, which could be about the remarkable adaptations, behaviors, and ecological importance of hummingbirds.  II. Appearance and Identification ..... ```  (gemini-2.5-flash) |

La requête ne mentionnait pas de format pour le plan et le modèle a choisi un format pour vous. Pour que le modèle renvoie un plan dans un format spécifique, vous pouvez ajouter du texte représentant le début du plan et laisser le modèle le terminer en fonction du schéma que vous avez initié.

|  |
| --- |
| **Requête :**    ``` Create an outline for an essay about hummingbirds. I. Introduction    * ```  **Réponse:**    ``` Okay, here is an outline for an essay about hummingbirds, starting from the introduction you provided:  I. Introduction * Hook: Start with a captivating fact or description about hummingbirds (e.g., their speed, iridescent colors, or tiny size). * Background: Briefly introduce hummingbirds – where they are found (Americas), their reputation as unique birds, and their general characteristics. * Thesis Statement: State the main point of the essay, focusing on the remarkable adaptations, behaviors, and ecological significance that make hummingbirds extraordinary. ..... ```  (gemini-2.5-flash) |

## Requêtes zero-shot et requêtes few-shot

Vous pouvez inclure des exemples dans la requête afin de montrer au modèle à quoi ressemble une réponse correcte. Le modèle tente d'identifier des schémas et des relations à partir des exemples, et les applique lors de la génération d'une réponse. Les requêtes contenant quelques exemples sont appelées des requêtes *few-shot*, tandis que les requêtes qui ne fournissent aucun exemple sont appelées *requêtes zero-shot*. Les requêtes few-shot sont souvent utilisées pour réguler la mise en forme, la formulation, le champ d'application ou la mise en forme générale des réponses du modèle. Utilisez des exemples spécifiques et variés pour aider le modèle à affiner sa cible et à générer des résultats plus précis.

Nous vous recommandons d'inclure systématiquement des exemples few-shot dans vos requêtes. Les requêtes sans exemples few-shot sont susceptibles d'être moins efficaces. En fait, vous pouvez supprimer les instructions de votre requête si vos exemples montrent clairement la tâche à accomplir.

La requête zero-shot suivante demande au modèle de choisir la meilleure explication.

|  |
| --- |
| **Requête :**    ``` Please choose the best explanation to the question:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Réponse:**    ``` Explanation1 is the better explanation because it provides more detail on the process, including how ice crystals combine and grow into snowflakes as they fall through the atmosphere. ```  (gemini-2.5-flash) |

Si votre cas d'utilisation nécessite que le modèle produise des réponses concises, vous pouvez inclure dans la requête des exemples qui privilégient les réponses concises.

La requête suivante fournit deux exemples qui indiquent une préférence pour les explications plus courtes. Dans la réponse, vous pouvez constater que les exemples ont poussé le modèle à choisir l'explication la plus courte (`Explanation2`), par opposition à la plus longue (`Explanation1`).

|  |
| --- |
| **Requête :**    ``` Below are some examples showing a question, explanation, and answer format:  Question: Why is the sky blue? Explanation1: The sky appears blue because of Rayleigh scattering, which causes shorter blue wavelengths of light to be scattered more easily than longer red wavelengths, making the sky look blue. Explanation2: Due to Rayleigh scattering effect. Answer: Explanation2  Question: What is the cause of earthquakes? Explanation1: Sudden release of energy in the Earth's crust. Explanation2: Earthquakes happen when tectonic plates suddenly slip or break apart, causing a release of energy that creates seismic waves that can shake the ground and cause damage. Answer: Explanation1  Now, Answer the following question given the example formats above:  Question: How is snow formed? Explanation1: Snow is formed when water vapor in the air freezes into ice crystals in the atmosphere, which can combine and grow into snowflakes as they fall through the atmosphere and accumulate on the ground. Explanation2: Water vapor freezes into ice crystals forming snow. Answer: ```  **Réponse:**    ``` Answer: Explanation2 ```  (gemini-2.5-flash) |

### Nombre optimal d'exemples

Des modèles tels que Gemini peuvent souvent détecter des schémas avec seulement quelques exemples, mais vous devrez peut-être tester le nombre d'exemples à fournir dans la requête pour obtenir les meilleurs résultats. Cependant, si vous incluez trop d'exemples, le modèle peut manifester un [surapprentissage](https://developers.google.com/machine-learning/glossary?hl=fr#overfitting) qui biaise les réponses obtenues.

### Toujours le même format

Assurez-vous que la structure et la mise en forme des exemples few-shot sont identiques pour éviter les réponses avec des formats indésirables. L'un des principaux objectifs de l'ajout d'exemples few-shot dans les requêtes est de montrer au modèle le format de réponse. Il est donc essentiel de veiller à ce que le format soit cohérent dans tous les exemples, en prêtant particulièrement attention aux balises XML, aux espaces blancs, aux sauts de ligne et aux séparateurs d'exemples.

## Ajouter le contexte

Vous pouvez inclure dans une requête des instructions et des informations dont le modèle a besoin pour résoudre un problème, au lieu de supposer que le modèle dispose de toutes les informations requises. Ces informations contextuelles aident le modèle à comprendre les contraintes et les détails de ce que vous lui demandez de faire.

L'exemple suivant demande au modèle de fournir des conseils de dépannage pour un routeur :

|  |
| --- |
| **Requête :**    ``` What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly. ```  **Réponse:**    ```   A yellow blinking light on your Google Wifi router usually indicates a problem   with the internet connection. Here are some steps to troubleshoot and fix the   issue:   1. Restart your router and modem:     - Unplug your modem from the power outlet and wait for 30 seconds.     - Plug your modem back in and wait for it to fully boot up.     - Unplug your Google Wifi router and wait for 30 seconds.     - Plug your Google Wifi router back in and wait for it to fully boot up. ..... ```  (gemini-2.5-flash) |

La réponse est semblable aux informations de dépannage génériques qui ne sont pas spécifiques au routeur ou à l'état des témoins LED.

Pour personnaliser la réponse en fonction du routeur spécifique, vous pouvez ajouter le guide de dépannage du routeur à la requête en tant que contexte auquel le modèle doit faire référence dans sa réponse.

|  |
| --- |
| **Requête :**    ``` Answer the question using the text below. Respond with only the text provided. Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.  Text: Color: Slowly pulsing yellow What it means: There is a network error. What to do: Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.  Color: Fast blinking yellow What it means: You are holding down the reset button and are factory resetting this device. What to do: If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.  Color: Solid yellow What it means: Router is factory resetting. What to do: This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.  Color: Solid red What it means: Something is wrong. What to do: Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support. ```  **Réponse:**    ``` Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again. ```  (gemini-2.5-flash) |

## Décomposer les requêtes en composants

Pour les cas d'utilisation qui nécessitent des requêtes complexes, vous pouvez aider le modèle à gérer cette complexité en décomposant les éléments en composants plus simples.

1. **Décomposez les instructions** : au lieu d'inclure plusieurs instructions dans une même requête, créez une requête par instruction. Vous pouvez choisir l'invite à traiter en fonction de la saisie de l'utilisateur.
2. **Requêtes de chaîne** : pour les tâches complexes impliquant plusieurs étapes séquentielles, faites de chaque étape une requête et associez les requêtes dans une séquence. Dans cette chaîne de prompts séquentielle, la sortie d'un prompt de la séquence devient l'entrée du prompt suivant. Le résultat de la dernière requête de la séquence est le résultat final.
3. **Réponses agrégées** : l'agrégation consiste à effectuer différentes tâches parallèles sur différentes parties des données et à agréger les résultats pour produire le résultat final. Par exemple, vous pouvez demander au modèle d'effectuer une opération sur la première partie des données, une autre opération sur le reste des données et d'agréger les résultats.

## Tester les paramètres du modèle

Chaque appel que vous envoyez à un modèle inclut des valeurs de paramètres qui contrôlent la manière dont le modèle génère sa réponse. Le modèle peut générer différents résultats pour différentes valeurs de paramètre. Testez différentes valeurs de paramètre pour obtenir les meilleures valeurs pour la tâche. Les paramètres disponibles pour les différents modèles peuvent différer. Les paramètres les plus courants sont les suivants :

1. **Nombre maximal de jetons de sortie** : spécifie le nombre maximal de jetons pouvant être générés dans la réponse. Un jeton correspond environ à quatre caractères. 100 jetons correspondent environ à 60-80 mots.
2. **Température** : la température permet de contrôler le degré de hasard dans la sélection des jetons. La température est utilisée pour l'échantillonnage pendant la génération de la réponse, qui se produit lorsque `topP` et `topK` sont appliqués. Les températures basses sont idéales pour les requêtes qui nécessitent une réponse plus déterministe ou moins ouverte, tandis que des températures plus élevées peuvent entraîner des résultats plus diversifiés ou créatifs. Une température de 0 est déterministe, ce qui signifie que la réponse dont la probabilité est la plus élevée est toujours sélectionnée.
3. **`topK`** : le paramètre `topK` modifie la façon dont le modèle sélectionne les jetons pour la sortie. Une valeur `topK` de 1 signifie que le jeton sélectionné est le plus probable parmi tous les jetons du vocabulaire du modèle (également appelé décodage glouton), tandis qu'une valeur `topK` de 3 signifie que le jeton suivant est sélectionné parmi les trois jetons les plus probables à l'aide de la température. Pour chaque étape de sélection de jeton, les principaux jetons `topK` ayant les probabilités les plus élevées sont échantillonnés. Les jetons sont ensuite filtrés en fonction de `topP`, puis le jeton final est sélectionné à l'aide de l'échantillonnage de température.
4. **`topP`** : le paramètre `topP` modifie la façon dont le modèle sélectionne les jetons pour la sortie. Les jetons sont sélectionnés de la probabilité la plus élevée à la plus faible jusqu'à ce que la somme de leurs probabilités soit égale à la valeur `topP`. Par exemple, si les jetons A, B et C ont une probabilité de 0,3, 0,2 et 0,1 et que la valeur `topP` est égale à 0,5, le modèle sélectionne A ou B comme jeton suivant en utilisant la température et exclut C comme candidat. La valeur `topP` par défaut est 0,95.
5. **`stop_sequences`** : définissez une séquence d'arrêt pour indiquer au modèle d'arrêter de générer du contenu. Une séquence d'arrêt peut être n'importe quelle séquence de caractères. Essayez d'éviter d'utiliser une séquence de caractères qui pourrait apparaître dans le contenu généré.

## Stratégies d'itération des invites

La conception d'une requête peut parfois nécessiter plusieurs essais avant d'obtenir la réponse souhaitée de manière consistante. Cette section fournit des conseils sur les mesures que vous pouvez appliquer lors de l'itération de vos requêtes :

1. **Utilisez des formulations différentes** : l'utilisation de formulations ou de mots différents dans vos requêtes permet souvent d'obtenir des réponses différentes du modèle, même lorsque les requêtes ont le même sens. Si vous n'obtenez pas les résultats attendus à partir de la requête, essayez de la reformuler.

   |  |
   | --- |
   | ``` Version 1: How do I bake a pie?  Version 2: Suggest a recipe for a pie.  Version 3: What's a good pie recipe? ``` |
2. **Passez à une tâche analogue** : si vous ne parvenez pas à ce que le modèle suive vos instructions pour une tâche, essayez de lui donner des instructions pour une tâche analogue qui permet d'obtenir le même résultat.

   Cette requête demande au modèle de catégoriser un livre en utilisant des catégories prédéfinies :

   |  |
   | --- |
   | **Requête :**    ``` Which category does The Odyssey belong to: thriller sci-fi mythology biography ```  **Réponse:**    ```     The Odyssey belongs to the category of **mythology**.       Here's why:      * **Mythology:** The Odyssey tells the story of Odysseus, a hero from Greek mythology, and his     journey home after the Trojan War. It features gods, monsters, and supernatural events common to     Greek mythology. ..... ```  (gemini-2.5-flash) |

   La réponse est correcte, mais le modèle n'est pas resté dans les limites des options. Vous souhaitez également que le modèle réponde avec l'une des options plutôt qu'avec une phrase complète. Dans ce cas, vous pouvez reformuler les instructions sous la forme d'une question à choix multiples et demander au modèle de choisir une option.

   |  |
   | --- |
   | **Requête :**    ``` Multiple choice problem: Which of the following options describes the book The Odyssey? Options: ``` |

   - thriller
   - sci-fi
   - mythology
   - biography
     **Réponse:**

     ```
     The correct answer is mythology.
     ```

     (gemini-2.5-flash)
   - **Modifier l'ordre du contenu dans la requête** : l'ordre du contenu dans la requête peut parfois affecter la réponse. Essayez de modifier l'ordre du contenu et vérifiez comment cela affecte la réponse.

     ```
     Version 1:
     [examples]
     [context]
     [input]

     Version 2:
     [input]
     [examples]
     [context]

     Version 3:
     [examples]
     [input]
     [context]
     ```

## Réponses de remplacement

Une réponse de remplacement est une réponse renvoyée par le modèle lorsque la requête ou la réponse déclenche un filtre de sécurité. Voici un exemple de réponse de remplacement : "Je ne peux pas vous aider, car je ne suis qu'un modèle de langage".

Si le modèle renvoie une réponse de remplacement, essayez d'augmenter la température.

## Ancrage et exécution de code

Gemini peut utiliser des outils pour éviter les hallucinations dans les scénarios où il pourrait produire des réponses incorrectes.

L'[ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) connecte le modèle Gemini à du contenu Web en temps réel. Il doit être activé chaque fois que le modèle peut avoir besoin de connaître des faits obscurs ou récents.

L'[outil d'exécution de code](https://ai.google.dev/gemini-api/docs/code-execution?hl=fr) de Gemini permet au modèle de générer et d'exécuter du code Python. Il doit être activé chaque fois que le modèle doit effectuer un calcul arithmétique, un décompte ou un calcul.

## Gemini 3

Les [modèles Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=fr#gemini-3) sont conçus pour le raisonnement avancé et le suivi des instructions.
Ils répondent mieux aux requêtes directes et bien structurées qui définissent clairement la tâche et les éventuelles contraintes. Les pratiques suivantes sont recommandées pour obtenir des résultats optimaux avec Gemini 3 :

### Principes de base du prompting

- **Soyez précis et direct** : énoncez votre objectif clairement et de manière concise. Évitez les formulations inutiles ou trop persuasives.
- **Utilisez une structure cohérente** : utilisez des délimiteurs clairs pour séparer les différentes parties de votre requête. Les balises de style XML (par exemple, `<context>`, `<task>`) ou les titres Markdown sont efficaces. Choisissez un format et utilisez-le de manière cohérente dans un même prompt.
- **Définissez les paramètres** : expliquez clairement tous les termes ou paramètres ambigus.
- **Contrôler la verbosité de la sortie** : par défaut, les modèles Gemini 3 fournissent des réponses directes et efficaces. Si vous avez besoin d'une réponse plus détaillée ou plus conversationnelle, vous devez l'indiquer explicitement dans vos instructions.
- **Gérez les entrées multimodales de manière cohérente** : lorsque vous utilisez du texte, des images, de l'audio ou des vidéos, traitez-les comme des entrées de même catégorie. Assurez-vous que vos instructions font clairement référence à chaque modalité, si nécessaire.
- **Donnez la priorité aux instructions critiques** : placez les contraintes comportementales essentielles, les définitions de rôle (persona) et les exigences de format de sortie dans l'instruction système ou tout au début du prompt utilisateur.
- **Structure pour les contextes longs** : lorsque vous fournissez de grandes quantités de contexte (par exemple, des documents ou du code), fournissez d'abord tout le contexte. Placez vos instructions ou questions spécifiques tout à la *fin* du prompt.
- **Contexte d'ancrage** : après un grand bloc de données, utilisez une phrase de transition claire pour faire le lien entre le contexte et votre requête, par exemple "Sur la base des informations ci-dessus…".

### Stratégies Gemini 3 Flash

- **Précision pour le jour actuel** : ajoutez la clause suivante aux instructions système pour aider le modèle à tenir compte du fait que le jour actuel est en 2026 :

  ```
  For time-sensitive user queries that require up-to-date information, you
  MUST follow the provided current time (date and year) when formulating
  search queries in tool calls. Remember it is 2026 this year.
  ```
- **Précision de la date limite des connaissances** : ajoutez la clause suivante aux instructions système pour informer le modèle de sa date limite des connaissances :

  ```
  Your knowledge cutoff date is January 2025.
  ```
- **Performances d'ancrage** : ajoutez la clause suivante aux instructions système (en la modifiant si nécessaire) pour améliorer la capacité du modèle à ancrer les réponses dans le contexte fourni :

  ```
  You are a strictly grounded assistant limited to the information provided in
  the User Context. In your answers, rely **only** on the facts that are
  directly mentioned in that context. You must **not** access or utilize your
  own knowledge or common sense to answer. Do not assume or infer from the
  provided facts; simply report them exactly as they appear. Your answer must
  be factual and fully truthful to the provided text, leaving absolutely no
  room for speculation or interpretation. Treat the provided context as the
  absolute limit of truth; any facts or details that are not directly
  mentioned in the context must be considered **completely untruthful** and
  **completely unsupported**. If the exact answer is not explicitly written in
  the context, you must state that the information is not available.
  ```

### Améliorer le raisonnement et la planification

Les modèles des séries Gemini 2.5 et 3 génèrent automatiquement du texte de "réflexion" interne pour améliorer les performances de raisonnement. Par conséquent, il n'est généralement pas nécessaire que le modèle fournisse un plan, un résumé ou des étapes de raisonnement détaillées dans la réponse renvoyée. Pour les problèmes qui nécessitent un raisonnement approfondi, des requêtes simples comme "Réfléchis bien avant de répondre" peuvent améliorer les performances, mais au prix de jetons de réflexion supplémentaires.

Pour en savoir plus, consultez la documentation [Pensée de Gemini](https://ai.google.dev/gemini-api/docs/thinking?hl=fr).

### Exemples de requêtes structurées

L'utilisation de tags ou de Markdown aide le modèle à faire la distinction entre les instructions, le contexte et les tâches.

**Exemple de code XML :**

```
<role>
You are a helpful assistant.
</role>

<constraints>
1. Be objective.
2. Cite sources.
</constraints>

<context>
[Insert User Input Here - The model knows this is data, not instructions]
</context>

<task>
[Insert the specific user request here]
</task>
```

**Exemple Markdown :**

```
# Identity
You are a senior solution architect.

# Constraints
- No external libraries allowed.
- Python 3.11+ syntax only.

# Output format
Return a single code block.
```

### Exemple de modèle combinant les bonnes pratiques

Ce modèle reprend les principes de base pour rédiger des requêtes avec Gemini 3. Veillez toujours à itérer et à modifier le code pour l'adapter à votre cas d'utilisation spécifique.

**Instruction système :**

```
<role>
You are Gemini 3, a specialized assistant for [Insert Domain, e.g., Data Science].
You are precise, analytical, and persistent.
</role>

<instructions>
1. **Plan**: Analyze the task and create a step-by-step plan.
2. **Execute**: Carry out the plan.
3. **Validate**: Review your output against the user's task.
4. **Format**: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Specify Low/Medium/High]
- Tone: [Specify Formal/Casual/Technical]
</constraints>

<output_format>
Structure your response as follows:
1. **Executive Summary**: [Short overview]
2. **Detailed Response**: [The main content]
</output_format>
```

**Requête de l'utilisateur** :

```
<context>
[Insert relevant documents, code snippets, or background info here]
</context>

<task>
[Insert specific user request here]
</task>

<final_instruction>
Remember to think step-by-step before answering.
</final_instruction>
```

## Workflows agentifs

Pour les workflows agentiques complexes, des instructions spécifiques sont souvent nécessaires pour contrôler la façon dont le modèle raisonne, planifie et exécute les tâches. Bien que Gemini offre de bonnes performances générales, les agents complexes vous obligent souvent à configurer le compromis entre le coût de calcul (latence et jetons) et la précision des tâches.

Lorsque vous concevez des requêtes pour les agents, tenez compte des dimensions de comportement suivantes que vous pouvez orienter dans l'agent :

### Raisonnement et stratégie

Configuration de la façon dont le modèle réfléchit et planifie avant d'agir.

- **Décomposition logique** : définit la profondeur d'analyse des contraintes, des conditions préalables et de l'ordre des opérations par le modèle.
- **Diagnostic des problèmes** : contrôle la profondeur de l'analyse lors de l'identification des causes et l'utilisation du raisonnement abductif par le modèle. Détermine si le modèle doit accepter la réponse la plus évidente ou explorer des explications complexes et moins probables.
- **Exhaustivité des informations** : compromis entre l'analyse de toutes les règles et tous les documents disponibles, et la priorité accordée à l'efficacité et à la rapidité.

### Exécution et fiabilité

Configuration du fonctionnement autonome de l'agent et de la gestion des obstacles.

- **Adaptabilité** : façon dont le modèle réagit aux nouvelles données. Détermine s'il doit s'en tenir strictement à son plan initial ou pivoter immédiatement lorsque les observations contredisent les hypothèses.
- **Persistance et récupération** : degré auquel le modèle tente de corriger lui-même les erreurs. Une persistance élevée augmente les taux de réussite, mais risque d'entraîner des coûts de jetons plus élevés ou des boucles.
- **Évaluation des risques** : logique d'évaluation des conséquences. Il distingue explicitement les actions exploratoires à faible risque (lectures) des modifications d'état à haut risque (écritures).

### Interaction et sortie

Configuration de la façon dont l'agent communique avec l'utilisateur et met en forme les résultats.

- **Gestion de l'ambiguïté et des autorisations** : définit les cas où le modèle est autorisé à faire des hypothèses et ceux où il doit suspendre l'exécution pour demander des éclaircissements ou une autorisation à l'utilisateur.
- **Niveau de détail** : contrôle le volume de texte généré en plus des appels d'outils. Cela détermine si le modèle explique ses actions à l'utilisateur ou reste silencieux lors de l'exécution.
- **Précision et exhaustivité** : fidélité requise de la sortie. Indique si le modèle doit résoudre tous les cas extrêmes et fournir des chiffres exacts, ou si des estimations approximatives sont acceptables.

### Modèle d'instruction système

L'instruction système suivante est un exemple qui a été évalué par des chercheurs pour améliorer les performances sur les benchmarks agentiques où le modèle doit respecter un ensemble de règles complexes et interagir avec un utilisateur. Il encourage l'agent à agir en tant que planificateur et raisonneur efficace, applique des comportements spécifiques aux dimensions listées ci-dessus et exige du modèle qu'il planifie de manière proactive avant d'entreprendre toute action.

Vous pouvez adapter ce modèle pour qu'il corresponde aux contraintes de votre cas d'utilisation spécifique.

```
You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses.

Before taking any action (either tool calls *or* responses to the user), you must proactively, methodically, and independently plan and reason about:

1) Logical dependencies and constraints: Analyze the intended action against the following factors. Resolve conflicts in order of importance:
    1.1) Policy-based rules, mandatory prerequisites, and constraints.
    1.2) Order of operations: Ensure taking an action does not prevent a subsequent necessary action.
        1.2.1) The user may request actions in a random order, but you may need to reorder operations to maximize successful completion of the task.
    1.3) Other prerequisites (information and/or actions needed).
    1.4) Explicit user constraints or preferences.

2) Risk assessment: What are the consequences of taking the action? Will the new state cause any future issues?
    2.1) For exploratory tasks (like searches), missing *optional* parameters is a LOW risk. **Prefer calling the tool with the available information over asking the user, unless** your `Rule 1` (Logical Dependencies) reasoning determines that optional information is required for a later step in your plan.

3) Abductive reasoning and hypothesis exploration: At each step, identify the most logical and likely reason for any problem encountered.
    3.1) Look beyond immediate or obvious causes. The most likely reason may not be the simplest and may require deeper inference.
    3.2) Hypotheses may require additional research. Each hypothesis may take multiple steps to test.
    3.3) Prioritize hypotheses based on likelihood, but do not discard less likely ones prematurely. A low-probability event may still be the root cause.

4) Outcome evaluation and adaptability: Does the previous observation require any changes to your plan?
    4.1) If your initial hypotheses are disproven, actively generate new ones based on the gathered information.

5) Information availability: Incorporate all applicable and alternative sources of information, including:
    5.1) Using available tools and their capabilities
    5.2) All policies, rules, checklists, and constraints
    5.3) Previous observations and conversation history
    5.4) Information only available by asking the user

6) Precision and Grounding: Ensure your reasoning is extremely precise and relevant to each exact ongoing situation.
    6.1) Verify your claims by quoting the exact applicable information (including policies) when referring to them. 

7) Completeness: Ensure that all requirements, constraints, options, and preferences are exhaustively incorporated into your plan.
    7.1) Resolve conflicts using the order of importance in #1.
    7.2) Avoid premature conclusions: There may be multiple relevant options for a given situation.
        7.2.1) To check for whether an option is relevant, reason about all information sources from #5.
        7.2.2) You may need to consult the user to even know whether something is applicable. Do not assume it is not applicable without checking.
    7.3) Review applicable sources of information from #5 to confirm which are relevant to the current state.

8) Persistence and patience: Do not give up unless all the reasoning above is exhausted.
    8.1) Don't be dissuaded by time taken or user frustration.
    8.2) This persistence must be intelligent: On *transient* errors (e.g. please try again), you *must* retry **unless an explicit retry limit (e.g., max x tries) has been reached**. If such a limit is hit, you *must* stop. On *other* errors, you must change your strategy or arguments, not repeat the same failed call.

9) Inhibit your response: only take an action after all the above reasoning is completed. Once you've taken an action, you cannot take it back.
```

## Étapes suivantes

- Maintenant que vous avez une meilleure compréhension de la conception des requêtes, essayez d'écrire vos propres requêtes à l'aide de [Google AI Studio](http://aistudio.google.com?hl=fr).
- Pour en savoir plus sur le prompting multimodal, consultez [Utiliser des fichiers multimédias dans les requêtes](https://ai.google.dev/gemini-api/docs/files?hl=fr#prompt-guide).
- Pour en savoir plus sur les prompts d'images, consultez les guides sur les prompts [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr#prompt-guide) et [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=fr#imagen-prompt-guide).
- Pour en savoir plus sur les prompts vidéo, consultez le [Guide sur les prompts Veo](https://ai.google.dev/gemini-api/docs/video?hl=fr#prompt-guide).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/04/29 (UTC)."],[],[]]
